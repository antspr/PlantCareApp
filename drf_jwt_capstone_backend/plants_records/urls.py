from django.urls import path
from plants_records import views

urlpatterns = [
    path('all/', views.all_records),
    path('plant_record/<int>/', views.get_plant_record)
]