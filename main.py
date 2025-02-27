import pickle
from dataclasses import dataclass


def main():
    @dataclass
    class Character:
        name: str
        age: str
        type: str

    class Attack():
        name : str
        hp: int
        attack: int
        mana: int

    test = input(" ")
    while test != 'exit':
        try:
            with open('characters.pkl', 'rb') as file:
                loaded_characters = pickle.load(file)
        except FileNotFoundError:

            print("New Character Creation")
            character_count = int(input("How many characters would you like to create? (Max is 4)"))
            while character_count > 4 or character_count < 0:
                character_count = int(input("INVALID : How many characters would you like to create? (Max is 4)"))

            characters = []
            attributes = ['name', 'age', 'type']

            for i in range(character_count):
                print(f'Character creation {i+1}')
                character_data = []
                for j in range(3):
                    attr = input(f'Enter {attributes[j]} of character {i+1}')
                    character_data.append(attr)
                char = Character(character_data[0], character_data[1], character_data[2])
                characters.append(char)

                #work on this
                Attack(character_data[0])
                if character_data[1] <= 18:
                    Attack(character_data[1])
            with open('characters.pkl', 'wb') as file:
                pickle.dump(characters, file)