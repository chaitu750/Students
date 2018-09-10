from django.urls import path, include
from . import views
from django.conf.urls import url
from stufac import rest_services
#from .rest_services import api_all_records_of_student_database, api_first_record_of_student_database


urlpatterns=[
    path('sample/',views.sample, name='sample'),
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('student_top/',views.student_top,name='student_top'),
    path('student_least/',views.student_least,name='student_least'),
    path('maths_top/',views.maths_top,name='maths_top'),
    path('faculty_max_90/',views.faculty_max_90,name='faculty_max_90'),
    path('faculty_max_pass/',views.faculty_max_pass,name='faculty_max_pass'),
    path('faculty_max_fail/',views.faculty_max_fail,name='faculty_max_fail'),
    path('subject_avg/',views.subject_avg,name='subject_avg'),
    url(r'^api/',include(rest_services))


]
