"""PID Fetchers."""

from collections import namedtuple

from .providers import GlossaryUUIDProvider

FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])


def cernopendata_glossid_fetcher(record_uuid, data):
    """Fetch a deposit's identifiers."""
    return FetchedPID(
        provider=GlossaryUUIDProvider,
        pid_type=GlossaryUUIDProvider.pid_type,
        pid_value=str(data['control_number']),
    )
