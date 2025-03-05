import pickle
from dataclasses import dataclass
import random

def main():
    @dataclass
    class Character:
        def __init__(self,name,age,region):
            self.name = name
            self.age = age
            self.region = region
        
        def add_attack(self,attack):
            pass

        def add_defense(self,defense):
            pass

        def add_hp(self,hplist):
            pass

        def add_items(self,items):
            pass
        
    class WeaponsList:
        def __init__(self,name,attacklist = None,defenselist = None,raisehp = None,itemlist=None):
            self.name = name
            self.attacklist = list()
            self.defenselist = list()
            self.raisehp = list()
            self.itemlist = list()
        def __weaponsnames__(self):
            if Character.region == 'wizard':
                attacks = ['Beam','Staff']
                defense = ['Barrier']
                hp = ['Revive']
                self.attacklist.extend(attacks)
            elif Character.region == 'knight':
                self.attacklist = ['Sword']
                self.defenselist = ['Shield','Block']
            elif Character.region == 'Solider':
                self.attacklist = ['Gun','']
        
    class AttackAttributes():
        def __init__(self,name,damage):
            pass
        
    class Action():
        def __init__(self,name,damage,hp):
            self.name = name
            self.damage = damage
        
        def attack_use(self,target):
            crit = random.random() < 0.2 
            final_damage = self.damage * (2 if crit else 1)
            crit_text = " (Critical Hit!)" if crit else ""
            return f"{Character.name} hits {target} for {final_damage} damage!{crit_text}"


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

            with open('characters.pkl', 'wb') as file:
                pickle.dump(characters, file)