from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
from .views import upload_certificate

app_name = "account"

urlpatterns = [
    path("", views.base, name="base"),
    #path("signup", views.user_signup, name="signup"),
    path("signup/employer", views.employer_sign_up, name="signupemployer"),
    path("signup/employee", views.employee_sign_up, name="signupemployee"),
    path("login/", views.user_login, name="login"),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
    path('update_employer/<int:employer_id>/', views.update_employer, name='update_employer'),
]