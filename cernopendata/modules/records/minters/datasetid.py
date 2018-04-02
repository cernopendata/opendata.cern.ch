"""PID minters."""

from __future__ import absolute_import, print_function

from ..providers.datasetid import DatasetUUIDProvider


def cernopendata_datasetid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = DatasetUUIDProvider.create(
        object_type='rec',
        pid_type='datid',
        object_uuid=record_uuid,
        pid_value=str(data['doi'])
    )

    data['control_number'] = provider.pid.pid_value
    return provider.pid
