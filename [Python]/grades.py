def grades():
    for count in range (0,10):
        import random
        count = random.randrange(60,101)
        print count
        if count > 89:
            print"That's a scarlet letter!"
        if count <90 and count >79:
            print"That's a b"
        if count <80 and count >69:
            print"Cs get degrees"
        if count <70:
            print"Suck on that D, boy!"
grades()
