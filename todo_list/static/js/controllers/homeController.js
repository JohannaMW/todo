function homeController($scope, $http, TaskFactory){
    TaskFactory.getTasks(function(response) {
        $scope.tasks = response;
        console.log(response)
    })
}