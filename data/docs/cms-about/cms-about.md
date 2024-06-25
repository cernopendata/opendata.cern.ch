The Compact Muon Solenoid (CMS) is one of the large particle detectors at CERN's Large Hadron Collider. The CMS Collaboration consists of more than 4000 scientists, engineers, technicians and students from around 240 institutes and universities from more than 50 countries. You can find more information about the CMS [detector](https://cms.cern/detector) on the official [CMS website](https://cms.cern).

You can find usage instructions and suggestions of CMS Open Data for different scopes in:

* [Guide page to education use of CMS Open Data](/docs/cms-guide-for-education)
* [Guide page to research use of CMS Open Data](/docs/cms-guide-for-research) and a separate [CMS Open Data guide](https://cms-opendata-guide.web.cern.ch/).

This page gives a brief overview of CMS Open Data contents:

- [<a name="cms-data">CMS Data and analysis tools</a>](#cms-data-and-analysis-tools)
- [<a name="primary">Primary and simulated datasets</a>](#primary-and-simulated-datasets)
- [<a name="disclaimer">Disclaimer</a>](#disclaimer)
- [<a name="other">Other CMS open data</a>](#other-cms-open-data)
- [<a name="policies">Policies</a>](#policies)

## <a name="cms-data">CMS Data and analysis tools</a>

The following are provided through this portal:

* Downloadable datasets
    * [Primary datasets](/search?page=1&size=20&subtype=Collision&type=Dataset&experiment=CMS): full reconstructed collision data with no other selections. The data here are referred to as "reconstructed data"; fragmented data from various sub-detectors are processed or "reconstructed" to provide coherent information about individual [physics objects](/docs/cms-physics-objects-2015) such as electrons or particle jets.
    * [Simulation data](/search?page=1&size=20&subtype=Simulated&type=Dataset&experiment=CMS)
    * Examples of [simplified datasets](/search?page=1&size=20&subtype=Derived&type=Dataset&experiment=CMS) derived from the primary ones for use in different applications and analyses
* Tools
    * Downloadable [container images](/docs/cms-guide-docker) with the CMS software environment through which the datasets can be accessed
    * Alternatively, a downloadable [Virtual Machine (VM)](https://opendata.cern.ch/search?page=1&size=20&tags=VM&experiment=CMS) image with the CMS software environment
    * Getting started instructions for reading and processing primary data in the [AOD format (Run 1)](/docs/cms-getting-started-aod), [MiniAOD format (Run 2)](/docs/cms-getting-started-miniaod), or [NanoAOD format (Run 2)](/docs/cms-getting-started-nanoaod).
    * Ready-to-use online applications, such as [an event display](/visualise/events/cms) and [simple histogramming software](/visualise/histograms/cms)
    * Source code for the various examples and applications, available in the [CMS software](/search?page=1&size=20&q=&type=Software&experiment=CMS) collection
* Guides
    * Set of [topical guide pages](http://opendata.cern.ch/search?page=1&size=20&q=&subtype=Guide&type=Documentation&experiment=CMS)
    * A omprehensive set of instructions is being collected in a separate [CMS Open Data guide](https://cms-opendata-guide.web.cern.ch/) with links to the latest tutorials.

## <a name="primary">Primary and simulated datasets</a>

Collision data in the primary datasets are typically in a format known as AOD or Analysis Object Data, while simulated data are in a format called AODSIM. Beginning in Run 2, smaller
data formats called MiniAOD and NanoAOD were developed in CMS to implement common physics object processing and remove information that not often needed for analysis.

**AOD(SIM) and MiniAOD(SIM) files**

AOD/AODSIM files are provided for Run 1 primary datasets and contain the information that is needed for analysis:

* all the high-level [physics objects](/docs/cms-physics-objects-2015) (such as muons, electrons, etc.);
* tracks with associated hits, calorimetric clusters with associated hits, vertices;
* candidate particles created by the Particle Flow algorithm;
* information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.

See the [Getting Started page for AOD data](/docs/cms-getting-started-aod) to learn more about analyzing AOD files.

Starting from Run 2 (2015), MiniAOD/MiniAODSIM files are provided. These files contain similar information to AOD, but physics objects are processed to include more
identification and selection information within a lighter C++ object, transverse momentum thresholds for storing objects are increased,
and some lower-level information has been removed.
MiniAOD datasets are appoximately one tenth of the size of AOD datasets. More information about MiniAOD:

* [Mini-AOD: A New Analysis Data Format for CMS](https://doi.org/10.1088/1742-6596/664/7/072052)
* [MiniAOD analysis documentation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015)
* [Getting Started with CMS MiniAOD data](/docs/cms-getting-started-miniaod)

AOD and MiniAOD files do not contain the final event interpretation with a simple list of particles.
The files can be read in [ROOT](http://root.cern.ch/), but they cannot be opened (and understood) as simple data tables.
A file typically contains several instances of the same physics object
(i.e. a jet reconstructed with different algorithms), and some physics objects may be "double-counted" (i.e. a physics object may appear as a single object of its own type, but
it may also be part of a jet).

Additional knowledge is needed to define a "good" physics object, and this definition can be different in each analysis.
Only the runs that are validated by data quality monitoring should be used in any analysis.
The [list of the validated runs](/search?page=1&size=20&q=&type=Environment&subtype=Validation) is provided.

**NanoAOD(SIM) files**

Starting from data collected in 2016, datasets in NanoAOD format are provided alongside MiniAOD.
Only a limited set of observables for each physics object is kept, with limited numerical precision.
For example, detector information is typically dropped in favor of pre-computed identification algorithm results.
The Particle Flow candidates are also dropped, since they are primarily used as inputs to higher-level physics object
reconstruction. The NanoAOD format is about 20 times smaller than MiniAOD, or about 200 times smaller than AOD.
NanoAOD files can be read in [ROOT](http://root.cern.ch) as a basic `TTree` containing standard data types.
More information about NanoAOD:

* [The NanoAOD event data format in CMS](https://doi.org/10.1088/1742-6596/1525/1/012038)
* [NanoAOD file documentation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD)
* [Getting Started with CMS NanoAOD data](/docs/cms-getting-started-nanoaod)

NanoAOD files may still contain several instances of the same physics object
(i.e. a jet reconstructed with different algorithms), and some physics objects may be "double-counted" (i.e. a physics object may appear as a single object of its own type, but
it may also be part of a jet).

Additional knowledge is needed to define a "good" physics object, and this definition can be different in each analysis.
Only the runs that are validated by data quality monitoring should be used in any analysis.
The [list of the validated runs](/search?page=1&size=20&q=&type=Environment&subtype=Validation) is provided.

**RECO files**

Some datasets, such as those containing heavy-ion data, are provided in a format called RECO, which contains more information than the AOD format.
This is done when the original analyses by the CMS collaboration were performed using this particular format.

**Raw data**

Small samples of [raw data](/search?page=1&size=20&q=&experiment=CMS&file_type=raw) are also provided.

## <a name="disclaimer">Disclaimer</a>

* The open data are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/). Neither CMS nor CERN endorses any works, scientific or otherwise, produced using these data, even if available on, or linked from, this portal.
* All datasets will have a unique DOI that you are requested to cite in any applications or publications.
* Despite being processed, the high-level primary datasets remain complex and selection criteria need to be applied in order to analyse them, requiring some understanding of particle physics and detector functioning. The data cannot be viewed in simple data tables for spreadsheet-based analyses.
* No further development is foreseen for either the data released or the software version needed to analyse them.
    * The methods have evolved since the released data were recorded.
    * More advanced techniques are used with recent data but the software is not compatible out-of-the-box with older data samples.
* The simulated data are not a full set of simulations, but only those datasets that have been reprocessed with a software release compatible with the respective collision data.
    * The release of 2010 data is accompanied by a small set of simulated data.
    * The release of 2011 data includes some simulated data, limited to those datasets that were reprocessed with a software release compatible with the 2012 collision data.
    * The release of 2012 data includes a larger sample of simulated data. A part of 2012 simulated data is released with the bibliographic information content only, and these datasets will be made available online on demand.
    * The release of 2013 heavy-ion-related data includes simulated data corresponding to different collision types and centre-of mass energies.
    * The release of 2015 data includes a large collection of simulated data, reprocessed with a software release compatible with the 2015 collision data, but it may still happen that some simulated data did not make it to this reprocessing and are therefore not available in this collection.
    * The release of 2016 data includes a large collection of simulated data, reprocessed with a software release compatible with the 2016 collision data.
* If you are interested in joining the CMS Collaboration, please read [How to join CMS](https://cms.cern/collaboration/how-join-cms).

## <a name="other">Other CMS open data</a>

* All [CMS publications](https://cms-results-search.web.cern.ch/) are open access.
* [Some of the papers also include open data](https://www.hepdata.net/search/?q=&collaboration=CMS) in the form of additional tables, plots, graphs and [Rivet](https://rivet.hepforge.org/) packages.

## <a name="policies">Policies</a>

* [Data preservation and open access policy](/record/415)
* [Papers by CMS members using public data [internal]](https://cms-docdb.cern.ch/cgi-bin/DocDB/ShowDocument?docid=14372)