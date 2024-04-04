from django.urls import path
from . import views
urlpatterns = [
    path("", views.history, name="history"),
    
    path("/<int:year>", views.history_table, name="history_table"),
    
]
