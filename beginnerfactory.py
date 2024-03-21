import random

import easy_goblin
import easy_skeleton
import easy_zombie
import enemyfactory


class BeginnerFactory(enemyfactory.EnemyFactory):

  def create_random_enemy(self):
    randomChoice = random.randint(1, 3)
    if randomChoice == 1:
      return easy_goblin.EasyGoblin()
    elif randomChoice == 2:
      return easy_skeleton.EasySkeleton()
    else:
      return easy_zombie.EasyZombie()
