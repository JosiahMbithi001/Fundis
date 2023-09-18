from django.db import models
from django.conf import settings

class Employer(models.Model):
    """A model representing an employer on JobKonnect website."""

    employerid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    password = models.TextField(max_length=50)
    location = models.CharField(max_length=20)

    class Meta:
        db_table = 'employer'
        verbose_name_plural = 'Employers'

    def __str__(self):
        return str(self.userid)

class Employee(models.Model):
    """A model representing an employee on JobKonnect website."""

    employeeid = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    password = models.TextField(max_length=50)
    profession = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    status = models.CharField(max_length=15, default='active')

    class Meta:
        db_table = 'employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return str(self.user)

class Certificate(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_of_issuance = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/')

    class Meta:
        db_table = 'certificate'
        verbose_name_plural = 'Certificates'
