from django.core.exceptions import ValidationError
import logging
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teachers
from .serializers import TeacherSerializer

# Configure logger
logger = logging.getLogger(__name__)

# Helper function to get global context data
def get_context_data():
    """Returns common context data for all templates"""
    from students.models import Student
    
    total_students = Student.objects.count()
    total_teachers = Teachers.objects.count()
    
    logger.info(f"get_context_data() - Total Students: {total_students}, Total Teachers: {total_teachers}")
    
    return {
        'total_students': total_students,
        'total_teachers': total_teachers,
    }


# GET all teachers (API)
@api_view(['GET'])
def get_teachers(request):
    logger.info(f"GET /teachers/ - Request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    teachers = Teachers.objects.all()
    logger.info(f"Retrieved {teachers.count()} teachers from database")
    serializer = TeacherSerializer(teachers, many=True)
    logger.info(f"Serialized {len(serializer.data)} teacher records for response")
    return Response(serializer.data)


# POST add teacher (API)
@api_view(['GET', 'POST'])
def add_teachers(request):
    logger.info(f"POST /teachers/add/ - Request method: {request.method}")
    logger.info(f"Request data: {request.data}")
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        logger.info(f"Validation passed for teacher data: {serializer.validated_data}")
        serializer.save()
        logger.info(f"Teacher saved successfully with ID: {serializer.instance.id}")
        return Response(serializer.data)
    logger.warning(f"Validation failed with errors: {serializer.errors}")
    return Response(serializer.errors)


# Teacher List Page (UI)
def teacher_list(request):
    logger.info(f"GET /teachers/list/ - Teacher list request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    teachers = Teachers.objects.all()
    teacher_count = teachers.count()
    logger.info(f"Retrieved {teacher_count} teachers from database")
    
    context = get_context_data()
    context.update({
        'teachers': teachers,
        'teacher_count': teacher_count,
    })
    logger.info(f"Teacher list context prepared with {teacher_count} teachers")
    return render(request, 'teacher_list.html', context)


# Teacher Detail Page (UI)
def teacher_detail(request, id):
    logger.info(f"GET /teachers/{id}/ - Teacher detail request for teacher ID: {id}")
    teacher = get_object_or_404(Teachers, id=id)
    logger.info(f"Teacher found: {teacher.name} (Email: {teacher.email})")
    
    context = get_context_data()
    context.update({'teacher': teacher})
    logger.info(f"Teacher detail context prepared for {teacher.name}")
    return render(request, 'teacher_detail.html', context)


# Add Teacher Page (UI)
def add_teacher_page(request):
    logger.info(f"{request.method} /teachers/add-teacher/ - Request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    
    if request.method == 'POST':
        logger.info(f"Processing POST request for add teacher")
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        logger.info(f"Teacher form data - Name: {name}, Email: {email}")

        teacher = Teachers(
            name=name,
            email=email
        )
        try:
           teacher.full_clean()
           teacher.save()

           logger.info(f"Teacher created successfully - ID: {teacher.id}, Name: {teacher.name}")

           return redirect(f'/teachers/{teacher.id}/')

        except ValidationError as e:
            context = get_context_data()
            context['errors'] = e.message_dict
            return render(request, 'add_teacher.html', context)

    logger.info(f"Rendering add teacher form")
    context = get_context_data()
    logger.info(f"Add teacher context prepared")
    return render(request, 'add_teacher.html', context)


# Edit Teacher Page (UI)
def edit_teacher(request, id):
    logger.info(f"{request.method} /teachers/edit/{id}/ - Edit teacher request for ID: {id}")
    teacher = get_object_or_404(Teachers, id=id)
    logger.info(f"Editing teacher: {teacher.name} (Current Email: {teacher.email})")

    if request.method == 'POST':
        logger.info(f"Processing POST request for edit teacher {id}")
        
        old_name = teacher.name
        old_email = teacher.email
        
        teacher.name = request.POST.get('name', teacher.name)
        teacher.email = request.POST.get('email', teacher.email)
        
        logger.info(f"Changes - Name: {old_name} → {teacher.name}, Email: {old_email} → {teacher.email}")
        
        teacher.save()
        logger.info(f"Teacher {teacher.id} updated successfully")
        return redirect(f'/teachers/{teacher.id}/')

    logger.info(f"Rendering edit form for teacher {id}")
    context = get_context_data()
    context.update({
        'teacher': teacher,
        'edit_mode': True
    })
    logger.info(f"Edit teacher context prepared for {teacher.name}")
    return render(request, 'edit_teacher.html', context)


# Delete Teacher
def delete_teacher(request, id):
    logger.info(f"DELETE /teachers/delete/{id}/ - Request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    teacher = get_object_or_404(Teachers, id=id)
    logger.info(f"Deleting teacher: {teacher.name} (ID: {teacher.id}, Email: {teacher.email})")
    teacher.delete()
    logger.info(f"Teacher {teacher.name} deleted successfully")
    return redirect('/teachers/list/')
