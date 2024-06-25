DELPHI was one of four large detectors on the Large Electron-Positron collider (LEP). It took 7 years to design and build, and it started up in 1989. In December 2000, DELPHI stopped taking data and was dismantled to leave room for the construction of the Large Hadron Collider in the LEP tunnel.

## Overview
DELPHI consisted of a central cylinder filled with subdetectors, with two end-caps. It was 10 meters in length and diameter, and weighed 3500 tons. The detector consisted of 20 subdetectors. A large superconducting magnet sat between an electromagnetic calorimeter (for tracking electrons) and a hadronic calorimeter (to detect hadrons). The magnet generated a field to deflect charged particles so their charge and momenta could be measured.

The collaboration running the detector consisted of about 550 physicists from 56 participating universities and institutes in 22 countries.

## DELPHI data access policy
In fall 2023, the DELPHI collaboration board decided to make DELPHI data and the required tools to read it open. The revised data access policy file can be found at the experiment web site at [https://delphi-www.web.cern.ch/](https://delphi-www.web.cern.ch/). It is mandatory to read this document before using DELPHI data.

## DELPHI data
DELPHI data structures are stored in ZEBRA format. Therefore, the software stack depends on [CERNLIB](https://cernlib.web.cern.ch/cernlib/). The data sets include:

- Raw data: used by the DELPHI event server
- Reconstructed data
- Simulated data
- DELPHI Conditions database

User analyses should only use short or long DST reconstructed data. There are different types:

* short DST (.sdst): available for the LEP1 phase
* long DST (.dst): available for some years of LEP1 and LEP2
* extended short DST (.xsdst): availble for the LEP2 phase

## The DELPHI software stack
The preserved DELPHI stack consist of the following components:

* The analysis framework: dstana package
* Simulation: delsim package
* Reconstruction: delana package
* Event display: delgra

A special case is the DELPHI event server, which allows to pick and reconstruct individual events from the raw data set. This can be useful for in depth analysis/scans of individual events or show cases.

### Distribution of binaries

DELPHI binaries are distributed via CVMFS via /cvmfs/delphi.cern.ch. Several Linux distributions are supported.

In addition, container images are available which can be directly used locally. The Alma9 container image can be found in [https://gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64](gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64).

## Quick start guide
A quickstart guide can be found in (here)[docs/delphi-getting-started].

## Documentation and photos
Documentation and photo collections can be found on the (CERN document server)[https://cds.cern.ch]. The most important manuals will be made available via the opendata portal.
