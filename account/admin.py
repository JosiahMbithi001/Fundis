from django.contrib import admin
from .models import  Certificate, Employee, Employer

# Register your models here.
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Certificate)
