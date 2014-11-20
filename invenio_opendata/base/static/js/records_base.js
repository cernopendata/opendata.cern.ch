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

	$('button#showmore_button').click( function() {
		$('#elec-loc-list li.elec-loc-item:hidden').slice( 0,4 ).css( "display", "inline-block" );
		if( $( '#elec-loc-list li.elec-loc-item' ).length == $( '#elec-loc-list li.elec-loc-item:visible' ).length ) {
			$('#showmore_buttons').hide();                             
		}
	});

	$('button#close_showmore_button').click( function() {
		$('#elec-loc-list li.elec-loc-item').hide();
		$('#elec-loc-list li.elec-loc-item').slice( 0,4 ).css( "display", "inline-block" );
		$('#showmore_buttons').css( "display", "inline-block" );
	});
	$('button#close_showmore_button_2').click( function() {
		$('#elec-loc-list li.elec-loc-item').hide();
		$('#elec-loc-list li.elec-loc-item').slice( 0,4 ).css( "display", "inline-block" );
		$('#showmore_buttons').css( "display", "inline-block" );
	});
});
