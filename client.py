import requests


class Client():
    URL = "https://pokeapi.co/api/v2"
    MAX_POKEMON = 964

    def __init__(self):
        self._pokemon = self._get_list_of_pokemon(self.MAX_POKEMON)

    def _get_list_of_pokemon(self, limit=20):
        print("Loading list of pokemon...")

        r = requests.get(f"{self.URL}/pokemon?limit={limit}")
        results = r.json()['results']

        # Parse results
        return self._parse_pokemon_list(results)

    def _parse_pokemon_list(self, pokemon_list):
        parsed_pokemon = {}
        for pokemon in pokemon_list:
            name = pokemon['name']
            url = pokemon['url']
            parsed_pokemon[name] = url
        return parsed_pokemon

    def pokemon_list(self):
        return self._pokemon.keys()

    def pokemon_count(self):
        return len(self._pokemon)

    def pokemon_search(self, pokemon_name):
        if pokemon_name not in self._pokemon:
            return None

        url = self._pokemon[pokemon_name]
        pokemon_info = self._get_pokemon_info(url)
        return pokemon_info

    def _get_pokemon_info(self, url):
        r = requests.get(url)
        return r.json()


if __name__ == "__main__":
    c = Client()
    print(f"{str(len(c._pokemon))} pokemon loaded successfully.")
