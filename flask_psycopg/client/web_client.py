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
#     "user_name": "Donald",
#     "user_surname": "Duck"
#     })
# r = requests.post('http://127.0.0.1:5000/users', json={
#     "user_name": "Red",
#     "user_surname": "Yellow"
#     })
# pprint(r.json())

# r = requests.put('http://127.0.0.1:5000/users', json={
#     "user_id": 19,
#     "user_name": "Donald",
#     "user_surname": "Ivanov"
#     })
# pprint(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={
    "user_id": 19,
    })
# pprint(r.text)
