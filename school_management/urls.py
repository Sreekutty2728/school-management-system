"""
URL configuration for school_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.db.models import Count

from django.conf import settings
from django.conf.urls.static import static

# Configure logger
logger = logging.getLogger(__name__)


def login_page(request):
    return render(request, 'login.html')

def admin_dashboard(request):
    from students.models import Student
    from teachers.models import Teachers
    from parents.models import Parent
    from staff.models import Staff

    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teachers.objects.count(),
        'total_parents': Parent.objects.count(),
        'total_staff': Staff.objects.count(),
    } 
    return render(request, 'admin_dashboard.html', context)


def home(request):
    logger.info(f"GET / - Home page request from {request.META.get('REMOTE_ADDR', 'Unknown')}")
    from students.models import Student
    from teachers.models import Teachers
    
    total_students = Student.objects.count()
    total_teachers = Teachers.objects.count()
    
    logger.info(f"Home page - Total Students: {total_students}, Total Teachers: {total_teachers}")
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
    }
    
    logger.info(f"Home page context prepared: {list(context.keys())}")
    return render(request, 'index.html', context)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('teachers/', include('teachers.urls')),
    path('students/', include('students.urls')),
    path('parents/', include('parents.urls')),
    path('staff/', include('staff.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)