## Description

Monte Carlo simulation of pile-up is controlled by the code and configuration files of the [CMSSW](/search?page=1&size=20&q=CMSSW&type=Software) package `SimGeneral/MixingModule`. An input distribution is specified for each set of production samples which is supposed to represent the distribution of the mean number of interactions seen during data-taking.

## Introduction

Monte Carlo simulation of pileup is controlled by the code and configuration files of the [CMSSW](/search?page=1&size=20&q=CMSSW&type=Software) package `SimGeneral/MixingModule`. An input distribution (histogram) is specified for each set of production samples which is supposed to represent the distribution of the mean number of interactions seen during data-taking. The simulation proceeds as follows:

1. For each event, the mean number of interactions per crossing is chosen from the input histogram. This sets the instantaneous luminosity to be simulated for all of the bunch crossings in that event. For each event, this value is recorded as the "true" number of interactions. (`TrueNumInteractions`)

2. For each bunch crossing, both in- and out-of-time, the number of interactions is randomly sampled from a poisson distribution with a mean equal to the value chosen in (1). Note that this implies that all bunches have the same instantaneous luminosity, rather than allowing for bunch-to-bunch luminosity variation. In practice, the spread of bunch-by-bunch luminosities is much smaller than the poisson distribution, so this effect is negligible. One might evolve the simulation to include such features as the beginning or end of bunch trains, where the out-of-time pileup will have a significantly different luminosity structure (i.e., there is none, either before or after a given event). Since the bunch trains are quite long, this effect of ignoring these variations is likely to be negligible as well. The number of interactions that is actually included in each bunch crossing is also recorded. (`num_PU_vertices_`).

## Pileup Distributions from Data

The pileup distributions measured from data are available in [the CMS Luminosity information page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults).

## Monte Carlo Pileup Distributions

The "ideal" distributions input for each year's Monte Carlo production samples are catalogued on [this page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/Pileup_MC_Gen_Scenarios), which contains the actual numerical contents of each bin represented in the plots below.

### 2011

For the 2011 Data, the distribution shown here was used to generate the Monte Carlo events. It is matched directly to that observed in the data for the 2011 running, so little or no reweighting should be necessary to achieve good agreement between data and simulation as far as pileup is concerned.

The pileup distribution used to generate 2011 Monte Carlo events.:

<p align="center">
<img src="/static/docs/cms-pileup-simulation/pileup_2011_plot.jpg" width="70%"></p>

### 2012

For the 2012 data, the distribution shown here was used to generate the Monte Carlo events. On the Twiki page referenced above, this is the S10 distribution. Unlike 2011, this distribution is not an exact match to the data, so reweighting of the Monte Carlo samples is required in order to obtain good agreement.
Pileup distribution used to generate the 2012 Monte Carlo samples:

<p align="center">
<img src="/static/docs/cms-pileup-simulation/MC2012_PU.png" width="70%"></p>

### 2015

For the 2015 data, the distribution measured from the [2012 collision data](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#2012_proton_proton_8_TeV_collisi), scaled by 4/5 to correspond to the estimated mean number of interactions per crossing in 2015, was used to generated the Monte Carlo events.

## Disclaimer

The open data are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/). Neither CMS nor CERN endorse any works, scientific or otherwise, produced using these data.
All releases will have a unique DOI that you are requested to cite in any applications or publications.
