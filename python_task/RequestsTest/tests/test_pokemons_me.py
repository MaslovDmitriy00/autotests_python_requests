import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "" #укажите свой токен тренера
HEADER = {"Content-Type" : "application/json",
          "trainer_token" : TOKEN}

def test__my_trainer_info__status_code_is_200():
    response = requests.get(
        url = f"{URL}me",
        headers = HEADER
    )
    assert response.status_code == 200

def test__my_trainer_info__part_of_response__actual_avatar_id():
    response = requests.get(
        url = f"{URL}me",
        headers = HEADER
    )
    assert response.json()['data'][0]["avatar_id"] == 5

@pytest.mark.parametrize('key, value', [('trainer_name', 'Макрочел'), ('id', '17416')])
def test__my_trainer_info__part_of_response__trainer_name__trainer_id(key, value):
    response = requests.get(
        url = f"{URL}me",
        headers = HEADER
    )
    assert response.json()['data'][0][key] == value

# print(response, response.text)