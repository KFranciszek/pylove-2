
def cenzura_cyfr(incoming):
    char_list = list(str(incoming))
    cyfry = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for idx, char in enumerate(char_list):
        if char in cyfry:
            char_list[idx] = "#"
    print(''.join(char_list))

cenzura_cyfr("hahaha11234bububu")