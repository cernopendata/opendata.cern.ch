============
 Developing
============

.. contents::
   :backlinks: none

Installation
============

If you'd like to install CERN Open Data portal demo site locally for
your personal developments, you can use `invenio2-kickstart
<https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart>`_
helper script and proceed as follows:

Firstly, fire up new VM:

.. code-block:: console

    laptop> mkdir -p ~/private/vm/opendata2trusty64
    laptop> cd ~/private/vm/opendata2trusty64
    laptop> vim Vagrantfile # enter following content:
    Vagrant.configure("2") do |config|
      config.vm.box = "trusty64"
      config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"
      config.vm.hostname = 'localhost.localdomain'
      config.vm.network :forwarded_port, host: 8080, guest: 8080
      config.vm.network :forwarded_port, host: 8443, guest: 8443
      config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
      end
    end
    laptop> vagrant up

Secondly, connect to the VM and launch Invenio kickstarter with
opendata.cern.ch overlay:

.. code-block:: console

    laptop> vagrant ssh
    vm> wget https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart
    vm> chmod u+x ./invenio2-kickstart
    vm> CFG_INVENIO2_REPOSITORY_OVERLAY=git://github.com/tiborsimko/opendata.cern.ch \
        CFG_INVENIO2_VIRTUAL_ENV=opendata \
        CFG_INVENIO2_DATABASE_USER=opendata \
        CFG_INVENIO2_DATABASE_NAME=opendata \
        CFG_INVENIO2_DEMOSITE_POPULATE_BEFORE="rsync -a invenio_opendata/testsuite/data/*/eos-file-indexes /tmp/" \
        CFG_INVENIO2_DEMOSITE_POPULATE="-f invenio_opendata/testsuite/data/cms/cms-primary-datasets.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-derived-pattuples-ana.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-eventdisplay-files.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-ana.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-ispy.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-vm-image.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-validated-runs.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-external-resources.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-masterclass-files.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-csv-files.xml \
                                        -f invenio_opendata/testsuite/data/alice/alice-derived-datasets.xml \
                                        -f invenio_opendata/testsuite/data/alice/alice-analysis-modules.xml \
                                        -e force-recids" \
        ./invenio2-kickstart --yes-i-know --yes-i-really-know

Thirdly, go brew some tee, come back in twenty minutes, enjoy!

.. code-block:: console

    laptop> firefox http://0.0.0.0:8080/

Running
=======

The above kickstarter will already start Invenio application for you.
Should you shut down and reboot your VM, you need to restart Invenio
as follows:

.. code-block:: console

    laptop> cd ~/private/vm/opendata2trusty64
    laptop> vagrant halt
    laptop> vagrant up
    laptop> vagrant ssh
    vm> workon opendata
    vm> cdvirtualenv src/invenio
    vm> honcho start

You can keep `honcho` running in a screen session for example.

Upgrading
=========

To upgrade your installation, it is sufficient to pull latest versions
of this overlay:

.. code-block:: console

    vm> workon opendata
    vm> cdvirtualenv src/opendata.cern.ch
    vm> git pull

You can also update Invenio itself:

.. code-block:: console

    vm> cdvirtualenv src/invenio
    vm> git pull

Populating
==========

If you change incoming data files for example and if you'd like to
re-populate your site anew to have your updated records, you can do:

.. code-block:: console

    vm> workon opendata
    vm> inveniomanage database recreate --yes-i-know
    vm> inveniomanage demosite populate --packages=invenio_opendata.base \
         -f invenio_opendata/testsuite/data/cms/cms-primary-datasets.xml \
         -f invenio_opendata/testsuite/data/cms/cms-derived-pattuples-ana.xml \
         -f invenio_opendata/testsuite/data/cms/cms-eventdisplay-files.xml \
         -f invenio_opendata/testsuite/data/cms/cms-tools-ana.xml \
         -f invenio_opendata/testsuite/data/cms/cms-tools-ispy.xml \
         -f invenio_opendata/testsuite/data/cms/cms-tools-vm-image.xml \
         -f invenio_opendata/testsuite/data/cms/cms-validated-runs.xml \
         -f invenio_opendata/testsuite/data/cms/cms-external-resources.xml \
         -f invenio_opendata/testsuite/data/cms/cms-masterclass-files.xml \
         -f invenio_opendata/testsuite/data/cms/cms-csv-files.xml \
         -f invenio_opendata/testsuite/data/alice/alice-derived-datasets.xml \
         -f invenio_opendata/testsuite/data/alice/alice-analysis-modules.xml \
         -e force-recids

JS/CSS Assets
=============

If you change JS or CSS requirements, you'd need to rebuild bundles:

.. code-block:: console

    vm> workon opendata
    vm> cdvirtualenv src/opendata.cern.ch
    vm> inveniomanage bower -i bower-base.json > bower.json
    vm> CI=true bower install
    vm> inveniomanage collect

See also
========

* http://invenio.readthedocs.org/en/latest/getting-started/overlay.html


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

Working on topical branches
---------------------------

You are now ready to work on something.  You should always create
separate topical branches for separate issues:

.. code-block:: console

   $ git checkout pu
   $ git checkout -b fix-event-display-icons
   $ emacsclient some_file.py
   $ git commit -a -m 'some fix'
   $ emacsclient some_other_file.py
   $ git commit -a -m 'some other fix'

When everything is ready, you may want to rebase your topical branch
to get rid of unnecessary commits:

.. code-block:: console

   $ git checkout fix-event-display-icons
   $ git rebase pu -i # squash commits here

Making pull requests
--------------------

You are now ready to issue a pull request: just push your branch in
your personal repository:

.. code-block:: console

   $ git push origin fix-event-display-icons

and use GitHub's "Pull request" button to make the pull request.

Updating pull requests
----------------------

Consider the integrator had some remarks about your branch and you
have to update your pull request.

Firstly, update to latest upstream "pu" branch, in case it may have
changed in the meantime:

.. code-block:: console

   $ git checkout pu
   $ git fetch upstream
   $ git merge upstream/pu --ff-only

Secondly, make any required changes on your topical branch:

.. code-block:: console

   $ git checkout fix-event-display-icons
   $ emacsclient some_file.py
   $ git commit -a -m 'amends something'

Thirdly, when done, interactively rebase your topical branch into
nicely organised commits:

.. code-block:: console

   $ git rebase pu -i # squash commits here

Finally, re-push your topical branch with a force option in order to
update your pull request:

.. code-block:: console

   $ git push origin fix-event-display-icons -f

Finishing pull requests
-----------------------

If your pull request has been merged upstream, you should update your
local sources:

.. code-block:: console

   $ git checkout pu
   $ git fetch upstream
   $ git merge upstream/pu --ff-only

You can now delete your topical branch locally:

.. code-block:: console

   $ git branch -d fix-event-display-icons

and remove it from your repository as well:

.. code-block:: console

   $ git push origin pu
   $ git push origin :fix-event-display-icons

This would conclude your work on ``fix-event-display-icons``.
