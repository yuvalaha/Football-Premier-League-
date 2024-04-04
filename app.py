
import requests
headers = {"X-Auth-Token": "ccaa541fc428481ca29c76efa21b6c0e",}
# Get team matches data from api
def get_team_matches_data():
    try:
        
        url = "http://api.football-data.org/v4/competitions/PL/scorers"
        
        params = {"season": 2022}
        response = requests.get(url, headers=headers, params=params)
        print(response.status_code)
        data = response.json()["scorers"]
        # data = (response.json()["standings"][0]["group"])
        for d in data:
            print (d["goals"])
        # print  (data)
        # print(data)
        return data        
    except Exception as err:
        print(err)
        
#         # 2021
        
get_team_matches_data()     

