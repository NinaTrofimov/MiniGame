import pickle
from dataclasses import dataclass
import random

def main():
    @dataclass
    class Character:
        def __init__(self,name,age,region,hp,mana,attacks,defense,healing,items):
            self.name = name
            self.age = age
            self.region = region
            self.hp = hp
            self.mana = mana
            self.attacks = list()
            self.defense = list()
            self.healing = list()
            self.items = list()
        
        def add_attack(self,attack):
            self.attacks.append(attack)

        def add_defense(self,defense):
            self.defense.append(defense)

        def add_healing(self,healinglist):
            self.healing.append(healinglist)

        def add_items(self,items):
            self.items.append(items)
    
    class itemPocket:
        def __init__(self):
            self.itembag = list()
        
        def __len__(self):
            return len(self.itembag)

        def __append__(self,item):
            if self.__len__() == 20:
                print('Not enough room in your bag')
            else:
                self.itembag.append(item)
        
        def __use__(self, item):
            if item not in self.itembag:
                raise KeyError(str(item) + "not in bag")
            else:
                self.itembag.pop(item)
            


    class WeaponsList:
        def __init__(self,attacklist = None,defenselist = None, healinglist = None,itemlist=None):
            self.attacklist = list()
            self.defenselist = list()
            self.healinglist = list()
            self.itemlist = list()
        def weaponsnames(self,region): # Character.weaponsname(region)
            if region == 'wizard':
                Beam = CharacterItemAttributes('Beam','Attack',15,10)
                Staff = CharacterItemAttributes('Staff','Attack',10,5)

                Barrier = CharacterItemAttributes('Barrier','Defense',15,8)

                Revive = CharacterItemAttributes('Revive','Healing',Character.hp,20)
                Potion = CharacterItemAttributes('Potion','Healing',10,5)

                self.attacklist.extend(Beam,Staff)
                self.defenselist.append(Barrier)
                self.healinglist.extend(Revive,Potion)
            elif region == 'knight':
                Sword = CharacterItemAttributes('Sword','Attack', 25,15)

                Shield = CharacterItemAttributes('Shield','Defense',20,10)
                Block = CharacterItemAttributes('Sword Block','Defense',10,5)

                Food = CharacterItemAttributes('Food','Healing',3,1)

                self.attacklist.append(Sword)
                self.defenselist.extend(Shield,Block)
                self.healinglist.append(Food)
            elif region == 'soldier':
                Gun = CharacterItemAttributes('Bullets','Multi-Attack',10,20)
                Shotgun = CharacterItemAttributes('Shotgun','Attack',20,13)



                self.attacklist.extend(Gun,Shotgun)
            elif region == 'ninja':
                Shuriken = CharacterItemAttributes('Shuriken','Multi-Attack',10,20)
        
    class CharacterItemAttributes():
        def __init__(self,type,count,manacost):
            self.type = type
            self.count = count
            self.manacost = manacost
        
    class Action():
        def __init__(self):
            pass
        def attack_use(self,target):
            crit = random.random() < 0.2 
            final_damage = self.damage * (2 if crit else 1)
            crit_text = " (Critical Hit!)" if crit else ""
            return f"{Character.name} hits {target} for {final_damage} damage!{crit_text}"



main()