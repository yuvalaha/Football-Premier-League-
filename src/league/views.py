from django.shortcuts import render
import requests
def league_table_data(request):
    url = "http://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": "ccaa541fc428481ca29c76efa21b6c0e"}  # Replace "YOUR_API_KEY" with your actual API key
    response = requests.get(url, headers=headers)
    data = response.json()["standings"][0]["table"]
    context = {"active":"league_table", "league_table":data}
    return render(request, "league_table.html", context)
        
    