
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_jango, name = "all_jango"),
   
]