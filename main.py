#!/usr/bin/env python3

from client import Client

def main():
    exit_flag = False
    c = Client()

    while exit_flag == False:
        command = input("Enter command: ")
        if command == "hello":
            print("Hello World!")
        elif command == "exit":
            exit_flag = True
        elif command == "pokemon":
            n_pokemon = len(c.pokemon)
            print(f"There are {n_pokemon} pokemon.")

if __name__ == "__main__":
    main()
