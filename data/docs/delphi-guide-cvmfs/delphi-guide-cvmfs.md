The DELPHI software is also availabe on CVMFS. Many decent Linux flavors are supported, however, there are no generic binaries available for Windows and MacOS.
If you run on Windows, you can use the Windows for Linux subsystem, using one of the supported systems, for example Ubuntu. It is possible to install both CVMFS
and EOS, allowing for direct access to the data.

This method is convenient if you are running a desktop or a virtual machine with one of the supported Linux flavors on it.

Running the stack locally from CVMFS has some advantages, in particular if the EOS storage system is available on the same host:

* No need to copy the data locally and expose them to the container.
* Software development can be done locally, without the risk to loose your work if the container is accidentially destroyed.
* Easy access to hardware accellerated graphics when running on the local desktop. This is only relevant for the event display though.
* No need for podman or docker.

## Requirements
You will need to have:

* */cvmfs/delphi.cern.ch* mounted. Documentation can be found at https://cvmfs.readthedocs.io/en/stable/
* */eos/opendata/delphi* mounted. More information about EOS can be found at https://github.com/cern-eos/eos
* A list of additional packages installed, see https://gitlab.cern.ch/delphi/deployment for more information:
    * general: tcsh xfonts-100dpi xfonts-75dpi libxfont2
    * compilers: cmake gcc g++ gfortran
    * library packages: libx11 libglu1-mesa xutils libmotif r-base xutils libxbae libxaw7 libssl libglew libdlm

Please check the instructions at https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html, https://eoscta.docs.cern.ch/install/eos/ and https://eos-web.web.cern.ch/eos-web.

## Initialising the environment
For C-Shell (csh, tcsh ), do

```
$ source /cvmfs/delphi.cern.ch/setup.csh
```

For Bourne shell (sh, bash, zsh, ...), type
```
$ . /cvmfs/delphi.cern.ch/setup.sh
```

After sourcing the environment, make sure that the environment variable **DELPHI_DATA_ROOT** points to the tip of the data area. This is specifically
important if you copied the data sets you want to use locally. It should default to */eos/opendata/delphi*.
