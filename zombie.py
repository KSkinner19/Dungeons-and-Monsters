import entity

import random


class Zombie(entity.Entity):

  def __init__(self):
    maxHP = random.randint(8, 10)
    super().__init__("Fast Zombie", maxHP)

  def attack(self, entity):
    dmg = random.randint(5, 12)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
