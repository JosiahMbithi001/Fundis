from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employer, Employee
from django.contrib.auth.models import User
import random 
from jobs.models import Job, Application
from .forms import CertificateForm
from django.http import HttpResponse

# Create your views here.
def base(request):
    """
    This is the landing autentication Page 
    """
    return render(request, "account/authenticate.html")

def employer_sign_up(request):
    """Employers View for the SignUp Form"""
  
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']
        username = email

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
                is_staff=True
            )

            employer = Employer(
                userid=user,
                firstname=firstname,
                lastname=lastname,
                phonenumber=phonenumber,
                email=email,
                password=password,
                location=location
            )
            employer.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect("/account/login")
        
    return render(request, 'account/employer.html')

def employee_sign_up(request):
    """Employee signup View"""

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phonenumber = request.POST['phonenumber']
        email = request.POST['email']
        password = request.POST['password']
        location = request.POST['location']
        profession = request.POST['profession']
        status = 'active'
        user_name = email
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'Username is already taken.')
        else:
            new_user = User.objects.create_user(
                username=user_name,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname,
                is_staff=True
            )
        new_employee = Employee(
            user=new_user,
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            email=email,
            password=password,
            location=location,
            profession=profession,
            status=status
        )
        new_employee.save()
        return redirect('/account/login')
    else:
        return render(request, 'account/employee.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, ("You were successfully Logged In"))
            if Employer.objects.filter(userid=request.user).exists():
                return redirect("/jobs/post_job")
            elif Employee.objects.filter(user=request.user).exists():
                return redirect("/jobs/")
            else:
                return redirect("/account/login")
        else:
            messages.success(request, ("Error Logging In - Please Try Again..."))
            return redirect("/account/login")
    else:
        return render(request, 'account/login.html')

def user_logout(request):
    """
    Function used to logout user
    """
    logout(request)
    messages.success(request, ("You were successfully Logged Out"))
    return redirect ("/")


def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)
            certificate.save()
            return redirect('certificate_list')
    else:
        form = CertificateForm()
    return render(request, 'upload_certificate.html', {'form': form})

from jobs.models import Job, Application
def profile(request):
     #if Employee exists display jobs they have curently applied for
    # if request.user.is_authenticated and request.user.is_employee:
    #     employee = request.user.employee
    #     applications = Application.objects.filter(employee=employee)
    #     return render(request, 'employee_applications.html', {'applications': applications}, {'employee': employee})
    # elif request.user.is_authenticated and request.user.is_employer:
    #         employer = request.user.employer
    #         jobs = Job.objects.filter(employer=employer)
    #         return render(request, 'employerprofile.html', {'jobs': jobs}, {'employer': employer})
    # else:
    #      return HttpResponse('You are not logged in')
    if Employee.objects.filter(user=request.user).exists():
        user = request.user.id
        employee = Employee.objects.get(user=user)
        applications = Application.objects.filter(userid=employee)
        return render(request, 'employeeprofile.html', {'employee': employee, 'applications': applications})
    elif Employer.objects.filter(userid=request.user).exists():
        user = request.user.id
        employer = Employer.objects.get(userid=user)
        jobs = Job.objects.filter(user_id=employer)
        return render(request, 'employerprofile.html', {'employer': employer, 'jobs': jobs})
    

def update_employee(request, employee_id):
    if request.method == 'POST':
        employee = Employee.objects.get(employeeid=employee_id)
        employee.firstname = request.POST['firstname']
        employee.lastname = request.POST['lastname']
        employee.phonenumber = request.POST['phonenumber']
        employee.email = request.POST['email']
        employee.profession = request.POST['profession']
        employee.location = request.POST['location']
        employee.save()
        messages.success(request, 'Employee details updated successfully.')
        return redirect('account:profile')
    else:
        employee = Employee.objects.get(employeeid=employee_id)
        return render(request, 'updateemployee.html', {'employee': employee})
    
#Write update for employer
def update_employer(request, employer_id):
    if request.method == 'POST':
        employer = Employer.objects.get(employerid=employer_id)
        employer.firstname = request.POST['firstname']
        employer.lastname = request.POST['lastname']
        employer.phonenumber = request.POST['phonenumber']
        employer.email = request.POST['email']
        employer.location = request.POST['location']
        employer.save()
        messages.success(request, 'Employer details updated successfully.')
        return redirect('account:profile')
    else:
        employer = Employer.objects.get(employerid=employer_id)
        return render(request, 'updateemployer.html', {'employer': employer})