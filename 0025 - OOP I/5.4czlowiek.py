class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def speak(self):
        print("I speak the truth")

    def count_bmi(self):
        bmi = self.weight / (self.height ** 2)
        return float("{0:.2f}".format(bmi))

    def diff_to_norm(self):
        bmi = self.count_bmi()

        # calculate min i max norm kg
        NORM_MIN = 18 * (self.height ** 2)
        NORM_MAX = 25 * (self.height ** 2)

        if bmi > 25:
            diff = self.weight - NORM_MAX
            print("Your weight is {0:.2f} kg above norm.".format(diff))
        if bmi < 18:
            diff = NORM_MIN - self.weight
            print("Your weight is {0:.2f}kg below norm.".format(diff))
        elif bmi >= 18 and bmi <= 25:
            print("Your BMI is normal.")


anks = Human("anks", 1.65, 45)
print(anks.count_bmi())
print(anks.diff_to_norm())
