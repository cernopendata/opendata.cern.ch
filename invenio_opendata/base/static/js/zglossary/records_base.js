$( document ).ready(function() {
	$("#rec_authors_rdmore").readmore({
		maxHeight: 20,
		moreLink: '<div class="pull-left"><a href="" class="fa fa-caret-square-o-down"></a></div>',
		lessLink: '<div class="pull-left"><a href="" class="fa fa-caret-square-o-up"></a></div>',
	});

	var options = {
		valueNames: ['author_name', 'author_affiliaton', 'author_ccid', 'author_inspire'],
	};

	if ($("#authors_list").length !== 0) {		
		var authors_list = new List('authors_list', options);
	}
});
