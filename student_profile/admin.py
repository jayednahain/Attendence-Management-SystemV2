from django.contrib import admin
from .models import Students
from .models import Department

admin.site.register(Students)
admin.site.register(Department)