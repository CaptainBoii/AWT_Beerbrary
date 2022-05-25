import requests

#response = requests.post('http://127.0.0.1:8000/all_available_rooms_date', data={"start": "202205041030", "end": "202206051330"})
response = requests.post('http://127.0.0.1:8000/beers', data={})
#response = requests.post('http://127.0.0.1:8000/change_theme', data={"user_id": "1", "theme": "2"})
#response = requests.post('http://127.0.0.1:8000/register', data={"username": "Boii", "login": "Boii", "password": "root"})
print(response.json())