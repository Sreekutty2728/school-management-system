from .forms import StudentForm
import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Configure logger
logger = logging.getLogger(__name__)

# Helper function to get global context data
def get_context_data():
    """Returns common context data for all templates"""
    from teachers.models import Teachers
    
    total_students = Student.objects.count()
    total_teachers = Teachers.objects.count()
    
    logger.info(f"get_context_data() - Total Students: {total_students}, Total Teachers: {total_teachers}")
    
    return {
        'total_students': total_students,
        'total_teachers': total_teachers,
    }


# GET all students
@api_view(['GET'])
def get_students(request):
    logger.info(f"GET /students/get/ - Request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    students = Student.objects.all()
    logger.info(f"Retrieved {students.count()} students from database")
    serializer = StudentSerializer(students, many=True)
    logger.info(f"Serialized {len(serializer.data)} student records for response")
    return Response(serializer.data)


# POST add student
@api_view(['GET', 'POST'])
def add_students(request):
    logger.info(f"POST /students/add/ - Request method: {request.method}")
    logger.info(f"Request data: {request.data}")
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        logger.info(f"Validation passed for student data: {serializer.validated_data}")
        serializer.save()
        logger.info(f"Student saved successfully with ID: {serializer.instance.id}")
        return Response(serializer.data)

    logger.warning(f"Validation failed with errors: {serializer.errors}")
    return Response(serializer.errors)


# DELETE student
def delete_student(request, id):
    logger.info(f"DELETE /students/delete/{id}/ - Request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    student = get_object_or_404(Student, id=id)
    logger.info(f"Deleting student: {student.name} (ID: {student.id}, Email: {student.email})")
    student.delete()
    logger.info(f"Student {student.name} deleted successfully")
    return redirect('/students/classes/')


# Dashboard Page
def dashboard(request):
    logger.info(f"GET /students/dashboard/ - Dashboard request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    context = get_context_data()
    recent_students = Student.objects.all()[:5]
    logger.info(f"Retrieved {len(recent_students)} recent students")
    context.update({
        'total_classes': 10,
        'recent_students': recent_students,
    })
    logger.info(f"Dashboard context prepared: {list(context.keys())}")
    return render(request, 'dashboard.html', context)


# Class List Page
def class_list(request):
    logger.info(f"GET /students/classes/ - Class list request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    classes = range(1, 11)
    context = get_context_data()
    
    class_stats = [
        {'class_no': i, 'count': Student.objects.filter(student_class=str(i)).count()}
        for i in range(1, 11)
    ]
    logger.info(f"Class statistics: {class_stats}")
    
    context.update({
        'classes': classes,
        'class_stats': class_stats
    })
    logger.info(f"Class list context prepared with {len(class_stats)} classes")
    return render(request, 'class_list.html', context)


# Students of selected class
def student_list(request, class_no):
    logger.info(f"GET /students/class/{class_no}/ - Student list request for class {class_no}")
    students = Student.objects.filter(student_class=str(class_no))
    student_count = students.count()
    logger.info(f"Retrieved {student_count} students for class {class_no}")

    class_teachers = {
        1: "Anitha",
        2: "Ramesh",
        3: "Priya",
        4: "Deepa",
        5: "Suresh",
        6: "Mini",
        7: "Arun",
        8: "Divya",
        9: "Rajesh",
        10: "Asha"
    }

    class_teacher = class_teachers.get(int(class_no), "Not Assigned")
    logger.info(f"Class {class_no} teacher: {class_teacher}")
    
    context = get_context_data()
    context.update({
        'students': students,
        'class_name': f'Class {class_no}',
        'class_teacher': class_teacher,
        'student_count': student_count,
    })
    logger.info(f"Student list context prepared with {student_count} students")
    return render(request, 'student_list.html', context)


# Student Detail Page
def student_detail(request, id):
    logger.info(f"GET /students/{id}/ - Student detail request for student ID: {id}")
    student = get_object_or_404(Student, id=id)
    logger.info(f"Student found: {student.name} (Email: {student.email}, Class: {student.student_class})")
    context = get_context_data()
    context.update({'student': student})
    logger.info(f"Student detail context prepared for {student.name}")
    return render(request, 'student_detail.html', context)


# Add Student Page
def add_student(request):
    logger.info(f"{request.method} /students/add/ - Add student request")
    
    if request.method == 'POST':
        logger.info(f"Processing POST request for adding student")
        form = StudentForm(request.POST, request.FILES)
        
        if form.is_valid():
            student = form.save()
            logger.info(f"Student {student.name} added successfully with ID: {student.id}")
            return redirect(f'/students/{student.id}/')
        else:
            logger.warning(f"Form validation failed with errors: {form.errors}")
    else:
        form = StudentForm()
        logger.info(f"Rendering empty form for adding new student")

    context = get_context_data()
    context.update({
    'form': form,
    'classes': range(1, 11)
})
    logger.info(f"Add student context prepared")
    return render(request, 'add_student.html', context)
    
# Edit Student Page
def edit_student(request, id):
    logger.info(f"{request.method} /students/edit/{id}/ - Edit student request for ID: {id}")
    student = get_object_or_404(Student, id=id)
    logger.info(f"Editing student: {student.name} (Current Email: {student.email}, Class: {student.student_class})")

    if request.method == 'POST':
        logger.info(f"Processing POST request for edit student {id}")
        
        old_name = student.name
        old_email = student.email
        
        student.name = request.POST.get('name', student.name)
        student.email = request.POST.get('email', student.email)
        student.student_class = request.POST.get('student_class', student.student_class)
        student.roll_number = request.POST.get('roll_number', student.roll_number)
        student.register_number = request.POST.get('register_number', student.register_number)
        student.age = request.POST.get('age', student.age)
        student.phone = request.POST.get('phone', student.phone)
        student.address = request.POST.get('address', student.address)
        
        logger.info(f"Changes - Name: {old_name} → {student.name}, Email: {old_email} → {student.email}")
        
        if request.FILES.get('profile_image'):
            profile_image = request.FILES.get('profile_image')
            student.profile_image = profile_image
            logger.info(f"Profile image updated: {profile_image.name}")

        student.save()
        logger.info(f"Student {student.id} updated successfully")
        return redirect(f'/students/{student.id}/')

    logger.info(f"Rendering edit form for student {id}")
    context = get_context_data()
    context.update({
        'student': student,
        'classes': range(1, 11),
        'edit_mode': True
    })
    logger.info(f"Edit student context prepared for {student.name}")
    return render(request, 'edit_student.html', context)