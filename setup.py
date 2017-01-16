# -*- coding: utf-8 -*-

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
    'invenio-config>=1.0.0b1',
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
    'invenio-assets>=1.0.0a11',
    'invenio-base>=1.0.0a9',
    'invenio-celery>=1.0.0b1',
    'invenio-collections>=1.0.0a1',
    'invenio-config>=1.0.0b1',
    'invenio-db[versioning,postgresql]>=1.0.0b3',
    'invenio-indexer>=1.0.0a1',
    'invenio-jsonschemas>=1.0.0a2',
    'invenio-marc21>=1.0.0a1',
    'invenio-oaiserver>=1.0.0a9',
    'invenio-pidstore>=1.0.0b1',
    'invenio-records-rest>=1.0.0a9',
    'invenio-records-ui>=1.0.0a8',
    'invenio-records>=1.0.0b1',
    'invenio-search-ui>=1.0.0a2',
    'invenio-search>=1.0.0a9',
    'invenio-theme>=1.0.0a16',
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
    url='https://github.com/cernopendata/cernopendata',
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
            'cernopendata_theme_css = cernopendata.bundles:css',
        ],
        'invenio_base.blueprints': [
            'cernopendata = '
            'cernopendata.views:blueprint',
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
