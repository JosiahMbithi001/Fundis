from django.db import models
from account.models import Employee,Employer
import datetime
# Create your models here.

"""
Models for the jobs app
 Table jobs
"""

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    job_status = models.IntegerField(choices=((1, 'Active'), (2, 'Inactive')))
    requiments = models.CharField(max_length=1000)
    job_location = models.CharField(max_length=500)
    description = models.CharField(max_length=4000)
    salary = models.IntegerField()
    Date_posted = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Employer, on_delete=models.CASCADE)

    class Meta:
        """
        Meta class for jobs model
        setted managed to True to create a table in the database
        using django orm
        """
        managed = True
        db_table = 'jobs'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.job_title + 'by' + self.user_id.firstname


class Application(models.Model):
    """
    Model for jobseeker applications
    """
    application_id = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.IntegerField(choices=((1, 'Pending'), (2, 'Accepted'), (3, 'Rejected'), (4, 'Done')))
    application_date = models.DateTimeField(auto_now_add=True)
    proposal = models.TextField(max_length=4000)
    cv = models.FileField(upload_to='cvs/')
    estimated_salary = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'applications'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return self.job_id.job_title

