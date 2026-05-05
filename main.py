import time
from character.setup_hero import hero, enemy

# PLAY
def battle(hero, enemy):
  while hero.is_alive() and enemy.is_alive():
    print("-" * 30)
    print(f" | {hero.name} HP: {hero.hp} | SP: {hero.sp} | ")
    print(f" | {enemy.name} HP: {enemy.hp} |")
    print("-" * 30)
    
    print("Aksi:")
    print("basic")
    for i, skill in enumerate(hero.skills):
      print(f"{i+1}. {skill.name} (Cost: {skill.cost})")
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
      
      
    else:
      print("Input tidak valid")
      continue
      
  if hero.is_alive():
      print(f"{hero.name} menang!")
  else:
      print(f"{enemy.name} menang!")
      
battle(hero, enemy)