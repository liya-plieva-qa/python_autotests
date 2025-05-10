import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f1f3617380c6dd7da480e2c2690bba0e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
body_registration = {
    "trainer_token": TOKEN,
    "email": "liyaplieva@yandex.ru",
    "password": "98GfRttt"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": '312080',
    "name": "Salut",
    "photo_id": 1
}

body_pokeboll = {
    "pokemon_id": "312080"
}

'''respons = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(respons.text)'''

'''respons_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(respons_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''


response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeball.text)
