"""PID minters."""

from ..providers.termid import TermUUIDProvider


def cernopendata_termid_minter(record_uuid, data):
    """Mint deposit's PID."""
    provider = TermUUIDProvider.create(
        object_type="rec",
        pid_type="termid",
        object_uuid=record_uuid,
        pid_value=str(data["anchor"]),
    )

    data["control_number"] = provider.pid.pid_value
    return provider.pid
