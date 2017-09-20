"""PID Fetchers."""

from collections import namedtuple

from ..providers.datasetid import DatasetUUIDProvider

FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])


def cernopendata_datasetid_fetcher(record_uuid, data):
    """Fetch a article's identifiers."""
    return FetchedPID(
        provider=DatasetUUIDProvider,
        pid_type=DatasetUUIDProvider.pid_type,
        pid_value=data['control_number'],
    )
