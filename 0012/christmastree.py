
size = int(input("Give christmas tree size:"))
z = size - 1
x = 1
for i in range(size):
    print(' ' * z + '+' * x + ' ' * z)
    x+=2
    z-=1
