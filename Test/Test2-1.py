from abc import ABC, abstractmethod


class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Mar {self.name}кастует заклинание! MP: {self.mp}")


class WarrionHero(MageHero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccaunt:
    bank_name = "Simba Bank"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        if password == self.__password:
            return "Вход выполнен !"
        return "Неверный пароль !"

    @property
    def full_info(self):
        return f"Герой : {self.hero.name}, Баланс: {self._balance} SOM"

    def get_bank_name(self):
        return BankAccaunt.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} |  Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) == type(other.hero):
            return self._balance + other._balance
        return "Ошибка! Герои разных классов."

    def __eq__(self, other):
        return (type(self.hero) == type(
            other.hero) and self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl)


class Sms(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass


class KGSms(Sms):

    def send_otp(self, phone):
        return f"ОТП отправлен на номер {phone}"


mage1 = MageHero("Merlin", 5, 100, 80)
mage2 = MageHero("Merlin", 5, 120, 100)
warrior = WarrionHero("Arthur", 5, 200, 0)

acc1 = BankAccaunt(mage1, 1000, "1234")
acc2 = BankAccaunt(mage2, 1500, "5678")
acc3 = BankAccaunt(warrior, 2000, "9999")

print("=== Hero ===")
mage1.action()
warrior.action()

print("\n=== Bank ===")
print(acc1.login("1234"))
print(acc1.full_info)
print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __str__ ===")
print(acc1)

print("\n=== Проверка __add__ ===")
print("Сумма всех двух счетов  магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

print("\n=== SMS ===")
sms = KGSms()
print(sms.send_otp("+996777123456"))