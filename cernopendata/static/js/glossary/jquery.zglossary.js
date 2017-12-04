(function($){

	$.fn.glossary = function(url, options, exp) {

		// Set plugin defaults
		var defaults = {
			ignorecase: false,
			tiptag: 'h6',
			excludetags: [],
			linktarget: '_blank',
			showonce: false
		};
		var options = $.extend(defaults, options);
		var id = 1;

		// Functions
		return this.each(function(i, e) {

			// Ensure any exclude tags are uppercase for comparisons
			$.each(options.excludetags, function(i,e) { options.excludetags[i] = e.toUpperCase(); });

			// Function to find and add term
			var _addTerm = function(e, term, type, def) {
				var patfmt = term;
				var skip = 0;

				// Check the element is a text node
				if (e.nodeType == 3) {

					// Case insensistive matching option
					if (options.ignorecase) {
						var pos = e.data.toLowerCase().search(new RegExp('\\b'+patfmt.toLowerCase()+'\\b'));
					} else {
						var pos = e.data.search(new RegExp('\\b'+patfmt+'\\b'));
					}

					// Check if the term is found
					if (pos >= 0) {
						// Check for excluded tagsnew
						if (( jQuery.inArray($(e).parent().get(0).tagName,options.excludetags) > -1) ||
							( $(e).parent().hasClass('no-glossary') )
						){} else {

							// Create link element
							var spannode = document.createElement('span');
							spannode.className = 'glossaryTerm';

							if (type == '0') {

								// Popup definition
								spannode.id = "glossaryID" + id;
								spannode.href = '#';
								// spannode.title = 'Click for \''+ term +'\' definition';
								spannode.className = 'glossaryTerm';
								$(spannode).hover(
									function(e) {
										$.glossaryTip('<'+ options.tiptag +'>'+ term + '</'+ options.tiptag +'><p>'+ def +'</p>', {mouse_event: e})
										return false;
									},
									function(e) {
										glossaryTip.holder.stop(true).fadeOut(200);
										return false;
									});
							} else if (type == '1') {

								// Wikipedia definition
								spannode.title = 'Click to look up \''+  term+'\' in Wikipedia';
								term = term.replace(/ /g, "_");
								spannode.href = 'http://en.wikipedia.org/wiki/'+term;
								spannode.target = options.linktarget;
							} else if (type == '2') {

								// Google search
								spannode.title = 'Click to search for \''+ term +'\' in Google';
								term = term.replace(/ /g, "+");
								spannode.href = 'http://www.google.co.uk/search?q='+term;
								spannode.target = options.linktarget;
							} else if (type == '3') {

								// Custom external link
								spannode.title = 'Click to view \''+ term +'\' definition';
								spannode.href = def;
								spannode.target = options.linktarget;
							}

							var middlebit = e.splitText(pos);
							var endbit = middlebit.splitText(patfmt.length);
							var middleclone = middlebit.cloneNode(true);

							spannode.appendChild(middleclone);
							middlebit.parentNode.replaceChild(spannode, middlebit);

							skip = 1;
							id += 1;
						}
					}
				}
				else if (e.nodeType == 1 && e.childNodes && !/(script|style)/i.test(e.tagName)) {

					// Search child nodes
					for (var i = 0; i < e.childNodes.length; ++i) {

						var ret = _addTerm(e.childNodes[i], term, type, def);

						// If term found and show once option go to next term
						if (options.showonce && ret == 1) {
							i = e.childNodes.length;
							skip = 1;
						} else {
							i += ret;
						}
					}
				}

				return skip;
			};

			// Get glossary list items
			$.ajax({
				type: 'GET',
				url: url,
				dataType: 'json',
				success: function(data) {

					if (data) {

						var count = data.length;
						for (var i=0; i<count; i++) {
							move_on = false;

							// Find term in text
							var item = data[i];
							if (item.category == 'specific') {
								item.experiment.forEach(function(e, i, a) {
									if( e.name == exp ){
										move_on = true;
									}
								});
							}
							else {
								move_on = true;
							}
							if (!move_on) {
								continue;
							}
							if ( item.term instanceof Array) {
								for (var o = 0 ; o < item.term.length ; o++) {
									_addTerm(e, item.term[o], 0, item.definition);
								}
							}
							else {
								_addTerm(e, item.term, 0, item.definition);
							}
						}
					}
				},
				error: function() {}
			});

		});

	};

	// Glossary tip popup
	var glossaryTip = function() {}

	$.extend(glossaryTip.prototype, {

		setup: function(){

			if ($('#glossaryTip').length) {
				$('#glossaryTip').remove();
			}
			glossaryTip.holder = $('<div id="glossaryTip" style="max-width:260px;"><div id="glossaryClose"></div></div>');
			glossaryTip.content = $('<div id="glossaryContent"></div>');

			$('body').append(glossaryTip.holder.append(glossaryTip.content));
		},

		show: function(content, event){

			glossaryTip.content.html(content);

			// Display tip at mouse cursor
			var x = parseInt(event.mouse_event.pageX) + 15
			var y = parseInt(event.mouse_event.pageY) + 5
			glossaryTip.holder.css({top: y, left: x});

			// Display the tip
			if (glossaryTip.holder.is(':hidden')) {
				glossaryTip.holder.show();
			}

			// Add click handler to close
			glossaryTip.holder.bind('click', function(){
				glossaryTip.holder.stop(true).fadeOut(200);
				return false;
			});

		}

	});

	$.glossaryTip = function(content, event) {
		var tip = $.glossaryTip.instance;

		if (!tip) { tip = $.glossaryTip.instance = new glossaryTip(); }

		tip.setup();
		tip.show(content, event);

		return tip;
	}
})(jQuery);
