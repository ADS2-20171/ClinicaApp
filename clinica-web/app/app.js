function Hello($scope, $http) {
  $scope.users = [];
  $http.get('http://localhost:8000/accounts/clientes').
  success(function(data) {
    console.log(data);
    $scope.users = data;
  });
}
/*
angular.module("MyFirstApp",[])
.controller("FirstController",function($scope,$http){
	$scope.user = [];
	$http.get("http://127.0.0.1:8000/accounts/clientes/6")
	.success(function(data){
		console.log(data);
		$scope.posts = data;
	})
	.error(function(err){

	});
});
*/