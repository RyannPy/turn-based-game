import time

class Skill:
  def __init__(self, name, cost, damage):
    self.name = name
    self.cost = cost
    self.damage = damage
    
  def use(self, user, target):
    if user.sp >= self.cost:
      target.hp -= self.damage # damage skill
      user.sp -= self.cost # biaya
      print(f"{user.name} menggunakan {self.name} | DMG : {self.damage}")
      print("-" * 30)
      return True
    else:
      print("Skill Point tidak cukup.")
      print("-" * 30)
      return False