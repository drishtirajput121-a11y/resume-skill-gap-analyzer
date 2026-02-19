from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='analyzer/login.html', authentication_form=UserLoginForm), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('upload/', views.upload_resume, name='upload_resume'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]
