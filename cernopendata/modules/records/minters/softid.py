"""PID minters."""

from __future__ import absolute_import, print_function

from ..providers.softid import SoftwareUUIDProvider


def cernopendata_softid_minter(record_uuid, data):
    """Mint deposit's PID."""
    if 'id' in data:
        recid = data['id']
    else:
        recid = data['recid']

    provider = SoftwareUUIDProvider.create(
        object_type='rec',
        pid_type='softid',
        object_uuid=record_uuid,
        pid_value=str(recid)
    )

    data['control_number'] = provider.pid.pid_value
    return provider.pid
