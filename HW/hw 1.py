class Hero:
    def __init__(self, name, level,hp,strength):
        self.name = name
        self.level = level
        self.hp = hp
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name} мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -=1

    def rest(self):
        print(f"{self.name} отдыхает ...")
        self.hp +=1


hero1 = Hero("Miki" , 3,100,20)
hero2 = Hero("Dima" , 4,110, 40)

hero1.greet()
print(f"Здоровье: {hero1.hp}, Сила: {hero1.strength}")

hero1.attack()
print(f"После атаки -> Сила:{hero1.strength}")

hero1.rest()
print(f"После отдыха -> Здоровье:{hero1.hp} ")

hero2.greet()
print(f"Здоровье: {hero2.hp}, Сила: {hero2.strength}")

hero2.attack()
print(f"После атаки -> Сила:{hero2.strength}")

hero2.rest()
print(f"После отдыха -> Здоровье:{hero2.hp} ")



