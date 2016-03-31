# -*- coding: utf-8 -*-

"""CERN Open Data Portal instance."""

import os

from setuptools import find_packages, setup

# Get the version string. Cannot be done with import!
version = {}
with open(os.path.join('cernopendata',
                       'version.py'), 'rt') as fp:
    exec(fp.read(), version)

setup(
    name='cernopendata',
    version=version['__version__'],
    description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'cernopendata = '
            'cernopendata.cli:cli',
        ],
        'dojson.contrib.marc21': [
            'cernopendata = cernopendata.rules',
        ],
        'invenio_assets.bundles': [
            'cernopendata_theme_css = cernopendata.bundles:css',
        ],
        'invenio_base.blueprints': [
            'cernopendata = '
            'cernopendata.views:blueprint',
        ],
    },
    install_requires=[
        'invenio-assets>=1.0.0a4',
        'invenio-base>=1.0.0a4',
        'invenio-config>=1.0.0a1',
        'invenio-collections>=1.0.0a1',
        'invenio-db>=1.0.0a9',
        'invenio-indexer>=1.0.0a1',
        'invenio-jsonschemas>=1.0.0a2',
        'invenio-marc21>=1.0.0a1',
        'invenio-oaiserver>=1.0.0a2',
        'invenio-pidstore>=1.0.0a6',
        'invenio-records-rest>=1.0.0a6',
        'invenio-records-ui>=1.0.0a4',
        'invenio-search-ui>=1.0.0a2',
        'invenio-search>=1.0.0a5',
        'invenio-theme>=1.0.0a10',
    ],
)
