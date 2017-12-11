var facetCtrl = function($scope){
    var isFacetChecked = function(key, value){
        var checkedValues = $scope.getValues(key);
        return (checkedValues && checkedValues.indexOf(value) > -1)
    }

    $scope.checkParent = function(key, value){
        if(!isFacetChecked(key, value))
            $scope.handleClick(key, value);
    }

    $scope.checkChildFacets = function(aggr, type){
        Object.keys(aggr).forEach(function(key){
            if(['doc_count', 'key'].indexOf(key) === -1 && aggr[key].buckets){
                aggr[key].buckets.forEach(function(subkey){
                    if(isFacetChecked(type, aggr.key)){
                        if(!isFacetChecked(key, subkey.key))
                            $scope.handleClick(key, subkey.key);
                    }else{
                        if(isFacetChecked(key, subkey.key))
                            $scope.handleClick(key, subkey.key);
                    }
                });
            }
        });
    }

    $scope.isFacetChecked = isFacetChecked;
};

facetCtrl.$inject = [
    '$scope'
];

angular.module('invenioSearch')
    .controller('facetCtrl', facetCtrl);
