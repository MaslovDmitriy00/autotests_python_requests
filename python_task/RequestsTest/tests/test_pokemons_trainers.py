import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "" #укажите свой токен тренера
HEADER = {"Content-Type" : "application/json",
          "trainer_token" : TOKEN}
MY_TRAINER_ID = "" #укажите свой id тренера

def test__trainers_info__status_code_is_200():
    response = requests.get(
        url = f"{URL}trainers",
        headers = HEADER
    )
    assert response.status_code == 200

def test__trainers_info__my_trainer_id_accessable():
    response = requests.get(
        url = f"{URL}trainers",
        headers = HEADER,
        params = {"trainer_id" : MY_TRAINER_ID}
    )
    assert response.json()['data'][0]["trainer_name"] == "" #укажите имя своего тренера

