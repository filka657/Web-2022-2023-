import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "id": 2,
#     "name": "Nikita",
#     "surname": "Filatov"
#     })
# pprint(r.json())

# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Tonya",
#     "user_surname": "Filatova"
#     })
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Red",
#     "user_surname": "Yellow"
#     })
# pprint(r.json())

r = requests.put('http://127.0.0.1:5000/users', json={
    "user_id": 10,
    "user_name": "Yellow",
    "user_surname": "Red"
    })
# pprint(r.json())
# r = requests.delete('http://127.0.0.1:5000/users', json={
#     "user_id": 5,
#     })
# pprint(r.text)
