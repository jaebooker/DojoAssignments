def twoface():
    for count in range(0,5000):
        import random
        count = random.randrange(0,2)
        round(count)
        print "The coin is tossed..."
        if count == 0:
            print "You get head!"
        else:
            print "You get some tail!"
twoface()
