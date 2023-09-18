from django.urls import path, include
from .views import *

app_name = 'jobs'
"""
URL configuration for jobs app
"""
urlpatterns = [
    path('', jobseeker_landing, name='employee_landing'),
    path('apply_job', ApplicationCreateView.as_view(), name='jobaplication'),
    path('<employee_name/applications', applicationhistory, name='aplicationhistory'),
    path('landing', employer_landing, name="employer_landing"),
    path('post_job', post_job, name='post_job'),
    path('search',search_job.as_view(), name='search_job'),
    path('delete_application/<int:application_id>/', delete_application, name='delete_application'),
    path('delete_job/<int:job_id>/', delete_job, name='delete_job'),
    path('update_job/<int:job_id>/', update_job, name='update_job'),
    path('update_application/<int:application_id>/', update_application, name='update_application'),
    path('applications/<int:job_id>/', applications, name='applications'),
]