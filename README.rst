==================
 opendata.cern.ch
==================

About
-----

This is `opendata.cern.ch <http://opendata.cern.ch>`_ source code
overlay that installs on top of `Invenio
<https://github.com/inveniosoftware/invenio>`_ digital library
platform.

Installation
------------

If you'd like to install an opendata site for personal developments,
you can use `invenio2-kickstart
<https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart>`_
helper script and proceed as follows:

* Firstly, fire up new VM:

.. code-block:: console

    laptop> mkdir -p ~/private/vm/opendata2trusty64
    laptop> cd ~/private/vm/opendata2trusty64
    laptop> vim Vagrantfile # enter following content:
    Vagrant.configure("2") do |config|
      config.vm.box = "trusty64"
      config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/20140813/trusty-server-cloudimg-amd64-vagrant-disk1.box"
      config.vm.hostname = 'localhost.localdomain'
      config.vm.network :forwarded_port, host: 8080, guest: 8080
      config.vm.network :forwarded_port, host: 8443, guest: 8443
      config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "2048"]
        vb.customize ["modifyvm", :id, "--cpus", "2"]
      end
    end
    laptop> vagrant up

* Secondly, connect to the VM and launch Invenio kickstarter with
  opendata.cern.ch overlay:

.. code-block:: console

    laptop> vagrant ssh
    vm> wget https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart
    vm> chmod u+x ./invenio2-kickstart
    vm> CFG_INVENIO2_REPOSITORY_OVERLAY=git://github.com/tiborsimko/opendata.cern.ch \
        CFG_INVENIO2_VIRTUAL_ENV=opendata \
        CFG_INVENIO2_DATABASE_USER=opendata \
        CFG_INVENIO2_DATABASE_NAME=opendata \
        CFG_INVENIO2_DEMOSITE_POPULATE="-f invenio_opendata/testsuite/data/cms/cms-primary-datasets.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-derived-pattuples-ana.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-eventdisplay-files.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-ana.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-ispy.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-tools-vm-image.xml \
                                        -f invenio_opendata/testsuite/data/cms/cms-validated-runs.xml \
                                        -e force-recids" \
        ./invenio2-kickstart --yes-i-know --yes-i-really-know

* Thirdly, go brew some tee, come back in twenty minutes, enjoy!

.. code-block:: console

    laptop> firefox http://0.0.0.0:8080/

See also
--------

* http://invenio.readthedocs.org/en/latest/getting-started/overlay.html
