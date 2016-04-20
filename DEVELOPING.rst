============
 Developing
============

.. contents::
   :backlinks: none

Installation
============

Here is how to install an instance of the CERN Open Data Portal on
your laptop.

Quick installation instructions
-------------------------------

Quick installation instructions for an impatient Invenio developer::

   cd ~/private/src/invenio
   git checkout maint-2.0
   docker build -t invenio:2.0 .
   cd ~/private/src/opendata.cern.ch
   git checkout master
   ./scripts/populate-fft-file-cache.sh
   docker-compose -f docker-compose-dev.yml build
   docker-compose -f docker-compose-dev.yml up
   # now wait until all daemons are fully up and running
   firefox http://127.0.0.1:28080/
   # now populate demo site with some records
   docker exec -i -t -u invenio opendatacernch_web_1 \
     inveniomanage demosite populate --packages=invenio_opendata.base \
       -f invenio_opendata/testsuite/data/lhcb/lhcb-derived-datasets.xml \
       -e force-recids --yes-i-know
   firefox http://127.0.0.1:28080/

Detailed installation instructions
----------------------------------

Detailed installation instructions for a patient Invenio developer.

Firstly, `install Docker <https://docs.docker.com/installation/>`_.

Secondly, clone Invenio and CERN Open Data Portal sources, following
`Appendix: Setting up repostory
<https://github.com/cernopendata/opendata.cern.ch/blob/master/DEVELOPING.rst#setting-up-repository>`_.

You now have sources in the following directories::

  ~/private/src/invenio
  ~/private/src/opendata.cern.ch

Thirdly, run helper script to pre-populate local fulltext file cache
archive from which the demo records will be later loaded::

  cd ~/private/src/opendata.cern.ch
  ./scripts/populate-fft-file-cache.sh

Note that this will download about 8 GB of files to the following
directory::

  ~/Local/opendata.cern.ch-fft-file-cache

Fourthly, build Invenio Docker image if you haven't built one yet::

  cd ~/private/src/invenio
  git checkout maint-2.0
  docker build -t invenio:2.0 .

Fifthly, create CERN Open Data Portal docker image and bring up the
containers::

  cd ~/private/src/opendata.cern.ch
  docker-compose -f docker-compose-dev.yml build
  docker-compose -f docker-compose-dev.yml up

Wait until all daemons are fully up and running.  Now you should be
able to see the empty site::

  firefox http://127.0.0.1:28080/

Sixthly, if you would like to populate your CERN Open Data local
installation with records, you can now do in another terminal::

  cd ~/private/src/opendata.cern.ch
  docker exec -i -t -u invenio opendatacernch_web_1 \
    inveniomanage demosite populate --packages=invenio_opendata.base \
    -f invenio_opendata/testsuite/data/lhcb/lhcb-derived-datasets.xml \
    -e force-recids --yes-i-know

for all the files you'd like to upload, depending on which collection
you'd like to work with.  For example, the above command will populate
only the LHCb Derived Datasets collection.  If you would like to
populate *all* collections, you can use::

  docker exec -i -t -u invenio opendatacernch_web_1 \
    inveniomanage demosite populate --packages=invenio_opendata.base \
    -f invenio_opendata/testsuite/data/alice/alice-analysis-modules.xml \
    -f invenio_opendata/testsuite/data/alice/alice-derived-datasets.xml \
    -f invenio_opendata/testsuite/data/alice/alice-learning-resources.xml \
    -f invenio_opendata/testsuite/data/alice/alice-reconstructed-data.xml \
    -f invenio_opendata/testsuite/data/alice/alice-vm-image.xml \
    -f invenio_opendata/testsuite/data/atlas/atlas-derived-datasets.xml \
    -f invenio_opendata/testsuite/data/atlas/atlas-higgs-challenge-2014.xml \
    -f invenio_opendata/testsuite/data/atlas/atlas-learning-resources.xml \
    -f invenio_opendata/testsuite/data/atlas/atlas-tools.xml \
    -f invenio_opendata/testsuite/data/cms/cms-author-list.xml \
    -f invenio_opendata/testsuite/data/cms/cms-csv-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-derived-pattuples-ana.xml \
    -f invenio_opendata/testsuite/data/cms/cms-eventdisplay-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-eventdisplay-files-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-hamburg-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-learning-resources.xml \
    -f invenio_opendata/testsuite/data/cms/cms-masterclass-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-open-data-instructions.xml \
    -f invenio_opendata/testsuite/data/cms/cms-primary-datasets.xml \
    -f invenio_opendata/testsuite/data/cms/cms-primary-datasets-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-trigger-information-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-trigger-path-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-ana.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-dimuon-filter.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-ispy.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-vm-image.xml \
    -f invenio_opendata/testsuite/data/cms/cms-validated-runs.xml \
    -f invenio_opendata/testsuite/data/cms/cms-condition-data-Run2010B.xml \
    -f invenio_opendata/testsuite/data/cms/cms-condition-data-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-configuration-files-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-hlt-2011-configuration-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-pileup-configuration-files.xml \
    -f invenio_opendata/testsuite/data/cms/cms-simulated-datasets-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-dimuon-spectrum-2010.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-vm-image-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-cmssw.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-cmssw-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-ispy-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-tools-ana-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-derived-pattuples-ana-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-author-list-Run2011A.xml \
    -f invenio_opendata/testsuite/data/cms/cms-validation-code-Run2010B.xml \
    -f invenio_opendata/testsuite/data/cms/cms-l1-trigger-information-Run2011A.xml \
    -f invenio_opendata/testsuite/data/lhcb/lhcb-derived-datasets.xml \
    -f invenio_opendata/testsuite/data/lhcb/lhcb-learning-resources.xml \
    -f invenio_opendata/testsuite/data/lhcb/lhcb-tools.xml \
    -f invenio_opendata/testsuite/data/data-policies.xml \
    -e force-recids --yes-i-know

Now you should be able to see the populated site::

  firefox http://127.0.0.1:28080/

Running
=======

The data in your newly built Docker containers are persistent.  You
can stop the containers by e.g. interrupting the ``docker-compose up``
process at any time, and bring your work back up by doing::

  cd ~/private/src/opendata.cern.ch
  docker-compose -f docker-compose-dev.yml up

Developing
==========

The sources in your local directories ``~/private/src/invenio`` and
``~/private/src/opendata.cern.ch`` are mounted in your running Docker
containers when ``docker-compose up`` starts them.  Hence you can
simply edit the files directly on your laptop and observe the changes
in the running application.

JS/CSS Assets
=============

If you change JS or CSS requirements, you may need to rebuild
bundles::

  docker exec -i -t -u invenio opendatacernch_web_1 \
    sh -c 'inveniomanage bower -i bower-base.json > bower.json'
  docker exec -i -t -u invenio opendatacernch_web_1 \
    sh -c 'CI=true bower install'
  docker exec -i -t -u invenio opendatacernch_web_1 \
    inveniomanage collect

See also
========

* http://invenio.readthedocs.org/en/latest/developers/docker.html


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
