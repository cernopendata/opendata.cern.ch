# Table of contents
This quick start guide is meant as a guide for the very first steps to get going with DELPHI software and data access.

* [Overview and requirements](#overview)
    * [Before you start](#before)
* [Accessing the software stack](#access)
    * [Docker](#docker)
    * [CVMFS](#cvmfs)
* [Documentation](#documentation)
    * [Source code](#sources)
    * [Compilers](#compilers)
    * [Getting help](#help)
* [Examples](#examples)
    * [About simulation](#simulation)
    * [Creating MonteCarlo interactively](#simulinter)
        * [Using internal generators](#internalgen)
        * [Using external generators](#externalgen)
    * [Running an analysis job on the result](#anajobinter)
    * [Using nicknames](#nicknames)
    * [Raw data access](#rawdata)
    * [Event visualisation](#delgra)
    * [More examples](#more)

# <a name="overview"> Overview</a>

The DELPHI stack consists of the following modules:

* DELPHI DST analysis framework, also referred to as `dstana`. Please take a look at the [Skelana framework](/record/80502) for detailed information.
* MonteCarlo production, includes simulation, reconstruction and short DST creation. Note that the DST format depends on the year. During LEP1, mainly [short DST](/record/80506) or [long DST](/record/80507) formats were used, while during LEP2 the [extendent short DST](/record/80505) format was the default.
Note that the reconstruction code returns results in [full DST format](/record/80504). Analyses should always use short or extended short DST format, because these generally contain fixes which were applied after the reconstruction itself.
* Event reconstruction from raw data, using the DELPHI event server.
* The graphical DELPHI Event display, also referred to as [delgra](/record/80503).

## <a name="before"> Before you start ... </a>

Please read and accept the [DELPHI data access rules](/record/417). They can as well be viewd at the [the DELPHI web pages](https://delphi-www.web.cern.ch/delphi-www/delsec/finalrules/DELPHI_Data_preservation-8.pdf).

# <a name="access"> Accessing the software stack</a>
There are two possible ways to access the software stack.

## <a name="docker"> Docker </a>
A container image is available which ships with all the modules installed. Please take a look at the [DELPHI docker guide](/docs/delphi-guide-docker).

## <a name="cvmfs"> CVMFS</a>
Binaries are also available from CVMFS, for a variety of different Linux flavors. Instructions can be found in our [dedicated CVMFS guide](/docs/delphi-guide-cvmfs).

# <a name="documentation"> Documentation</a>
DELPHI manuals and notes are available from [https://cds.cern.ch/](http://cds.cern.ch/search?c=DELPHI&sc=1)

Here is a selection for getting started:

* [Analysis framework](/record/80502)
* [Event display](/record/80503)
* [DST contents](/record/80504)

## <a name="sources">Source code</a>
The sources are available from <https://gitlab.cern.ch/delphi>. Some modules still requires CERN authentication. The plan is to release the software in the near future.

## <a name="compilers">Compilers</a>
The DELPHI stack is mostly written in `Fortran`, with some bits written in `C`. Only `gfortran` and `GNU gcc` are supported. We use the `gfortran` version which comes with the
supported operating system. Recommended compiler and linker flags are set by the environment and should be used when building software linking with the DELPHI libraries.

## <a name="help">Getting help</a>

The collaboration main contact for data preservation is the mailing list DELPHI-data-preservation-board@cern.ch. Support can only be given on a best effort basis though. In addition, there is a [discussion forum](https://opendata-forum.cern.ch/c/delphi/20) which you are invited to join, to exchange experiences and get in touch with former members of the collaboration.

Suggestions and feedback is welcome!



# <a name="examples">Examples</a>
Some basic examples of how to run the software stack and perform various tasks can be found in the repository <https://gitlab.cern.ch/delphi/examples>. In addition, the repository <https://gitlab.cern.ch/delphi/modern-delphi-examples> has some proof-of-concept level examples about how to access the DELPHI data from e.g. C++.

In the following, we will

* Create some Monte Carlo events and run simulation, reconstruction and DST production on them
    * First, we will show how to do so interactively
    * Then, how to do this on the batch farm at CERN
* Show how to read the result from an analysis job

## <a name="simulation"> About simulation</a>
Simulation is reconstruction code is supported for all the years 1992 and later. The code differs a bit for each of the years.

 * The DELPHI simulation code comes with a few build-in generators. Typically, generators are run externally though.
 * The script *runsim* is used to do the detector simulation, reconstruction and short DST creation steps. Use -gext to process an external file from some generator.

There is a [dedicated guide](delphi-guide-simulation) available with more details about how to run DELPHI simulations.

## <a name="simulinter"> Creating Monte Carlo samples interactively</a>

### <a name="internalgen">Using internal generators</a>
For creating a few events with a build-in generator run

```
$ runsim -VERSION v94c -LABO CERN -NRUN 1000 -EBEAM 45.625 -igen qqps -NEVMAX 10

```
This will create 10 Z-> qqbar events at a beam energy of 45.625 GeV (ECM 91.25 GeV), using the build-in QQPS generator and the detector setup of 1994.

It will as well pass the events through the detector simulation, and create a short DST file named `simana.sdst` which can be used for analysis, scanning etc.

### <a name="externalgen">Using external generators</a>
In this case the generator is run externally and the output is written to a file
in a specific format. This can then be passed through the detector simulation with

```
$ runsim -VERSION 94c -LABO CERN -NRUN 1000 -EBEAM 45.625 -gext generated.lund -NEVMAX 10
```

Again, this will create a short DST file name simana.sdst. Note that for the LEP 2 phase, a sol called extended short DST file will be created, which is typically called simana.xsdst instead.


## <a name="anajobinter">Running an analysis job on the result</a>
A [dedicated guide](delphi-guide-analysis) is availabe with more details about how to run an analysis job for DELPHI.

The DELPHI analysis framework is called `skelana`. The way to write analysis code is by overriding one or more of the following Fortran functions:

* `USER00` for the initialisation at the start of the run
* `USER01` for the event selection. It should return 0 to skip the current event and 1 to read it.
* `USER02` is called for each selected event.
* `USER99` is called at the end of the run

An example can be found in the examples folder on the [DELPHI container](delphi_guide_docker) or on [CERN gitlab](https://gitlab.cern.ch/delphi/examples). Take a look e.g. at the `dump` folder there.

## <a name="nicknames">Using nicknames</a>
DELPHI data is organised in data sets which are identified via a nickname. When using opendata, each nickname comes with a corresponding DOI which you can quote.

To analyse data, use the nicknames which you can find at http://delphiwww.cern.ch/offline/data/castor/html.
In this case, the PDLINPUT file created by the script above should contain the keyword PDL, followed by the nickname, e.g.

```bash
FAT = short94_c2
```

to read 94 C2 data. It will automatically resolve the data files and loop over all of them.

## <a name="rawdata">Raw data access</a>
The DELPHI event server can be used to pick and reprocss individual events from raw data.
A [dedicated guide](delphi-guide-eventserver) is available on the DELPHI event server.

Example:
```
$ des -m dstana -e 84078:10815
```

## <a name="delgra">Event visualisation</a>
After setting up the DELPHI environment you can start the DELPHI event display with

```
$ cd
$ rungra
```

For convenience, copy the files you want to scan to `~/graexe/data`.
Please take a look at the [DELGRA guide](delphi-guide-delgra) on how to proceed.

## <a name="more">More examples</a>
More examples can be found at <https://gitlab.cern.ch/delphi/examples>.
