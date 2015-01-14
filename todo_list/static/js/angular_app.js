var todo = angular.module('todo', ['ngRoute', 'ngCookies', 'ui.bootstrap']);

todo.run(function ($http, $cookies) {
    console.log(csrftoken);
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    $http.defaults.headers.put['X-CSRFToken'] = $cookies['csrftoken'];
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

todo.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/home.html', controller: homeController }).
        otherwise({redirectTo: '/'});
}]);