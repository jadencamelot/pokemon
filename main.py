#!/usr/bin/env python3

from client import Client


def main():
    exit_flag = False
    c = Client()

    while exit_flag is False:
        command = input("Enter command: ").lower()
        if command == "exit":
            exit_flag = True
        elif command == "list":
            list_pokemon(c)
        elif command == "count":
            count(c)
        elif command == "search":
            search(c)


def list_pokemon(c):
    for i, pokemon_name in enumerate(c.pokemon_list()):
        print(f"{str(i+1)}. {pokemon_name}")


def count(c):
    n_pokemon = c.pokemon_count()
    print(f"There are {str(n_pokemon)} pokemon.")


def search(c):
    search_term = input("Pokemon name: ")
    search_result = c.pokemon_search(search_term)
    if search_result:
        abilities = search_result['abilities']
        pretty_print_abilities(abilities)
    else:
        print(f"Pokemon {search_term} not found!")


def pretty_print_abilities(abilities):
    print("\n-- Abilities --\n")
    for ability in abilities:
        is_hidden = ability['is_hidden']
        if is_hidden:
            hidden_str = "(hidden)"
        else:
            hidden_str = ""

        print(f"Name: {ability['ability']['name'].capitalize()} {hidden_str}")
        print(f"  Slot: {ability['slot']}")
    print()


if __name__ == "__main__":
    main()
