function sumXY(x, y) {
    var sum = 0;
    if (y>x) {
    for (var i = x; i<=y; i++) {
        sum += i;
      }
    } else {
      for (var i = y; i<=x; i++) {
          sum += i;
        }
      }
    return sum;
}

function findMin(arr) {
    if (arr) {
        var min = arr[0];
        for (var i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
}

function findAvg(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
}

var sumXY = function(x, y) {
  var sum = 0;
  if (y>x) {
  for (var i = x; i<=y; i++) {
      sum += i;
    }
  } else {
    for (var i = y; i<=x; i++) {
        sum += i;
      }
    }
  return sum;
};

var findAvg = function(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
};

var findMin = function findMin(arr) {
    if (arr) {
        var min = arr[0];
        for (var i = 1; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        return min;
    }
};

var myObject = {
    sumXY: function(x, y) {
      var sum = 0;
      if (y>x) {
      for (var i = x; i<=y; i++) {
          sum += i;
        }
      } else {
        for (var i = y; i<=x; i++) {
            sum += i;
          }
        }
      return sum;
    },
    findAvg: function(arr) {
        var sum = 0;
        for (var i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        return sum / arr.length;
    },
    findMin: function findMin(arr) {
        if (arr) {
            var min = arr[0];
            for (var i = 1; i < arr.length; i++) {
                if (arr[i] < min) {
                    min = arr[i];
                }
            }
            return min;
        }
    }
}

var person = {
  name : "Name",
  distance_traveled : 0,
  say_name : function(){
    console.log(person.name);
  },
  say_something : function(phrase){
    console.log(`${person.name} says: ${phrase}`);
  },
  walk : function(){
    console.log(`${person.name} is walking!`);
    person.distance_traveled += 3;
    return person;
  },
  run : function(){
    console.log(`${person.name} is running!`);
    person.distance_traveled += 10;
    return person;
  },
  crawl : function(){
    console.log(`${person.name} is crawling!`);
    person.distance_traveled += 1;
    return person;
  },
  satanicRitual : function(){
    console.log(`${person.name} is sacrificing his first born to Satan!`);
    person.distance_traveled -= 10;
    return person;
  },
  chewGum:function(){
    console.log("Chewing gum is sticky and gross, chewing gum I hate the most");
    retturn person;
  }
}

person.walk().chewGum();satanicRitual();
