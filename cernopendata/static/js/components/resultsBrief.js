

var defaultTemplate = "default.html";
var templateMap = {
  "term-v1.0.0.json": 'terms.html',
  "article-v1.0.0.json": 'articles.html'
}

angular.module('invenioSearch').directive('resultsBrief', function() {
  return {
    restrict: 'E',
    scope: {
      record: "="
    },
    controller: function($scope) {
      $scope.getTemplateUrl = function() {
        var schema_name = $scope.record.metadata.$schema.split('/');
        var schema_template = defaultTemplate;

        schema_name = schema_name[schema_name.length-1];
        if ( templateMap[schema_name] )
          schema_template = templateMap[schema_name];

        return '/static/templates/search/briefs/'+ schema_template;
      }
    },
    template: '<li class="col-sm-12" ng-include="getTemplateUrl()"></li>'
  }
});