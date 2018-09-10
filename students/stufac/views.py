from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import *
from django.db.models.functions import Cast
from .models import Student, Subject

# Create your views here.

def sample(request):
    return HttpResponse("<p style=color:blue>This is a Sample page</p>")

def home(request):
    return render(request,'index.html')


def student_top(request): ## For finding out the Top student who scored max total among all
    student = Student.objects.filter(marks__gte=40).values("sname").annotate(sum=Sum('marks')).order_by('-sum')[:1]
    if student:
        context = {
        'student_top':student
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def student_least(request): ## For finding out the student who scored minimum total among all
    student = Student.objects.values("sname").annotate(sum=Sum('marks')).order_by('sum')[:1]
    if student:
        context = {
        'student_least':student
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def maths_top(request): ## For finding the faculty with highest student count who got more than 90% marks ##
    student = Student.objects.filter(subject__contains='Math').values("sname","marks").order_by('-marks')[:1]
    if student:
        context = {
        'maths_top':student
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def faculty_max_90(request): ## For finding the faculty with highest student count who got more than 90% marks ##
    obj1 = Student.objects.filter(marks__gt=90).values("subject").annotate(count=Count("sname")).order_by("-count")
    obj2 = obj1[0]
    sub = obj2["subject"]
    obj3 = Subject.objects.filter(subject=sub).values("faculty")
    #obj4 = obj3["faculty"]
    #obj1 = Student.objects.all()
    #obj2 = Subject.objects.all()
    #obj3 = obj1.union(obj2)
    #obj4 = obj3.filter(marks__gte=90).values("subject").annotate(count=Count("sname")).order_by('-count')[:1]
    if sub:
        context = {
        'fac_max_90':obj3,'sub_max_90':obj2
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def faculty_max_pass(request): ## For finding the faculty with highest student count who failed exam ##
    obj1 = Student.objects.filter(marks__gt=40).values("subject").annotate(count=Count("sname")).order_by('-count','-subject')[0]
    sub = obj1["subject"]
    obj2 = Subject.objects.filter(subject=sub).values('faculty')
    if obj2:
        context = {
        'fac_max_pass':obj2,'sub_max_pass':obj1
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def faculty_max_fail(request): ## For finding the faculty with highest student count who failed exam ##
    obj1 = Student.objects.filter(marks__lte=40).values("subject").annotate(count=Count("sname")).order_by('-count')[0]
    sub = obj1["subject"]
    obj2 = Subject.objects.filter(subject=sub).values('faculty')
    if obj2:
        context = {
        'fac_max_fail':obj2,'sub_max_fail':obj1
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")

def subject_avg(request): ## For finding the average marks in each subject for all students ##
    #average = Student.objects.values('subject').annotate(avg = Sum('marks')/Count('sname')).order_by('-avg')#avg as int
    #average = Student.objects.filter(marks__gt=40).values('subject').annotate(avg = Cast(Sum('marks')/Count('sname'),FloatField())).order_by('-avg')
    average = Student.objects.filter(marks__gt=40).values("sname","subject","marks")
    d={}
    for i in average:
        count = 0
        if i["subject"] not in d:
            count += 1
            d[i["subject"]] = [i["marks"]]
        else:
            count +=1
            d[i["subject"]].append(i["marks"])
    d1={}
    for i,j in d.items():
        sum = 0
        for k in j:
            sum += k
        avg = round(sum/len(j),2)
        d1[i] = avg
    if average:
        context = {
        'sub_avg':d1
        }
        return render(request,'frontpage.html',context)
    else:
        return HttpResponseNotFound("Record not found")
