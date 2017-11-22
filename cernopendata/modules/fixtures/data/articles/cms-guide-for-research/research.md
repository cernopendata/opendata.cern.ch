If you are interested in conducting a more sophisticated analysis using CMS Open Data, you should find hints, tips and guidance on this page. Please note that possible solutions to frequently encountered issues can be found on [our page of known errors](FIXME).

---

#### Quick introduction

> "I want to get a general introduction into HEP and CMS software and terminology, with a simplified event format."

- Read the instructions related to [educational content](/articles/cms-guide-to-education-use-of-cms-open-data) and follow the corresponding exercises.

<center>–––</center>

> "I want to learn about the terms under which I can access and use the CMS Open Data, and publish results obtained from them."

- Go to ["Data preservation and open access policy"](https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ShowDocument?docid=6032) (if you are a CMS member see also "papers by CMS members using public data").

<center>–––</center>

> "I want to get inspiration for some potential physics topics."

- A link with examples of potentially interesting physics topics and their relation to CMS Open Data might be added here soon.

<center>–––</center>

> "I want to learn about the nature of the CMS physics objects and the corresponding variables and terminology."

- Go to ["CMS Physics Objects"](http://opendata.cern.ch/about/CMS-Physics-Objects).

---

#### Deciding which datasets to explore

> "I want to find out whether I should go for data from 2010 or 2011 (both are pp data at 7 TeV)."

- The 2010 data have been released first; have fewer, smaller datasets with better low-p<sub>T</sub> tracking, low trigger thresholds, low pile-up and more/simpler analysis/validation examples; but have no MC. If you do not need MC or maximal statistics, you might want to try 2010 data first (simpler).
- The 2011 data have more statistics, more diverse datasets, many associated MC sets, and a slightly more advanced VM environment. If you are immediately interested in maximal statistics and/or MC acceptance corrections you should go for 2011 data (more sophisticated).
- Information on the respective luminosities and pile-up rates vs time can be found on [this Twiki page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#Multi_year_Collisions_Plots).
- If you want to try both datasets, you will need to use the appropriate VMs.

<center>–––</center>

> "I want to install the CMS software environment on the virtual machine (separately for 2010 and 2011 data) which is needed for access to and analysis of CMS Research level data."

- Go to ["Start analysing the data"](http://opendata-dev.web.cern.ch/articles/getting-started-with-cms-open-data), and
- choose "2011" (default) or "2010".

**Note**: The 2010 (SL5) virtual machine will only work on 2010 data with CMSSW 4-2-8. The 2011 (SL6) virtual machine will only work on 2011 data and MC with CMSSW 5-3-32.

<center>–––</center>

> "I want to produce some example physics distributions (e.g. inclusive di-muon spectrum analysis example directly from AOD or two-/four-lepton analysis example with intermediate ntuples)."

- Install the CMS software as in the previous item (for 2010 or 2011).
- Follow options A (di-muon spectrum, simpler) or B (two-/four-lepton example, more sophisticated). For 2011 option A, take the SingleMu or DoubleMu dataset index files from [http://opendata.cern.ch/record/32](http://opendata.cern.ch/record/32) or [http://opendata.cern.ch/record/17](http://opendata.cern.ch/record/17).

---

#### Exploring the 2010 datasets

> "I want to find out which 2010 datasets exist, and how to get a feel for their content."

- Go to 2010 CMS primary datasets,
- choose a dataset, and read the comments.

<center>–––</center>

> "I also want to view some corresponding event displays."

- Go to 2010 CMS derived datasets,
- choose `Event display file derived from`… + the name of the CMS primary dataset you want (ZeroBias is known to be essentially empty).

<center>–––</center>

> "I want an alternative way to view these event displays."

- Load the [CMS event display](http://opendata-dev.web.cern.ch/visualise/events/CMS),
- choose `Open File` &rarr; `Open Files from Web` &rarr; `2010`, and
- choose your dataset.

<center>–––</center>

> "I want to find out which 2010 dataset and/or analysis/validation example is most useful for my purpose."

- To learn how to do a muon analysis, follow "*I want to produce some first physics distributions*," (above) with either option A (recommended) or B, or try one of the relevant "*I want to (re)validate the 2010 datasets examples*," (further below).
- To learn how to do an electron analysis, follow "*I want to produce some first physics distributions*," (above) with option B, or try one of the relevant "*I want to (re)validate the 2010 datasets examples*," (below).
- To learn how to do a minimum-bias track analysis, try the MinimumBias example on "*I want to (re)validate the 2010 datasets*," (below).
- [More to come…]

---

#### Exploring the 2011 datasets

> "I want to find out which 2011 data and MC sets exist, and how to get a feel for their content."

- Go to 2011 CMS primary datasets or 2011 CMS simulated datasets,
- choose a dataset, and read the comments.

<center>–––</center>

> "I also want to  to view some corresponding event displays."

- These are available for data only for the time being.
- Go to 2011 CMS derived datasets,
- choose `Event display file derived from`… + the name of the CMS primary dataset you want (ZeroBias is known to be essentially empty).

<center>–––</center>

> "I want an alternative way to view these event displays."

- Load the [CMS event display](http://opendata-dev.web.cern.ch/visualise/events/CMS),
- choose `Open File` &rarr; `Open Files from Web` &rarr; `2011`, and
- choose your dataset.

<center>–––</center>

> "I want to find out which 2011 dataset and/or analysis/validation example is most useful for my purpose."

- Dedicated examples for 2011 beyond those available in "Getting Started" are [in preparation](https://github.com/cms-opendata-validation) to be added to the portal, including jet and top cross-sections. Alternatively, start from a 2010 example and adjust to run on 2011 data.

<center>–––</center>

- For more information on Monte Carlo, see below.

---

#### Trigger information, condition data, luminosity

> "I want to find out how to use the trigger and trigger prescale information in the dataset I am interested in."

- Go to CMS Trigger Information (currently for 2011 only).
- This information is still very basic, and will be improved.

<center>–––</center>

> "I want to find out how to access the luminosity information for the dataset I am interested in and how to select "good data" only."

- Check the [luminosity record](/record/1051), and
- check the [JSON description](/record/1000).

<center>–––</center>

> "I want to find out whether I need condition data base information, and if so, how to access it."

- Condition data are needed only on sophisticated examples using e.g. jet energy corrections (many of the simpler analysis/validation examples documented here do not use this).
- Using condition data significantly slows down data access, so use them only if really needed. If so:
    - go to CMS Condition Data for basic information (in contrast to what is stated there, they are NOT needed to run CERNVM in general, only to perform sophisticated tasks).
- This information is still very basic and will be improved.

<center>–––</center>

> "I want to find the luminosity of my dataset, possibly constrained by using specific triggers."

- Please check [CMS luminosity information](/record/1051),
- decide on the triggers you want to use,
- find out the runs/lumi sections in which these triggers were active and whether they were prescaled,
- overlap with the available CMS Open Data samples (run range) and with the JSON data-quality selection.
    - If not prescaled, sum up the luminosity for the surviving runs/lumi sections.
    - If prescaled, life is more complicated…

---

#### Performing an analysis

> "I want to find more CMS software and data format documentation from public sources."

- This is strongly recommended for serious analysis, but is hard to navigate!
- Check the [CMS public Twiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WebHome) or the CMS Fermilab website or use your favourite web-search engine.

<center>–––</center>

> "I want to use the public analysis example from the MIT jet-analysis group's papers."

- See *Jet Substructure Studies with CMS Open Data*, A. Tripathee et al., Apr 19, 2017, MIT-CTP-4890, [arXiv:1704.05842](https://inspirehep.net/record/1593756),
- and *Exposing the QCD Splitting Function with CMS Open Data*, A. Larkoski et al., Apr 17, 2017, MIT-CTP-4891, [arXiv:1704.05066](https://inspirehep.net/record/1591972).

<center>–––</center>

> "I want to (re)validate the 2010 datasets within my setup…"

- … for the MinimumBias, Commissioning, Mu or MuMonitor datasets:
    - Go to 2010 Validation Utilities,
    - choose and execute the corresponding Validation code.

- … for the Multijet dataset (see also [here](http://hep.caltech.edu/cms/opendata/)):
    - Go to 2010 CMS Tools,
    - choose and execute `Razor filter and analyzer for SUSY searches`.

- … for the Electron (or Mu) dataset:
    - Go to 2010 CMS Tools,
    - choose and execute `Software to preprocess the CMS 2010 Muon and Electron datasets for the two-lepton/four-lepton analysis example of CMS open data`, then
    - choose `Two-lepton/four-lepton analysis example of CMS 2010 open data` and compare PAT-tuples from the previous to those linked therein, or execute it on your new PAT tuples.

- … for the ZeroBias dataset:
    - Not useful, no validation needed.

- … for the Jet, MuOnia, BTau, Photon, JetMETTaumonitor, METFwd datasets:
    - Validation not yet available (partially in preparation).

<center>–––</center>

> "I want to backup my code, or import some external code."

- We recommend you use `scp` from and to your host from within the VM.

---

#### Monte Carlo

> "How do I interpret the MC set names?"

- Check [CMS Simulated Dataset Names](http://opendata.cern.ch/about/CMS-Simulated-Dataset-Names).

<center>–––</center>

> "I want to find the effective luminosity of my MC set."

- To be documented.
- Generically: divide MC cross-section (next item) times matching efficiency times filter efficiency by the number of events.

> "I want to find the generator cross section of a particular MC set."

- To be documented.
- On some MC sets, the following might work (reliability of information not guaranteed): open the ROOT file, create TBrowser and navigate to `Runs` &rarr; `GenRunInfoProduct_generator__SIM.` &rarr; `GenRunInfoProduct_generator__SIM.obj` &rarr; `InternalXSec` &rarr; `value_`.

---

### Further information / Contact us

> I want information that is not documented here and elsewhere on the [CERN Open Data portal](http://opendata.cern.ch/).

- Kindly contact &lt;[opendata-support@cern.ch](mailto:opendata-support@cern.ch)&gt;

> "I ran into a problem and need help!"

- Please check our page related to known errors.
