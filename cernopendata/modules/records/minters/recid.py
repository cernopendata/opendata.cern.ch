"""PID minters."""

from ..providers.recid import RecordUUIDProvider


def cernopendata_recid_minter(record_uuid, data):
    """Mint deposit's PID."""
    if "id" in data:
        recid = data["id"]
    else:
        recid = data["recid"]

    provider = RecordUUIDProvider.create(
        object_type="rec",
        pid_type="recid",
        object_uuid=record_uuid,
        pid_value=str(recid),
    )

    data["control_number"] = provider.pid.pid_value
    return provider.pid
