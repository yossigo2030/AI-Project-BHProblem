
class EnemyType:

    def __init__(self, location, health = 1):
        self.location = location
        self.health = health


    # dir is a tuple that dictates the direction of enemy movment
    @abstractmethod
    def EnemyBehaivour(self):
        return