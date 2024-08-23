# About simulation
Simulation is supported for all the years 1992 and later.
The code differs a bit for each of the years due to changes in the detector setup. The basic steps are:

 * Generation of events. This was typically done with stand-alone external generators, such as Pythia, HZHA, etc. DELPHI also supports  few build-in generators.
 * Detector simulation. This step passes the generated events through the detector simulation. The output is equivalent to DELPHI raw data, for simulation
 * Reconstruction. The reconstruction step creates a readable DST file
 * Short DST creation. During this step, latest tunings are applied, e.g. for b-tagging. Short DST is the file format which should be used for analysis.

# Creating Monte Carlo samples interactively

## Using internal generators
For creating a few events with a build-in generator run
```
$ runsim -VERSION va0u -LABO CERN -NRUN 1000 -EBEAM 45.625 -igen qqps -NEVMAX 10

```

The parameters are:

* `VERSION`:  The requested detector setup is for the year 1994, using the latest processing version number. Allowed values are: `92e`, `93d`, `94c`, `95g`, `96g`, `97g`, `98e`, `99e`, `a0e` and `a0u` where a0 processings are for the year 2000.
* `LABO` sets the laboratory identifier, here CERN. This setting is mainly used to setup random number seeds.
* `NRUN` sets th run nummber. Note that for simulation this will turn up as as a negative number in the final data file, indicating that this is simulated data.
* `EBEAM` sets the beam energy which has to match the settings in the generator
* `igen qqps` instructs the script to use an internal generator. `qqps` is the desired end state. Possible values include `baba`, `bbps`, `mumu` and some more


The example above will create 10 **e+e-->Z->qqbar** events at a beam energy of 45.625 GeV (ECM 91.25 GeV), using the build-in *QQPS* generator.

It will then pass the events through the detector simulation with the following settings:

* Run number *-1000*, where the negative number indicate simulated events
* Laboratory identifier, here *CERN*
* *va0u* selects the detector setup for the second part of year 2000 data taking period, where *TPC* sector 6 had failed.

The events will be reconstructed and an [extended short DST](/record/80505) file will be created, ready for further analysis.

The important created files are :

* *simana.fadsim* : detector simulation output, corresponds to raw data, not to be used directly
* *simana.fadana* : reconstructed output, [full DST](/record/80504) format, not to be used directly
* *simana.xsdst*  : [extended short DST](/record/80505) output for analysis, the final output

Technically, analysis code can be run as well on the [full DST](/record/80504) output, however, this requires that a bunch of modules and fixes have to be rerun on top
of the input data before they can be used.

## Using external generators
In this case the generator is run externally and the output is written to a file in a specific format. This can then be passed through the detector simulation.

