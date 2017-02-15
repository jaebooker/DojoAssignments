class Car(object):
    def __init__(self, price, max_speed, fuel, mileage):
        def taxman(x):
            if x > 10000:
                x = x * .15
            else:
                x = x * .10
            return x
        self.price = price
        self.max_speed = max_speed
        self.fuel = fuel
        self.mileage = mileage
        self.mpg = "mpg"
        self.tax = taxman(self.price)
    def displayInfo(self):
        print self.price, self.max_speed, self.fuel, self.mileage, self.mpg, self.tax
        return
mazda = Car(800, "80mph", "diesel", 25)
mustang = Car(80000, "80mph", "gas", 2)
tesla = Car(20000, "500mph", "electric", 10000)
rollsroyce = Car(1500000, "150mph", "only the finest champaign laced with gold", 50)
prius = Car(19.99, "10mph", "kale and the power of love", 100)
batmobile = Car(1000000000,"2000mph", "the darkness and rage that lives inside of my enemies... and within myself", 40)

mazda.displayInfo()
mustang.displayInfo()
tesla.displayInfo()
rollsroyce.displayInfo()
prius.displayInfo()
batmobile.displayInfo()
