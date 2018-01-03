
def policz_samogloski(str):
    char_list = list(str.lower())
    samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
    counter = 0
    for char in char_list:
        if char in samogloski:
            counter += 1
    print(counter)

sentence = input("Wpisz zdanie: ")
policz_samogloski(sentence)