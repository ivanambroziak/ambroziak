from random import randint
from time import sleep
win = 0

class Hero():
    def __init__(self, name, health, power, armor, weapon, stature):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.weapon = weapon
        self.stature = stature

    def print_info(self):
        print("Його ім'я", self.name)
        print("Статура:", self.stature)
        print("Здоров'я:", self.health)
        print("Броня:", self.armor)
        print("Зброя:", self.weapon)

    def strike(self, enemy):
        print("Удар!", self.name, "атакує", enemy.name)
        sleep(1)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "броня:", enemy.armor, "та здоров'я:", enemy.health)
        sleep(1)

    def fight(self, enemy):
        while self.health > 0 or enemy.health > 0:
            self.strike(enemy)
            if enemy.health <= 0:
                print(enemy.name, "програв у бою")
                sleep(1)
                break
            enemy.strike(self)
            if self.health <= 0:
                print(self.name, "програв у бою")
                sleep(1)
                break

class Fox(Hero):
    def __init__(self, name, health, power, armor, weapon, stature):
        super().__init__(name, health, power, armor, weapon, stature)

    def strike(self, enemy):
        print("Укус!!!", self.name, "кусає", enemy.name)
        enemy.armor = enemy.armor - self.power
        if enemy.armor <= 0:
            enemy.health = enemy.health + enemy.armor
            enemy.armor = 0
        print(enemy.name, "броня:", enemy.armor, "та здоров'я:", enemy.health)
        sleep(1)
