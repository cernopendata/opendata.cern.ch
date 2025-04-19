============
 Developing
============

.. contents::
   :backlinks: none

This document describes how you can run a local instance of the CERN Open Data
portal in order to work with the content records and associated documentation.

Prerequisites
=============

You will need to fork and clone two repositories:

- `opendata.cern.ch <https://github.com/cernopendata/opendata.cern.ch>`_ which
  contains the open data content;

- `cernopendata-portal <https://github.com/cernopendata/cernopendata-portal>`_
  which contains the portal infrastructure code.

Please make sure to also install `Docker
<https://docs.docker.com/get-started/get-docker/>`_ and `Docker Compose
<https://docs.docker.com/compose/install/>`_ (version 2) that is used for local
developments.

You will also need to pull Docker container images from `CERN Harbor registry
<https://registry.cern.ch/>`_. If this is your first time using CERN Harbor,
you will need to login using a command-line secret that you can obtain at
`registry.cern.ch <https://registry.cern.ch/>`_ in the right-hand-side menu
"johndoe > User Profile". Once you obtain and copy your CLI secret, you can
login to the CERN Harbor registry as follows:

.. code-block:: console

   $ docker login registry.cern.ch -u johndoe

Installation
============

In order to create a local CERN Open Data portal instance, please proceed as
follows:

.. code-block:: console

   $ git clone https://github.com/cernopendata/opendata.cern.ch
   $ git clone https://github.com/cernopendata/cernopendata-portal
   $ cd cernopendata-portal && git checkout -B stable v0.2.9
   $ cd ../opendata.cern.ch
   $ docker compose pull
   $ docker compose up -d
   $ sleep 120 # give enough time for the containers to start properly
   $ docker exec -i -t opendatacernch-web-1 /code/scripts/populate-instance.sh \
        --skip-records --skip-docs --skip-glossary

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

Upload the locally-modified file into your instance:

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
this would require working with the `cernopendata-portal` repository. Please
see its own `documentation
<https://github.com/cernopendata/cernopendata-portal/>`_ about how to add new
metadata fields. We would be happy to assist with the process.

Understanding output templates
==============================

If you would like to change the way how the data records are displayed on the
web, for example to introduce new section displaying newly added field, this is
something that is governed by `Jinja templating language
<https://jinja.palletsprojects.com/en/2.10.x/templates/>`_ in the
`cernopendata-portal` repository. Please see its own `documentation
<https://github.com/cernopendata/cernopendata-portal/>`_ about how to amend
look and feel of the record metadata. We would be happy to assist with the
process.

Verifying metadata conformance
==============================

You can use the provided helper script `check_fixtures.py` to check the
conformance of record files to the required minimal standard:

.. code-block:: console

   $ ./scripts/check_fixtures.py

Working with documents: metadata
================================

If you would like to work with certain documents and test your edits on your
local instance, you can proceed as follows.

Edit the record file, such as About LHCb documentation:

.. code-block:: console

   $ vim data/docs/lhcb-about/lhcb-about.json
   $ vim data/docs/lhcb-about/lhcb-about.md

Upload the locally-modified file into your instance:

.. code-block:: console

   $ docker exec -i -t opendatacernch-web-1 cernopendata fixtures docs \
        --mode insert-or-replace \
        -f data/docs/lhcb-about/lhcb-about.json

Note that, similarly as for records, we are uploading document JSON files,
using the `fixtures docs` command. Even if you would like to change only the
document content that is living in the associated Markdown files, the document
JSON file is to be uploaded.

You can then check your changes at `http://127.0.0.1:500
<http://127.0.0.1:5000>`_.

Working with documents: Markdown
================================

The portal uses `Python-markdown <https://python-markdown.github.io/>`_ for
Markdown rendering. There are `some differences
<https://python-markdown.github.io/#differences>`_ between this implementation
and the `syntax rules <https://daringfireball.net/projects/markdown/syntax>`_,
mainly concerning lists:

