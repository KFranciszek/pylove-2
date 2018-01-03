while True:
    weight = input("Give you weight in kg: ")
    try: 
        weight = float(weight)
    except ValueError:
        print("Not a valid float")
        continue  
    height = input("Give your height in m2: ")
    try: 
        height = float(height)
    except ValueError:
        print("Not a valid float")
        continue
    break  

bmi = float(weight)/(float(height)**2)
print("Your bmi is {}".format(bmi))
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("normal weight")
elif bmi >= 25.0:
    print("overweight")
else:
    print("your data seem to be pretty incorrect...")