from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Certificate, Employer, Employee


class EmployerForm(forms.ModelForm):
 
    class Meta:
        """
        Employers MetaData
        """
        model = Employer
        fields = '__all__'

class EmployeeForm(forms.ModelForm):

    class Meta:
        """
        Employees MetaData
        """
        model = Employee
        fields = '__all__'

class RegisterForm(UserCreationForm):
    """This Class is for Form Registration"""
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from .models import Certificate

class CertificateForm(forms.ModelForm):
    """Where Users will display their Certificates"""

    class Meta:
        """Certificates Metadata"""
        model = Certificate
        fields = '__all__'
