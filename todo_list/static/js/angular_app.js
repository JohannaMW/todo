var todo = angular.module('todo', ['ngRoute']);

todo.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/home.html', controller: homeController }).
        otherwise({redirectTo: '/'});
}]);