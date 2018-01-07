import json

class Czlowiek:
    bmi = 0

    def __init__(self, name = 'anks', height=1.65, weight=30):
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        print("Mówię prawdę")

    def count_bmi(self):
        self.bmi = self.weight / self.height**2
        return self.bmi

    def diff_to_norm(self):
        self.count_bmi()
        min = 18.5
        max = 24.9
        if self.bmi >= min and self.bmi <= max:
            print("Your BMI is normal")
        else:
            if self.bmi < min:
                min_weight = ""
                diff = min - self.bmi
                print("You have to gain %s kg to have normal weight" % diff)
            else:
                max_weight = ""
                diff = self.bmi - max
                print("You have to lose %s kg to have normal weight" % diff)


    def save_data(self):
        with open("{}.json".format(self.name), 'w') as file:
            file.write(json.dumps(self.__dict__))

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    received_bribe = False

    def speak(self):
        if self.received_bribe:
            super().speak()
        else:
            print("Kłamię, bo mogę")

    def receive_bribe(self):
        self.received_bribe = True


anks = Czlowiek()
anks.diff_to_norm()
anks.bmi

anks.save_data()

@dekorator
