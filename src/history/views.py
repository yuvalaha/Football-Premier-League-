from django.shortcuts import render
import requests

headers = {"X-Auth-Token": "ccaa541fc428481ca29c76efa21b6c0e",}
def get_history_data(year):
    try:    
        url = f"http://api.football-data.org/v4/competitions/PL/standings"
        params = {"season": year}
        response = requests.get(url, headers=headers,params=params)
        data = (response.json()["standings"][0]["table"])
        return data
    except Exception as err:
        print(err)
        
        
def get_scorers_data(year):
    try:
        
        url = "http://api.football-data.org/v4/competitions/PL/scorers"  
        params = {"season": year, "limit":5}
        response = requests.get(url, headers=headers, params=params)
        print(response.status_code)
        data = response.json()["scorers"]
        return data        
    except Exception as err:
        print(err)        
        
        
def history(request):
    context = {"active":"history"}
    return render(request, "history.html", context)

def history_table(request, year):
    try:
        print(year)
        history_data = get_history_data(year)
        scorers_data=  get_scorers_data(year)
        context = {"history" : history_data,
                   "scorers" : scorers_data, 
                   "year": year,"active":"history"}  
        
        return render(request, "history_table.html", context)
        
    except Exception as err:
        print(err)