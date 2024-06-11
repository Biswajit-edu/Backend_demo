from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_app1, name='all_app1'),
]
