todo.factory('UserFactory', function($http) {
    return {
        getUser: function(callback) {
            $http.get('/get_user/')
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error);
                });
        },

        getTasks: function(user, callback) {
            $http.get('/api/users/' + user.pk)
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error)
                });
        },

        deleteUser: function(user, callback) {
            $http.delete('/api/users/' + user.id)
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error);
                });
        },

        editUser: function(user, data, callback) {
            $http.put('/api/users/' + user.id, data)
                .success(function(response) {
                    callback(response);
                }).error(function(error) {
                    console.log(error);
                });
        }
    }
});