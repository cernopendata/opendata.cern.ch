============
 Developing
============

.. contents::
   :backlinks: none

Installation
============

You can run a local CERN Open Data instance for development purposes using
Docker with ``docker-compose-dev.yml`` configuration. The source code directory
will be mounted in the container and the system will be ready for "live
editing". This is useful for active feature development or for pull request
integration purposes. A usage example:

.. code-block:: console

   $ docker-compose -f docker-compose-dev.yml build
   $ docker-compose -f docker-compose-dev.yml up
   $ docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh --skip-files
   $ firefox http://0.0.0.0:5000/
   $ docker-compose -f docker-compose-dev.yml down

If you want to use production-like conditions locally, you can use Docker with
``docker-compose.yml`` configuration. This is useful for tuning overall system
performance such as reverse proxy caching. The source code directory will not be
mounted in the container in this case. A usage example:

.. code-block:: console

   $ docker-compose build
   $ docker-compose up
   $ docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh
   $ firefox http://0.0.0.0/
   $ docker-compose down -v

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
  character (-, *, +, numbers) for items list.
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

   $ docker exec -i -t opendatacernch_web_1 /code/scripts/clean-instance.sh
   $ docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh --skip-records

Working with records
--------------------

If you are working with certain records only, for example OPERA datasets and
events, you can edit the fixtures under
``cernopendata/modules/fixtures/data/records`` and upload only the files you
wish by doing:

.. code-block:: console

   $ docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh --skip-records
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

If you alter one of the fixture files, you can upload your changes by using the
``replace`` mode:

.. code-block:: console

   $ docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode replace

Working with files
------------------

If you are working with serving file assets, please note that ``web-files``
container may loose XRootD connection to EOS if you change networks or resume
your laptop from the deep sleep. In this case it may be necessary to restart the
``web`` and ``web-files`` containers:

.. code-block:: console

   $ docker-compose -f docker-compose-dev.yml restart web web-files

Working with proxy
------------------

If you are working in a production environment and you need to delete the proxy
cache content, you can run:

.. code-block:: console

   $ docker exec opendatacernch_nginx_1 find /var/cache/nginx -type f -delete

Switching between PROD and DEV contexts
---------------------------------------

If you need to switch between testing a feature is the development environment
context (using ``docker-compose-dev.yml``) and the production environment
context (using ``docker-compose.yml``), you can use a helper script joining the
above tips together to quickly initialise your working environment.

For switching from any mode to the production mode working on OPERA records, you
can do:

.. code-block:: shell

   docker-compose down -v
   docker-compose -f docker-compose-dev.yml down -v
   docker-compose build
   docker-compose up -d
   sleep 20
   docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh --skip-records
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

For switching from any mode to the development mode working on OPERA records,
you can do:

.. code-block:: shell

   docker-compose down -v
   docker-compose -f docker-compose-dev.yml down -v
   docker-compose -f docker-compose-dev.yml build
   docker-compose -f docker-compose-dev.yml up -d
   sleep 20
   docker exec -i -t opendatacernch_web_1 /code/scripts/populate-instance.sh --skip-records
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/cms-derived-csv-Run2011A.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-multiplicity.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-author-list-tau.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-multiplicity.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-detector-events-tau.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ecc-datasets.json --mode insert
   docker exec -i -t opendatacernch_web_1 cernopendata fixtures records -f /code/cernopendata/modules/fixtures/data/records/opera-ed-datasets.json --mode insert

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
  Where the bleeding-edge developments happen.

qa
  What is installed on the `pre-production server <http://opendataqa.cern.ch>`_.

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
   $ emacsclient some_file.py
   $ git commit -a -m 'some improvement'
   $ emacsclient some_other_file.py
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

Watch Travis-CI build status report to see whether your pull request
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
   $ emacsclient some_file.py
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
