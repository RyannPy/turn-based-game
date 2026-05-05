from character.character import Character

class Enemy(Character):
  def __init__(self, name, hp, attack):
    super().__init__(name, hp, attack)
    
  def basic_attack(self, target):
    target.hp -= self.attack
    print(f"{self.name} menggunakan Basic Attack | DMG : {self.attack}")
    print("-" * 30)