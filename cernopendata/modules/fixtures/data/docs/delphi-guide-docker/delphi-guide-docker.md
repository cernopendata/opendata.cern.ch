## Running DELPHI software from a container
An alternative way to run DELPHI software is to use a container image.
The following guide assumes that you are using [Podman](https://podman.io/), nevertheless it is expected to work in a similar way with other container management technologies, such as Docker.
The images are automatically created from a CI when the software stack is being build, and contain the full software stack.

## Available images
Images are available in the registry of the deployment project at CERNs gitlab instance, https://gitlab.cern.ch/delphi/deployment/container_registry

In this guide we will use the latest Alma9 image.

## Starting the container
In this guide, we will assume to be running on a Linux desktop, which has podman and podman-docker installed. Some of the applications require a graphical interface, namely the CERNLIB applications paw, paw++ and kxterm, as well as the event display.

If you want to run on any data samples, please download them first. You can then attach them using the -v option of the ```podman run ``` command. Please check the podman documentation for more details.

The image is configured with a local user called delphi. To start the container on a Linux based system, use:

```
xhost + local:docker
docker run --privileged --rm -it -e DISPLAY --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/home/delphi/.Xauthority --user delphi gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64 /bin/bash -l
```

This command will download the Alma9 based container and create a login shell for the DELPHI user. This image comes with support for EOS: when launched on a system which supports fuse file systems, the DELPHI data will be available inside the container beneath the path ```/eos/opendata/delphi```.

For Debian based distribution, you need to source the environment:

```
. /etc/profile.d/delphi.sh
```

Note that Debian and Ubuntu images currently do not yet support EOS.

## Contents of the image
The image ships with the following modules:

* CERNLIB: This is the community CERNLIB version
* [dstana](/record/80502): dstana is the analysis framework of DELPHI. For historical reasons there are 3 different versions available. The default one and the one which should be used is the pro version. Only switch to a non default version is you know what you are doing.
* simana: Simana is the simulation and reconstruction framework of DELPHI. Note that it differs for each year. For the year 2000 there are 2 different versions: va0e and va0s. The former is valid for the first year, the latter for the second part of the year when a part of the TPC went offline.
* [delgra](/record/80503): delgra is the event display of delphi.

## Running an example
The binaries are installed in /delphi. The home directory of the delphi user contains a set of basic examples which can be used as templates. For example, to simulate a couple of events and scan them with the event display, do

```
cd examples/pythia
pythia.sh
mkdir -p ~/graexe/data ~/graexe/hcopy  ~/graexe/macro  ~/graexe/run
cp simana.sdst ~/graexe/data
rungra
```
