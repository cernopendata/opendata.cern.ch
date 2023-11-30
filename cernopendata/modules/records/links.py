"""Record links factory."""

from invenio_records_files.links import default_bucket_link_factory
from invenio_records_rest.links import default_links_factory


def links_factory(pid):
    """Record links factory with files."""
    links = default_links_factory(pid)

    bucket_link = default_bucket_link_factory(pid)
    if bucket_link is not None:
        links["bucket"] = bucket_link
    return links
