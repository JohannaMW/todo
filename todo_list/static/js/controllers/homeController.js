function homeController($scope, TaskFactory, UserFactory, $location){
    $scope.editing = false;
    var userId;
    var currentTask;

    UserFactory.getUser(function(data) {
       userId = data[0].pk;
       console.log(data[0].pk);
       console.log(data);
       UserFactory.getTasks(userId, function(response) {
       $scope.tasks = response.tasks;
       console.log(response.tasks);
    });
    });

    $scope.createTask = function() {
        var data = {
            "title": $scope.newTaskTitle,
            "due": $scope.newTaskDue,
            "description": $scope.newTaskDescription,
            "owner": userId
        };
        TaskFactory.createTask(data, function(response) {
            $scope.tasks.push(response);
            $location.path('/')
        });
    };

    $scope.editingTask = function(task) {
        currentTask = task;
        if ($scope.editing === true) {
                $scope.editing = false;
        } else {
            $scope.editing = true
        }
    };

    $scope.editTask = function() {
        var data = {
            "title": $scope.taskTitle,
            "due": $scope.taskDue,
            "description": $scope.taskDescription,
            "owner": userId
        };
        TaskFactory.editTask(currentTask, data, function(response) {
            $location.path('/')
        });
    };

    $scope.deleteTask = function(task) {
        TaskFactory.deleteTask(task, function (response) {
            var index = $scope.tasks.indexOf(task);
            $scope.tasks.splice(index, 1);
            $location.path('/')
        })
    }
}