from django.urls import path
from . import views

urlpatterns = [
    path('add-parent/', views.add_parent, name='add_parent'),
    path('list/', views.parent_list, name='parent_list'),
]
