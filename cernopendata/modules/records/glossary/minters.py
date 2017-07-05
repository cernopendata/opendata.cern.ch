"""PID minters."""

from __future__ import absolute_import, print_function

from .providers import GlossaryUUIDProvider


def cernopendata_glossid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = GlossaryUUIDProvider.create(
        object_type='rec',
        object_uuid=record_uuid,
        pid_value=data['term']
    )

    data['control_number'] = provider.pid.pid_value
    return provider.pid
