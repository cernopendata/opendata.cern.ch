
Possible solutions to frequently encountered issues can be found at the bottom of this page.

**I want to get a general introduction into HEP and CMS software and terminology, with a simplified event format**

- read the instructions related to educational content and follow the corresponding exercises

**I want to learn about the terms under which I can access and use the CMS Open Data, and publish results obtained from them**

- go to [Data preservation and open access policy](https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ShowDocument?docid=6032) (if you are a CMS member see also "papers by CMS members using public data") 

**I want to get inspiration for some potential physics topics**

- a link with examples of potentially interesting physics topics and their relation to CMS open data might be added here soon.

**I want to learn about the nature of the CMS physics objects and the corresponding variables and terminology**

- go to [CMS Physics Objects](http://opendata.cern.ch/about/CMS-Physics-Objects) 

**I want to find out whether I should go for 2010 or 2011 data (both are pp data at 7 TeV)**
- the 2010 data have been released first, have fewer, smaller data sets, better low pt tracking, low trigger thresholds, low pileup, and more/simpler analysis/validation examples, but no MC. If you do not need MC or maximal statistics, you might want to try 2010 data first (simpler).
- the 2011 data have more statistics, more diverse data sets, many associated MC sets, and a slightly more advanced VM environment. If you are immediately interested in maximal statistics and/or MC acceptance corrections you should go for 2011 data (more sophisticated).
- information on the respective luminosities and pileup rates vs. time can be found [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#Multi_year_Collisions_Plots). 
- there is nothing wrong with trying both (on separate VM's).

**I want to install the CMS virtual machine (separately for 2010 and 2011 data) which is needed for CMS Research level data analysis.**

- go to [CMS virtual machines](http://opendata.cern.ch/VM/CMS) 

**I want to install the CMS software environment on the virtual machine (separately for 2010 and 2011 data) which is needed for access to and analysis of CMS Research level data.**
- go to [Start analysing the data](http://opendata-dev.web.cern.ch/articles/getting-started-with-cms-open-data) 
- choose "2011" (default) or "2010"

The 2010 (SL5) virtual machine will only work on 2010 data with CMSSW 4-2-8. The 2011 (SL6) virtual machine will only work on 2011 data and MC with CMSSW 5-3-32.

**I want to produce some example physics distributions (inclusive dimuon spectrum analysis example directly from AOD or two lepton/four lepton analysis example with intermediate ntuples)**

- Install the CMS software as in the previous item (for 2010 or 2011)
- follow options A (dimuon spectrum, simpler) or B (two/four lepton example, more sophisticated). For 2011 option A, take the SingleMu or DoubleMu dataset index files from [http://opendata.cern.ch/record/32](http://opendata.cern.ch/record/32) or [http://opendata.cern.ch/record/17](http://opendata.cern.ch/record/17) 

**I want to find out which 2010 data sets exist, and how to get a feel for their content**

- go to 2010 CMS primary datasets
- choose a data set, and read comments

**and/or, to view some corresponding event displays**

- go to 2010 CMS derived data sets
- choose `Event display file derived from`... the name of the CMS primary data set you want (ZeroBias is known to be essentially empty)

**alternative way to view these event displays**

- load the [CMS event display](http://opendata-dev.web.cern.ch/visualise/events/CMS) 
- choose `Open File`, `Open Files from Web`, `2010`
- choose your data set

**I want to find out which 2010 data set and/or analysis/validation example is most useful for my purpose**

- to learn how to do a muon analysis, follow I want to produce some first physics distributions, options A (recommended) or B, or try one of the relevant I want to (re)validate the 2010 data sets examples
- to learn how to do an electron analysis, follow I want to produce some first physics distributions, option B, or try one of the relevant I want to (re)validate the 2010 data sets examples
- to learn how to do a minimum bias track analysis, try the MinimumBias example on I want to (re)validate the 2010 data sets
- more will follow

**I want to find out which 2011 data and MC sets exist, and how to get a feel for their content**

- go to 2011 CMS primary datasets or 2011 CMS simulated datasets
- choose a data set, and read comments

**and/or, to view some corresponding event displays (data only for the time being)**

- go to 2011 CMS derived data sets
- choose `Event display file derived from`... the name of the CMS primary data set you want (ZeroBias is known to be essentially empty)

**alternative way to view these event displays (data only)**
- load the [CMS event display](http://opendata-dev.web.cern.ch/visualise/events/CMS) 
- choose `Open File`, `Open Files from Web`, `2011`
- choose your data set

**how to interpret the MC set names?**
- check [description](http://opendata.cern.ch/about/CMS-Simulated-Dataset-Names) 

**I want to find out which 2011 data set and/or analysis/validation example is most useful for my purpose**
- dedicated examples for 2011 beyond those available in "Getting Started" are [in preparation](https://github.com/cms-opendata-validation) to be added to the portal, including jet and top cross sections. Alternatively, start from a 2010 example and adjust to run on 2011 data. 

**I want to find out how to use the trigger and trigger prescale information in the data set I am interested in (still very basic, to be improved)**
- go to CMS Trigger Information (currently for 2011 only)

**I want to find out how to access the luminosity information for the data set I am interested in and how to select "good data" only**
- check the [luminosity record](http://opendata.cern.ch/record/1051) 
- check the [JSON description](http://opendata.cern.ch/record/1000) 

**I want to find out whether I need condition data base information, and if so, how to access it (still very basic, to be improved)**
- condition data are needed only on sophisticated examples using e.g. jet energy corrections (many of the simpler analysis/validation examples documented here do not)
- using condition data significantly slows down data access, so use them only if really needed. If so:
- go to CMS Condition Data for basic information (in contrast to what is stated there, they are NOT needed to run CERNVM in general, only to perform sophisticated tasks)

**I want to find more CMS software and data format documentation from public sources (strongly recommended for serious analysis, but hard to navigate!)**

- check the [CMS public web](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WebHome) or the CMS Fermilab website or Google 

**I want to use the external public analysis example from the MIT jet analysis group papers**
- Jet Substructure Studies with CMS Open Data, A. Tripathee et al., Apr 19, 2017, MIT-CTP-4890, [arXiv:1704.05842](https://inspirehep.net/record/1593756) 
- Exposing the QCD Splitting Function with CMS Open Data, A. Larkoski et al., Apr 17, 2017, MIT-CTP-4891, [arXiv:1704.05066](https://inspirehep.net/record/1591972) 

**I want to (re)validate the 2010 data sets within my setup**

**for the MinimumBias, Commissioning, Mu or MuMonitor data sets:**

- go to 2010 Validation Utilities
- choose and execute the corresponding Validation code

**for the Multijet data set: (see also [here](http://hep.caltech.edu/cms/opendata/))**
- go to 2010 CMS Tools
- choose and execute `Razor filter and analyzer for SUSY searches`

**for the Electron (or Mu) data set:**
- go to 2010 CMS Tools
- choose and execute `Software to preprocess the CMS 2010 Muon and Electron datasets for the two-lepton/four-lepton analysis example of CMS open data`, then
- choose `Two-lepton/four-lepton analysis example of CMS 2010 open data` and compare PAT-tuples from the previous to those linked therein, or execute it on your new PAT tuples

**for the ZeroBias data set:**
- not useful, no validation needed

**for the Jet, MuOnia, BTau, Photon, JetMETTaumonitor, METFwd data sets:**
- validation not yet available (partially in preparation)

**I want to backup my code, or import some external code**
- we recommend to use scp from and to your host from within the VM

**I want to find the luminosity of my data set, possibly constrained by using specific triggers**

- please check [CMS luminosity information](http://opendata.cern.ch/record/1051),  
- decide on the triggers you want to use
- find out the runs/lumi sections in which these triggers were active and whether they were prescaled
- overlap with the available Open Data samples (run range) and with the JSON data quality selection
- if not prescaled, sum up the luminosity for the surviving runs/lumi sections
- if prescaled, life is more complicated ...

**I want to find the effective luminosity of my MC set**
- to be documented.
- generically: divide MC cross section (next item) times matching efficiency times filter efficiency by number of events.

**I want to find the generator cross section of a particular MC set**
- to be documented ...
- on some MC sets, the following might work (reliability of information not guaranteed): open the ROOT file, create TBrowser, navigate to: `Runs` -> `GenRunInfoProduct_generator__SIM.` -> `GenRunInfoProduct_generator__SIM.obj` -> `InternalXSec` -> `value_`

**I want other information than the one documented here and on [http:opendata.cern.ch](http://opendata.cern.ch/)**
- kindly contact opendata-support@cern.ch

**I ran into a problem and need help**
- Please check our page related to known errors

