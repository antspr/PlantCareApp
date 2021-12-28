from django.urls import path
from plants import views

urlpatterns = [
    path('', views.PlantList.as_view())
]