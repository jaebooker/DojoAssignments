function CarConstructor(name, wheels, passangers,speed) {
  if (!(this instanceof CarConstructor)){
  return new CarConstructor(name,wheels,passengers, speed);
}
  this.name = name;
  this.wheels = wheels;
  this.passangers = passangers;
  this.speed = speed;
  this.distance = 0;
}
CarConstructor.prototype.distanceTravelled = function(){
  this.distance = this.speed;
  console.log(this.distance);
}
  CarConstructor.prototype.honk = function() {
    console.log("Honk! Honk!");
  }
  CarConstructor.prototype.moveV = function() {
    this.distanceTravelled()
    this.honk()
  }
  CarConstructor.prototype.check = function(){
    console.log(this.distance)
  }


                      // Create new car
var Sudan = new CarConstructor("Sudan", 4, 5,40);
Sudan.honk();
var bus = new CarConstructor("Bus", 6, 100,"If your gonna do speed, at least share it");
bus.honk();
                      // Create bike
var bike = new CarConstructor("Bike", 2,2,8);
                      // here we redefine the method
bike.honk = function() {
  console.log("Ring-ring, I'm on a prissy-ass bike, ring-ring!");
}
bike.honk();
bus.Numpassangers = function(num) {
  if(num < 101) {
  bus.passangers = num;
} else {
  console.log("People overload! CRRRRRAAAAAAAAASSSSSHHHHHH!!!!!!")
  bus.wheels = 1;
  bus.passangers = 0;
}
}
bus.Numpassangers(32)
console.log(bus.passangers);
bus.moveV();
bus.check();
bus.Numpassangers(5000);
console.log(bus.passangers);
bus.check();
