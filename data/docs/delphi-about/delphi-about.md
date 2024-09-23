DELPHI was one of four large detectors on the Large Electron-Positron collider (LEP). It took 7 years to design and build, and it started up in 1989. In December 2000, DELPHI stopped taking data and was dismantled to leave room for the construction of the Large Hadron Collider in the LEP tunnel. A detailed description of the detector as it was in 1990 can be found in [this preprint](https://cds.cern.ch/record/212026/files/cer-000124113.pdf), which has been published in [Nuclear Instruments and Methods, A303 (1991), 233-276](https://doi.org/10.1016/0168-9002%2891%2990793-P).

## Overview
The DELPHI detector consisted of a central cylinder filled with subdetectors, with two end-caps. It was 10 meters in length and diameter, and weighed 3500 tons. The detector consisted of 20 subdetectors. A large superconducting magnet sat between an electromagnetic calorimeter and a hadronic calorimeter. The magnet generated a field to deflect charged particles so their charge and momenta could be measured.

The DELPHI collaboration running the detector comprised more than 550 physicists from 56 participating universities and institutes in 22 countries.

## DELPHI data access policy
In autumn 2023, the DELPHI collaboration board decided to make DELPHI data and the required tools to read it open. The revised data access policy file can be found at [here](/record/417). It is mandatory to read this document before using DELPHI data.

## DELPHI data
DELPHI data structures are stored in ZEBRA format. Therefore, the software stack depends on [CERNLIB](https://cernlib.web.cern.ch/cernlib/). The data set includes:

- Raw data
- Reconstructed data
- Simulated data
- DELPHI conditions database

There are different DST types available:

* short DST (.sdst): available for the LEP1 phase
* long DST (.dst): available for some years of LEP1 and LEP2
* extended short DST (.xsdst): availble for the LEP2 phase

User analyses should only use short or long DST reconstructed data.

## The DELPHI software stack
The preserved DELPHI stack consist of the following components:

* The analysis framework: [dstana package](/record/80502)
* Event display: [delgra package](/record/80503)
* Simulation: delsim package
* Reconstruction: delana package

A special case is the DELPHI event server, which allows to pick and reconstruct individual events from the raw data set. This can be useful for in depth analysis/scans of individual events or show cases.

### Distribution of binaries

Container images are available which can be directly used locally. The Alma9 container image can be found in [https://gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64](gitlab-registry.cern.ch/delphi/deployment/delphi/al9_64).

Apart from that, it is also possible to run the DELPHI stack from /cvmfs/delphi.cern.ch.

## Quick start guide
A quickstart guide can be found in [here](/docs/delphi-getting-started).

## Documentation
Documentation and photo collections can be found on the [CERN document server](https://cds.cern.ch). A subset of manuals can be found on this portal for quick access as well.
