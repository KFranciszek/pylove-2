import itertools
n = 0
setA = ['A1', 'A2', 'A3']
setB = ['B1', 'B2', 'B3']
setC = ['C1', 'C2', 'C3']
for element in itertools.product(setA, setB):
    print(element)
    n += 1
print(n)