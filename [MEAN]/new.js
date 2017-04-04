function NinjaConstructor(name, age, prevOccupation) {
  var ninja = {};     // the object that will eventually be returned
/*
Addition of properties to ninja.
*/
  ninja.name = name;
  ninja.age = age;
  ninja.prevOccupation = prevOccupation;
/*
Addition of methods to ninja
*/
  ninja.introduce = function() {
    console.log("Hi, my name is " + ninja.name + ". I am " + ninja.age + " years old. I used to be a " + ninja.prevOccupation + " and now I'm a Ninja!");
  }
/*
return ninja
*/
  return ninja;
}


                      // Create the Andrew Ninja
var Andrew = NinjaConstructor("Andrew", 87, "Murderer");
Andrew.introduce();
var Marshall = NinjaConstructor("Slim Shady",33,"ganster");
Marshall.introduce();
                      // Create the Michael Ninja
var Michael = NinjaConstructor("Michael", 34, "Serial Killer");
                      // here we redefine the introduce method for a particular "Instance" or Object
Michael.introduce = function() {
  console.log("Hi, I'm " + this.name + ". I used to be a " + this.prevOccupation + ", and I still am!");
}
Michael.introduce();
