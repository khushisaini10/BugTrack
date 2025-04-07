from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_list, name='bug_list'),
    path('add/', views.add_bug, name='add_bug'),
]
