todo.directive('button', function() {
    return {
        restrict: 'E',
        compile: function(element, attributes) {
            element.addClass('btn btn-warning');
            if (attributes.type == 'submit') {
                element.addClass('btn btn-success');
            }
            if (attributes.size) {
                element.addClass('btn-' + attributes.size);
            }
        }
    }
});