- [Introduction](#intro)
  
- [Workflow](#work)

- [Pileup Distributions Used in MC Productions](#dist)
  
- [Access Pileup Infromation Stored in Datasets](#access)

## Introduction

LHC collides proton bunches every 25ns. Many collisions occur simultaneously within one proton-proton bunch crossing. These additional interactions (collisions) from the current bunch crossing are called in-time pilep-ups. Furthermore, the detector response may be affected by both the current brunch crossing and the nearby bunch crossings. The interactions from the nearby bunch crossings are called out-of-time pile-ups. We need to model the additional "pileup" collisions to make the simulation match the data. 

Monte Carlo simulation of pile-up is controlled by the code and configuration files in `SimGeneral/MixingModule` of the CMSSW package. 

## Workflow

The simulation proceeds as follows:

1. From [the pileup distribution measured from data](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults), which is a histogram of the mean number of interactions per bunch crossing, sample a number as the expected number of interactions to be simulated in an event. Store this value as the "true" number of interactions for the event.

2. The number of interactions per bunch crossing (in-time and out-of-time) in the event is randomly sampled from a poisson distribution with its mean equal to the valule chosen in (1). This procesure determines how many pile-ups to be added to the simulated event. Store this value as the actual number of interactions included in the event.
   
   Note that sampling one the number for all the bunch crossings in an event implicity imposes an assumption that all bunches in one single event have the same instantaneous luminosity. It is okay to neglect bunch-to-bunch luminosity variations, because the spread of bunch-by-bunch luminosities is much smaller than the spread of the poisson distribution, and the effect of the bunch-train structure is negligibly small as well.
   
## Pileup Distributions Used in MC Productions

The numerical contents of the estimated pileup distributions used in the MC productions can be found on [this Twiki page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/Pileup_MC_Gen_Scenarios). The distribution varies for each year. The plots below are made from the numerical values (corresponding to each year's pileup scenario) provided on the TWiki page. The x-axis of the histograms below are "mean number of interactions per bunch crossing".

#### 2011

For the 2011 Data, the distribution shown here was used to generate the Monte Carlo events. It is matched directly to that observed in the data for the 2011 running, so little or no reweighting should be necessary to achieve good agreement between data and simulation as far as pileup is concerned.

The pileup distribution used to generate 2011 Monte Carlo events.:

<p align="center">
<img src="/static/docs/cms-pileup-simulation/pileup_2011_plot.jpg" width="70%"></p>

#### 2012

For the 2012 data, the distribution shown here was used to generate the Monte Carlo events. On the Twiki page referenced above, this is the S10 distribution. Unlike 2011, this distribution is not an exact match to the data, so reweighting of the Monte Carlo samples is required in order to obtain good agreement.
Pileup distribution used to generate the 2012 Monte Carlo samples:

<p align="center">
<img src="/static/docs/cms-pileup-simulation/MC2012_PU.png" width="70%"></p>

#### 2015

For the 2015 data, the distribution measured from the [2012 collision data](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#2012_proton_proton_8_TeV_collisi), scaled by 4/5 to correspond to the estimated mean number of interactions per crossing in 2015, was used to generated the Monte Carlo events.

#### 2016

For the 2016 data, the distribution shown here was used to generate the Monte Carlo events. This distribution is not an exact match to the data, so reweighting of the Monte Carlo samples is required in order to obtain good agreement.

<p align="center">
<img src="/static/docs/cms-pileup-simulation/MC2016_PU.png" width="70%"></p>

## Access Pileup Information Stored in Datasets

#### AOD and MiniAOD

The MC truth information about pileup is available in the form of a vector of `PileupSummaryInfo` objects for the different bunch crossings. In AOD, the collection is `addPileupInfo`, which has detailed information for both in-time and out-of-time bunch crossings. In MiniAOD, the collection is `slimmedAddPileupInfo` slimmed by not saving the detailed information for the out-of-time bunch crossings.

The information is accessed using two functions definied in `SimDataFormats/PileupSummaryInfo/` of the CMSSW package:

- `getTrueNumInteractions()` retrieves the true mean number of the poisson distribution, from which the number of interactions in each bunch crossing of the event has been sampled.
- `getPU_NumInteractions()` retrieves the actual number of insteractions that have been added.

Here's an example of using these two functions. In your analyzer, include the code similar to this code snippet:
```
...
void Analyzer::BeginJob(edm::ConsumesCollector && iC)
{
        // Access the collection
        // "addPileupInfo" for AOD, "slimmedAddPileupInfo" for MiniAOD
	PupInfoToken = iC.consumes<std::vector<PileupSummaryInfo>>(edm::InputTag("slimmedAddPileupInfo")); 
}
...
void Analyzer::AnalyzePU(edm::Event const & event){
	int NumTrueInts = -1;
	int NumPUInts = -1;
	if(isMc){ // Fetch pileup info only for MC samples
	  edm::Handle<std::vector<PileupSummaryInfo>> PupInfo;
	  event.getByToken(PupInfoToken, PupInfo);

	  for(std::vector<PileupSummaryInfo>::const_iterator PVI = PupInfo->begin(); PVI != PupInfo->end(); PVI++){
	    int BX = PVI->getBunchCrossing();
	    if(BX == 0){
	      NumTrueInts = PVI->getTrueNumInteractions();
	      NumPUInts = PVI->getPU_NumInteractions();
	    }
	  }
	}
}
```

If you do not know how to work with an EDAnalyzer, check how to use an EDAnalyzer to analyze the CMS data in [AOD format](/doc/cms-getting-started-aod) or in [MiniAOD format](/doc/cms-getting-started-miniaod) first.

#### NanoAOD
- The true mean number of the poisson distribution, from which the number of interactions in each bunch crossing in the event has been sampled, is stored in the branch `Pileup_nTrueInt`.

- The number of insteractions that have been added to the event in the current bunch crossing is stored in the branch `Pileup_nPU`.

## Disclaimer

The open data are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/). Neither CMS nor CERN endorse any works, scientific or otherwise, produced using these data.
All releases will have a unique DOI that you are requested to cite in any applications or publications.
