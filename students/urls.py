from django.urls import path
from .import views

urlpatterns=[
    path('get/',views.get_students),
    path('add/',views.add_students),
]