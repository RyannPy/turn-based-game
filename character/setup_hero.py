from skill import Skill, make_damage, make_heal
from character.hero import Hero
from character.enemy import Enemy

hero = Hero(
    "Ryan",
    100,
    20,
    [
        Skill("Burning Bow", 1, make_damage(30)),
        Skill("Time to Sleep", 2, make_heal(50))
    ]
)

enemy = Enemy("Naruto", 130, 5)