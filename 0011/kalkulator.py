while True: 
    first_num = input('Wprowadź pierwszą liczbę:')
    try: 
        first_num = int(first_num)
    except ValueError:
        print("Not a valid integer")
        continue  
    symbol = input("Wprowadź znak operacji matematycznej (+, -, \*, /):")
    try:
        index = ['+', '-', '*', '/'].index(symbol)    
    except ValueError:
        print("Not a valid operator")
        continue        
    second_num = input('Wprowadź drugą liczbę:')
    try: 
        second_num = int(second_num)
    except ValueError:
        print("Not a valid integer")
        continue  
    break

if symbol == '+':
    result = int(first_num) + int(second_num)
elif symbol == '-':
    result = int(first_num) - int(second_num)
elif symbol == '*':
    result = int(first_num) * int(second_num)
elif symbol == '/':
    result = int(first_num) / int(second_num)

print("{} {} {} = {}".format(first_num, symbol, second_num, result))

