from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Department, Attendance, Kin

# Register your models here.
admin.site.register([Employee, Department, Attendance, Kin])
