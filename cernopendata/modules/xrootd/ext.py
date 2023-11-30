"""Initialization of XRootD."""

from invenio_files_rest.storage.pyfs import pyfs_storage_factory
from invenio_xrootd import EOSFileStorage
from pkg_resources import DistributionNotFound, get_distribution


def cernopendata_eos_storage_factory(**kwargs):
    """File storage factory for EOS."""
    return pyfs_storage_factory(filestorage_class=EOSFileStorage, **kwargs)


try:
    # Import XRootDPyFS if available so opener gets registered on
    # PyFilesystem.
    get_distribution("xrootdpyfs")
    import xrootdpyfs  # noqa

    XROOTD_ENABLED = True
except DistributionNotFound:
    XROOTD_ENABLED = False
    xrootdpyfs = None


class CODPXRootD(object):
    """CODP xrootd extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        # import ipdb
        # ipdb.set_trace()
        app.config["XROOTD_ENABLED"] = XROOTD_ENABLED
        if XROOTD_ENABLED:
            #: Overwrite reported checksum from CERN EOS (due to XRootD 3.3.6).
            app.config["XROOTD_CHECKSUM_ALGO"] = "md5"
            app.config["FILES_REST_STORAGE_FACTORY"] = cernopendata_eos_storage_factory
            # 'invenio_xrootd:eos_storage_factory'
        app.extensions["cernopendata-xrootd"] = self
