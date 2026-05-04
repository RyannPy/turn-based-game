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
  def __init__(self, name, hp, attack):
    super().__init__(name, hp, attack)
    self.sp = 3
    
  def basic_attack(self, target):
    target.hp -= self.attack
    self.sp += 1
    print(f"{self.name} menggunakan Basic Attack | Damage: {self.attack}")
  
  def skill_1(self, target):
    if self.sp >= 1:
      damage = self.attack * 1.5
      target.hp -= damage
      self.sp -= 1
      print(f"{self.name} menggunakan Skill 1, damage: {damage}")
    else:
      print("Skill Point tidak cukup")
      return False
    return True
    
  def skill_2(self, target):
    if self.sp >= 2:
      damage = self.attack * 2
      target.hp -= damage
      self.sp -= 2
      print(f"{self.name} menggunakan Skill 2, damage: {damage}")
    else:
      print("Skill Point tidak cukup")
      return False
    return True

class Enemy(Character):
  pass


hero = Hero("Ryan", 100, 20)
enemy = Enemy("Naruto", 130, 5)

def battle(hero, enemy):
  while hero.is_alive() and enemy.is_alive():
    print(f"{hero.name} HP: {hero.hp} | SP: {hero.sp} | {enemy.name} HP: {enemy.hp}")
    print("-" * 30)
    
    action = input("Pilih aksi (basic/skill1/skill2/heal) : ")
    
    
    if action == "att":
      hero.attack_target(enemy)
      time.sleep(1)
      if enemy.is_alive():
          enemy.attack_target(hero)
      time.sleep(1)
      
    elif action == "skill1":
      success = hero.skill_1(enemy)
      if success:
        if enemy.is_alive():
          enemy.attack_target(hero)
        time.sleep(1)
      else:
        continue

      
    elif action == "skill2":
      success = hero.skill_2(enemy)
      if success:
        if enemy.is_alive():
          enemy.attack_target(hero)
        time.sleep(1)
      else:
        continue
      
    elif action == "heal":
      hero.hp += 10
      print(f"{hero.name} heal +10 HP!")
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