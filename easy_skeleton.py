import entity

import random


class EasySkeleton(entity.Entity):

  def __init__(self):
    maxHP = random.randint(3, 4)
    super().__init__("Skeleton", maxHP)

  def attack(self, entity):
    dmg = random.randint(1, 4)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
