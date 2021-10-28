class Animal:
    def __init__(self,sound):
        self.sound = sound
    
    def speak(self, word):
        print(self.sound, word)

    def move(self, distance=1):
        print(self.__class__.__name__, "moves " + str(distance))