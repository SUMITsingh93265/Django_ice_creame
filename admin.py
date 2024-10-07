from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)

class Subject_marks_Admin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(Subject_marks, Subject_marks_Admin) 