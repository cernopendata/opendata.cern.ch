The LHCb collaboration is happy to announce the official release of the [LHCb
Ntupling Service](https://opendata-lhcb-ntupling-service.app.cern.ch/): a web
service for on-demand production and publishing of custom LHCb open data. This
provides the public access to both Run I, and for the first time, Run II pp
data collected by LHCb. This amounts to over 4 PB of data to explore! The image
displays an event recorded during Run II.

<p align="center">
  <img src="/static/docs/lhcb-releases-service-to-access-run2-data/LHCb7.png" width="50%" alt="A typical LHCb Run II event">
  <br/><em>A typical LHCb event fully reconstructed during data taking on May 9th 2016.</em>
  <br/><em>Particles identified as pions, kaon, etc. are shown in different colours.</em>
</p>

This follows the release of the full [Run I pp data on the CERN Open Data
Portal](/docs/lhcb-releases-entire-run1-dataset) in December 2023. While for
the previous release, knowledge of the LHCb software stack was necessary for
subsequent analysis of the released data, this is no longer the case for users
of the LHCb Ntupling Service. Instead, custom ntuples are produced containing a
collection of physics objects and quantities based on user specifications. The
Ntupling Service serves as an all in one place for users to request custom
ntuples with LHCb data, track the request process, communicate with the LHCb
open data team, and download the resulting ntuples.

During the ntuple creation step, users interact with the [LHCb Ntuple
Wizard](https://inspirehep.net/literature/2637214), providing an intuitive
step-by-step process for specifying their ntuple configuration. This process
consists of (1) selecting a physics object of interest, (2) choosing a
corresponding dataset, and (3) specifying the configuration of the
corresponding ntuples.

This release marks a significant advancement in the LHCb open data
infrastructure, and is an exciting step for the larger open data community,
where the barrier for entry of data analysis is lowered without the need for
any experiment specific software. The release is accompanied by a growing
[usage guide](https://lhcb-opendata-guide.web.cern.ch/ntupling-service/) with
a detailed walkthrough for request submission and tracking, in addition to
analysis example workflows with the resulting ntuples.

This work was carried out through the [Data Processing & Analysis
project](https://lhcb-dpa.web.cern.ch/lhcb-dpa/) of LHCb in collaboration with
[CERN’s Information Technology
Department](https://information-technology.web.cern.ch/). The LHCb
collaboration would like to thank the CERN Information Technology Department
for co-designing, co-developing and co-operating the new service.
