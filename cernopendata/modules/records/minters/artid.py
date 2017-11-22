"""PID minters."""

from __future__ import absolute_import, print_function

from slugify import slugify

from ..providers.artid import ArticleUUIDProvider


def cernopendata_articleid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = ArticleUUIDProvider.create(
        object_type='rec',
        pid_type='artid',
        object_uuid=record_uuid,
        pid_value=str(slugify(data.get('slug', data['title'])))
    )

    data['control_number'] = provider.pid.pid_value
    return provider.pid
