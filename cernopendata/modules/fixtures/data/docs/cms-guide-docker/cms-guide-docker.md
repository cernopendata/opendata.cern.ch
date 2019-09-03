## Introduction

As an alternative to using a virtual machine, you can run CMS analysis code in a [Docker](https://www.docker.com/) container. If you have not already installed Docker instructions for installation are [provided by Docker](https://docs.docker.com/install/).

## Fetch and create a CMSSW image and start a container

### Instructions for 2011/2012 data

Once Docker is installed, you can fetch a CMSSW image, and create and start a container using the `docker run` command:

```sh
docker run --name opendata -it cmsopendata/cmssw_5_3_32 /bin/bash
```

Here we fetch the `CMSSW_5_3_32` docker image from [dockerhub](https://hub.docker.com/u/cmsopendata) and name the container `opendata`.

As described [in this GitHub repository](https://github.com/clelange/cmssw-docker/), this will install a stand-alone CMSSW image (a few gigabytes). Therefore this may take a few minutes. However, the image will only have to be downloaded once. The following will appear in your terminal once you type the `docker run` command:

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

### Instructions for 2010 data

Once Docker is installed, you can fetch a CMSSW image and create and start a container using the `docker run` command:

```sh
docker run --name opendata-2010 -it cmsopendata/cmssw_4_2_8 /bin/bash
```

Here we fetch the `CMSSW_4_2_8` docker image from [dockerhub](https://cloud.docker.com/u/cmsopendata/repository/list) and name the container `opendata-2010`.

As described [in this GitHub repository](https://github.com/clelange/cmssw-docker/), this will install a stand-alone CMSSW image that is a few GBs. Therefore this may take a few minutes. However, the image will only have to be downloaded once. The following will appear in your terminal once you type the `docker run` command:

```console
Unable to find image 'cmsopendata/cmssw_4_2_8' locally
latest: Pulling from cmsopendata/cmssw_4_2_8
acb4e939ccb9: Pull complete
99519598bf9e: Pull complete
bd33a5d7d5de: Pull complete
Digest: sha256:511ece0c921dffa39470c785e5cade41bfd25f8ebc4e7ac72e6a622bb1a477c9
Status: Downloaded newer image for cmsopendata/cmssw_4_2_8:latest
Setting up CMSSW_4_2_8
CMSSW should now be available.
```

Once done, you should see the commmand prompt for the CMSSW instance within Docker:

```console
cmsusr@b3dad0c0068a ~/CMSSW_4_2_8/src $
```

## Further instructions

### Install and run CMS analysis code

Now we can try an example analysis like [DimuonSpectrum2011](https://github.com/cms-opendata-analyses/DimuonSpectrum2011), which analyses 2011 and 2012 data.

In the command prompt in `~/CMSSW_5_3_32/src` run the following commands:

```sh
mkdir WorkDir
cd WorkDir
git clone git://github.com/cms-opendata-analyses/DimuonSpectrum2011.git
```

Move to the `DimuonSpectrum2011` directory and build with the `scram` command:

```sh
cd DimuonSpectrum2011
scram b
```

Once the code is built, you can run the example analysis:

```sh
cmsRun demoanalyzer_cfg.py
```

which will produce a file `DoubleMu.root`.

### Copying files

In order to copy files out of a running container, open another terminal and run (for example) the following command:

```sh
docker cp opendata:/home/cmsusr/CMSSW_5_3_32/src/WorkDir/DimuonSpectrum2011/DoubleMu.root .
```

Likewise, in order to copy a file into a running container:


```sh
docker cp <my file> opendata:/home/cmsusr/CMSSW_5_3_32/src/
```

### Exiting and restarting a container

When you want to exit the container simply type `exit`.

If you want to restart the container (e.g. the one named `opendata`) and return to your work then use the command `docker start -i opendata`.

If the container was created and started using the `--rm` option (e.g. `docker run --rm`) then the container will be removed when you exit. You can create a new container from the image using `docker run`.
