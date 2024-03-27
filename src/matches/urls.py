from django.urls import path
from . import views


urlpatterns = [
    
    path('', views .matches, name="matches"),

    path('your_team/<int:team_id>', views.team_matches, name="team_matches"),
    
    path('your_team/<int:team_id>/<int:h2h_id>', views.head_to_head, name="head_to_head"),
    
]
