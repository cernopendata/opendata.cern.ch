"""PID minters."""

from slugify import slugify

from ..providers.docid import DocUUIDProvider


def cernopendata_docid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = DocUUIDProvider.create(
        object_type="rec",
        pid_type="docid",
        object_uuid=record_uuid,
        pid_value=str(slugify(data.get("slug", data["title"]))),
    )

    data["control_number"] = provider.pid.pid_value
    return provider.pid
