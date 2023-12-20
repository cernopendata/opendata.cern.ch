============
 Developing
============

.. contents::
   :backlinks: none

Installation
============

You can run a local CERN Open Data instance for development purposes using
container technology such as Docker or Podman.

Install with Docker
-------------------

One popular solution to develop the CERN Open Data instance locally is to use
Docker. For development purposes, please use the ``docker-compose-dev.yml``
configuration. The source code directory will be mounted in the container and
the system will be ready for "live editing". This is useful for active feature
development or for pull request integration purposes. A usage example:

.. code-block:: console

   $ ./scripts/generate-localhost-certificate.sh
   $ docker compose -f docker-compose-dev.yml build
   $ docker compose -f docker-compose-dev.yml up -d
   $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh
   $ firefox http://0.0.0.0:5000/
   $ docker compose -f docker-compose-dev.yml down -v

If you want to simulate production-like deployment conditions locally, please
use the ``docker-compose.yml`` configuration. This is useful for tuning overall
system performance such as reverse proxy caching. The source code directory
will not be mounted in the container in this case. A usage example:

.. code-block:: console

   $ ./scripts/generate-localhost-certificate.sh
   $ docker compose build
   $ docker compose up -d
   $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh
   $ firefox http://0.0.0.0/
   $ docker compose down -v

Install with Podman
-------------------

Another possibility to develop the CERN Open Data instance locally is to use
the Podman container technology. This has an advantage that your containers
will be running in the regular user space, not requiring any superuser access.

If you are using Linux operating system with SELinux, and would like to use the
developer-oriented installation method with the live code-reload feature, then
please configure your SELinux to use either "permissive", "minimal" or
"disabled" policy. You can use the ``getsebool`` command to show your current
SELinux policy level.

An example of a Podman development session:

.. code-block:: console

   $ ./scripts/generate-localhost-certificate.sh
   $ podman-compose -f docker-compose-dev.yml --podman-build-args='--format docker' build
   $ podman-compose -f docker-compose-dev.yml up
   $ podman exec -i -t opendatacernch_web_1 \
       ./scripts/populate-instance.sh --skip-docs --skip-glossary --skip-records
   $ podman exec -i -t opendatacernch_web_1 \
       cernopendata fixtures records --mode insert -f cernopendata/modules/fixtures/data/records/cms-primary-datasets.json
   $ firefox http://0.0.0.0:5000/
   $ podman-compose -f docker-compose-dev.yml down -v

Note that if you would like to test production-like conditions with Podman, you
will have to allow the regular user processes to listen to privileged
HTTP/HTTPS ports, for example by allowing all ports from 80 up:

.. code-block:: console

   $ echo 80 | sudo tee /proc/sys/net/ipv4/ip_unprivileged_port_start

Then, when you are done with the testing, you can return back to the default
operating system configuration allowing only ports 1024 and up:

.. code-block:: console

   $ echo 1024 | sudo tee /proc/sys/net/ipv4/ip_unprivileged_port_start

Development tips
================

Working with Markdown
---------------------

The portal uses `Python-markdown <https://python-markdown.github.io/>`_ for
Markdown rendering. There are `some differences
<https://python-markdown.github.io/#differences>`_ between this implementation
and the `syntax rules <https://daringfireball.net/projects/markdown/syntax>`_,
mainly concerning lists:

* You must always use 4 spaces (or a tab) for indentation and the same
  character (-, \*, +, numbers) for items list.
* To add a Table Of Contents to a document place the identifier ``[TOC]``
  where you want it to be.

The following extensions are enabled:

* `markdown.extensions.attr_list <https://python-markdown.github.io/extensions/attr_list/>`_
* `markdown.extensions.tables <https://python-markdown.github.io/extensions/tables/>`_
* `markdown.extensions.toc <https://python-markdown.github.io/extensions/toc/>`_
* `pymdownx.magiclink <https://facelessuser.github.io/pymdown-extensions/extensions/magiclink/>`_
* `pymdownx.betterem <https://facelessuser.github.io/pymdown-extensions/extensions/betterem/>`_
* `pymdownx.tilde <https://facelessuser.github.io/pymdown-extensions/extensions/tilde/>`_
* `pymdownx.emoji <https://facelessuser.github.io/pymdown-extensions/extensions/emoji/>`_
* `pymdownx.tasklist <https://facelessuser.github.io/pymdown-extensions/extensions/tasklist/>`_
* `pymdownx.superfences <https://facelessuser.github.io/pymdown-extensions/extensions/superfences/>`_
* `mdx_math <https://pypi.org/project/python-markdown-math/>`_

