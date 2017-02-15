class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0;
        return self
mountain_bike = Bike(800, "80mph")
bmx_bike = Bike(100, "25mph")
road_bike = Bike(50, "15mph")

mountain_bike.ride().ride().ride().reverse().displayInfo()

road_bike.ride().ride().reverse().reverse().displayInfo()

bmx_bike.reverse().reverse().reverse().displayInfo()
