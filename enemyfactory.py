import abc


class EnemyFactory(abc.ABC):
  
  @abc.abstractmethod
  def create_random_enemy(self):
    "Method that creates and returns enemy objects."
    pass
