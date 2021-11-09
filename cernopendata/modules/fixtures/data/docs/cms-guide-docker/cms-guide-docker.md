## Introduction

As an alternative to using a virtual machine, you can run CMS analysis code in a [Docker](https://www.docker.com/) container. If you have not already installed Docker instructions for installation are [provided by Docker](https://docs.docker.com/install/). For an introduction, you can also follow the links provided in [the CMS Open data guide](https://cms-opendata-guide.web.cern.ch/tools/docker/).

## Available CMSSW container images

For the first access of each set of CMS open data, you will need a specific container image containing the software corresponding to that particular set of data. The following images are available:

| CMS open data | CMSSW version | Container image (dockerhub) | Alternative image location (GitLab) |
| ------------- |-------------| -----| -----: |
| 2015 proton-proton | CMSSW_7_6_7 | cmsopendata/cmssw_7_6_7 (not yet) | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker/container_registry/10519) |
| 2011-2012 proton-proton | CMSSW_5_3_32 | cmsopendata/cmssw_5_3_32 cmsopendata/cmssw_5_3_32_vnc | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker-opendata/container_registry/10289) <br /> [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker-opendata/container_registry/10290) |
| 2011 heavy-ion | CMSSW_4_4_7 | cmsopendata/cmssw_4_4_7 (not yet) | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker/container_registry/8237) |
| 2010 proton-proton | CMSSW_4_2_8 | cmsopendata/cmssw_4_2_8 | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker/container_registry/7721) |
| 2010 proton-proton with CASTOR calorimeter | CMSSW_4_2_8_lowpupatch1 | cmsopendata/cmssw_4_2_8_lowpupatch1 | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker/container_registry/10519) |
| 2010 heavy-ion | CMSSW_3_9_2_patch5 | cmsopendata/cmssw_3_9_2_patch5 (not yet) | [link](https://gitlab.cern.ch/cms-cloud/cmssw-docker/container_registry/8225) |

## Fetch a CMSSW image and start a container

In the following instructions, make sure to replace the CMSSW version and the container image name according to the table above. These commands are for 2011-2012 proton-proton data, with the CMSSW version CMSSSW_5_3_32 and the cmssw_5_3_32 container image.

Once Docker is installed, you can fetch a CMSSW image, and create and start a container using the `docker run` command:

```sh
docker run --name my_od -it cmsopendata/cmssw_5_3_32 /bin/bash
```

Here we fetch the `cmssw_5_3_32` docker image from [dockerhub](https://hub.docker.com/u/cmsopendata) and name the container `my_od`.

This will install a stand-alone CMSSW image (a few gigabytes). Therefore this may take a few minutes. However, the image will only have to be downloaded once. The following will appear in your terminal once you type the `docker run` command:

```console
Unable to find image 'cmsopendata/cmssw_5_3_32' locally
latest: Pulling from cmsopendata/cmssw_5_3_32
e8114d4b0d10: Pull complete
a3eda0944a81: Pull complete
a88502447863: Pull complete
Digest: sha256:6b9a12992ba088a168b87df98a841d3c56dede326684f5551368fd359acfb43c
Status: Downloaded newer image for cmsopendata/cmssw_5_3_32:latest
Setting up CMSSW_5_3_32
CMSSW should now be available.
```

Once done, you should see the commmand prompt for the CMSSW instance within Docker:

```console
cmsusr@eb9ecf54fd2a ~/CMSSW_5_3_32/src $
```

## Further instructions

### Install and run CMS example code

Now you can try an example code like [Physics Object Extractor Tool (POET)](https://github.com/cms-legacydata-analyses/PhysObjectExtractorTool) which has separate "branches" for different data. The following commands are for 2012 data (branch name `2012`). For 2015 data, you would have fetched the cmssw_7_6_7 container image, be working in `~/CMSSW_7_6_7/src` area, and the branch name to be used would be `2015MiniAOD`.

In the command prompt in `~/CMSSW_<version>/src` run the following commands:

```sh
git clone -b 2012 git://github.com/cms-legacydata-analyses/PhysObjectExtractorTool.git
cd PhysObjectExtractorTool
```

Move to the `PhysObjectExtractor` directory and compile with the `scram` command:

```sh
cd PhysObjectExtractor
scram b
```

Once the code is built, you can run the example analysis:

```sh
cmsRun python/poet_cfg.py
```

which will produce a file `myoutput.root`.

### Copying files

In order to copy files out of a running container, open another terminal and run (for example) the following command:

```sh
docker cp my_od:/home/cmsusr/CMSSW_5_3_32/src/PhysObjectExtractorTool/PhysObjectExtractor/myoutput.root .
```

Likewise, in order to copy a file into a running container:


```sh
docker cp <my file> my_od:/home/cmsusr/CMSSW_5_3_32/src/
```

### Graphics with X11 forwarding with docker on Linux

If you want to use ROOT or some other program from within the container that needs X11-forwarding for the graphics to pop up, on Linux, you can start the container with

```sh
docker run -it --name my_od --net=host --env="DISPLAY" -v $HOME/.Xauthority:/home/cmsusr/.Xauthority:rw  cmsopendata/cmssw_5_3_32:latest /bin/bash
```

### Graphics with VNC

For opening graphics windows, as an alternative to X11 forwarding, you can install a VNC server on you local computer (Linux, MacOS or Windows), and use the container image with a VNC application installed. In this case, you can start the container with

```sh
docker run -it --name my_od -P -p 5901:5901 cmsopendata/cmssw_5_3_32_vnc:latest /bin/bash
```

and start the VNC application in the container with

```sh
start_vnc
```

### Using ROOT

If you have set up X11 forwarding or use a container with VNC as explained above, you can explore the example output file with ROOT. Start ROOT with

```sh
root myoutput.root
```

If it has worked, you’ll see the ROOT splash screen. If you are already familiar with ROOT, you can explore the example root file. If you are new to ROOT, have a quick look to [the Getting started page](/docs/cms-getting-started-2015), or follow the links in [the CMS open data guide](https://cms-opendata-guide.web.cern.ch/tools/root/), and note that you can exit root with `.q`.



### Exiting and restarting a container

When you want to exit the container simply type `exit`.

If you want to restart the container (e.g. the one named `my_od`) and return to your work then use the command `docker start -i my_od`.

If the container was created and started using the `--rm` option (e.g. `docker run --rm`) then the container will be removed when you exit. You can create a new container from the image using `docker run`.


### Running CMS open data containers on WSL2

The CMS open data containers, or any CentOS6-based containers, may fail if docker is run on WSL2. This problem is fixed by adding a new file `.wslconfig` with the following contents

```sh
[wsl2]
kernelCommandLine = vsyscall=emulate
```

in \Users\[username] (without extension), then shutting down with `wsl --shutdown` in the Windows command prompt and restarting again.

Test that the settings are properly passed by doing, in the WSL2 linux installation:

```sh
docker run -ti ubuntu cat /proc/cmdline
```

The ouput should contain `vsyscall=emulate`, e.g.:

```sh
initrd=\initrd.img panic=-1 pty.legacy_count=0 nr_cpus=4 vsyscall=emulate
```

### Accessing cvmfs from a container

The CMS open data container images contain the software needed for analysis, and the CMS condition database can be accessed from predefined locations. Therefore, when using these containers, access to the namespace `/cvmfs` (CernVM-File System) for software and condition data access is not mandatory.

If desired, it is possible to "see" the cvmfs space by installing the cvmfs client following [the official instructions](https://cvmfs.readthedocs.io). In essence, there are two basic ways to achieve this:

The preferred option is to [install](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) the cvmfs client locally, on the host machine, and [mount](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#bind-mount-from-the-host) it on the container:

```sh
docker run --name my_od -it -v "/cvmfs:/cvmfs:shared" cmsopendata/cmssw_5_3_32 /bin/bash
```

The other option is to [install](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) the cvmfs client directly in the container after it is created (only working for the slc6-based containers).  For this, the container needs to get started in [privileged](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#mount-inside-a-container) mode like

```sh
docker run --privileged --name my_od -it cmsopendata/cmssw_5_3_32 /bin/bash
```
