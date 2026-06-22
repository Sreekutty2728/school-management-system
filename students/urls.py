from django.urls import path
from . import views

urlpatterns = [

    # Existing API URLs
    path('get/', views.get_students),
    path('add/', views.add_students),

    # Dashboard UI URLs
    path('dashboard/', views.dashboard, name='dashboard'),
    path('classes/', views.class_list, name='class_list'),
    path('class/<str:class_no>/', views.student_list, name='student_list'),
    path( '<int:id>/',
    views.student_detail,
    name='student_detail'),
    path('add-student/', views.add_student_page, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path(
    'edit/<int:id>/',
    views.edit_student,
    name='edit_student'
),
    path('delete/<int:id>/',
    views.delete_student,
    name='delete_student'
),
]