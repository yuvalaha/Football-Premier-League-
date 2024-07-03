import requests
from django.shortcuts import render
from datetime import datetime 
import matplotlib.pyplot as plt
import os


headers = {"X-Auth-Token": "ccaa541fc428481ca29c76efa21b6c0e",}
# Get team matches data from api
def get_team_matches_data(team_id):
    try:
        time = (str(datetime.today()))[:10]
        url = f"http://api.football-data.org/v4/teams/{team_id}/matches"
        
        params = {"dateFrom": time,
                "dateTo": "2025-05-30",}
        response = requests.get(url, headers=headers, params=params)
        print(response.json())
        return response.json()        
    except Exception as err:
        print(err)


# Get teams head 2 head data from api
def get_teams_head_to_head(match_id):
    try:
        url = f"http://api.football-data.org/v4/matches/{match_id}/head2head?limit=20"
        response = requests.get(url, headers=headers)
       
        return response.json() 
    except Exception as err:
        print(err)

# Get pie chart H2H


def generate_graph(match_id):
    h2h_data = get_teams_head_to_head(match_id)
    # Extract relevant data for the graph
    home_team_wins = h2h_data['aggregates']['homeTeam']['wins']
    away_team_wins = h2h_data['aggregates']['awayTeam']['wins']
    draws = h2h_data['aggregates']['awayTeam']['draws']
    
    # Define labels and values for the pie chart
    labels = [f"{h2h_data['aggregates']['homeTeam']['name']}", f"{h2h_data['aggregates']['awayTeam']['name']}", 'Draws']
    values = [home_team_wins, away_team_wins, draws]

    # Plot the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Add title
    plt.title('Head to Head Statistics', pad=30, fontsize=20)
    

    # Save the pie chart to a file
    graph_filename = 'src/static/images/head_to_head_pie_chart.png'
    plt.savefig(graph_filename, transparent = True)

    # Close the plot to release memory
    plt.close()

    # Return the filename of the generated pie chart
    return graph_filename



# All teams
def matches(request):
    context = {"active": "matches"}
    return render(request, "matches.html", context)

# One team matches
def team_matches(request, team_id):
    context = {"matches": get_team_matches_data(team_id), "team_id":team_id}
    return render(request, "team_matches.html", context)

# Head 2 head between 2 teams
def head_to_head(request, team_id, h2h_id):
    context = {"h2h": get_teams_head_to_head(h2h_id)}
    generate_graph(h2h_id)
    return render(request, "head2head.html", context)
