The search engine of the CERN Open Data Portal allows different types of queries. The most common filters can be applied with the selection boxes on the left: experiment, type of record, file format, etc...

The search bar offers more flexibility, and it allows to search by any terms. By default, it will do an `AND` of all
the terms that have been introduced. For instance, a search for `heavy ion` will return only documents that contain both
words. The default behaviour can be modified using the reserved word `AND`, `OR` and the parenthesis `(`, `)`. Note that
this is case sensitive. Some examples of queries are:

* `heavy ion`: returns documents that contain both words.
* `heavy ion electron`: returns documents that contain the three words.
* `heavy ion AND electron`: identical to the previous case, it will return documents that contain the three words.
* `heavy ion OR electron`: returns documents that contain the word `heavy`, and either `ion` or `electron`.
* `(heavy ion) OR electron`: returns documents that contain either `heavy ion` or `electron`.

It is possible to filter out results using the `-`. A couple more examples:

* `heavy ion -electron`: returns documents that contain `heavy ion` and do not contain `electron`.
* `-electron`: returns all the documents that do not contain the word `electron.
* `-"heavy ion" electron`: returns documents that contain electron and not `heavy ion`.

On top of that, it is also possible to search on specific fields. For instance, take a look at the following queries:

* `authors.orcid:0000-0002-4485-2972`: returns all the documents from that author.
* `10.7483/OPENDATA.CMS.W26R.J96R`: returns all documents with those terms in any field.
* `doi:10.7483/OPENDATA.CMS.W26R.J96R`: returns the document with that Digital Object Identifier (doi)
* `doi:10.7483*`: returns all the documents with a doi starting with those values.


The syntax for these queries is defined by the OpenSearch query_string, which is based in the [Apache Lucene syntax](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html)

