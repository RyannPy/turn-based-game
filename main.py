import time

class Character:
  def __init__(self, name, hp, attack):
    self.name = name
    self.hp = hp
    self.attack = attack
    
  def attack_target(self, target):
    target.hp -= self.attack
    if target.hp <= 0:
      target.hp = 0
    print(f"{self.name} menyerang {target.name} dengan damage {self.attack}. Sisa HP {target.name} = {target.hp}")
    print("-" * 30)
    
  
  def is_alive(self):
    return self.hp > 0
    

class Hero(Character):
  pass

class Enemy(Character):
  pass


hero = Hero("Ryan", 100, 20)
enemy = Enemy("Naruto", 130, 5)

def battle(hero, enemy):
  while hero.is_alive() and enemy.is_alive():
    print(f"{hero.name} HP: {hero.hp} | {enemy.name} HP: {enemy.hp}")
    print("-" * 30)
    action = input("Pilih aksi (att): ")
    if action == "att":
      hero.attack_target(enemy)
      time.sleep(1)
      if enemy.is_alive():
          enemy.attack_target(hero)
      time.sleep(1)
    else:
      print("Input tidak valid")
      continue
      
  if hero.is_alive():
      print(f"{hero.name} menang!")
  else:
      print(f"{enemy.name} menang!")
      
battle(hero, enemy)