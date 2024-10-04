from django.contrib import admin
from.models import student, teacher, Admin,Attendance,Marks,Subject
# Register your models here.

admin.site.register(student)
admin.site.register(teacher)
admin.site.register(Admin)
admin.site.register(Attendance)
admin.site.register(Marks)
admin.site.register(Subject)

