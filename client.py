import requests

class Client():
    URL = "https://pokeapi.co/api/v2"

    def __init__(self):
        self._setup()

    def _setup(self):
        r = requests.get(f"{self.URL}/pokemon")
        self.pokemon = r.json()['results']

if __name__ == "__main__":
    c = Client()
    print(c.pokemon)
