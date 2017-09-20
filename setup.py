# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
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
    'mock>=1.3.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4.2',
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
    'Flask-BabelEx>=0.9.3',
    'Flask-Breadcrumbs>=0.4.0',
    'Flask-CeleryExt>=0.2.2',
    'Flask-Markdown>=0.3.0',
    'Flask-Menu>=0.5.0',
    'Flask-Mistune>=0.1.1',
    'Flask>=0.11.1',
    'idna==2.5',
    'invenio-assets>=1.0.0b6',
    'invenio-base>=1.0.0a9',
    'invenio-celery>=1.0.0b1',
    'invenio-config>=1.0.0b1',
    'invenio-db[versioning,postgresql]>=1.0.0b3',
    'invenio-i18n>=1.0.0b1',
    'invenio-indexer>=1.0.0a1',
    'invenio-jsonschemas>=1.0.0a2',
    'invenio-marc21>=1.0.0a1',
    'invenio-xrootd>=1.0.0a4',
    # FIXME invenio-oaiserver 1.0.0a10, 1.0.0a11 lead to functools32 troubles
    'invenio-oaiserver>=1.0.0a9,<1.0.0a10',
    'invenio-pidstore>=1.0.0b1',
    'invenio-records-files>=1.0.0a9',
    'invenio-records-rest>=1.0.0a9',
    'invenio-records-ui>=1.0.0a8',
    'invenio-records>=1.0.0b1',
    'invenio-search-ui>=1.0.0a2',
    'invenio-search>=1.0.0a9',
    'invenio-theme==1.0.0b2',
    'mistune>=0.7.4',
    'py-gfm>=0.1.3',
    'pymdown-extensions>=3.5',
    'python-slugify>=1.2.4',
    'xrootdpyfs>=0.1.4',
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
        'dojson.contrib.marc21': [
            'cernopendata = cernopendata.rules',
        ],
        'invenio_assets.bundles': [
            'cernopendata_theme_css = cernopendata.modules.theme.bundles:css',
            'cernopendata_visualise_css = '
            'cernopendata.modules.theme.bundles:visualise_css',
            'cernopendata_visualise_js = '
            'cernopendata.modules.theme.bundles:visualise_js',
            'cernopendata_search_js = cernopendata.modules.theme.bundles'
            ':search_js',
            'cernopendata_glossary_js = cernopendata.modules.theme.bundles'
            ':glossary_js',
            'cernopendata_glossary_css = cernopendata.modules.theme.bundles'
            ':glossary_css',
            'opera_js = cernopendata.modules.theme.bundles'
            ':opera_js',
            'opera_css = cernopendata.modules.theme.bundles'
            ':opera_css',
        ],
        'invenio_base.apps': [
            'cernopendata_xrootd = cernopendata.modules.xrootd:CODPXRootD'
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
        ],
        'invenio_base.apps': [  # Wrappers for init of certain extensions.
            # 'cod_md = '
            # 'cernopendata.modules.markdown.ext:CernopendataMarkdown',
            'cod_mistune = '
            'cernopendata.modules.mistune.ext:CernopendataMistune',
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
            'cernopendata_articleid_minter = '
            ' cernopendata.modules.records.minters.artid:'
            'cernopendata_articleid_minter',
        ],
        'invenio_pidstore.fetchers': [
            'cernopendata_recid_fetcher = '
            ' cernopendata.modules.records.fetchers.recid:'
            'cernopendata_recid_fetcher',
            'cernopendata_termid_fetcher = '
            ' cernopendata.modules.records.fetchers.termid:'
            'cernopendata_termid_fetcher',
            'cernopendata_articleid_fetcher = '
            ' cernopendata.modules.records.fetchers.artid:'
            'cernopendata_articleid_fetcher',
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
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 4 - Beta',
    ],
)
