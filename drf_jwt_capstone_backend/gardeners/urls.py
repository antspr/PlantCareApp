from django.urls import path
from gardeners import views

urlpatterns = [
    path('', views.GardenerList.as_view())
]