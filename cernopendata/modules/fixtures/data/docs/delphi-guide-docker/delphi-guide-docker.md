## Running DELPHI software from a container
An alternative way to run DELPHI software is to use a container image.
The following guide assumes that you are using [Podman](https://podman.io/), nevertheless it is expected to work in a similar way with other container management technologies, such as Docker.
The images are automatically created from a CI when the software stack is being build, and contain the full software stack.

## Available images
Images are available in the registry of the deployment project at CERNs gitlab instance, https://gitlab.cern.ch/delphi/deployment/container_registry

In this guide we will use the latest Alma9 image.

## Starting the container
In this guide, we will assume to be running on a Linux desktop, which has podman and podman-docker installed. Some of the applications require a graphical interface, namely the CERNLIB applications paw, paw++ and kxterm, as well as the event display.

If you want to run on any data samples, please download them first. You can then attach them using the -v option of the `podman run` command. Please check the podman documentation for more details.

The image is configured with a local user called delphi. To start the container on a Linux based system, use:

```
xhost + local:docker
docker run --privileged --rm -it -e DISPLAY --network host -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/home/delphi/.Xauthority --user delphi gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64 /bin/bash -l
```

This command will download the Alma9 based container and create a login shell for the DELPHI user. This image comes with support for EOS: when launched on a system which supports fuse file systems, the DELPHI data will be available inside the container beneath the path `/eos/opendata/delphi`. Note that due to the --rm option, the container will be destroyed when you exit it.

<p><center><img src="/static/docs/delphi-guide-docker/delphi-container-start.png" width="60%"></center></p>

## Contents of the container image
The image ships with the following modules:

* CERNLIB: This is the community CERNLIB version
* [dstana](/record/80502): dstana is the analysis framework of DELPHI. For historical reasons there are 3 different versions available. The default one and the one which should be used is the pro version. Only switch to a non default version is you know what you are doing.
* simana: Simana is the simulation and reconstruction framework of DELPHI. Note that it differs for each year. For the year 2000 there are 2 different versions: va0e and va0s. The former is valid for the first year, the latter for the second part of the year when a part of the TPC went offline.
* [delgra](/record/80503): delgra is the event display of delphi.

The software stack itself can be found in /delphi on the container.

## Running a simple example: Simulation and event display
The home directory of the delphi user contains a set of basic examples which can be used as templates.
### Event simulation
As an example, let's generate some events with the Pythia generator, and pass them through the DELPHI detector simulation and reconstruction. Todo that, inside the container, first switch to
the examples folder

```
cd examples/pythia
```
Take a look at the script `pythia.sh` in that folder. In the first part, the configuration (also called the title card) for the generator is created and stored in a file named pythia.tit. Here, you can define the desired end states etc. Then, the generator binary is compiled using the provided Makefile. When the generator is run, it will store the generated events in a file called pythia.fadgen.

The last step consist in passing these generated events through the DELPHI detector simulation, reconstruction and short DST creation. The `runsim` script takes care of this. The requested detector setup is for the year 1994, using the latest processing version number. The laboratory is set to CERN. This setting is used to setup random number seeds only. The run nummber is set to 1000, and the beam energy to 45.625 which should match the settings in the generator. The gext version instructs the tools to read the external file pythia.fadgen which was just created.

Run the script by typing inside the pythia folder in the container via

```
./pythia.sh
```
The script will create a bunch of files:

* simana.fadsim is the raw simulated data
* simana.fadana is the reconstructed simulated data
* simana.sdst is the short DST data which is what should be used for analysis.

### Scanning the short dst events

To run the event display, let's first make sure that the required folders are present. So please run
```
mkdir -p ~/graexe/data ~/graexe/hcopy  ~/graexe/macro  ~/graexe/run
```

For convenience, let's copy over the short dst file

```
cp simana.sdst ~/graexe/data
```

Finally, start the event display from the home directory
```
cd
rungra
```

Please take a look at the [DELGRA guide](delphi-guide-delgra) on how to proceed.
