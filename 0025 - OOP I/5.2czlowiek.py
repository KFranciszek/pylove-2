class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        print("I speak the truth")

    def count_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return "{0:.2f}".format(bmi)

class Politician(Human):
    received_bribe = False

    def __init__(self):
        super().__init__()

    def receive_bribe(self):
        self.received_bribe = True

    def speak(self):
        if self.received_bribe:
            super().speak()
        else:
            print("I lie because I can")

anks = Human("anks", 1.65, 65)
print(anks.count_bmi())
