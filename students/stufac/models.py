from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20)
    marks = models.IntegerField()

    def __str__(self):
        return self.sname

class Subject(models.Model):
    subject = models.CharField(max_length = 20)
    faculty = models.CharField(max_length = 20)

    def __str__(self):
        return self.faculty
