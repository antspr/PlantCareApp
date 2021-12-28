from django.urls import path
from plants_records import views

urlpatterns = [
    path('', views.Plant_RecordList.as_view())
]