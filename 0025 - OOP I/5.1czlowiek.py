class Human:

    def __init__(self):
        pass

    def speak(self):
        print("I speak the truth")

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

anks = Politician()
anks.receive_bribe()
print(anks.speak())
