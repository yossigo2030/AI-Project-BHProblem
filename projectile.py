
class Projectile:

    def __init__(self, location, direction = (0, -1), speed = 5):
        self.location = location
        self.dir = direction
        self.speed = speed


    # dir is a tuple that dictates the direction of enemy movment
    def ProjectileBehaivour(self):
        oldloc = self.location
        self.location = self.location + self.dir
        return oldloc, self.location