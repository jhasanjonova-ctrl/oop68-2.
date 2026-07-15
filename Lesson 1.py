
# HeroMage heroMage
# hero_mage

class Hero:
    # Конструкция класса
    def __init__(self, name, hp,lvl):
        # Атрибуты экземпляра класса
        self.hero_name = name
        self.hero_hp = hp
        self.hero_lvl = lvl

# Метод класса
    def base_action(self):
        return f"this base action {self.hero_name}"

# Объект | Экземпляр класса
kirito = Hero("kirito", 1000, 100)
asuna = Hero("Asuna", 1200, 110)
my_int = 123
my_tuple = (1,2,3)
my_list = [3,2,3,1,2,5,82,12]

print(my_tuple.count(2))
print(my_list)
my_list.sort()
print(my_list)
print(kirito.base_action())
print(asuna.base_action())
# print(kirito.hero_lvl)
# print(asuna.hero_lvl)
