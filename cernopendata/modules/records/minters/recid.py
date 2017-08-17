"""PID minters."""

from __future__ import absolute_import, print_function

from slugify import slugify

from ..providers.recid import RecordUUIDProvider


def cernopendata_recid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = RecordUUIDProvider.create(
        object_type='rec',
        pid_type='recid',
        object_uuid=record_uuid,
        pid_value=str(data['id'])
    )

    data['control_number'] = provider.pid.pid_value
    return provider.pid