* You must always use 4 spaces (or a tab) for indentation and the same
  character (-, \*, +, numbers) for items list.
* To add a Table Of Contents to a document, please place the identifier
  ``[TOC]`` where you want it to be.

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

Working with document: LaTeX
============================

LaTeX is enabled with the `mdx_math` extension. Inline equations are between
single ``$``, e.g. ``$E = m c^2$``. For standalone math, use ``\[...\]``.

Working with documents: images
==============================

Sometimes the document pages may have illustrating images. The images should be
placed into the `data/images` directory following the document slug. They can
then be referred to in your Markdown content by means of links. Please check an
existing documentation page such as
``totem-releases-first-set-of-open-data.md`` and where it stores and how it
loads the illustrating image ``totem-roman-pots-in-the-lhc-tunnel.jpeg``.

After you add an image and reference it in your Markdown source file, you
should load the image into the system:
portal instance,

.. code-block:: console

   $ docker compose exec -it web /content/scripts/load-images.sh

You should now be able to see the image locally in the document record.

Appendix A: repository structure
================================

This repository holds the sources behind the CERN Open Data portal content. The
bibliographic records live as JSON files, the documentation records live as
JSON files with Markdown content and possible associated images. The repository
is structured as follows:

- ``data/docs``: This directory contains the source of the documentation pages.
  Each documentation page is identifies by a slug under which it is exposed in
  the portal web interface. The documentation sources are then usually living
  in a dedicated directory named with the slug. The documentation page lives as
  a JSON file with the appropriate metadata describing title, authors, short
  abstract, etc. The documentation page body usually lives as a separate
  Markdown file that is linked from the JSON file.

- ``data/images``: This directory contains any illustrative images that the
  documentation pages may use. The images are usually stored in a similar
  slug-based directories to make a link to the documentation page where they
  are used.

- ``data/records``: This directory contains the source of the bibliographic
  records representing the main open data content (collision data, simulated
  data, derived data, software, examples, configuration files, etc). The master
  format is JSON following the schema of allowed optional and required fields.
  It is usually in this directory where you would prepare new records for
  inclusion into the open data portal.

- ``data/skeletons``: This is a special directory that holds only "skeletons"
  of bibliographic records, i.e. snippets of record JSON files containing only
  persistent identifies such as record IDs, DOIs, and record titles. This is
  used only in cases where the record content is huge, such as 40k of CMS 2016
  simulated data, which would not be practical to store in a git repository.
  You could consider record skeletons to serve as a sort of "git lfs" pointer
  to where the record JSON tarball is hosted, all the while keeping persistent
  identifiers in this repository in order to avoid any mishap of "reserved"
  identifiers. Usually, you would not work in this repository.

- ``scripts``: This directory contains helper scripts assisting in record
  preparation, such as metadata formatters and checkers. This helps to make
  sure that the record JSON files are correct, and that they are formatted in
  the unique way regardless of different text editors the different
  collaborators may be using, preventing their subsequent reformatting.

- ``run-tests.sh``: This helper script is used to perform all the metadata
  checks in the Continuous Integration process. You can also run it locally
  prior to submitting your pull requests.

Appendix B: Git workflow
========================

Here is detailed example of our `GitHub flow
<https://guides.github.com/introduction/flow/index.html>`_.

Setting up repository
---------------------

Let's assume your GitHub account name is ``johndoe``.

Firstly, fork `opendata.cern.ch repository
<https://github.com/cernopendata/opendata.cern.ch/>`_ by using the "Fork"
button on the top right.  This will give you your personal repository:

.. code-block:: console

   http://github.com/johndoe/opendata.cern.ch

Secondly, clone this repository onto your laptop and set up remotes so that
``origin`` would point to your repository and ``upstream`` would point to the
canonical location:

.. code-block:: console

   $ cd ~/private/src
   $ git clone git@github.com:johndoe/opendata.cern.ch
   $ cd opendata.cern.ch
   $ git remote add upstream git@github.com:cernopendata/opendata.cern.ch

