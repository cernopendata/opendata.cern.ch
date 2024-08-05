FIXME: Introduce table of contents

# Introduction
This quick start guide is meant as a guide for the very first steps to get going with DELPHI software and data access.

## Overview

The DELPHI stack consists of the following modules:

* DELPHI DST analysis framework, also referred to as dstana. Please take a look at the [Skelana framework](/record/80502) for detailed information.
* MonteCarlo production, consisting of simulation, reconstruction and short DST production. Note that the DST format depends on the year. During LEP1, mainly short DST was used, while during LEP2 the extendent short DST format was used. The various formats are described [here](/record/80504)
* Event reconstruction from raw data, using the DELPHI event server.
* The graphical DELPHI Event display, also referred to as [delgra](/record/80503).

## Before you start ...

Please read and accept the data access rules.

DELPHI data access rules are available [here](/record/417), or from [the DELPHI web pages](https://delphi-www.web.cern.ch/delphi-www/delsec/finalrules/DELPHI_Data_preservation-8.pdf).

Please read these before accessing the DELPHI software and data.

## Accessing the software stack
There are two possible ways to access the software stack.

### Docker
A docker container is available which ships with all the modules installed. Please take a look [here](docs/delpi-guide-docker)

### CVMFS
Binaries are also available from CVMFS, for a variety of different Linux flavors. There are no native Windows or Apple ports available for the time being.

This method is convenient if you are running a desktop or a virtual machine with one of the supported Linux flavors on it.

#### Requirements
You will need to have:

* /cvmfs/delphi.cern.ch mounted. Documentation can be found at https://cvmfs.readthedocs.io/en/stable/
* /eos/opendata/delphi mounted. Documentation can be found at
* A list of additional packages installed, see https://gitlab.cern.ch/delphi/deployment for more information:
    * general: tcsh xfonts-100dpi xfonts-75dpi libxfont2
    * compilers: cmake gcc g++ gfortran
    * library packages: libx11 libglu1-mesa xutils libmotif r-base xutils libxbae libxaw7 libssl libglew libdlm

Please check the instructions at https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html and https://eoscta.docs.cern.ch/install/eos/ and https://eos-web.web.cern.ch/eos-web.

#### Initialising the environment:
For C-Shell (csh, tcsh ), do
```
 source /cvmfs/delphi.cern.ch/setup.csh
```

For Bourne shell (sh, bash, zsh, ...), type
```
. /cvmfs/delphi.cern.ch/setup.sh
```
If using the container, please use ```/etc/profile.d/delphi.sh``` or ```/etc/profile.d/delphi.csh``` instead.

After sourcing the environment, make sure that the environment variable **DELPHI_DATA_ROOT** points to the tip of the data area. This is specifically important if you copied the data sets you want to use locally. The default is ```/eos/experiment/delphi/castor2015```.

## Documentation
DELPHI manuals and notes are available from [https://cds.cern.ch/](http://cds.cern.ch/search?c=DELPHI&sc=1)

Here is a selection for getting started:

* [Analysis framework](/record/80502)
* [Event display](/record/80503)
* [DST contents](/record/80504)

## Source code
The sources are available on https://gitlab.cern.ch/delphi. Some modules still requires CERN authentication. The plan is to release the software in the near future.

## Compilers
The DELPHI stack is mostly written in Fortran, with some bits written in C. Only gfortran and GNU gcc are supported. We use the gfortran version which comes with the supported operating system.

## Getting help

The collaboration main contact for data preservation is the mailing list DELPHI-data-preservation-board@cern.ch. Support can only be given on a best effort basis. Suggestions and feedback is of course welcome!

# Examples
Some basic examples of how to run the software stack and perform various tasks can be found in the ```/cvmfs/delphi.cern.ch/examples``` tree.

In the following, we will
* Create some Monte Carlo events and run simulation, reconstruction and DST production on them
    * First, we will show how to do so interactively
    * Then, how to do this on the batch farm at CERN
* Show how to read the result from an analysis job

## About simulation
Simulation is reconstruction code is supported for all the years 1992 and later. The code differs a bit for each of the years.

 * The DELPHI simulation code comes with a few build-in generators. Typically, generators are run externally though.
 * The script *runsim* is used to do the detector simulation, reconstruction and short DST creation steps. Use -gext to process an external file from some generator.

## Creating Monte Carlo samples interactively

### Using internal generators
For creating a few events with a build-in generator run
```
runsim -VERSION va0u -LABO CERN -NRUN 1000 -EBEAM 45.625 -igen qqps -NEVMAX 10

```
This will create 10 Z-> qqbar events at a beam energy of 45.625 GeV (ECM 91.25 GeV), using the build-in QQPS generator.

It will as well pass the events through the detector simulation with the following settings:

* Run number -1000 (negative numbers indicate simulated events)
* Laboratory identifier CERN (please change that if possible)
* year 2000 (no TPC sector 6 period)

The events will be reconstructed and an extended short DST file will be created, which is ready for analysis.

Created files:

* simana.fadsim : detector simulation output (corresponds to raw data, not to be used directly)
* simana.fadana : reconstructed output, full DST format (not to be used directly)
* simana.xsdst  : short DST output for analysis

In principle, analysis code can be run as well on the full DST output, however, this requires that a bunch of modules and fixes have to be rerun on top of the data, before they can be used.

### Using external generators
In this case the generator is run externally and the output is written to a file in a specific format. This can then
be passed through the detector simulation with
```
runsim -VERSION va0u -LABO CERN -NRUN 1000 -EBEAM 45.625 -gext generated.lund -NEVMAX 10
```
Old executables for generators can be found in /cvmfs/delphi.cern.ch/mc-production/generators/pgf77_glibc2.2

A source code example of DELPHI tuned Pythia can be found in the example tree.

## Running an analysis job on the result
The following script can be run interactively or submitted to a batch farm with DELPHI setup

```
#!/bin/bash
pgm=skelana

export DELLIBS=`dellib skelana dstana pxdst vfclap vdclap ux tanagra ufield bsaurus herlib trigger uhlib dstana`
export CERNLIBS=`cernlib  genlib packlib kernlib ariadne herwig jetset74`
echo "+OPTION VERbose" > $pgm.cra1
echo "+USE, ${PLINAM}." >> $pgm.cra1
cat $DELPHI_PAM/skelana.cra >> $pgm.cra1

# modify
ycmd=`which nypatchy`
command="$ycmd - $pgm.f $pgm.cra1 $pgm.ylog $pgm.c - - ${pgm}R.f .go"
echo "Running $command"
eval $command

# compile
for ending in .f .F ; do
    ls *$ending >/dev/null 2>&1
    if [ $? -eq 0 ]; then
	for file in *$ending  ; do
	    $FCOMP $FFLAGS -c $file
	done
    fi
done

for ending in  *.c *.C *.cc ; do
    ls *$ending >/dev/null 2>&1
    if [ $? -eq 0 ]; then
	for file in *ending ; do
	    $CCOMP $CFLAGS -c $file
	done
    fi
done

# link
$FCOMP $LDFLAGS *.o -o $pgm.exe $ADDLIB $DELLIBS $CERNLIBS

# cleanup
rm -f *.f *.c *.o

# create input file
echo "FILE = simana.xsdst" > ./PDLINPUT

# execute
./$pgm.exe 1>$pgm.log 2>$pgm.err
```

This simple script will:

* get the sources
* run nypatchy to create the compilable Fortran input files
* compile the Fortran code to create an executable file
* create a data input fiel which would read **simana.xsdst** from the local folder where the executable will be started
* run the job

## Using nicknames
DELPHI data is organised in data sets which are identified via a nickname. When using opendata, each nickname comes with a corresponding DOI which you can quote.

To analyse data, use the nicknames which you can find at http://delphiwww.cern.ch/offline/data/castor/html.
In this case, the PDLINPUT file created by the script above should contain the keyword PDL, followed by the nickname, e.g.

```bash
FAT = short94_c2
```
to read 94 C2 data. It will automatically resolve the data files and loop over all of them.

# Raw data access
The DELPHI event server can be used to pick and reprocss individual events from raw data.
It supports different modes:

* *pick* only selects the raw data of a specific event and returns that
* *delana* picks an event from raw data, and runs the reconstruction code on it, returning a full dst file#
* *dstana* picks the event from raw data, runs reconstruction and dst creation on it, subsequently

The *wired* option is no longer supported as the wired code no longer exists.

Example:
```
des -m dstana -e 84078:10815
```
creates the following output files:
```
R84078_E10815.dst
dstana.dst
```
where the first one is the full DST output, and the second the short dst one.

Note: Running the event server requires access to the DELPHI raw data sets.

## Event visualisation:
After setting up the DELPHI environment you can start the DELPHI event display with
```
rungra
```
Note that the event display can read only reconstructed data, not raw data. Both full and short DST work.

# More examples
More examples can be found at https://gitlab.cern.ch/delphi/examples.
