from django.contrib import admin

from . models import Student, Subject

# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display=('id','sname','subject','marks')
    search_fields=('sname','subject')

admin.site.register(Student,StudentsAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display=('id','subject','faculty')
    search_fields=('subject','faculty')

admin.site.register(Subject,FacultyAdmin)
