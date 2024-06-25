If you are interested in step-by-step instructions to start working with CMS Open Data, please consult these pages:

* [Install Virtual Machine](https://opendata.cern.ch/search?q=&f=tags%3AVM&f=experiment%3ACMS&l=list&order=desc&p=1&s=10&sort=mostrecent) or [Use a container](/docs/cms-guide-docker)
* Getting started with CMS [AOD Data](/docs/cms-getting-started-aod), for data collected during Run 1 of the LHC.
* Getting started with CMS [MiniAOD Data](/docs/cms-getting-started-miniaod) or [NanoAOD Data](/docs/cms-getting-started-nanoaod), for data collected during Run 2 of the LHC.
* Getting started with CMS [Heavy Ion Data](/docs/cms-getting-started-hi-2013-2015).

This page offers hints, tips and guidance for conducting a research-oriented analysis using CMS Open Data. More detailed information can be found in the [CMS Open Data Guide](https://cms-opendata-guide.web.cern.ch/).

---

### Quick introduction

**I want to get a general introduction into HEP and CMS software and terminology, with a simplified event format.**

* Read the instructions related to our [educational content](/docs/cms-guide-for-education) and follow the corresponding exercises.

**I want to learn about the terms under which I can access and use the CMS Open Data, and publish results obtained from them.**

* Go to the ["Data preservation and open access policy"](/record/414) (if you are a CMS member, also see the internal document ["Rules for use of open access CMS data by individual members of CMS"](https://cms-docdb.cern.ch/cgi-bin/DocDB/ShowDocument?docid=12242)).

**I want to get inspiration for some potential physics topics.**

* See what others are doing with CMS Open Data! Papers citing DOI [10.7483/OPENDATA.CMS](https://inspirehep.net/literature?sort=mostrecent&size=25&page=1&q=references.reference.dois%3A10.7483%2FOPENDATA.CMS%2A) show a broad scope of usage for Open Data, including physics analyses, data science, and research tool development.

**I want to learn about the nature of the CMS physics objects and the corresponding variables and terminology.**

* Check out the ["CMS Open Data Guide"](https://cms-opendata-guide.web.cern.ch/) as well as the pages describing CMS Physics Objects for [2011-2012 data](/docs/cms-physics-objects-2011) and for [2015 data](/docs/cms-physics-objects-2015).

**I want to follow a set of detailed tutorials to learn how to analyze CMS Open Data.**

* Beginning in 2020, CMS has offered workshops targeting research use of Open Data. You can follow the lessons of previous workshops by [visiting this page](https://cms-opendata-guide.web.cern.ch/cmsOpenData/workshops/).

---

### Deciding which datasets to explore

CMS has released data proton collision data from Run 1 and Run 2, as well as heavy ion collision data from Run 1.

High-energy proton collisions:

<table class=\"ui table\">
  <thead>
    <tr>
      <th>Collisions</th>
      <th>Energy (TeV)</th>
      <th>Simulation</th>
      <th>Getting Started</th>
      <th>CMSSW version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2010&f=collision_energy%3A7TeV&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2010</a></td>
      <td>7</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2010&f=collision_energy%3A7TeV&l=list&order=desc&p=1&s=10&sort=mostrecent">2010 simulation</a></td>
      <td><a href="/docs/cms-getting-started-aod">AOD data</a></td>
      <td>CMSSW_4_2_8</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2011&f=collision_energy%3A7TeV&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2011</a></td>
      <td>7</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=collision_energy%3A7TeV&f=year%3A2011&l=list&order=desc&p=1&s=10&sort=mostrecent">2011 simulation</a></td>
      <td><a href="/docs/cms-getting-started-aod">AOD data</a></td>
      <td>CMSSW_5_3_32</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2012&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2012</a></td>
      <td>8</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2012&l=list&order=desc&p=1&s=10&sort=mostrecent">2012 simulation</a></td>
      <td><a href="/docs/cms-getting-started-aod">AOD data</a></td>
      <td>CMSSW_5_3_32</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2015&f=collision_energy%3A13TeV&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2015</a></td>
      <td>13</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2015&l=list&order=desc&p=1&s=10&sort=mostrecent">2015 simulation</a></td>
      <td><a href="/docs/cms-getting-started-miniaod">MiniAOD data</a></td>
      <td>CMSSW_7_6_7</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2016&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2016</a></td>
      <td>13</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2016&l=list&order=desc&p=1&s=10&sort=mostrecent">2016 simulation</a></td>
      <td><a href="/docs/cms-getting-started-miniaod">MiniAOD data</a><br><a href="/docs/cms-getting-started-nanoaod">NanoAOD data</a></td>
      <td>CMSSW_10_6_30<br>Not required</td>
    </tr>
  </tbody>
</table>

For Run 1 data, the 2010 datasets are smaller and offer a better environment for low-momentum, low-pileup studies. The 2011-2012 datasets are suitable for replicating CMS Run 1 physics results or performing new searches or studies at 7 - 8 TeV collision energy. Considering Run 2, the 2015 dataset is smaller than the 2011-2012 Run 1 datasets, but offered the first look at 13 TeV collisions and a much broader array of simulation. The 2016 13 TeV dataset (released as of 2024) has a similar luminosity to the Run 1 datasets, and offers a more advanced computing environment and new identification algorithms for Run 2. Information on the respective luminosities and pile-up rates vs time can be found in [public CMS luminosity information](https://twiki.cern.ch/twiki/bin/view/CMSPublic/LumiPublicResults#Multi_year_Collisions_Plots).

Heavy-ion program:

<table class=\"ui table\">
  <thead>
    <tr>
      <th>Collisions</th>
      <th>Energy (TeV)</th>
      <th>Simulation</th>
      <th>Getting Started</th>
      <th>CMSSW version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=collision_energy%3A2.76TeV&f=collision_type%3APbPb&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2010&l=list&order=desc&p=1&s=10&sort=mostrecent">lead-lead 2010</a></td>
      <td>2.76</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2013&f=collision_type%3APbPb&l=list&order=desc&p=1&s=10&sort=mostrecent">2010-2011 Pb-Pb simulation</a></td>
      <td><a href="https://opendata.cern.ch/record/466">Pb-Pb 2010</a></td>
      <td>CMSSW_3_9_2_patch5\*</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=collision_energy%3A2.76TeV&f=collision_type%3APbPb&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2011&l=list&order=desc&p=1&s=10&sort=mostrecent">lead-lead 2011</a></td>
      <td>2.76</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2013&f=collision_type%3APbPb&l=list&order=desc&p=1&s=10&sort=mostrecent">2010-2011 Pb-Pb simulation</a></td>
      <td><a href="https://opendata.cern.ch/record/467">Pb-Pb 2011</a></td>
      <td>CMSSW_4_4_7\*</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=year%3A2011&f=collision_energy%3A2.76TeV&f=collision_type%3App&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2011</a></td>
      <td>2.76</td>
      <td>N/A</td>
      <td><a href="https://opendata.cern.ch/record/467">Pb-Pb 2011</a></td>
      <td>CMSSW_4_4_7</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=collision_energy%3A2.76TeV&f=collision_type%3App&f=year%3A2013&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2013</a></td>
      <td>2.76</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2013&f=collision_type%3App&l=list&order=desc&p=1&s=10&sort=mostrecent">2013 p-p simulation</a></td>
      <td><a href="/docs/cms-getting-started-hi-2013-2015">p-Pb data</a></td>
      <td>CMSSW_5_3_20</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=collision_energy%3A5.02TeV&f=collision_type%3ApPb&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-lead 2013</a></td>
      <td>5.02</td>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ASimulated&f=year%3A2013&f=collision_type%3ApPb&l=list&order=desc&p=1&s=10&sort=mostrecent">2013 p-Pb simulation</a></td>
      <td><a href="/docs/cms-getting-started-hi-2013-2015">p-Pb data</a></td>
      <td>CMSSW_5_3_20</td>
    </tr>
    <tr>
      <td><a href="https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ADataset%2Bsubtype%3ACollision&f=collision_type%3App&f=collision_energy%3A5.02TeV&l=list&order=desc&p=1&s=10&sort=mostrecent">proton-proton 2015</a></td>
      <td>5.02</td>
      <td>N/A</td>
      <td><a href="/docs/cms-getting-started-hi-2013-2015">p-Pb data</a></td>
      <td>CMSSW_7_5_8_patch3</td>
    </tr>
  </tbody>
</table>

\* The Pb-Pb simulation linked in these rows was produced later and should be analyzed using CMSSW_5_3_20.

The Pb-Pb collisions from 2010 and 2011 are accompanied by "reference" proton-proton collisions at the same energy, collected during 2011 and 2013. The p-Pb collisions from 2013 are accompanied by referece proton-proton collisions collected during 2015. Some simulations have also been released that correspond to the heavy-ion collisions, as well as some of the reference collision data.

---

### Exploring event displays

Visualizing CMS events is a very helpful way to get acquainted with the CMS detector and the features of different datasets. [Software](https://opendata.cern.ch/search?q=event%20display&f=experiment%3ACMS&f=type%3ASoftware&l=list&order=asc&p=1&s=10&sort=bestmatch) is provided to produce event display files from the Run 1 datasets, but many events are already available in this format for viewing on the web:

* Load the [CMS event display](/visualise/events/cms),
* From the menu bar at the top, choose `Open File` &rarr; `Open Files from Web` &rarr; choose a year, and choose a dataset.
* Select a particular event from the list, and then other events can be explore using the arrow buttons in the menu bar.
* Various detector and/or physics features can be toggled on or off in the left-hand-side menu.

### Exploring example analyses

Example analyses help demonstrate how analysts can process CMS data files to accomplish a real physics goal. Examples range from data validation exercises to full searches. The "Getting Started" pages linked in the table able all offer links to example analyses.

* [2010 proton-proton examples](https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ASoftware&f=year%3A2010&l=list&order=desc&p=1&s=10&sort=mostrecent)
* [2011 proton-proton examples](https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ASoftware&f=year%3A2011&l=list&order=desc&p=1&s=10&sort=mostrecent)
* [2012 proton-proton examples](https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ASoftware&f=year%3A2012&l=list&order=desc&p=1&s=10&sort=mostrecent)
* [Run 2 proton-proton examples](https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ASoftware&f=year%3A2015&f=year%3A2016&f=year%3A2017&f=year%3A2018&f=year%3A2019&l=list&order=desc&p=1&s=10&sort=mostrecent)
* [Heavy Ion examples](https://opendata.cern.ch/search?q=&f=experiment%3ACMS&f=type%3ASoftware&f=keywords%3Aheavy-ion%20physics&l=list&order=desc&p=1&s=10&sort=mostrecent)

---

### Trigger information, condition data, luminosity

**I want to find out how to use the trigger and trigger prescale information in the dataset I am interested in.**

* Check [the guide to CMS trigger system](/docs/cms-guide-trigger-system).

**I want to find out how to access the luminosity information for the dataset I am interested in and how to select "good data" only.**

* Check the [CMS luminosity information for each year](/search?page=1&size=20&q=luminosity&type=Supplementaries&subtype=Luminosity), and
* check the [list of validated runs](/search?page=1&size=20&q=%22CMS%20list%20of%20validated%20runs%22).

**I want to find the luminosity of my dataset, possibly constrained by using specific triggers.**

* Check the [Guide to calculate luminosity](https://opendata.cern.ch/docs/cms-guide-luminosity-calculation)

**I want to find out whether I need condition data base information, and if so, how to access it.**

* Condition data are needed for examples using e.g. jet energy corrections and trigger configuration information, many of the simpler analysis examples do not need any additional corrections from the conditions database.
* The most recent CMSSW containers contain the conditions database information needed for the relevant year's data, and example analysis frameworks such as the [Physics Object Extractor Tool](https://opendata.cern.ch/search?q=PhysObjectExtractorTool&f=type%3ASoftware%2Bsubtype%3ATool&l=list&order=asc&p=1&s=10&sort=bestmatch) demonstrate how to access this information.
* More information is available in the ["Guide to the CMS condition database"](/docs/cms-guide-for-condition-database).

---

### Using simulation

**How do I interpret the simulated dataset names?**

* Check [CMS Simulated Dataset Names](/docs/cms-simulated-dataset-names).

**I want to find the generator cross section of a particular simulation.**

* Check [CMS Simulation cross sections](/docs/cms-guide-cross-sections).

**I want to find the effective luminosity of my simulated dataset.**

* Effective luminosity = (cross section) $\times$ (generator matching efficiency, if applicable) $\times$ (generator filter efficiency, if applicable) / (Number of positive-weight events - Number of negative-weight events).
* Find more information about using simulation in the [CMS Open Data Guide](https://cms-opendata-guide.web.cern.ch/analysis/backgrounds/).

---

### Contact us

**I want information that is not documented here and elsewhere on the [CERN Open Data portal](http://opendata.cern.ch/).**

* Please check the [CMS Open Data Guide](https://cms-opendata-guide.web.cern.ch).
* Kindly reach out on the [CERN Open Data Forum](https://opendata-forum.cern.ch/) and tag "CMS" in your message.

**I ran into a problem and need help!**

* Please check [our page related to known errors](/docs/cms-guide-troubleshooting).
* Kindly reach out on the [CERN Open Data Forum](https://opendata-forum.cern.ch/) and tag "CMS" in your message.