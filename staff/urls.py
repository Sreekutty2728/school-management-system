from django.urls import path
from . import views

urlpatterns = [
    path('add-staff/', views.add_staff, name='add_staff'),
    path('list/', views.staff_list, name='staff_list'),
]