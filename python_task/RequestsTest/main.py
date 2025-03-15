import requests

URL = "https://api.pokemonbattle.ru/v2/"
TOKEN = "" #укажите свой токен тренера
HEADER = {"Content-Type" : "application/json",
          "trainer_token" : TOKEN}


response_create_pokemon = requests.post(
    url = f"{URL}pokemons",
    headers = HEADER,
    json = {"name": "microchel the 2450", #необходимо править под себя
            "photo_id": 549}
)

print(response_create_pokemon.text)

pokemon_id = response_create_pokemon.json()['id']

response_change_pokemon = requests.put(
    url = f"{URL}pokemons",
    headers = HEADER,
    json = {"pokemon_id": pokemon_id, #необходимо править под себя
            "name": "microchel the 245",
            "photo_id": 548}
)

print(response_change_pokemon.text)

response_catch_pokemon = requests.post(
    url = f"{URL}trainers/add_pokeball",
    headers = HEADER,
    json = {"pokemon_id": pokemon_id}
)

print(response_catch_pokemon.text)
