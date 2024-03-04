1. [Introduction](#intro)
2. [Available CMSSW container images](#images)
3. [Fetch a CMSSW image and start a container](#fetch-start)
4. [Useful commands](#commands)
    1. [Exiting and restarting a container](#exit-start)
    2. [Copying files](#cp)
    3. [Execute a command in a running container](#exec)
    4. [Removing a container](#rm)
5. [Graphics](#graphics)
    1. [VNC](#vnc)
    2. [X11 forwarding on Linux](#x11)
    3. [Test graphics](#test-graphics)
6. [Container prompt](#prompt)
7. [Install and run CMS example code](#get-started)
8. [Running CMS open data containers on WSL2](#on-wsl2)
9. [Accessing cvmfs from a container](#cvmfs)

## <a name="intro">Introduction</a>

You can run CMS analysis code in a [Docker](https://www.docker.com/) container provided together with the CMS open data. If you have not already installed Docker, instructions for installation are [provided by Docker](https://docs.docker.com/install/). For an introduction and for getting started, you can follow the links provided in [the CMS Open data guide](https://cms-opendata-guide.web.cern.ch/tools/docker/).

## <a name="images">Available CMSSW container images</a>

For the first access of each set of CMS open data, you will need a specific container image containing the software corresponding to that particular set of data. The following images are available:

<table class="table table-condensed">

<thead>

<tr class="header">

<th align="left">CMS open data<br> </th>

<th align="left">CMSSW version<br> </th>

<th align="left">Container image (<a href="https://hub.docker.com/u/cmsopendata">dockerhub</a>) <br> Alternative image location (<a href="https://gitlab.cern.ch/cms-cloud/cmssw-docker-opendata/container_registry">GitLab</a>)</th>

</tr>

</thead>

<tbody>

<tr class="odd">

<td align="left">2015 proton-proton</td>

<td align="left">CMSSW_7_6_7</td>

<td align="left">cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493<br> gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_7_6_7-slc6_amd64_gcc493</td>

</tr>

<tr class="odd">

<td align="left">2015 proton-proton heavy-ion reference data at 5.02TeV</td>

<td align="left">CMSSW_7_5_8_patch3</td>

<td align="left">cmsopendata/cmssw_7_5_8_patch3-slc6_amd64_gcc491<br> gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_7_5_8_patch3-slc6_amd64_gcc491</td>

</tr>

<tr class="odd">

<td align="left">2013 proton-lead and proton-proton heavy-ion reference data</td>

<td align="left">CMSSW_5_3_20</td>

<td align="left">cmsopendata/cmssw_5_3_20-slc6_amd64_gcc472<br> gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_5_3_20-slc6_amd64_gcc472</td>

</tr>

<tr class="odd">

<td align="left">2011-2012 proton-proton</td>

<td align="left">CMSSW_5_3_32</td>

<td align="left">cmsopendata/cmssw_5_3_32-slc6_amd64_gcc472<br>
gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_5_3_32-slc6_amd64_gcc472</td>

</tr>

<tr class="odd">

<td align="left">2011 heavy-ion</td>

<td align="left">CMSSW_4_4_7</td>

<td align="left">cmsopendata/cmssw_4_4_7-slc5_amd64_gcc434<br>
gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_4_7-slc5_amd64_gcc434</td>

</tr>

<tr class="odd">

<td align="left">2010 proton-proton</td>

<td align="left">CMSSW_4_2_8</td>

<td align="left">cmsopendata/cmssw_4_2_8-slc5_amd64_gcc434<br>
gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_2_8-slc5_amd64_gcc434</td>

</tr>

<tr class="odd">

<td align="left">2010 proton-proton with CASTOR calorimeter</td>

<td align="left">CMSSW_4_2_8_lowpupatch1</td>

<td align="left">cmsopendata/cmssw_4_2_8_lowpupatch1-slc5_amd64_gcc434<br>
gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_4_2_8_lowpupatch1-slc5_amd64_gcc434</td>

</tr>

<tr class="odd">

<td align="left">2010 heavy-ion</td>

<td align="left">CMSSW_3_9_2_patch5</td>

<td align="left">cmsopendata/cmssw_3_9_2_patch5-slc5_amd64_gcc434<br>
gitlab-registry.cern.ch/cms-cloud/cmssw-docker-opendata/cmssw_3_9_2_patch5-slc5_amd64_gcc434</td>

</tr>

</tbody>

</table>

## <a name="fetch-start">Fetch a CMSSW image and start a container</a>

In the following instructions, make sure to replace the CMSSW version and the container image name according to the table above. These commands are for 2015 proton-proton data, with the CMSSW version 7_6_7 and the `cmssw_7_6_7-slc6_amd64_gcc493` container image.

Once you have installed Docker on your computer, you can fetch a CMSSW image, and create and start a container using the `docker run` command:

```sh
docker run --name my_od -P -p 5901:5901 -p 6080:6080 -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```

Here we fetch the `cmssw_7_6_7-slc6_amd64_gcc493` docker image from [dockerhub](https://hub.docker.com/u/cmsopendata) and name the container `my_od`.

This will install a stand-alone CMSSW image (several gigabytes). Therefore this may take a while. However, the image will only have to be downloaded once. The following will appear in your terminal, with messages changing during the download:

```console
$ docker run --name my_od -P -p 5901:5901 -p 6080:6080 -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
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
This is a standalone image for CMSSW_7_6_7 slc6_amd64_gcc493.
```

Once done, you should see the commmand prompt for the CMSSW instance within Docker:

```console
(/code/CMSSW_7_6_7/src)
```

If you are using a linux distribution on WSL2, and do not get this prompt, but get back to your local terminal prompt, see the instructions [below](#on-wsl2) under "Running CMS open data containers on WSL2".

## <a name="commands">Useful commands</a>

In the following, some useful commands are given. For a complete list of commands, see the [docker command line documentation](https://docs.docker.com/engine/reference/commandline/cli/).

### <a name="exit-start">Exiting and restarting a container</a>

When you want to exit the container simply type `exit`.

If you want to restart the container (e.g. the one named `my_od`) and return to your work then use the command

```sh
docker start -i my_od
```

### <a name="cp">Copying files</a>

You can copy file out of a runnning container to your local computer. Create an file in the container (for example) with

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

### <a name="exec">Execute a command in a running container</a>

You may need to submit a command from your local host into a running container. For example, to see the running processes in the `my_od` container, run:

```sh
docker exec my_od ps -ef
```

### <a name="rm">Removing a container</a>

You can remove the container `my_od` with

```sh
docker rm my_od
```

This does not remove the image, which took long to download. You can create a new container from that image with the same `docker run ...` command as above, but it will be much faster than the first time.

If the container was created and started using the `--rm` option (e.g. `docker run --rm ...`) then the container will be removed when you exit.

## <a name="graphics">Graphics</a>

### <a name="vnc">VNC</a>

For opening graphics windows, the container image has a VNC application installed. Start the VNC application in the container with

```sh
start_vnc
```

You can either install a VNC viewer (e.g. TigerVNC) on your local computer (Linux, MacOS or Windows) and start the viewer there, or open the graphics window in your browser with the http address given in the message.

Connect with the default VNC password `cms.cern`.

Each time you exit from the container, close the VNC application with

```sh
stop_vnc
```

You can find more details on the configuration and usage of VNC in the CMS open data containers in [the image repository](https://gitlab.cern.ch/cms-cloud/cmssw-docker-opendata/-/tree/master#use-vnc).

### <a name="x11">X11 forwarding on Linux</a>

If you are running on a Linux computer, you can also use X11 forwarding. If you already started a container name `my_od` and now decide to use X11 forwarding instead of VNC, exit from the container shell with `exit`, remove the existing container with `docker rm my_od`. Then start a new container with

```sh
docker run -it --name my_od --net=host --env="DISPLAY" -v $HOME/.Xauthority:/home/cmsusr/.Xauthority:rw cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```
### <a name="test-graphics">Test graphics</a>

You can test if the graphics window opens by typing in the container shell

```sh
root
```

In the `root [0]` prompt, type

```sh
TBrowser t
```
This will open the ROOT browser window. You can exit ROOT with `.q` in the `root[..]` prompt, or from the browser window menu.

If you are new to ROOT, have a quick look to [the Getting started page](/docs/cms-getting-started-2015), or follow the links in [the CMS open data guide](https://cms-opendata-guide.web.cern.ch/tools/root/).

## <a name="prompt">Container prompt</a>

If the container prompt causes trouble for line wrapping, increase the size of the terminal. If it does not help, you can change the prompt with

```sh
export PS1="(\w) "
```

To change it permanently, add this line to the file `/home/cmsusr/.bashrc` in the container.


## <a name="get-started">Install and run CMS example code</a>

If you have read the instructions above, you can now follow [the getting started instructions](/docs/cms-getting-started-2015) for the first steps with the CMS open data.

## <a name="on-wsl2">Running CMS open data containers on WSL2</a>

The CMS open data containers, or any CentOS6-based containers, may fail if docker is run on WSL2. This problem is fixed by adding a new file `.wslconfig` with the following contents

```sh
[wsl2]
kernelCommandLine = vsyscall=emulate
```

in the `\Users\<username>` folder (make sure that it is saved without extension), then shutting down with `wsl --shutdown` in the Windows command prompt and restarting again.

Test that the settings are properly passed by doing, in the WSL2 linux installation:

```sh
docker run -ti ubuntu cat /proc/cmdline
```

The ouput should contain `vsyscall=emulate`, e.g.:

```sh
initrd=\initrd.img panic=-1 pty.legacy_count=0 nr_cpus=4 vsyscall=emulate
```

## <a name="cvmfs">Accessing cvmfs from a container</a>

The CMS open data container images contain the software needed for analysis, and the CMS condition database can be accessed from predefined locations. In the container images for standard proton-proton data, they are stored in a local `/cvmfs` file system. Therefore, when using these containers, access to the namespace `/cvmfs` (CernVM-File System) at CERN for software and condition data access is not mandatory.

If desired, it is possible to "see" the full cvmfs space by installing the cvmfs client following [the official instructions](https://cvmfs.readthedocs.io). In essence, there are two basic ways to achieve this:

The preferred option is to [install](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) the cvmfs client locally, on the host machine, and [mount](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#bind-mount-from-the-host) it on the container:

```sh
docker run --name my_od -it -v "/cvmfs/cms-opendata-conddb.cern.ch:/cvmfs/cms-opendata-conddb.cern.ch:shared" cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```

Do not mount the full `/cvmfs` or `/cvmfs/cms.cern.ch` areas as that will overwrite necessary settings in the local `/cvmfs` area of the container.

The other option is to [install](https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html) the cvmfs client directly in the container after it is created (only working for the slc6-based containers). For this, the container needs to get started in [privileged](https://cvmfs.readthedocs.io/en/stable/cpt-configure.html#mount-inside-a-container) mode like

```sh
docker run --privileged --name my_od -it cmsopendata/cmssw_7_6_7-slc6_amd64_gcc493 /bin/bash
```
