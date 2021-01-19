

var defaultTemplate = "default.html";
var templateMap = {
  "glossary-term-v1.0.0.json": 'terms.html',
  "docs-v1.0.0.json": 'docs.html',
  "record-v1.0.0.json": 'record.html',
  "datasets-v1.0.0.json": 'dataset.html',
  "software-v1.0.0.json": 'software.html'
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
    template: '<li class="col-sm-12 list-unstyled" ng-include="getTemplateUrl()"></li>'
  }
});
