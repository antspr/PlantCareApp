from django.urls import path
from plants import views

urlpatterns = [
    path('all/', views.all_plants),
    path('add_plant/', views.add_plant),
    path('gardener/<str:id>/', views.get_my_plants),
    path('plant/<str:id>', views.get_plant_by_id),
    path('plant/<str:id>/activate/<str:id>/', views.activate_plant),
]