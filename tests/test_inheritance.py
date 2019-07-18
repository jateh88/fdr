class Bird:
    wingspan = None

class Duck(Bird):
    pass

class Turkey(Bird):
    pass

duck = Duck()
duck.wingspan = 42
print(duck.wingspan)

turkey = Turkey()
turkey.wingspan = 100
print(turkey.wingspan)

print(duck.wingspan)
