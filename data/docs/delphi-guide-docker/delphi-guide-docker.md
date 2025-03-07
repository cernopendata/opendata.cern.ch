## Running DELPHI software from a container
An alternative way to run DELPHI software is to use a container image.
The following guide assumes that you are using [Podman](https://podman.io/), nevertheless it is expected to work in a similar way with other container management technologies, such as [Docker](https://www.docker.com/).
The required images to run the DELPHI software are automatically created from a CI when the software stack is being build, and contain the full software stack.

## Available images
Images are available in the registry of the `DELPHI deployment` project at [CERNs gitlab instance](https://gitlab.cern.ch/delphi/deployment).

In this guide we will use the latest `Alma9` image.

## Starting the container
In this guide, we will assume to be running on a Linux desktop, which has the `podman` and `podman-docker` packages installed. Some of the applications require a graphical interface,
namely the CERNLIB applications `paw`, `paw++` and `kxterm`, as well as the [DELPHI event display](delphi-guide-delgra).

If you want to run on any data samples, please download them first. You can then attach them using the -v option of the `podman run` command. Please check the podman documentation for more details. The `Alma9` image we use in this guide can also access the data directly from the `EOS` file system.

The image is configured with a local user called `delphi`. For the commands below, we'll use the following conventions:

* a prompt `$ xyz` indicates that the command `xyz` is to be run on your local machine or VM.
* a prompt `[delphi ~] $ xyz` indicates that the command `xyz` is to be run inside the started container.

The Alma9 images come with support for `EOS`: when launched on a system which supports fuse file systems, the DELPHI data will be available inside the container beneath the path `/eos/opendata/delphi`. In addition, they support reading data over the network using the xrootd protocol.

Be aware that due to the --rm option, the container will be destroyed when you exit it, and all the work done inside the container will be lost.

### On a Linux based system
To start the container on a Linux based system, use:

```
$ xhost + local:docker
$ docker run --privileged --rm -it -e DISPLAY --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/home/delphi/.Xauthority --user delphi gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64 /bin/bash -l
```

This command will download the Alma9 based container and create a login shell for the DELPHI user.

### On MacOS
On recent Macs with M1, M2 or M3 CPUs it is better to use the ARM64 image, to avoid issues when linking executables inside the container. Also, if you are running MacOS, the command to start the container is a bit different.

```
podman run --privileged -it -e DISPLAY=host.docker.internal:0 --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/home/delphi/.Xauthority --user delphi gitlab-registry.cern.ch/delphi/deployment/delphi/al9_aarch64 /bin/bash -l
```

Also, the X server settings must allow connections from external sources. In addition, you may have to set
```
export LIBGL_ALWAYS_INDIRECT=1
```
in the container shell if you plan to run the event display.

### On Windows
Running the container images on Windows has not been tested. Feedback is welcome.


<p><center><img src="/static/docs/delphi-guide-docker/delphi-container-start.png" width="60%"></center></p>

## Contents of the container image
The image ships with the following modules:

* CERNLIB: The DELPHI software uses the [community version](https://cernlib.web.cern.ch) of CERNLIB
* [dstana](/record/80502) is the analysis framework of DELPHI. For historical reasons there are 3 different versions available. The default one and the one which should be used is the pro version. Only switch to a non default version is you know what you are doing.
* simana  contains the simulation and reconstruction framework of DELPHI. Note that it differs for each year. For the year 2000 there are 2 different versions: va0e and va0s. The former is valid for the first year, the latter for the second part of the year when a part of the `TPC` went offline.
* [delgra](/record/80503) is the event display of delphi.

The software stack itself can be found in `/delphi` on the container.

## Running a simple example: Simulation and event display
The home directory of the delphi user contains a set of basic examples which can be used as templates.

### Event simulation
Follow the [DELPHI event simulation guide](delphi-guide-simulation) to create a few sample events to scan. For the next chapter, the short DST output file will be needed.

### Scanning events

To run the event display, let's first make sure that the required folders are present. So please run

```
[delphi ~] $ mkdir -p ~/graexe/data ~/graexe/hcopy  ~/graexe/macro  ~/graexe/run
```

For convenience, let's copy over the short dst file

```
[delphi ~] $ cp simana.sdst ~/graexe/data
```

Finally, start the event display from the home directory

```
[delphi ~] $ cd
[delphi ~] $ rungra
```

Please take a look at the [DELGRA guide](delphi-guide-delgra) for a quick start on how to use the event display.
