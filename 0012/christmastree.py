def christmas_tree(size):
    size = int(input("Give christmas tree size:"))
    zzz = size - 1
    xxx = 1
    for _ in range(size):
        print(' ' * zzz + '+' * xxx + ' ' * zzz)
        xxx += 2
        zzz -= 1