Working with LaTeX
------------------

LaTeX is enabled with the `mdx_math` extension. Inline equations are between
single ``$``, e.g. ``$E = m c^2$``. For standalone math, use ``\[...\]``.

Working with docs
-----------------

If you are working with docs, for example ``/docs/cms-simulated-dataset-names``,
and you edit the fixtures under ``cernopendata/modules/fixtures/data/docs``, you
will need to re-upload the docs fixtures to see your changes. For example, you
can re-upload all the docs by cleaning the instance first:

.. code-block:: console

   $ docker exec -i -t opendatacernch-web-1 /code/scripts/clean-instance.sh
   $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh --skip-records

Working with records
--------------------

If you are working with certain records only, for example OPERA datasets and
events, you can edit the fixtures under
``cernopendata/modules/fixtures/data/records`` and upload only the files you
wish by doing:

.. code-block:: console

   $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh --skip-records
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

If you alter one of the fixture files, you can upload your changes by using the
``replace`` mode:

.. code-block:: console

   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode replace

Working with files
------------------

If you are working with serving file assets, please note that ``web-files``
container may loose XRootD connection to EOS if you change networks or resume
your laptop from the deep sleep. In this case it may be necessary to restart the
``web`` and ``web-files`` containers:

.. code-block:: console

   $ docker compose -f docker-compose-dev.yml restart web web-files

Working with proxy
------------------

If you are working in a production environment and you need to delete the proxy
cache content, you can run:

.. code-block:: console

   $ docker exec opendatacernch-nginx-1 find /var/cache/nginx -type f -delete

Working with UI packages
------------------------

When working on UI packages that have JavaScript and CSS files, you can have
"live editing" by running the following command on a new terminal:

.. code-block:: console

   $ docker exec -i -t opendatacernch_web_1 cernopendata webpack run start

Keep in mind that you need to recreate the ``package.json`` when adding or
removing dependencies:

.. code-block:: console

   $ docker exec -i -t opendatacernch_web_1 cernopendata webpack clean create

Working with iSpy visualizer
----------------------------

CSS dependencies which are needed for iSpy CMS visualizer are sandboxed in order
to make it compatible with ``Semantic UI``. This was achieved by:

* Wrapping all the ``Bootstrap`` html with a ``<div class="bootstrap-ispy">``
* Prefixing all the css classes of ``Bootstrap`` framework and custom ispy css file with ``bootstrap-ispy`` class.
* As a result ``Bootstrap`` css can be used inside a div with ``bootstrap-ispy`` class without any conflicts with ``Semantic UI``.

Procedure to prefix css files with ``bootstrap-ispy`` class:

