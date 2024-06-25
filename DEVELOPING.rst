============
 Developing
============

.. contents::
   :backlinks: none

Installation
============

This module contains the content of the CERN Open Data instance. It does not contain the code of the portal itself.
For local development, it is recommended to have an installation of the CERN Open Data Portal. For detail instructions
on how to install the portal, please follow `these instructions <https://github.com/cernopendata/cernopendata-portal/blob/main/DEVELOPING.rst>`_.

Quick start
-------------------
For a quickstart guide, do the following:

.. code-block:: console

  $ # Checkout this repository
  $ git clone https://github.com/cernopendata/opendata.cern.ch.git
  $ # Checkout the module with the portal
  $ git clone https://github.com/cernopendata/cernopendata-portal.git
  $ # Move to the directory of the content
  $ cd opendata.cern.ch
  $ # Make sure that the latest images are available
  $ docker compose pull
  $ # Start the services
  $ docker compose up -d
  $ # Give enough time to the containers to start properly. Note that there are some dependencies among them,
  $ # and the web container starts by setting up the development environment
  $ sleep 120
  $ # Create the basic structure
  $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh --skip-records --skip-docs
  $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records \
              --mode insert-or-replace \
              -f /content/data/records/cms-primary-datasets.json
..


At this point, all the services should be up and running. If you go to a web browser to http://0.0.0.0:5000/, you should
see the web portal, with the vocabularies and some documents about the portal itself.

From this moment on,

Defining new entries
====================

This repository has the following data structure:

* data:
    * records: Put here the entries that should be inserted as records
    * docs: This folder will be for the documents
    * images: And this is for static images that might be needed
* scripts: Directory with shell scripts to help the development

If you want to modify the json schema, mappings or templates, you will find these folders in the
`cernopendata portal <https://github.com/cernopendata/cernopendata-portal/>`_ repository

Working with docs/records
-------------------------

The recommended development process is the following:

1. Create the entries under data/(records/docs)
2. Validate that the yaml syntax is correct

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
