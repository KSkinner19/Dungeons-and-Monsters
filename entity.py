import abc


class Entity(abc.ABC):
  """Abstract class - Describes a character in the game
  Attributes:
    _name - name of the enemy
    max_hp - max health of the enemy
  """

  def __init__(self, name, max_hp):
    """Initializes the name and hp of the entity."""
    self._name = name
    self._hp = max_hp
    self.max_hp = max_hp

  @property
  def name(self):
    return self._name

  @property
  def hp(self):
    return self._hp

  def take_damage(self, dmg):
    """Subtracts the dmg from the hp, but does not allow the hp to drop below 0"""
    if dmg >= self._hp:
      self._hp = 0
    else:
      self._hp -= dmg

  def heal(self):
    """Restores the entity's hp to max_hp"""
    self._hp = self.max_hp

  def __str__(self):
    """Returns entity's name and hp"""
    return f"{self._name}\nHP: {self._hp}/{self.max_hp}"

  @abc.abstractmethod
  def attack(self, entity):
    """Attack and do damage to the oppisng entity"""
    pass