* Download unminified version (CMS visualizer currently uses Bootstrap v3.3.1) of the ``Bootstrap`` framework from the official website (usually it's bootstrap.css file)
* Install LESS preprocessor locally: ``npm install -g less``
* Create a file ``prefix-bootstrap.less`` which contains the following:

.. code-block:: console

   .bootstrap-ispy {
      @import (less) 'bootstrap.css';
   }

* Preprocess css file with LESS to generate a new prefixed file (it will create ``bootstrap-prefixed.css`` file):

.. code-block:: console

   lessc prefix-bootstrap.less bootstrap-prefixed.css

* Place this file in ``/static/assets/`` to serve it
* Same exact procedure needs to be done for custom `ispy.css file <https://github.com/cms-outreach/ispy-webgl/blob/master/css/ispy.css>`_

Switching between PROD and DEV contexts
---------------------------------------

If you need to switch between testing a feature is the development environment
context (using ``docker-compose-dev.yml``) and the production environment
context (using ``docker-compose.yml``), you can use a helper script joining the
above tips together to quickly initialise your working environment.

For switching from any mode to the production mode working on OPERA records, you
can do:

.. code-block:: shell

   docker compose down -v
   docker compose -f docker-compose-dev.yml down -v
   docker compose build
   docker compose up -d
   sleep 20
   docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh --skip-records
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

For switching from any mode to the development mode working on OPERA records,
you can do:

.. code-block:: shell

   docker compose down -v
   docker compose -f docker-compose-dev.yml down -v
   docker compose -f docker-compose-dev.yml build
   docker compose -f docker-compose-dev.yml up -d
   sleep 20
   docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh --skip-records
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/cms-derived-csv-Run2011A.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   docker exec -i -t opendatacernch-web-1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

Beware when switching between production and development or between different
version of Python, since this may necessitate to delete all `*.pyc` and similar
files created during development. The best is to make sure that you don't have
any non-committed changes to the source code in your workspace and then to
clean your workspace fully by running:

.. code-block:: shell

   sudo git clean -d -ff -x

Appendix: Git workflow
======================

Here is detailed example of our `GitHub flow
<https://guides.github.com/introduction/flow/index.html>`_.

Setting up repository
---------------------

Let's assume your GitHub account name is ``johndoe``.

Firstly, fork `opendata.cern.ch repository
<https://github.com/cernopendata/opendata.cern.ch/>`_ by using the
"Fork" button on the top right.  This will give you your personal
repository:

.. code-block:: console

   http://github.com/johndoe/opendata.cern.ch

Secondly, clone this repository onto your laptop and set up remotes so
that ``origin`` would point to your repository and ``upstream`` would
point to the canonical location:

.. code-block:: console

   $ cd ~/private/src
   $ git clone git@github.com:johndoe/opendata.cern.ch
   $ cd opendata.cern.ch
   $ git remote add upstream git@github.com:cernopendata/opendata.cern.ch

Optionally, if you are also going to integrate work of others, you may
want to set up `special PR branches
<http://simko.home.cern.ch/simko/github-local-handling-of-pull-requests.html>`_
like this:

.. code-block:: console

   $ vim .git/config
   $ cat .git/config
   [remote "upstream"]
       url = git@github.com:cernopendata/opendata.cern.ch
       fetch = +refs/heads/*:refs/remotes/upstream/*
       fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*

Understanding repository branches
---------------------------------

We use three official base branches:

master
  What is installed on the `development server <http://opendata-dev.cern.ch>`_.

qa
  What is installed on the `pre-production server <http://opendata-qa.cern.ch>`_.

production
  What is installed on the `production server <http://opendata.cern.ch>`_.

The life-cycle of a typical new feature is therefore: (1) development
starts on a personal laptop in a new topical branch stemming from the
``master`` branch; (2) when the feature is ready, the developer issues
a pull request, the branch is reviewed by the system integrator,
merged into the ``qa`` branch , and deployed on the pre-production
server; (3) after sufficient testing time on the pre-publication
server, the feature is merged into the ``production`` branch and
deployed on the production server.

The following sections document the development life cycle in fuller
detail.

Working on topical branches
---------------------------

You are now ready to work on something.  You should always create
separate topical branches for separate issues, starting from
appropriate base branch:

- for bug fixes solving problems spotted on the production server, you
  would typically start your topical branch from the ``production``
  branch;

- for new developments, you would typically start your topical branch
  from the ``master`` branch.

Here is example:

.. code-block:: console

   $ git checkout master
   $ git checkout -b improve-event-display-icons
   $ $EDITOR some_file.py
   $ git commit -a -m 'some improvement'
   $ $EDITOR some_other_file.py
   $ git commit -a -m 'some other improvement'

When everything is ready, you may want to rebase your topical branch
to get rid of unnecessary commits:

.. code-block:: console

   $ git checkout improve-event-display-icons
   $ git rebase master -i # squash commits here

Making pull requests
--------------------

You are now ready to issue a pull request: just push your branch in
your personal repository:

.. code-block:: console

   $ git push origin improve-event-display-icons

and use GitHub's "Pull request" button to make the pull request.

Watch GitHub Actions build status report to see whether your pull request
is OK or whether there are some troubles.

Updating pull requests
----------------------

Consider the integrator had some remarks about your branch and you
have to update your pull request.

Firstly, update to latest upstream "master" branch, in case it may
have changed in the meantime:

.. code-block:: console

   $ git checkout master
   $ git fetch upstream
   $ git merge upstream/master --ff-only

Secondly, make any required changes on your topical branch:

.. code-block:: console

   $ git checkout improve-event-display-icons
   $ $EDITOR some_file.py
   $ git commit -a -m 'amends something'

Thirdly, when done, interactively rebase your topical branch into
nicely organised commits:

.. code-block:: console

   $ git rebase master -i # squash commits here

Finally, re-push your topical branch with a force option in order to
update your pull request:

.. code-block:: console

   $ git push origin improve-event-display-icons -f

Finishing pull requests
-----------------------

If your pull request has been merged upstream, you should update your
local sources:

.. code-block:: console

   $ git checkout master
   $ git fetch upstream
   $ git merge upstream/master --ff-only

You can now delete your topical branch locally:

.. code-block:: console

   $ git branch -d improve-event-display-icons

and remove it from your repository as well:

.. code-block:: console

   $ git push origin master
   $ git push origin :improve-event-display-icons

This would conclude your work on ``improve-event-display-icons``.
