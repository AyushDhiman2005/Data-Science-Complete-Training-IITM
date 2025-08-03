class Character():
    def __init__(self,name,health,attack):
        self.character_name = name
        self.character_health = health
        self.character_attack = attack
        print(f"{name} Health = {health} with attack = {attack}")
    def attack(self):
        print("Character is attacking")

class Warrior(Character):
    def __init__(self, name, health, attack,sword_skill):
        super().__init__(name, health, attack)
        self.swardSkills= sword_skill
    def attack(self):
        print(f"Character is attacking using sward with power = {self.swardSkills}")

class Mage(Character):
    def __init__(self, name, health, attack,magic_power):
        super().__init__(name, health, attack)
        self.magic_Power= magic_power
    def attack(self):
        print(f"Character is attacking using magic power with power = {self.magic_Power}")

class Archer(Character):
    def __init__(self, name, health, attack,bow_skill):
        super().__init__(name, health, attack)
        self.bow_Skill= bow_skill
    def attack(self):
        print(f"Character is attacking using Archery with power = {self.bow_Skill}")

print("_"*40)
char1=Character('Lee',100,15)
char1.attack()

print("_"*40)
char2=Warrior('Paul',120,20,'High')
char2.attack()

print("_"*40)
char3=Mage('King',140,10,'Moderate')
char3.attack()

print("_"*40)
char4=Archer('Law',90,50,'Low')
char4.attack()

print("_"*40)