In the container you can find an example in the folder *~/examples/pythia*. It is as well available from [CERN gitlab](https://gitlab.cern.ch/delphi/examples).
This guide assumes you are using the [DELPHI container](delphi-guide-docker) to run the software stack.

```
[delphi ~] $ cd examples/pythia
```

Take a look at the script `pythia.sh` in that folder. It looks like this:

```
#! /bin/bash -f
rm pythia.tit
cat >> pythia.tit <<EOF
C-- This is an example Title file for running the PYTHIA generator
C--

C-- turn on FFKEY steering file debug- this can be commented out for production
LIST

C-- Lab ID (used to generate random number seed)
LABO 'CERN'

C-- Run number (used to generate random number seed)
NRUN 1001

C-- Centre of mass energy
ECMS 91.25

C-- Number of events to generate
NEVT 10

C-- Process to generate
C-- See the PYTHIA manual for details, but common ones are:
C-- 1  = Z/gamma
C-- 22 = ZZ
C-- 25 = WW
C-- 35 = Zee (use with caution, double counts with gamma-gamma generators)
C-- 36 = Wev (use with caution, probably unreliable)
ACHAN 22

C-- Allowed Z decays
C-- order is d u s c b e v_e mu v_mu tau v_tau
C-- code is as per MDME(IDC,1) - see PYTHIA manual
C--      0 = off
C--      1 = on
C--      2 = on for particle but off for antiparticle
C--      3 = on for antiparticle but off for particle
C--      4 = for pairs eg W+W-, one but not both is allowed
C--      5 = as =4 but an independent group of channels
C-- eg for taus only ZDK 0 0 0 0 0 0 0 0 0 1 0
ZDK 1 1 1 1 1 1 1 1 1 1 1

C-- Allowed W decays
C--   order is ud us ub cd cs cb ev_e muv_mu tauv_tau
C--   code is as per ZDK above
C-- eg for semileptonic evqq, choose WDK 4 4 4 4 4 4 5 0 0
WDK 1 1 1 1 1 1 1 1 1

C-- Tau polarisation
C-- 0 = Standard JETSET
C-- 1 = use TAUOLA library
TAUP 1

C-- Maximum mass cut on heavy bosons (CKIN 41 and CKIN 43)
C-- default is 12.0 GeV/c**2
C--   minimum is 2.0 GeV/c**2 (hard coded in PYTHIA)
MCUT 2.0

C-- ISR
ISR 1

C-- FSR
FSR 1

C-- Fragmentation
FRAG 1

C-- Coulomb correction
ACOUL 1

C-- Mw
MW 80.41

C-- W width; negative value : calculate internally
GAMW -1.0

C-- Mz
MZ 91.187

C-- Z width
GAMZ 2.490

C-- Mtop
MTOP 173.8

C-- M Charged Higgs
MCHIG 1000.0

C-- M Neutral Higgs
MNHIG 125.36

C-- Normalisation Scheme
C--   MSTP(8) - see manual
C--   0 = running alpha_em(Q**2) and a fixed sin**2 theta_weak
C--   1 = calculate from Gf, Mz, sin**2 theta_weak, Mw
C--   2 = calculate from Gf, Mz, Mw only
NORM 1

C-- Scale for showering of ISR
C--   MSTP(68) switch
C--   0 = Limit to s-hat
C--   1 = scale limited as s for ISR
C--   2 = scale limited to s for ISR and cross-section calulcation
SSCAL 2

C-- Running alpha_em
C-- 0 = fixed at Q**2 = 0
C-- 1 = running alpha_em
C-- 2 = fixed to Q**2 = 0   value below 1 GeV**2;
C--     and to   Q**2 = 2Mw value above 1 GeV**2
C-- 1 is recommended
RUNA 1

C-- Alpha_em(0)
AEM0 137.0359895

C-- Alpha_em(2Mw) (only used if RUNA = 2)
AEMW 128.07

C-- Sin**2 theta_weak
C--   will be ignored if using scheme NORM = 2
S2WE 0.2319

C-- Output flag
C-- 0 = write nothing else use this LUN
LOUT 26

C-- Output format
C-- 0 = DELSIM unformatted
C-- 1 = EXCALIBUR formatted
C-- 2 = FASTSIM formatted
OFORM 0

C-- Number of debug events to print out
NDBG 10

C-- Safety factor on cross sections
C--  increase if "Maxiumum violated" error messages occur
C--  but it slows down the program
SAFE 5.0

END

EOF

ln -s pythia.tit fort.11

make pythia

rm fort.26
pythia | tee pythia$$.log
mv fort.26 pythia.fadgen

# run detector simulation and reconstruction
runsim -VERSION v94c -LABO CERN -NRUN 1000 -EBEAM 45.625 -gext pythia.fadgen

```

In the first part, the configuration (also called the **title card**) for the generator is created and stored in a file named *pythia.tit* and linked to a file named *fort.11*. This is where the program will read it from later on.
The title card is where you can define the desired end states etc. This part is not DELPHI but generator specific.
´
Then, the generator binary is compiled using the provided *Makefile* with the `make` command. Then the *pythia* generator is started.
It will store the generated events in a file named *fort.26* which is then renamed to *pythia.fadgen*. Logging information goes both to the screen and to a file.

The next step consist of passing the generated events through the DELPHI detector simulation, reconstruction and short DST creation.
The `runsim` script takes care of all of this. The arguments are:

* `VERSION`:  The requested detector setup is for the year 1994, using the latest processing version number. Allowed values are: `92e`, `93d`, `94c`, `95g`, `96g`, `97g`, `98e`, `99e`, `a0e` and `a0u` where a0 processings are for the year 2000.
* `LABO` sets the laboratory identifier, here CERN. This setting is mainly used to setup random number seeds.
* `NRUN` sets th run nummber
* `EBEAM` sets the beam energy which has to match the settings in the generator
* `gext` instructs the tools to read the external file name pythia.fadgen which was just created by the `pythia` generator run

Run the script by typing inside the *pythia* folder in the container via

```
[delphi ~] $ ./pythia.sh
```
The script will create the following important data files:

* `simana.fadsim` is the raw simulated data
* `simana.fadana` is the reconstructed simulated data
* `simana.sdst` is the short DST data which is what should be used for analysis.
