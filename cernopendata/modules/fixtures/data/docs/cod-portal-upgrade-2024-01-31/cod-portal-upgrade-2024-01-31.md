A new version of the CERN Open Data Repository has been deployed in January 2024.
Some of the highlights of this release are:

* Change of technologies, from Angular to [ReactJS](https://react.dev/) and from Bootstrap to [Semantic UI](https://semantic-ui.com/)
for the web interface, which improves the navigation and overall user experience.
* Improvements in the search functionality, including setting the default search to do an `AND` of the terms (instead of `OR`)
and simplifying searches by DOI. For more information about the search functionality, see the [search tips](/docs/cod-search-tips).
* Redesign facets for results filtering and fix existing issues if the user selected too many facets and pagination.
* Change the self-maintained ElasticSearch instance, which had reached its end of life support, by the open-sourced
OpenSearch instances provided by the CERN OpenSearch service.
* Update to the latest version of the underlying components, including the invenio framework and xrootd.


