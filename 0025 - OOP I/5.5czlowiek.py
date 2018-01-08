import json

class Human:
    bmi = 0

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
        self.bmi = self.count_bmi()

        # calculate min i max norm kg
        NORM_MIN = 18 * (self.height ** 2)
        NORM_MAX = 25 * (self.height ** 2)

        if self.bmi > 25:
            diff = self.weight - NORM_MAX
            print("Your weight is {0:.2f} kg above norm.".format(diff))
        if self.bmi < 18:
            diff = NORM_MIN - self.weight
            print("Your weight is {0:.2f}kg below norm.".format(diff))
        elif self.bmi >= 18 and self.bmi <= 25:
            print("Your BMI is normal.")
        return diff

    def save_data(self):
        with open("{}.json".format(self.name), 'w') as new_file:
            new_file.write(json.dumps(self.__dict__))

    def to_burn(self):
        run_per_hour = 500
        bike_per_hour = 600
        hobby_per_hour = 250
        chess_per_hour = 150
        kg_burn = 6000

        diff = self.diff_to_norm()
        if self.bmi > 25:
            run_hours = diff * kg_burn / run_per_hour
            bike_hours = diff * kg_burn / bike_per_hour
            hobby_hours = diff * kg_burn / hobby_per_hour
            chess_hours = diff * kg_burn / chess_per_hour

            print(
                "In order to loose {0:.2f}kg, you need to run for {1:.2f} hours,\
bike for {2:.2f} hours, do hobby for {3:.2f} hours or play chess \
for {4:.2f}".format(
                    diff, run_hours, bike_hours, hobby_hours, chess_hours
                    )
            )
        elif self.bmi < 18:
            print("You need to get weight, not loose it!")
        else:
            print("Hey, you're weight is OK.")




anks = Human("huhuha", 1.65, 75)
anks.diff_to_norm()
anks.to_burn()
