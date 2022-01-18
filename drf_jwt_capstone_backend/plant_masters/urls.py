from django.urls import path
from plant_masters import views

urlpatterns = [
    path('all/', views.master_plant_list),
    path('add_master/', views.new_master),
    path('master/<str:id>', views.master_by_id),
]