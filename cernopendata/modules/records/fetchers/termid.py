"""PID Fetchers."""

from collections import namedtuple

from ..providers.termid import TermUUIDProvider

FetchedPID = namedtuple("FetchedPID", ["provider", "pid_type", "pid_value"])


def cernopendata_termid_fetcher(record_uuid, data):
    """Fetch a term's identifiers."""
    return FetchedPID(
        provider=TermUUIDProvider,
        pid_type=TermUUIDProvider.pid_type,
        pid_value=data["control_number"],
    )
