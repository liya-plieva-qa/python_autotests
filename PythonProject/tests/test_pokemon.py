import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f1f3617380c6dd7da480e2c2690bba0e'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN }
TRAINER_ID = '33616'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_or_response():
    response_get = requests.get(url = f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_get.status_code == 200
 
