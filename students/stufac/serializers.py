from rest_framework import serializers
from .models import Student, Subject

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'sname', 'subject', 'marks')

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fileds = ('id', 'subject', 'faculty')
