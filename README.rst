===================
 open-data.cern.ch
===================

About
-----

This is `open-data.cern.ch <http://open-data-demo.cern.ch>`_ source
code overlay that installs on top of `Invenio
<https://github.com/inveniosoftware/invenio>`_ digital library
platform.

Installation
------------

If you'd like to install an open-data demo site for personal
developments, you can use `invenio2-kickstart
<https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart>`_
helper script and proceed as follows:

* Firstly, fire up new VM:

.. code-block:: console

    laptop> mkdir -p ~/private/vm/invenio2trusty64
    laptop> cd ~/private/vm/invenio2trusty64
    laptop> vim Vagrantfile # enter following content:
    Vagrant.configure("2") do |config|
      config.vm.box = "trusty64"
      config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/20140813/trusty-server-cloudimg-amd64-vagrant-disk1.box"
      config.vm.hostname = 'localhost.localdomain'
      config.vm.network :forwarded_port, host: 8080, guest: 8080
      config.vm.network :forwarded_port, host: 8443, guest: 8443
      config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
      end
    end
    laptop> vagrant up

* Secondly, connect to the VM and launch Invenio kickstarter with
  open-data.cern.ch overlay:

.. code-block:: console

    laptop> vagrant ssh
    vm> wget https://raw.githubusercontent.com/tiborsimko/invenio-devscripts/master/invenio2-kickstart
    vm> chmod u+x ./invenio2-kickstart
    vm> CFG_INVENIO2_REPOSITORY_OVERLAY=git://github.com/tiborsimko/open-data.cern.ch \
        CFG_INVENIO2_VIRTUAL_ENV=opendata \
        CFG_INVENIO2_DATABASE_USER=opendata \
        CFG_INVENIO2_DATABASE_NAME=opendata \
        ./invenio2-kickstart --yes-i-know --yes-i-really-know

* Thirdly, go brew some tee, come back in twenty minutes, enjoy!

.. code-block:: console

    laptop> firefox http://0.0.0.0:8080/

See also
--------

* http://invenio.readthedocs.org/en/latest/getting-started/overlay.html
