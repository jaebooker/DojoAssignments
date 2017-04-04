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
    console.log(`${person.name} is sacrificing their first born to Satan!`);
    person.distance_traveled += 1;
    return person;
  },
  chewGum:function(){
    console.log("I can walk and chew gum, but I can't chew gum and walk...");
    return person;
  }
}

function ninjaConstructor(name, cohort){
  var ninja = {}
  var belts = ["yellow", "red", "black"]
  var kills = ['Rooky', 'Accomplished assassin', 'cold-blooded murderer', "out-of-control serial kille-oh my god, he's right behind me!"]
  ninja.name = name;
  ninja.cohort = cohort;
  ninja.beltLevel = 0;
  ninja.kill_level = 0;
  ninja.levelUp = function(){
    if (ninja.beltLevel < 2){
      ninja.beltLevel += 1;
      ninja.belt = belts[ninja.beltLevel];
    }
    return ninja
  }
  ninja.finishHim = function(){
    if (ninja.kill_level < 4){
      ninja.kill_level += 1;
      ninja.kill_level = kills[0];
      console.log("Excellent");
    }
    else if (ninja.kill_level < 11){
      ninja.kill_level += 1;
      ninja.kill_level = kills[1];
      console.log("Impressive. Most impressive");
    }
    else if (ninja.kill_level < 120){
      ninja.kill_level += 1;
      ninja.kill_level = kills[2];
      console.log("Wow, I mean... wow. That's, that's a lot of dead bodies.");
    }
    else {
      ninja.kill_level += 1;
      ninja.kill_level = kills[2];
      console.log("OH GOD! WHAT HAVE WE CREATED???!! SOMEONE STOP H-");
    }
    return ninja
  }
  ninja.belt = belts[ninja.beltLevel];
  ninja.kills = belts[ninja.kill_level];
  return ninja;
}
