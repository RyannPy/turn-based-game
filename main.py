import time
from skill import Skill

class Character:
  def __init__(self, name, hp, attack):
    self.name = name
    self.hp = hp
    self.attack = attack
    
  
  def is_alive(self):
    return self.hp > 0
    

class Hero(Character):
  def __init__(self, name, hp, attack):
    super().__init__(name, hp, attack)
    self.sp = 3
    self.skills = []
    
  def basic_attack(self, target):
    target.hp -= self.attack
    self.sp += 1
    print(f"{self.name} menggunakan Basic Attack | DMG : {self.attack} | +1 SP")
    print("-" * 30)


class Enemy(Character):
  def __init__(self, name, hp, attack):
    super().__init__(name, hp, attack)
    
  def basic_attack(self, target):
    target.hp -= self.attack
    print(f"{self.name} menggunakan Basic Attack | DMG : {self.attack}")
    print("-" * 30)


hero = Hero("Ryan", 100, 20)
skill1 = Skill("Burning Bow", 1, 30)
skill2 = Skill("Last Rythm", 2, 50)

hero.skills.append(skill1)
hero.skills.append(skill2)

enemy = Enemy("Naruto", 130, 5)

def battle(hero, enemy):
  while hero.is_alive() and enemy.is_alive():
    print("-" * 30)
    print(f"{hero.name} HP: {hero.hp} | SP: {hero.sp} | {enemy.name} HP: {enemy.hp}")
    print("-" * 30)
    
    print("Aksi:")
    print("basic")
    for i, skill in enumerate(hero.skills):
      print(f"{i+1}. {skill.name} (Cost: {skill.cost})")
    print("heal")
    action = input("Pilih aksi: ")
    
    if action == "basic":
      hero.basic_attack(enemy)
      time.sleep(1)
      if enemy.is_alive():
          enemy.basic_attack(hero)
      time.sleep(1)
      
    if action.isdigit():
      index = int(action) - 1
      if 0 <= index < len(hero.skills):
        success = hero.skills[index].use(hero, enemy)
        if success:
          if enemy.is_alive():
            enemy.basic_attack(hero)
          time.sleep(1)
        else:
          continue
      else:
        print("Skill tidak valid.")
        continue
      
    elif action == "heal":
      hero.hp += 10
      print(f"{hero.name} heal +10 HP!")
      if enemy.is_alive():
          enemy.basic_attack(hero)
      time.sleep(1)
      
      
      
      
    else:
      print("Input tidak valid")
      continue
      
  if hero.is_alive():
      print(f"{hero.name} menang!")
  else:
      print(f"{enemy.name} menang!")
      
battle(hero, enemy)