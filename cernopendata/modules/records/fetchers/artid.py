"""PID Fetchers."""

from collections import namedtuple

from ..providers.artid import ArticleUUIDProvider

FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])


def cernopendata_articleid_fetcher(record_uuid, data):
    """Fetch a article's identifiers."""
    return FetchedPID(
        provider=ArticleUUIDProvider,
        pid_type=ArticleUUIDProvider.pid_type,
        pid_value=data['control_number'],
    )