Optionally, if you are also going to integrate work of others, you may want to
set up `special PR branches
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
  What is installed on the bleeding edge `development server <http://opendata-dev.cern.ch>`_.

qa
  What is installed on the pre-production `quality assurance server <http://opendata-qa.cern.ch>`_.

production
  What is installed on the `production server <http://opendata.cern.ch>`_.

The life-cycle of a typical new feature is therefore: (1) development starts on
a personal laptop in a new topical branch stemming from the ``master`` branch;
(2) when the feature is ready, the developer issues a pull request, the branch
is reviewed by the system integrator, merged into the ``qa`` branch , and
deployed on the pre-production server; (3) after sufficient testing time on the
pre-publication server, the feature is merged into the ``production`` branch
and deployed on the production server.

The following sections document the development life cycle in fuller detail.

Working on topical branches
---------------------------

You are now ready to work on something.  You should always create
separate topical branches for separate issues.

Here is example:

.. code-block:: console

   $ git checkout master
   $ git checkout -b fix-cms-about-page-content-typos
   $ vim data/docs/cms-about/cms-about.md
   $ git commit -a -m 'fix(docs): correct About CMS page typos'
   $ vim data/docs/cms-about/cms-about.md
   $ git commit -a -m 'fix(docs): more About CMS grammatical fixes'

When everything is ready, you may want to rebase your topical branch
to get rid of unnecessary commits:

.. code-block:: console

   $ git checkout fix-cms-about-page-content-typos
   $ git rebase master -i  # squash commits here

Making pull requests
--------------------

You are now ready to issue a pull request: just push your branch in
your personal repository:

.. code-block:: console

   $ git push origin fix-cms-about-page-content-typos

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

   $ git checkout fix-cms-about-page-content-typos
   $ vim data/docs/cms-about/cms-about.md
   $ git commit -a --no-edit

Thirdly, when done, interactively rebase your topical branch into
nicely organised commits:

.. code-block:: console

   $ git rebase master -i  # squash commits here

Finally, re-push your topical branch with a force option in order to
update your pull request:

.. code-block:: console

   $ git push origin fix-cms-about-page-content-typos -f

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

   $ git branch -d fix-cms-about-page-content-typos

and remove it from your repository as well:

.. code-block:: console

   $ git push origin master
   $ git push origin :fix-cms-about-page-content-typos

This would conclude your work on ``fix-cms-about-page-content-typos`` branch.

Appendix C: Git commit messages
===============================

We are using `conventional commits
<https://www.conventionalcommits.org/en/v1.0.0/>`_ style which is also checked
by the continuous integration process.

The commit message structure is as follows:

.. code-block:: text

    <type>(scope): <description>

    [optional body line 1]
    [optional body line 2]
    [optional body line 3]

    [optional footer: BREAKING CHANGE: foo bar blah]
    [optional footer: Closes #<issuenumber>]

The commit message headline examples:

.. code-block:: text

    feat(skeletons): add CMS 2016 SIM record skeletons
    fix(docs): remove trailing slash from TOTEM release image URL
    fix(records): improve description of DELPHI full DST manuals
    build(docker): upgrade cernopendata-portal to 0.2.5

The commit message types are:

- **build** for changes affecting the build process or external dependencies (e.g. docker)
- **chore** for miscellaneous tasks not affecting source code or tests (e.g. release)
- **ci** for changes affecting continuous integration (e.g. linting)
- **docs** for documentation-only changes
- **feat** for changes introducing new features or backwards-compatible improvements to existing features
- **fix** for changes fixing bugs
- **perf** for changes improving performance without changing functionality
- **refactor** for changes that do not fix bugs or add features
- **style** for changes not affecting the meaning (e.g. formatting)
- **test** for adding missing tests or correcting existing tests

The commit message scope refers to an internal module of this repository, which
would be typically ``records`` and ``docs``, and occasionally something else
such as ``scripts``. So, in the vast majority of cases, you may be writing
``feat(records)`` when adding new records, ``fix(docs)`` when fixing existing
docs, etc.
