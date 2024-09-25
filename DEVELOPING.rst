============
 Developing
============

.. contents::
   :backlinks: none

This document describes how you can run a local instance of the CERN Open Data
portal in order to work with the content records and associated documentation.

Prerequisites
=============

You will need to clone two repositories:

- `opendata.cern.ch <https://github.com/cernopendata/opendata.cern.ch>`_ which
  contains the open data content;

- `cernopendata-portal <https://github.com/cernopendata/cernopendata-portal>`_
  which contains the portal infrastructure code.

Please make sure to also install `Docker
<https://docs.docker.com/get-started/get-docker/>`_ and `Docker Compose
<https://docs.docker.com/compose/install/>`_ v2 that is used for local
developments.

Quick start
===========

In order to create a local CERN Open Data portal instance, please proceed as
follows:

.. code-block:: console

  $ git clone https://github.com/johndoe/opendata.cern.ch
  $ git clone https://github.com/johndoe/cernopendata-portal
  $ cd opendata.cern.ch
  $ docker compose pull
  $ docker compose up -d
  $ sleep 120 # give enough time for the containers to start properly
  $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh \
        --skip-records --skip-docs

This will create a running instance of the CERN Open Data portal with a
relatively empty content. The portal will be accessible locally at
`http://127.0.0.1:500 <http://127.0.0.1:5000>`_.

If you would like to stop and delete your local instance, you can do:

.. code-block:: console

   $ docker compose down -v

Working with records
====================

If you would like to work with certain data records and test your edits on your
local instance, you can proceed as follows.

Edit the record file, such as CMS 2012 collision dataset records:

   .. code-block:: console

  $ vim data/records/cms-primary-datasets.json

Upload the local file into your instance:

.. code-block:: console

  $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records \
        --mode insert-or-replace \
        -f /content/data/records/cms-primary-datasets.json

You can then check your changes at `http://127.0.0.1:500
<http://127.0.0.1:5000>`_.

Note that you can take advantage of shell scripting if you would like to upload
all experiment records locally, for example for ATLAS:

.. code-block:: console

  $ for file in data/records/atlas-*; do \
       docker exec -i -t opendatacernch-web-1 cernopendata fixtures records \
           --mode insert-or-replace -f $file; \
    done

Understanding metadata fields
=============================

When working with data records, there are several fields such as
`collision_energy` that you can use to store the content. The list of all
available record fields, together with their semantic meaning, is described in
the JSON Schema files. You can find the `record schema
<https://github.com/cernopendata/cernopendata-portal/blob/main/cernopendata/jsonschemas/records/record-v1.0.0.json>`_
in the portal infrastructure repository.

If you would like to modify the JSON schema, for example to add a new field,
this would require working with the `cernopendata-portal` sister repository.
Please see its own `documenation
<https://github.com/cernopendata/cernopendata-portal/>`_ about how to add new
metadata fields. We would be happy to assist with the process.

Understanding output templates
==============================

If you would like to change the way how the data records are displayed on the
web, for example to introduce new section displaying newly added field, this is
something that is governed by `Jinja templating language
<https://jinja.palletsprojects.com/en/2.10.x/templates/>`_ in the
`cernopendata-portal` sister repository. Please see its own `documenation
<https://github.com/cernopendata/cernopendata-portal/>`_ about how to amend
look and feel of the record metadata. We would be happy to assist with the
process.

Verifying metadata conformance
==============================

You can use the provided helper script `check_fixtures.py` to check the
conformance of record files to the required minimal standard:

.. code-block:: console

   ./scripts/check_fixtures.py

Working with docs/records
-------------------------

The recommended development process is the following:

1. Create the entries under data/(records/docs) 2. Validate that the yaml
   syntax is correct

.. code-block:: console

   $ my_docker exec -it web /content/scripts/check_fixtures.py

..

3. Load the entries in the system. To reload all the entries defined in this repo, do:

.. code-block:: console

   $ my_docker exec -it web /content/scripts/load-fixtures.sh

..

4. If you want to load only some records/docs

.. code-block:: console

   $ my_docker exec -it web cernopendata fixtures records --file /content/data/records/<full_path>
   $ my_docker exec -it web cernopendata fixtures docs --file /content/data/docs/<full_path>

..

5. Finally, if there are new images, ensure that they appear in the correct folder

.. code-block:: console

   $ my_docker exec -it web /content/scripts/load-images.sh

..


Understanding repository branches
---------------------------------

We use three official base branches:

master
  What is installed on the `development server <http://opendata-dev.cern.ch>`_.

qa
  What is installed on the `pre-production server <http://opendata-qa.cern.ch>`_.

production
  What is installed on the `production server <http://opendata.cern.ch>`_.

The life-cycle of a typical releasing new content is therefore:
(1) development starts on a personal laptop in a new topical branch stemming from the
``master`` branch;
(2) when the new content is ready, the developer issues a pull request against master, the branch is reviewed by the system
integrator, and merged if appropriate;
(3) If there are no issues with development, it will also be merged into the ``qa`` branch, and deployed on the pre-production
server;
(3) after sufficient testing time on the pre-publication
server, the new content is merged into the ``production`` branch and
deployed on the production server.
