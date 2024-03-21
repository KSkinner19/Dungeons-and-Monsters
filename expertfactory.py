import goblin
import skeleton
import zombie
import enemyfactory


import random


class ExpertFactory(enemyfactory.EnemyFactory):

  def create_random_enemy(self):
    randomChoice = random.randint(1, 3)
    if randomChoice == 1:
      return goblin.Goblin()
    elif randomChoice == 2:
      return skeleton.Skeleton()
    else:
      return zombie.Zombie()
