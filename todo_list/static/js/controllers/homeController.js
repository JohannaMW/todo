function homeController($scope, $http, TaskFactory, UserFactory, $location){
    $scope.create = false;

    $scope.creating = function() {
        $scope.create = true;
    };

    UserFactory.getUser(function(response) {
       $scope.user = response;
       console.log(response.data);
       console.log(response);
    });

    UserFactory.getTasks(function(user, response) {
        $scope.tasks = response;
        console.log(response);
    });

    $scope.createTask = function() {
        var data = {
            "title": $scope.newTaskTitle,
            "due": $scope.newTaskDue,
            "description": $scope.newTaskDescription
        };
        TaskFactory.createTask(data, function(response) {
            $location.path('/')
        });
    };

    $scope.editTask = function(task) {
        var data = {
            "title": $scope.taskTitle,
            "due": $scope.taskDue,
            "description": $scope.taskDescription
        };
        TaskFactory.editTask(task, data, function(response) {
            $location.path('/')
        });
    };

    $scope.deleteTask = function(task) {
        TaskFactory.deleteTask(task, function (response) {
            $location.path('/')
        })
    }
}