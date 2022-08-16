class cooldown:

    def __init__(self, time):
        self.time = time
        self.counter = time

    def is_ready(self):
        return self.counter == self.time

    def use(self):
        self.counter = 0

    def update(self):
        if not self.is_ready():
            self.counter += 1