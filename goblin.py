import entity

import random


class Goblin(entity.Entity):

  def __init__(self):
    maxHP = random.randint(8, 12)
    super().__init__("Angry Goblin", maxHP)

  def attack(self, entity):
    dmg = random.randint(6, 12)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
