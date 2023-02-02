# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018, 2021, 2022, 2023 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""CERN Open Data Portal instance."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('cernopendata', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.2.2',
    'locustio>=0.8,<0.13',
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pycodestyle>=2.4.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.2,<5.0.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.6.2',
]

install_requires = [
    # General Invenio dependencies
    'invenio-app==1.3.0',
    'invenio-base==1.2.5',
    'invenio-config==1.0.3',
    # Custom Invenio `base` bundle
    'invenio-assets==1.2.7',
    'invenio-accounts==1.4.5',
    'invenio-logging[sentry]==1.3.0',
    'invenio-rest==1.2.1',
    'invenio-theme==1.3.6',
    # Custom Invenio `metadata` bundle
    'invenio-indexer==1.2.0',
    'invenio-jsonschemas==1.1.0',
    'invenio-pidstore==1.2.1',
    'invenio-records-rest[datacite]==1.7.2',
    'invenio-records-ui==1.2.0',
    'invenio-records==1.4.0a3',
    'invenio-search-ui==2.0.4',
    # Custom Invenio `files` bundle
    'invenio-previewer==1.3.2',
    'invenio-records-files==1.2.1',
    # Custom Invenio `postgresql` bundle
    'invenio-db[versioning,postgresql]==1.0.5',
    # Custom Invenio `elasticsearch7` bundle
    'invenio-search[elasticsearch7]==1.4.1',
    # Specific Invenio dependencies
    'invenio-xrootd>=1.0.0a6',
    'xrootdpyfs>=0.2.2',
    # Specific dependencies
    'Flask-Markdown>=0.3.0',
    'Flask-Mistune>=0.1.1',
    'mistune>=0.7.4',
    'pymdown-extensions>=5.0.0',
    'python-markdown-math>=0.3',
    'python-slugify>=1.2.4',
    # Webserver
    'uWSGI>=2.0.21',
    'uwsgitop>=0.11',
    # Pin SQLAlchemy version due to sqlalchemy-utils compatibility
    # <https://github.com/kvesteri/sqlalchemy-utils/issues/505>
    'SQLAlchemy<1.4.0',
    # Pin Flask-SQLAlchemy version due to apply_driver_hacks
    'Flask-SQLAlchemy<2.5.0',
    # Pin Celery due to worker runtime issues
    'celery==5.0.4',
    # Pin XRootD consistently with Dockerfile
    'xrootd==4.12.7',
    # Pin Flask/gevent/greenlet/raven to make master work again
    'Flask<1.2',
    'gevent<1.6',
    'greenlet<1.2',
    'raven<6.11',
]

packages = find_packages()

setup(
    name='cernopendata',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='CERN Open Data',
    license='GPLv2',
    author='CERN',
    author_email='info@inveniosoftware.org',
    url='https://github.com/cernopendata/opendata.cern.ch',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'cernopendata = '
            'cernopendata.cli:cli',
        ],
        'invenio_assets.webpack': [
            'cernopendata_theme = cernopendata.modules.theme.webpack:theme',
            'cernopendata_glossary = cernopendata.modules.theme.webpack:glossary',
            'cernopendata_search = cernopendata.modules.theme.webpack:search_ui',
            'cernopendata_visualise = cernopendata.modules.theme.webpack:visualise',
            'cernopendata_records_file_box = '
            'cernopendata.modules.theme.webpack:records_file_box',
        ],
        'invenio_base.apps': [
            'cernopendata_xrootd = cernopendata.modules.xrootd:CODPXRootD',
            'cernopendata_sitemap = '
            'cernopendata.modules.sitemap:CERNOpenDataSitemap',
            # cod_md and cod_mistune are just wrappers to init the actual
            # markdown flask-extensions properly.
            'cod_md = '
            'cernopendata.modules.markdown.ext:CernopendataMarkdown',
            # 'cod_mistune = '
            # 'cernopendata.modules.mistune.ext:CernopendataMistune',
        ],
        'invenio_base.api_apps': [
            'cernopendata_xrootd = cernopendata.modules.xrootd:CODPXRootD'
        ],
        'invenio_base.blueprints': [
            'cernopendata = cernopendata.views:blueprint',
            'cernopendata_pages = '
            'cernopendata.modules.pages.views:blueprint',
            'cernopendata_theme = '
            'cernopendata.modules.theme.views:blueprint',
            'cernopendata_sitemap = '
            'cernopendata.modules.sitemap.views:blueprint',
        ],
        'invenio_config.module': [
            'cernopendata = cernopendata.config',
        ],
        'invenio_pidstore.minters': [
            'cernopendata_recid_minter = '
            ' cernopendata.modules.records.minters.recid:'
            'cernopendata_recid_minter',
            'cernopendata_termid_minter = '
            ' cernopendata.modules.records.minters.termid:'
            'cernopendata_termid_minter',
            'cernopendata_docid_minter = '
            ' cernopendata.modules.records.minters.docid:'
            'cernopendata_docid_minter',
        ],
        'invenio_pidstore.fetchers': [
            'cernopendata_recid_fetcher = '
            ' cernopendata.modules.records.fetchers.recid:'
            'cernopendata_recid_fetcher',
            'cernopendata_termid_fetcher = '
            ' cernopendata.modules.records.fetchers.termid:'
            'cernopendata_termid_fetcher',
            'cernopendata_docid_fetcher = '
            ' cernopendata.modules.records.fetchers.docid:'
            'cernopendata_docid_fetcher',
        ],
        'invenio_search.mappings': [
            'records = cernopendata.mappings',
        ],
        'invenio_jsonschemas.schemas': [
            'cernopendata_schemas = cernopendata.jsonschemas',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
