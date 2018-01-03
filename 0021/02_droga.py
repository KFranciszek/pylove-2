def droga(t, a, vs=0):
    result = vs*t + (a * (t **2))/2
    print(result)

droga(5, 5)
droga(10, 10, vs=100)
