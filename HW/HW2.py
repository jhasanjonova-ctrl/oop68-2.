import random
class Hero:
    def __init__(self, name,level, health,strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name} мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар! ")

    def rest(self):
        print(f"{self.name} отдыхает и восстанавливает здоровье")

class Warrior (Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name}: Воин аттакует мечом!")


class Mage (Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name}: Маг кастует заклинание! ")

class Assassin (Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name}: Ассасин атакует из-под тишка!")

warrior = Warrior("Воин", 10, 100, 20, 50)
mage = Mage("Маг", 12,80,15,90)
assassin = Assassin("Ассасин",11,90,18,70)

warrior.greet()
warrior.attack()
warrior.rest()
mage.greet()
mage.attack()
mage.rest()
assassin.greet()
assassin.attack()
assassin.rest()

choice = input("Выберите героя(Warrior / Mage / Assassin):")
if choice == "Warrior":
    player = warrior
elif choice == "Mage":
    player = mage
elif choice == "Asssassin":
    player = assassin
else:
    print("Неверный выбор!")
    exit()

enemy = random.choice([warrior, mage, assassin])
