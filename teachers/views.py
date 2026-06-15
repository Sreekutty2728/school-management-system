from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teachers
from .serializers import TeacherSerializer

#GET all teachers
@api_view(['GET'])
def get_teachers(request):
    teachers=Teachers.objects.all()
    serializer=TeacherSerializer(teachers,many=True)
    return Response(serializer.data)

#POST add teacher
@api_view(['GET','POST'])
def add_teachers(request):
    serializer=TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)