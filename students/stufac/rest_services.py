from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from django.conf.urls import url
from .models import Student, Subject
from django.http import JsonResponse
from django.db.models import *
from .serializers import StudentSerializer, SubjectSerializer


@api_view(['GET'])
def api_first_record_student(request):
    obj = Student.objects.all()[0]  ##obj = Student.objectsall().first()
    if obj:
        serializer = StudentSerializer(obj)
        return JsonResponse(serializer.data)
    else:
        return Response({"message":'Record not found'})


@api_view(['GET'])
def api_all_record_student(request):
    obj = Student.objects.all()
    if obj:
        serializer = StudentSerializer(obj,many=True)
        return Response(serializer.data)
    else:
        return Response({"message":'Record not found'})

@api_view(['POST'])
def api_add_new_student(request):
    sname = request.POST.get('sname')
    subject = request.POST.get('subject')
    marks = request.POST.get('marks')
    student = Student.objects.create(sname = sname, subject = subject,marks = marks)

    return Response({'message':'student{:d} created'.format(student.id)},status=301)

urlpatterns =[

    path('first/',api_first_record_student),
    path('all/',api_all_record_student),
    path('add/',api_add_new_student),

]
