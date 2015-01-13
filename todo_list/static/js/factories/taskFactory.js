todo.factory('TaskFactory', function($http) {
    return {
        getTasks: function(callback) {
            $http.get('/api/tasks/' )
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error);
                });
        },
        deleteTasks: function (task, callback) {
            $http.delete('/api/tasks/' + task.id)
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error);
                });
        },
        editTask: function (task, data, callback) {
            $http.put('/api/tasks/', task.id, data)
                .success(function (response) {
                    callback(response);
                }).error(function (error) {
                    console.log(error);
                });
        },
        createTask: function (data, callback) {
            $http.post('/api/tasks/', data)
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error)
                });
        }
    }
});