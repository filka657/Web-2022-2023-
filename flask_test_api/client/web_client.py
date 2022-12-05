import requests
from pprint import pprint
r = requests.get('http://127.0.0.1:5000/users')
print(r.status_code, r.headers, type(r.text), r.json())
#response = requests.post('http://127.0.0.1:5000/users', data={
#    "name": "Nikita",
#    "surname": "Filatov"
#    })
r = requests.post('http://127.0.0.1:5000/users', json={
    "id": 2,
    "name": "Nikita",
    "surname": "Filatov"
    })
pprint(r.json())
r = requests.post('http://127.0.0.1:5000/users', json={
    "id": 4,
    "name": "Nikita",
    "surname": "Pop"
    })
pprint(r.json())
r = requests.put('http://127.0.0.1:5000/users', json={
    "id": 1,
    "name": "Thom",
    "surname": "Boy"
    })
pprint(r.json())
r = requests.delete('http://127.0.0.1:5000/users', json={
    "id": 0,
    "name": "Alex",
    "surname": "Turner"
    })
pprint(r.text)


