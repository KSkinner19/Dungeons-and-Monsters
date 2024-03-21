import entity

import random


class EasyGoblin(entity.Entity):

  def __init__(self):
    maxHP = random.randint(4, 6)
    super().__init__("Goblin", maxHP)

  def attack(self, entity):
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
