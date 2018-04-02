"""PID Fetchers."""

from collections import namedtuple

from ..providers.softid import SoftwareUUIDProvider

FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])


def cernopendata_softid_fetcher(record_uuid, data):
    """Fetch a term's identifiers."""
    return FetchedPID(
        provider=SoftwareUUIDProvider,
        pid_type=SoftwareUUIDProvider.pid_type,
        pid_value=data['control_number'],
    )
