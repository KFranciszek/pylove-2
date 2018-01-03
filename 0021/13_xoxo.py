def xo_checker(str):
    char_list = list(str.lower())
    x_counter = 0
    o_counter = 0

    for char in char_list:
        if char == "x":
            x_counter += 1
        elif char == "o":
            o_counter += 1
        else:
            print("Illegal letters in text")
            return

    if x_counter == o_counter:
        print("True")
        return True
    else:
        print("False")
        return False

sentence = input("Wpisz jakieś xoxo: ")
xo_checker(str(sentence))

