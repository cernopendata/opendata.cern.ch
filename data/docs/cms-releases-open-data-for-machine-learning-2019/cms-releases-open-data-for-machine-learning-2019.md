The [CMS Collaboration at CERN](https://cms.cern/) is happy to announce the release of its fourth batch of open data to the public. With this release, which brings the volume of its open data to more than 2 PB (or two million GB), CMS has now provided open access to 100% of its research data recorded in proton-proton collisions in 2010, in line with the collaboration’s data-release policy. The release also includes several new data and simulation samples. The new release builds upon and expands the scope of the successful use of CMS open data in research and in education.

<center>
<img src="/static/docs/cms-releases-open-data-for-machine-learning-2019/cms-machine-learning-2019-01-28.jpg" width="55%" align="middle">
<br><em>(Image: Fermilab/CERN.)</em>
</center>

In this release, CMS open data address the ever-growing application of machine learning (ML) to challenges in high-energy physics. According to [a recent paper](https://arxiv.org/abs/1807.02876), collaboration with the data-science and ML community is considered a high-priority to help advance the application of state-of-the-art algorithms in particle physics.  CMS has therefore also made available samples that can help foster such collaboration.

“Modern machine learning is having a transformative impact on collider physics, from event reconstruction and detector simulation to searches for new physics,” remarks Jesse Thaler, an Associate Professor at MIT, who is working on ML using CMS open data with two doctoral students, Patrick Komiske and Eric Metodiev. “The performance of machine-learning techniques, however, is directly tied to the quality of the underlying training data. With the extra information provided in the latest data release from CMS, outside users can now investigate novel strategies on fully realistic samples, which will likely lead to exciting advances in collider data analysis.”

The ML datasets, derived from millions of CMS simulation events for previous and future runs of the Large Hadron Collider, focus on solving a number of representative challenges for particle identification, tracking and distinguishing between multiple collisions that occur in each crossing of proton bunches. All the datasets come with extensive documentation on what they contain, how to use them and how to reproduce them with modified content.

In its policy on data preservation and open access, CMS commits to releasing 100% of its analysable data within ten years of collecting them. Around half of proton-proton collision data collected at 7 TeV center-of-mass in 2010 were released in the first CMS release in 2014, and the remaining data are included in this new release. In addition, a small sample of unprocessed raw data from LHC’s Run 1 (2010 to 2012) are also released. These samples will help test the chain for processing CMS data using the legacy software environment.

Reconstructed data and simulations from the CASTOR calorimeter, which was used by CMS in 2010, are also available and represent the first release of data from the very-forward region of CMS. Finally, CMS has released instructions and examples on how to generate simulated events and how to analyse data in isolated “containers”, within which one has access to the CMS software environment required for specific datasets. It is also easier to search through the simulated data and to discover the provenance of datasets.

As before, the data are released into the public domain under the [Creative Commons CC0](https://creativecommons.org/publicdomain/zero/1.0/) waiver via the [CERN Open Data portal](http://opendata.cern.ch/). The portal is [openly developed on GitHub]((https://github.com/cernopendata/opendata.cern.ch/)) by the [CERN Information Technology](http://information-technology.web.cern.ch/) team in cooperation with the experimental collaborations. CMS would like to thank CERN for providing resources and expertise to build and maintain the portal. We would also like to acknowledge the support of many of our collaboration members who have helped us release this latest batch of CMS open data.

---

This announcement was originally published on the [CMS](http://cms.cern/news/cms-releases-open-data-machine-learning) and [CERN](https://home.cern/news/news/knowledge-sharing/cms-releases-open-data-machine-learning) news websites.

---

**Release highlights**

- This is the fourth release of high-level CMS open data, following release of around 50% of data from the LHC's Run 1: 2010 data in 2014, 2011 data in 2016, and 2012 data in 2017. This brings the volume of CMS open data to more than 2 PB.
- The release includes [datasets](http://opendata.cern.ch/search?page=1&size=20&keywords=datascience&experiment=CMS&type=Dataset) prepared specifically for use in Machine Learning or in data science
    - A dataset derived from Run 2 simulation data is devoted to the challenge of [event and object tagging in events with two b quarks produced from the decay of a Higgs boson](http://opendata.cern.ch/record/12102). It is particularly difficult to distinguish this Higgs signal channel from the background.
    - Further datasets derived from Run 1 and Run 2 simulated data are devoted to [identifying top quarks produced in events](http://opendata.cern.ch/record/12220) and to [studying the flavour content of jets](http://opendata.cern.ch/record/12100).
    - Another dataset is devoted to the challenge of [particle tracking in the future era of high-luminosity collisions](http://opendata.cern.ch/record/12320) and is derived from simulations of collisions in the tracker after Phase 2 upgrades
- The [parent datasets and production workflows](http://opendata.cern.ch/search?page=1&size=20&keywords=datascience&experiment=CMS&type=Software) for the ML samples also available for full reproducibility.
    - These include the first [simulation samples in the "MiniAODSIM" format](http://opendata.cern.ch/search?page=1&size=20&type=Dataset&file_type=miniaodsim) in use in Run 2 data analysis.
- Small [samples of raw data](http://opendata.cern.ch/search?page=1&size=20&type=Dataset&file_type=raw) are released, useful for testing of the data-processing chain and eventually reconstruction-algorithm development.
- Instructions are now available on [how to generate simulated events](http://opendata.cern.ch/docs/cms-guide-event-production) in the open data environment.
- The release completes the 2010 data release with now [all proton-proton data](http://opendata.cern.ch/search?page=1&size=20&q=&subtype=Collision&type=Dataset&experiment=CMS&year=2010) available publicly and adds [some simulated data](http://opendata.cern.ch/search?page=1&size=20&q=&subtype=Simulated&type=Dataset&experiment=CMS&year=2010&file_type=aodsim) also for 2010 data taking.
- Contains datasets from [early commissioning runs](http://opendata.cern.ch/search?page=1&size=20&q=&subtype=Collision&type=Dataset&experiment=CMS&year=2010&file_type=reco) used in studies with CASTOR calorimeter and [corresponding simulations](http://opendata.cern.ch/search?page=1&size=20&q=&subtype=Simulated&type=Dataset&experiment=CMS&year=2010&file_type=gen-sim-reco).
- In addition to already available 2012 simulation data, large amount of 2012 simulation data of rarely used processes is now available [on demand](http://opendata.cern.ch/search?page=1&size=20&type=Dataset&experiment=CMS&year=2012&ondemand=True&subtype=Simulated).
- Search functionalitiy for simulation data is now available based on [physics processes](http://opendata.cern.ch/docs/simulated-dataset-categories)
- Provenance information display for simulation data has been improved.
- New examples of [simplified datasets](http://opendata.cern.ch/record/12341) and [code to analyse them](http://opendata.cern.ch/record/12342) are made available
- Instructions are provided on [how to run open data analysis on a container](http://opendata.cern.ch/docs/cms-guide-docker).
