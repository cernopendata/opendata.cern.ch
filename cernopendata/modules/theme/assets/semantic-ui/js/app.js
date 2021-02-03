import jquery from "jquery/dist/jquery";

// This line sets jQuery version from Invenio to `jquery` variable globally
// in order to make it compatible with other jQuery versions needed for
// ispy and opera visualizers, since other versions are loaded through script
// tag and take over `$` and `jQuery` namespaces.
global.jquery = jquery;
