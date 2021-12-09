## Introduction

You can run CMS analysis code in a [Docker](https://www.docker.com/) container provided together with the CMS open data. If you have not already installed Docker, instructions for installation are [provided by Docker](https://docs.docker.com/install/). For an introduction and for getting started, you can follow the links provided in [the CMS Open data guide](https://cms-opendata-guide.web.cern.ch/tools/docker/).

## Available CMSSW container images

For the first access of each set of CMS open data, you will need a specific container image containing the software corresponding to that particular set of data. The following images are available:

| CMS open data | CMSSW version | Container image (dockerhub) <br> Alternative image location (GitLab) |
| ------------- |-------------| -----|
| 2015 proton-proton | CMSSW_7_6_7 | cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_7_6_7-slc6_amd64_gcc493` |
| 2011-2012 proton-proton | CMSSW_5_3_32 | cmsopendata/cmssw_5_3_32-slc6_amd64_gcc472 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_5_3_32-slc6_amd64_gcc472` |
| 2011 heavy-ion | CMSSW_4_4_7 | cmsopendata/cmssw_4_4_7-slc5_amd64_gcc434 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_4_7-slc5_amd64_gcc434` |
| 2010 proton-proton | CMSSW_4_2_8 | cmsopendata/cmssw_4_2_8-slc5_amd64_gcc434 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_2_8-slc5_amd64_gcc434` |
| 2010 proton-proton with CASTOR calorimeter | CMSSW_4_2_8_lowpupatch1 | cmsopendata/cmssw_4_2_8_lowpupatch1-slc5_amd64_gcc434 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_2_8_lowpupatch1-slc5_amd64_gcc434` |
| 2010 heavy-ion | CMSSW_3_9_2_patch5 | cmsopendata/cmssw_3_9_2_patch5-slc5_amd64_gcc434 <br> `gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_3_9_2_patch5-slc5_amd64_gcc434` |

## Fetch a CMSSW image and start a container

In the following instructions, make sure to replace the CMSSW version and the container image name according to the table above. These commands are for 2015 proton-proton data, with the CMSSW version 7_6_7 and the `cmssw_7_6_7-slc6_amd64_gcc493` container image.

Once you have installed Docker on your computer, you can fetch a CMSSW image, and create and start a container using the `docker run` command:

```sh
docker run --name my_od -P -p 5901:5901 -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```

Here we fetch the `cmssw_7_6_7-slc6_amd64_gcc493` docker image from [dockerhub](https://hub.docker.com/u/cmsopendata) and name the container `my_od`.

This will install a stand-alone CMSSW image (several gigabytes). Therefore this may take a while. However, the image will only have to be downloaded once. The following will appear in your terminal, with messages changing during the download:

```console
$ docker run --name my_od -P -p 5901:5901 -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
Unable to find image 'cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493:latest' locally
latest: Pulling from cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493
a34e8f61dde2: Already exists
c341e9bd0d75: Pull complete
b00c4ec204ea: Pull complete
b75a825d190f: Pull complete
c1d073a0336d: Pull complete
650dcb078423: Pull complete
90c8f402a4b2: Pull complete
6fbc78240c7f: Pull complete
1a000c4d9168: Pull complete
684aeffff49a: Pull complete
2bf2b8821c7a: Pull complete
c3325087056c: Pull complete
acc958e9a46a: Pull complete
aebfbe474a64: Pull complete
e869fa526195: Pull complete
80a3efb6451b: Pull complete
b27531c14546: Pull complete
dc3997c36289: Pull complete
af1734a85201: Pull complete
0a263c644307: Pull complete
ba24eee3284a: Pull complete
a622f52fef0b: Pull complete
aff80dc8ccdd: Pull complete
49f941d726e3: Pull complete
Digest: sha256:f5ec05556302a31fd59ce031af06e9a6163990a6d4a64aacf76b7c775667c65e
Status: Downloaded newer image for cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493:latest
Setting up CMSSW_7_6_7
CMSSW should now be available.
```

Once done, you should see the commmand prompt for the CMSSW instance within Docker:

```console
cmsusr@839c90c48f82 ~/CMSSW_7_6_7/src $
```

If you are using a linux distribution on WSL2, and do not get this prompt (the string after `cmsusr@` will be different), see the instructions below under "Running CMS open data containers on WSL2".

## Further instructions

### Exiting and restarting a container

When you want to exit the container simply type `exit`.

If you want to restart the container (e.g. the one named `my_od`) and return to your work then use the command

```sh
docker start -i my_od
```

### Removing a container

You can remove the container `my_od` with

```sh
docker rm my_od
```

This does not remove the image, which took long to download. You can create a new container from that image with the same `docker run ...` command as above, but it will be much faster than the first time.

If the container was created and started using the `--rm` option (e.g. `docker run --rm ...`) then the container will be removed when you exit.

### Graphics

#### VNC

For opening graphics windows, you can install a VNC viewer on your local computer (Linux, MacOS or Windows). The container image has a VNC application installed. Start the VNC application in the container with

```sh
start_vnc
```

Define a password, it will be requested by the VNC viewer program on your local computer. Now start the VNC viewer program and give the password you've chosen.

Each time you exit from the container, close the VNC application as indicated in the starting message

```sh
vncserver -kill :1
```

#### X11 forwarding with docker on Linux

If you are running on a Linux computer, you can also use X11 forwarding. If you already started a container name `my_od` and now decide to use X11 forwarding instead of VNC, exit from the container shell with `exit`, remove the existing container with `docker rm my_od`. Then start a new container with

```sh
docker run -it --name my_od --net=host --env="DISPLAY" -v $HOME/.Xauthority:/home/cmsusr/.Xauthority:rw cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```
#### Test graphics

You can test if the graphics window opens by typing in the container shell

```sh
root
```

In the `root [0]` prompt, type

```sh
TBrowser t
```
This will open the ROOT browser window. You can exit ROOT with `.q` in the `root[..]` prompt, or from the browser window menu.

If you are new to ROOT, have a quick look to [the Getting started page](/docs/cms-getting-started-2015), or follow the links in [the CMS open data guide](https://cms-opendata-guide.web.cern.ch/tools/root/), and note that you can exit root with `.q`.

### Copying files

You can copy file out of a runnning container to your local computer. Create an example file in the container (for example) with

```sh
echo $CMSSW_VERSION > $HOME/example.txt
```

In order to copy this file out of a running container, open another terminal of your local computer and run the following command:

```sh
docker cp my_od:/home/cmsusr/example.txt .
```

Likewise, in order to copy a file into a running container:


```sh
docker cp <my file> my_od:/home/cmsusr/
```

### Install and run CMS example code

You can now follow [the getting started instructions](/docs/cms-getting-started-2015) for the first steps with the CMS open data.

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
docker run --name my_od -it -v "/cvmfs:/cvmfs:shared" cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```

The other option is to [install](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) the cvmfs client directly in the container after it is created (only working for the slc6-based containers). For this, the container needs to get started in [privileged](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#mount-inside-a-container) mode like

```sh
docker run --privileged --name my_od -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```
