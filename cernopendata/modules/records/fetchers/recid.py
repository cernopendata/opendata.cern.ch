"""PID Fetchers."""

from collections import namedtuple

from ..providers.recid import RecordUUIDProvider

FetchedPID = namedtuple("FetchedPID", ["provider", "pid_type", "pid_value"])


def cernopendata_recid_fetcher(record_uuid, data):
    """Fetch a term's identifiers."""
    return FetchedPID(
        provider=RecordUUIDProvider,
        pid_type=RecordUUIDProvider.pid_type,
        pid_value=data["control_number"],
    )
