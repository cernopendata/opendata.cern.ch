If you are interested in step-by-step instructions to start working with CMS Open Data, please consult these pages:

* [Install Virtual Machine](/docs/cms-virtual-machine-2011) or [Use a container](/docs/cms-guide-docker)
* [Get started with CMS Open Data](/docs/cms-getting-started-2011)

However, if you are interested in finding hints, tips and guidance for conducting a research-oriented analysis using CMS Open Data, please see our notes on this page. Note that possible solutions to frequently encountered issues can be found on [our page of known errors](/docs/cms-guide-troubleshooting).

---

### Quick introduction

**I want to get a general introduction into HEP and CMS software and terminology, with a simplified event format.**

* Read the instructions related to [educational content](/docs/cms-guide-for-education) and follow the corresponding exercises.


**I want to learn about the terms under which I can access and use the CMS Open Data, and publish results obtained from them.**

* Go to ["Data preservation and open access policy"](/record/414) (if you are a CMS member, also see the internal document ["Rules for use of open access CMS data by individual members of CMS"](https://cms-docdb.cern.ch/cgi-bin/DocDB/ShowDocument?docid=12242)).


**I want to get inspiration for some potential physics topics.**

* A link with examples of potentially interesting physics topics and their relation to CMS Open Data might be added here soon.


**I want to learn about the nature of the CMS physics objects and the corresponding variables and terminology.**

* Go to ["CMS Physics Objects"](/docs/cms-physics-objects-2011).

---

### Deciding which datasets to explore

**I want to find out whether I should go for data from 2010 or 2011 (both are pp data at 7 TeV) or from 2012 (pp data at 8 TeV).**

* The 2010 data have been released first; have fewer, smaller datasets with better low-p<sub>T</sub> tracking, low trigger thresholds, low pile-up and more/simpler analysis/validation examples; but have no MC. If you do not need MC or maximal statistics, you might want to try 2010 data first.
* The 2011/2012 data have more statistics, more diverse datasets, many associated MC sets, and a slightly more advanced VM environment. If you are immediately interested in maximal statistics and/or MC acceptance corrections you should go for 2011/2012 data.
* Information on the respective luminosities and pile-up rates vs time can be found in [public CMS luminosity information](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#Multi_year_Collisions_Plots).
* If you want to try both datasets, you will need to use [the appropriate VMs](/search?page=1&size=20&tags=VM&experiment=CMS).


**I want to install the CMS software environment needed for access to and analysis of CMS Research level data.**

* Install the appropriate virtual machine, [2010 VM](/record/250) for 2010 data, and [2011 VM](/record/252) for 2011/2012 data.
* As an alternative to a virtual machine you can try running the CMS software environment in a container by following [these instructions](/docs/cms-guide-docker).
* Go to ["Getting started with CMS 2010 open data"](/docs/cms-getting-started-2010) for 2010 or ["Getting started with CMS 2011 open data"](/docs/cms-getting-started-2011) for 2011/2012 data.

**Note**: The 2010 (SL5) virtual machine will only work on 2010 data with CMSSW 4-2-8 (and other SLC5-based CMSSW releases). The 2011 (SL6) virtual machine will only work on 2011/2012 data and MC with CMSSW 5-3-32 (and other SLC6-based CMSSW releases).


**I want to produce some example physics distributions.**

* Install the CMS software as in the previous item (for 2010 or 2011).
* Follow options A (inclusive di-muon spectrum analysis example directly from AOD) or B (two-/four-lepton analysis example with intermediate ntuples) in ["Getting started with CMS 2010 open data"](/docs/cms-getting-started-2010) or ["Getting started with CMS 2011 open data"](/docs/cms-getting-started-2011).

---

### Exploring the 2010 datasets

**I want to find out which 2010 datasets exist, and how to get a feel for their content.**

* Go to [2010 CMS primary datasets](/search?page=1&size=20&q=&type=Dataset&subtype=Collision&experiment=CMS&year=2010),
* choose a dataset, and read the comments.


**I also want to view some corresponding event displays.**

* Go to [2010 CMS derived datasets of event display ("ig") type](/search?page=1&size=20&q=&type=Dataset&subtype=Derived&experiment=CMS&year=2010&file_type=ig),
* choose `Event display file derived from`… + the name of the CMS primary dataset you want (ZeroBias is known to be essentially empty).

or, alternatively:

* Load the [CMS event display](/visualise/events/cms),
* choose `Open File` &rarr; `Open Files from Web` &rarr; `2010`, and
* choose your dataset.


**I want to find out which 2010 dataset and/or analysis/validation example is most useful for my purpose.**

* To learn how to do a muon analysis, follow "*I want to produce some example physics distributions*," (above) with either option A (recommended) or B, or try one of the relevant "*I want to run the examples used for validation of the 2010 datasets*," (further below).
- To learn how to do an electron analysis, follow "*I want to produce some first physics distributions*," (above) with option B, or try one of the relevant "*I want to run the examples used for validation of the 2010 datasets*," (below).
- To learn how to do a minimum-bias track analysis, try the MinimumBias example on "*I want to run the examples used for validation of the 2010 datasets*," (below).
- [More to come…]

---

### Exploring the 2011-2012 datasets

**I want to find out which 2011-2012 data and MC sets exist, and how to get a feel for their content.**

* For collision data, go to [2011 CMS primary datasets](/search?page=1&size=20&q=&subtype=Collision&experiment=CMS&year=2011) or [2012 CMS primary datasets](/search?page=1&size=20&q=&subtype=Collision&experiment=CMS&year=2012)
* For MC, go to [2011 CMS simulated datasets](/search?page=1&size=20&q=&subtype=Simulated&experiment=CMS&year=2011) or [2012 CMS simulated datasets](/search?page=1&size=20&q=&subtype=Simulated&experiment=CMS&year=2012)
* choose a dataset, read the comments, and read also about [simulated dataset names](/docs/cms-simulated-dataset-names).


**I also want to  to view some corresponding event displays.**

* These are available for data only for the time being.
* Go to CMS derived datasets of event display ("ig") type for the [2011 data](/search?page=1&size=20&q=&subtype=Derived&experiment=CMS&year=2011&file_type=ig) or the [2012 data](/search?page=1&size=20&q=&subtype=Derived&experiment=CMS&year=2012&file_type=ig) ,
* choose `Event display file derived from`… + the name of the CMS primary dataset you want (ZeroBias is known to be essentially empty).

or, alternatively:

* Load the [CMS event display](/visualise/events/cms),
* choose `Open File` &rarr; `Open Files from Web` &rarr; `2011` or `2012`, and
* choose your dataset.


**I want to find out which 2011 or 2012 dataset and/or analysis/validation example is most useful for my purpose.**

* Dedicated examples beyond those available in "Getting Started" can be found in [software](/search?page=1&size=20&type=Software&subtype=Analysis&experiment=CMS&year=2011&year=2011-2012), including Higgs-to-four-lepton analysis, jet tuple production and top cross-sections. Alternatively, start from a 2010 example and adjust to run on 2011 or 2012 data (see [the CMS troubleshooting guide](/docs/cms-guide-troubleshooting) for instructions).


* For more information on Monte Carlo, see below.

---

### Trigger information, condition data, luminosity

**I want to find out how to use the trigger and trigger prescale information in the dataset I am interested in.**

* Go to [the guide to CMS trigger system](/docs/cms-guide-trigger-system).


**I want to find out how to access the luminosity information for the dataset I am interested in and how to select "good data" only.**

* Check the [CMS luminosity information](/search?page=1&size=20&q=luminosity&type=Supplementaries&subtype=Luminosity), and
* check the [list of validated runs](/search?page=1&size=20&q=%22CMS%20list%20of%20validated%20runs%22).


**I want to find out whether I need condition data base information, and if so, how to access it.**

* Condition data are needed on examples using e.g. jet energy corrections and trigger configuration information, many of the simpler analysis/validation examples do not need any additional corrections from condition database.
* Using condition data slows down data access, so use them only if really needed. If so:
    * see the instructions in ["The Guide to the CMS condition database"](/docs/cms-guide-for-condition-database).


**I want to find the luminosity of my dataset, possibly constrained by using specific triggers.**

* Please check [CMS luminosity information](/search?page=1&size=20&q=luminosity&type=Supplementaries&subtype=Luminosity),
* decide on the triggers you want to use,
* find out the runs/lumi sections in which these triggers were active and whether they were prescaled,
* overlap with the available CMS Open Data samples (run range) and with the selection in the list of validated runs.
    * If not prescaled, sum up the luminosity for the surviving runs/lumi sections.
    * If prescaled, life is more complicated. Find the prescales as in [the trigger example code](/record/5004)

---

### Performing an analysis

**I want to find more CMS software and data format documentation from public sources.**

* This is strongly recommended for serious analysis, but is hard to navigate!
* Check the [CMS public Twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WebHome) or the CMS Fermilab website or use your favourite web-search engine.


**I want to learn about the published jet-analysis papers by the MIT group.**

* See *Jet Substructure Studies with CMS Open Data*, A. Tripathee et al., Apr 19, 2017, MIT-CTP-4890, [arXiv:1704.05842](https://inspirehep.net/record/1593756),
* and *Exposing the QCD Splitting Function with CMS Open Data*, A. Larkoski et al., Apr 17, 2017, MIT-CTP-4891, [arXiv:1704.05066](https://inspirehep.net/record/1591972).


**I want to run the examples used for validation of the 2010 datasets within my setup…**

* … for the MinimumBias, Commissioning, Mu or MuMonitor datasets:
    * Go to [Validation software](/search?page=1&size=20&q=&subtype=Validation&type=Software&year=2010)
    * choose and execute the corresponding Validation code.
* … for the Multijet dataset (see also [here](http://hep.caltech.edu/cms/opendata/)):
    * choose and execute ["Razor filter and analyzer for SUSY searches"](/record/553).
* … for the Electron (or Mu) dataset:
    * choose and execute ["Software to preprocess the CMS 2010 Muon and Electron datasets for the two-lepton/four-lepton analysis example of CMS open data"](/record/200), then
    * choose ["Two-lepton/four-lepton analysis example of CMS 2010 open data"](/record/101) and compare PAT-tuples from the previous to those linked therein, or execute it on your new PAT tuples.
* … for the ZeroBias dataset:
    * Not useful, no validation needed.
* … for the Jet, MuOnia, BTau, Photon, JetMETTaumonitor, METFwd datasets:
    - Validation not yet available (partially in preparation).


**I want to backup my code, or import some external code.**

* You can use `scp` from and to your host from within the VM.

---

### Monte Carlo

**How do I interpret the MC set names?**

* Check [CMS Simulated Dataset Names](/docs/cms-simulated-dataset-names).


**I want to find the effective luminosity of my MC set.**

* Information will be added to the portal.
* Generically: divide MC cross-section (next item) times matching efficiency times filter efficiency by the number of events.

**I want to find the generator cross section of a particular MC set.**

* To be documented.
* On some MC sets, the following might work (reliability of information not guaranteed): open the ROOT file, create TBrowser and navigate to `Runs` &rarr; `GenRunInfoProduct_generator__SIM.` &rarr; `GenRunInfoProduct_generator__SIM.obj` &rarr; `InternalXSec` &rarr; `value_`.

---

### Further information / Contact us

**I want information that is not documented here and elsewhere on the [CERN Open Data portal](http://opendata.cern.ch/).**

* Kindly contact &lt;[opendata-support@cern.ch](mailto:opendata-support@cern.ch)&gt;

**I ran into a problem and need help!**

* Please check [our page related to known errors](/docs/cms-guide-troubleshooting).
