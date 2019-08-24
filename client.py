import requests

MAX_POKEMON = 964

class Client():
    URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        self.pokemon = self._get_list_of_pokemon(MAX_POKEMON)

    def _get_list_of_pokemon(self, limit=20)
        r = requests.get(f"{self.URL}/pokemon?limit={limit}")
        return r.json()['results']

if __name__ == "__main__":
    c = Client()
    print(c.pokemon)
