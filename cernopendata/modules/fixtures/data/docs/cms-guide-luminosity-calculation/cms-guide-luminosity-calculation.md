## What is this?

This document provides instruction for how to calculate the luminosity information
for CMS in the open data environment. This is done using `brilcalc`, which is a command line tool from the CMS Beam Radiation Instrumentation and Luminosity (BRIL) group.

Before you continue, consider that some of the information that you wish to calculate is already available for [2010](http://opendata-dev.web.cern.ch/record/1050), [2011](http://opendata-dev.web.cern.ch/record/1053), and [2012](http://opendata-dev.web.cern.ch/record/1054) data. The information available includes:

* the integrated luminosity for validated runs and luminosity sections
* the trigger prescales by run and luminosity section
* the luminosity by luminosity section for the list of validated runs and luminosity sections

## Install the CMS environment

There are two options for installing the CMS environment, using a Virtual
Machine (VM) or using a Docker container.

### Virtual machine

Follow the instructions [here](http://opendata.cern.ch/docs/cms-virtual-machine-2011) to install the CMS VM and then the instructions for [getting started](http://opendata.cern.ch/docs/cms-getting-started-2011).

Click on the `CMS Shell` icon on the desktop to open the terminal. At the terminal prompt, run the command

`
$ cmsrel CMSSW_5_3_32
`

and then change directory

`
$ cd CMSSW_5_3_32/src
`

 and then finally intialize the CMS environment

 `
$cmsenv
 `

Now we are ready to [install the `brilcalc` package.](#install-brilcalc)

### Docker container

Following the instructions [here](http://opendata.cern.ch/docs/cms-guide-docker) we download and install an image
and run a Docker container using the following command:

`docker run --name opendata-2011 -it cmsopendata/cmssw_5_3_32 /bin/bash`

When completed successfully we should be at the command prompt:

`cmsusr@a17b2a79d067 ~/CMSSW_5_3_32/src $`

Now we are ready to [install the `brilcalc` package.](#install-brilcalc)

## Install brilcalc

### cvmfs
If you are using the VM, or if are using the docker container and have the `cvmfs` file system installed locally, you have access to `cvmfs`.
In these cases, follow these instructions:

1.    Set your `PATH`:

      ```sh
      export PATH=$HOME/.local/bin:/cvmfs/cms-bril.cern.ch/brilconda/bin:$PATH
      ```

2.    Install using `pip` with the command:

      ```sh
      pip install --user brilws
      ```

      At the end of a successful installation you should see the messages:

      ```console
      Successfully built brilws
      Installing collected packages: brilws
      Successfully installed brilws
      ```

3.    Check the installation by running the command:

      ```sh
      brilcalc --version
      ```

      which should output `3.6.2`

Now you are ready to [test `brilcalc`.](#test-brilcalc)

### conda

Alternatively you can install a conda environment:

1.    In the command prompt go to the home directory in your container with the command `cd`

2.    Fetch the installer for the `brilcalc` conda environment:

      ```sh
      wget https://cern.ch/cmslumisw/installers/linux-64/Brilconda-1.1.7-Linux-x86_64.sh
      ```

      (you may need to use the `--no-check-certificate` option with `wget`)

3.    Run the installer:

      ```sh
      bash Brilconda-1.1.7-Linux-x86_64.sh -b -p <localbrilcondabase>
      ```

      where we substitute `<localbrilcondabase>` with `brilconda`. This is the directory in which the `brilcalc` tools
      will be installed.

4.    Once installed successfully add the tools to your `PATH` with the following command:

      ```sh
      export PATH=$HOME/.local/bin:$HOME/brilconda/bin:$PATH
      ```

5.    Then install `brilcalc` with this command:

      ```sh
      pip install brilws
      ```

6.    Finally check by running the following:

     ```sh
     brilcalc --version
     ```

     which should output `3.53`

Now you are ready to [test `brilcalc`.](#test-brilcalc)

## Test brilcalc

As a test, let's see what the integrated luminosity was for run 160431 by running the command

 `brilcalc lumi -c web -r 160431`

which should output

```console
#Data tag : 19v3 , Norm tag: onlineresult
+-------------+-------------------+-----+------+----------------+----------------+
| run:fill    | time              | nls | ncms | delivered(/ub) | recorded(/ub)  |
+-------------+-------------------+-----+------+----------------+----------------+
| 160431:1615 | 03/14/11 03:08:07 | 243 | 218  | 8781.334977241 | 7879.289611261 |
+-------------+-------------------+-----+------+----------------+----------------+
#Summary:
+-------+------+-----+------+-------------------+------------------+
| nfill | nrun | nls | ncms | totdelivered(/ub) | totrecorded(/ub) |
+-------+------+-----+------+-------------------+------------------+
| 1     | 1    | 243 | 218  | 8781.334977241    | 7879.289611261   |
+-------+------+-----+------+-------------------+------------------+
```

**Note:** It is important that you use the `-c web` option when running `brilcalc`. This specifies that you use indirect access to BRIL servers via web cache. For users of CMS open data outside CERN and CMS this is the only option that will work.

**Note:** There is a useful `help` option for `brilcalc` and its commands:

`brilcalc --help`

```console
usage:
   brilcalc (-h|--help|--version)
   brilcalc [--debug|--warn] <command> [<args>...]

 commands:
   lumi Luminosity
   beam Beam
   trg Trigger configurations
 See 'brilcalc <command> --help' for more information on a specific command.
```

## Common queries

### Integrated luminosity for a run

See test above

### Integrated luminosity for validated runs and luminosity sections

First obtain the file with the list of validated runs and luminosity sections. Here we use the [list for 2011 data](http://opendata-dev.web.cern.ch/record/1001).

`wget http://opendata.cern.ch/record/1001/files/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt`

It is recommended to steer the output to a file (e.g. called `2011lumi.txt`) using this command:

`brilcalc lumi -c web -i Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt > 2011lumi.txt`

The output will appear as follows:

```console
#Data tag : v1 , Norm tag: onlineresult
+-------------+-------------------+------+------+----------------+---------------+
| run:fill    | time              | nls  | ncms | delivered(/ub) | recorded(/ub) |
+-------------+-------------------+------+------+----------------+---------------+
| 160431:1615 | 03/14/11 03:14:43 | 200  | 200  | 7366.884       | 7366.875      |
| 160577:1622 | 03/16/11 01:44:38 | 53   | 53   | 1719.888       | 1631.386      |
| 160578:1622 | 03/16/11 02:20:03 | 175  | 175  | 5201.105       | 4952.155      |
| 160871:1636 | 03/19/11 02:43:57 | 141  | 141  | 109739.586     | 106354.581    |
| 160872:1636 | 03/19/11 03:50:05 | 38   | 38   | 28346.738      | 23977.109     |
| 160873:1636 | 03/19/11 04:20:20 | 147  | 147  | 104914.534     | 103031.004    |
```

### Select luminometer

CMS measures the luminosity with different luminometers (luminosity detectors) and algorithms. You can choose which to use with the `--type` option as below. Here we use the list of validated runs from [2012](http://opendata.cern.ch/record/1002).

`brilcalc lumi --type pxl -c web -i Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt > 2012lumi.txt`

In this example the pixel detectors are used. This is the preferred option. For 2010 data a calculation using the hadronic forward calorimeters is used and is given by the option `--type hfoc`.

**Note**  You may notice at the end of the output luminosity sections that are listed in the json quality file but do not have any luminosity values corresponding to them. These correspond to sections that are left-overs at the end of a run, which where still tagged as STABLE RUN, but actually did not provide any luminosity. These are safe to ignore as they do not contain any events.

### Integrated luminosity for validated runs and luminosity sections over a range of runs

First obtain the file with the list of validated runs and luminosity sections. Here we use the [list for 2011 data](http://opendata-dev.web.cern.ch/record/1001).

`wget http://opendata.cern.ch/record/1001/files/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt`

RunA of 2011 proton-proton data comprises runs 160431 to 173692 (inclusive) so to calculate the integrated luminosity for this era run the command:

`brilcalc lumi -c web --begin 160431 --end 173692 -i Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt > RunA2011lumi.txt`

### Integrated luminosity for validated runs and luminosity sections, separated by luminosity sections

If you want to fetch the integrated luminosity by luminosity section and output the results to a `csv` file (which is recommended), first obtain the file with the list of validated runs and luminosity sections. Here we use the [list for 2011 data](http://opendata-dev.web.cern.ch/record/1001).

`wget http://opendata.cern.ch/record/1001/files/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt`

Then run the command:

`brilcalc lumi --byls --output-style csv -c web -i Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt > my2011lumibyls.csv`

The contents of the `csv` file will appear as below:

```console
#Data tag : v1 , Norm tag: None
#run:fill,ls,time,beamstatus,E(GeV),delivered(/ub),recorded(/ub),avgpu,source
160431:1615,19:19,03/14/11 03:14:43,STABLE BEAMS,3500,39.312,39.312,3.4,hfoc
160431:1615,20:20,03/14/11 03:15:07,STABLE BEAMS,3500,39.368,39.368,3.4,hfoc
160431:1615,21:21,03/14/11 03:15:30,STABLE BEAMS,3500,39.305,39.305,3.4,hfoc
160431:1615,22:22,03/14/11 03:15:53,STABLE BEAMS,3500,35.843,35.843,3.1,hfoc
160431:1615,23:23,03/14/11 03:16:17,STABLE BEAMS,3500,37.093,37.093,3.2,hfoc
160431:1615,24:24,03/14/11 03:16:40,STABLE BEAMS,3500,39.620,39.620,3.4,hfoc
160431:1615,25:25,03/14/11 03:17:03,STABLE BEAMS,3500,34.396,34.396,3.0,hfoc
160431:1615,26:26,03/14/11 03:17:27,STABLE BEAMS,3500,39.874,39.874,3.4,hfoc
```

### Integrated luminosity for a HLT trigger path

Here as an example we calculate the total integrated luminosity for a particular for high-level triggers whose name matches the
pattern `HLT_DoubleMu` and output the results to a `csv` file:

`brilcalc lumi -c web -r 173692 --hltpath="HLT_DoubleMu*" --output-style csv > run173692_DoubleMu.csv`

**Note**: It is strongly recommended to make your HLT query as specific as possible and to output to `csv`.

### Calculate trigger prescales for a run and trigger path

`brilcalc trg --prescale -c web -r 148002 --hltpath "HLT_Jet*"`

```console
+--------+-------+----------+-------------+---------------------------------+-------+--------------------+
| run    | cmsls | prescidx | totprescval | hltpath/prescval                | logic | l1bit/prescval     |
+--------+-------+----------+-------------+---------------------------------+-------+--------------------+
| 148002 | 1     | 1        | 12000       | HLT_Jet15U/20                   | ONE   | L1_SingleJet6U/600 |
| 148002 | 1     | 1        | 12000       | HLT_Jet15U_HcalNoiseFiltered/20 | ONE   | L1_SingleJet6U/600 |
| 148002 | 1     | 1        | 1200        | HLT_Jet30U/1200                 | ONE   | L1_SingleJet20U/1  |
| 148002 | 1     | 1        | 170         | HLT_Jet50U/170                  | ONE   | L1_SingleJet30U/1  |
| 148002 | 1     | 1        | 30          | HLT_Jet70U_v2/30                | ONE   | L1_SingleJet40U/1  |
| 148002 | 1     | 1        | 1           | HLT_Jet100U_v2/1                | ONE   | L1_SingleJet60U/1  |
| 148002 | 1     | 1        | 1           | HLT_Jet140U_v1/1                | ONE   | L1_SingleJet60U/1  |
+--------+-------+----------+-------------+---------------------------------+-------+--------------------+
```

### Change of prescales over a run

`brilcalc trg --prescale -c web -r 173243`

```console
+--------+-------+----------+
| run    | cmsls | prescidx |
+--------+-------+----------+
| 173243 | 1     | 5        |
| 173243 | 14    | 4        |
+--------+-------+----------+
```
