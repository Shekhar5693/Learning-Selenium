from animal import Animal

class Dog(Animal):
    sound = "woof!"

    def __init__(self):
        super().__init__(Dog.sound)