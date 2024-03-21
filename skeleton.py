import entity

import random


class Skeleton(entity.Entity):

  def __init__(self):
    maxHP = random.randint(6, 10)
    super().__init__("Possessed Skeleton", maxHP)

  def attack(self, entity):
    dmg = random.randint(6, 10)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
