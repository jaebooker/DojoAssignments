myAppModule.controller("PlayersController", function($scope, PlayerFactory){
  $scope.players = [];
  PlayerFactory.getPlayers(function(players){
    $scope.players = players;
  })
  $scope.addPlayer(function(){
    PlayerFactory.addPlayer($scope.newPlayer)
    $scope.newPlayer = {};
  })
  $scope.removePlayer = function($index){
    PlayerFactory.removePlayer($index);
  }
})
