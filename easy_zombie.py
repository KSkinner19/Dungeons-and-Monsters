import entity

import random


class EasyZombie(entity.Entity):

  def __init__(self):
    maxHP = random.randint(4, 5)
    super().__init__("Zombie", maxHP)

  def attack(self, entity):
    dmg = random.randint(1, 5)
    entity.take_damage(dmg)
    return f"{self.name} attacks {entity.name} for {dmg} damage."
