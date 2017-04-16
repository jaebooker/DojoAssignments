myAppModule.controller("associationsController", function($scope, PlayerFactory, TeamFactory){
  $scope.players = [];
  $scope.teams = [];
  PlayerFactory.getPlayers(function(players){
    $scope.players = players;
  })
  TeamFactory.getTeams(function(teams){
    $scope.teams = teams;
  })
  $scope.addPlayerToTeam = function(){
    PlayerFactory.addPlayerToTeam($scope.newAssoc)
  }
  $scope.removePlayerFromTeam = function($index){
    PlayerFactory.removePlayerFromTeam($index);
  }
})
