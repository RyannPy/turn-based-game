import time

class Skill:
  def __init__(self, name, cost, effect):
    self.name = name
    self.cost = cost
    self.effect = effect
    
  def use(self, user, target):
    if user.sp >= self.cost:
      user.sp -= self.cost # biaya
      print(f"{user.name} menggunakan {self.name}")
      self.effect(user, target) # efek
      print("-" * 30)
      return True
    else:
      print("Skill Point tidak cukup.")
      print("-" * 30)
      return False
      
      
      
# Fungsi Effect Skill
def make_damage(value):
  def effect(user, target):
    target.hp -= value
    print(f"DMG : {value}")
  return effect
  
def make_heal(value):
  def effect(user, target):
    user.hp += value
    print(f"+ {value} HP")
  return effect