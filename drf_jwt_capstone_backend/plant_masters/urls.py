from django.urls import path
from plant_masters import views

urlpatterns = [
    path('', views.Plants_MastersList.as_view())
]