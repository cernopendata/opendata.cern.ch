"""PID Fetchers."""

from collections import namedtuple

from ..providers.docid import DocUUIDProvider

FetchedPID = namedtuple("FetchedPID", ["provider", "pid_type", "pid_value"])


def cernopendata_docid_fetcher(record_uuid, data):
    """Fetch a article's identifiers."""
    return FetchedPID(
        provider=DocUUIDProvider,
        pid_type=DocUUIDProvider.pid_type,
        pid_value=data["control_number"],
    )
