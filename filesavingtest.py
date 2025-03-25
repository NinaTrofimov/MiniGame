import pickle
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
                    print(f'Enter {attributes[j]} of character {i+1}')
                    if attributes[j] == 'type':
                        attr = input(f'Pick character class:\n Wizard\n Knight\n Soldier\n Ninja\n')
                    else:
                        attr = input("")
                    character_data.append(attr)
                char = Character(character_data[0], character_data[1], character_data[2])
                characters.append(char)

            with open('characters.pkl', 'wb') as file:
                pickle.dump(characters, file)