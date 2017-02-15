class Bike(object): #Paired Programmed with James Ye and Jon Lee
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return
    def ride(self):
        print "Riding"
        self.miles += 10
        return
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0;
        return
mountain_bike = Bike(800, "80mph")
bmx_bike = Bike(100, "25mph")
road_bike = Bike(50, "15mph")

mountain_bike.ride()
mountain_bike.ride()
mountain_bike.ride()
mountain_bike.reverse()
mountain_bike.displayInfo()

road_bike.ride()
road_bike.ride()
road_bike.reverse()
road_bike.reverse()
road_bike.displayInfo()

bmx_bike.reverse()
bmx_bike.reverse()
bmx_bike.reverse()
bmx_bike.displayInfo()
