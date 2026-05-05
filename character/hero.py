from character.character import Character


class Hero(Character):
  def __init__(self, name, hp, attack, skills):
    super().__init__(name, hp, attack)
    self.sp = 3
    self.skills = skills
    
  def basic_attack(self, target):
    target.hp -= self.attack
    self.sp += 1
    print(f"{self.name} menggunakan Basic Attack | DMG : {self.attack} | +1 SP")
    print("-" * 30)
