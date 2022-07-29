
class Enemy():

    def __init__(self, location, health = 1):
        self.location = location
        self.health = health

    # dir is a tuple that dictates the direction of enemy movment
    def move(self, dir):
        # not sure if you can add location like that,
        self.location = location + dir