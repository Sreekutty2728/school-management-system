from django.urls import path
from .import views

urlpatterns=[
    path('',views.get_teachers),
    #GET teachers list
    path('add/',views.add_teachers),
    #ADD teacher
]