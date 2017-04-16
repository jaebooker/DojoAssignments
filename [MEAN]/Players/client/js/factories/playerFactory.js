var myAppModule = angular.module("myApp", ["ngRoute"]);
myAppModule.factory("playerFactory", function(){
  var players = [
    {name:"Chuck Norris", team:"Merica"},
    {name:"Bruce Lee", team:"The Dragons"}
  ];
  var factory = {};
  factory.getPlayers = function(callback){
    callback(players);
  }
  factory.addPlayer = function(player){
    player.team = "";
    player.push(player)
  }
  factory.removePlayer = function($index){
    players.splice($index, 1);
  }
  factory.addPlayerToTeam = function(data){
    players[data.playerIdx].team = data.team;
  }
  factory.removePlayerFromTeam = function($index){
    players[$index].team = "";
  }
  return factory;
})
