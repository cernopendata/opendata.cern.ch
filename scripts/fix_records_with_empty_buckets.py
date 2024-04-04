from invenio_db import db
from invenio_pidstore.models import *
from invenio_records_files.api import Record
from invenio_records_files.models import *

recids_list = []
empty_rbs = []

for recid in recids_list:
    pid = PersistentIdentifier.query.filter_by(pid_value=recid).one()
    rec = Record.get_record(pid.object_uuid)
    records_buckets = RecordsBuckets.query.filter_by(record_id=pid.object_uuid).all()
    if (
        len(rec.files) == 0
        and len(records_buckets) > 1
        and rec.bucket == records_buckets[0].bucket
    ):
        empty_rb = records_buckets[0]
        empty_rbs.append(empty_rb)
        db.session.delete(empty_rb)
        db.session.commit()
