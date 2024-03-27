from django.urls import path 
from . import views

urlpatterns = [
    path("", views.league_table_data, name="league_table"),
]
