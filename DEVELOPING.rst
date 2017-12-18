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
   $ docker-compose -f docker-compose-dev.yml down -v

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
