from django.urls import path
from gardeners import views

urlpatterns = [
    path('register_profile/', views.register_gardener)
]