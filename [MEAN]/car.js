function CarConstructor(name, wheels, passangers) {
  var car = {};     // the object that will eventually be returned
/*
Addition of properties to car
*/
  car.name = name;
  car.wheels = wheels;
  car.passangers = passangers;
/*
Addition of methods to car
*/
  car.honk = function() {
    console.log("Honk! Honk!");
  }
  return car;
}


                      // Create new car
var Sudan = CarConstructor("Sudan", 4, 5);
Sudan.honk();
var bus = CarConstructor("Bus", 6, 100);
bus.honk();
                      // Create bike
var bike = CarConstructor("Bike", 2,2);
                      // here we redefine the method
bike.honk = function() {
  console.log("Ring-ring, I'm on a prissy-ass bike, ring-ring!");
}
bike.honk();
bus.Numpassangers = function(num) {
  if(num < 101) {
  bus.passangers = num;
} else {
  console.log("People overload! CRAAAASSSSHHHHHHHH!!!!!!")
  bus.wheels = 1;
  bus.passangers = 0;
}
}
bus.Numpassangers(32)
console.log(bus.passangers);
bus.Numpassangers(5000);
console.log(bus.passangers);
