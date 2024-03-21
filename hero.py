import random

import entity
import map


class Hero(entity.Entity):
  """Represetns a hero
  Attributes:
    _name - name of the enemy
    max_hp - max health of the enemy
  """

  def __init__(self, name):
    """Initializes the name, hp, location of the hero."""
    super().__init__(name, 25)
    self._location = [0, 0]

  @property
  def location(self):
    return self._location

  def attack(self, entity):
    """Hero attacks the enemy"""
    dmg = random.randint(2, 5)
    entity.take_damage(dmg)
    return f"{self._name} attacks a {entity._name} for {dmg} damage."

  def go_north(self):
    m = map.Map()
    if len(self._location) - 1 < len(m) - 1:
      if self._location[0] > 0:
        self._location[0] -= 1
        m.reveal(self.location)
        return m[self.location[0]][self.location[1]]
      else:
        return 'o'
    return 'o'

  def go_south(self):
    m = map.Map()
    if len(self._location) - 1 < len(m) - 1:
      if self._location[0] < 4:
        self._location[0] += 1
        m.reveal(self.location)
        return m[self.location[0]][self.location[1]]
      else:
        return 'o'
    else:
      return 'o'

  def go_east(self):
    m = map.Map()
    if len(self._location) - 1 < len(m) - 1:
      if self._location[1] < 4:
        self._location[1] += 1
        m.reveal(self.location)
        return m[self.location[0]][self.location[1]]
      else:
        return 'o'
    else:
      return 'o'

  def go_west(self):
    m = map.Map()
    if len(self._location) - 1 < len(m) - 1:
      if self._location[1] > 0:
        self._location[1] -= 1
        m.reveal(self.location)
        return m[self.location[0]][self.location[1]]
      else:
        return 'o'
    else:
      return 'o'
