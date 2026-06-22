from django.urls import path
from . import views

urlpatterns = [
    # API URLs
    path('', views.get_teachers, name='teachers_api'),
    path('add/', views.add_teachers, name='add_teachers_api'),

    # UI URLs
    path('list/', views.teacher_list, name='teacher_list'),
    path('<int:id>/', views.teacher_detail, name='teacher_detail'),
    path('add-teacher/', views.add_teacher_page, name='add_teacher'),
    path('edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
]
