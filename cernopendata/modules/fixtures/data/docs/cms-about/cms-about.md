The Compact Muon Solenoid (CMS) Experiment is one of the large particle detectors at CERN's Large Hadron Collider. The CMS Collaboration consists of more than 3000 scientists, engineers, technicians and students from 180+ institutes and universities from 40+ countries. You can find more information about the CMS [detector design](https://cms.cern/news/cms-detector-design) and [overview](https://cms.cern/news/detector-overview) on the official [CMS website](https://cms.cern).

You can find usage instructions and suggestions of CMS Open Data in two detailed guides:

* [Guide to education use of CMS Open Data](/docs/cms-guide-for-education)
* [Guide to research use of CMS Open Data](/docs/cms-guide-for-research).

This page gives a brief overview of CMS Open Data contents:

1. [CMS Data and analysis tools](#cms-data)
2. [Primary and simulated datasets](#primary)
3. [Disclaimer](#disclaimer)
4. [Other CMS open data](#other)
5. [Policies](#policies)

## <a name="cms-data">CMS Data and analysis tools</a>

The following are provided through this portal:

* Downloadable datasets
    * [Primary datasets](/search?page=1&size=20&subtype=Collision&type=Dataset&experiment=CMS): full reconstructed collision data with no other selections. The data here are referred to as "reconstructed data"; fragmented data from various sub-detectors are processed or "reconstructed" to provide coherent information about individual [physics objects](/docs/cms-physics-objects-2011) such as electrons or particle jets.
    * [Simulation data](/search?page=1&size=20&subtype=Simulated&type=Dataset&experiment=CMS)
    * Examples of [simplified datasets](/search?page=1&size=20&subtype=Derived&type=Dataset&experiment=CMS) derived from the primary ones for use in different applications and analyses
* Tools
    * A downloadable [Virtual Machine (VM)](/docs/cms-virtual-machine-2011) image with the CMS software environment through which the datasets can be accessed
    * An [analysis example chain](/docs/cms-getting-started-2011), reading the primary dataset and producing intermediate derived data for the final analysis
    * Ready-to-use online applications, such as [an event display](/visualise/events/cms) and [simple histogramming software](/visualise/histograms/cms)
    * Source code for the various examples and applications, available in the [CMS software](/search?page=1&size=20&q=&type=Software&experiment=CMS) collection

## <a name="primary">Primary and simulated datasets</a>

* Collision data in the primary datasets are in a format known as AOD or Analysis Object Data, while simulated data are in a format called AODSIM.
* AOD/AODSIM files contain the information that is needed for analysis:
    * all the high-level [physics objects](/docs/cms-physics-objects-2011) (such as muons, electrons, etc.);
    * tracks with associated hits, calorimetric clusters with associated hits, vertices; and
    * information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.
* The file is not the final event interpretation with a simple list of particles.
    * It contains several instances of the same physics object (i.e. a jet reconstructed with different algorithms).
    * It may have double-counting (i.e. a physics object may appear as a single object of its own type, but it may also be part of a jet).
    * Additional knowledge is needed to define a "good" physics object.
    * Definition of same objects is different in each analysis.
* Some simulated datasets are provided in the MiniAODSIM format, which is the format used in physics analysis starting from Run2 (2015):
    * MiniAOD/MiniAODSIM is approximately one tenth of the size of AOD/AODSIM.
    * The reduction is obtained defining light-weight physics-object candidate representations, increasing transverse momentum thresholds for storing physics-object candidates, and reduced numerical precision when it is not required at the analysis level.
    * More information on the MiniAOD format
        * [Mini-AOD: A New Analysis Data Format for CMS G Petrucciani, A Rizzi, C Vuosalo on behalf of the CMS Collaboration](https://doi.org/10.1088/1742-6596/664/7/072052)
        * [MiniAOD analysis documentation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016)
* The files can be read in [ROOT](http://root.cern.ch/), but they cannot be opened (and understood) as simple data tables.
* Only the runs that are validated by data quality monitoring should be used in any analysis. The [list of the validated runs](/search?page=1&size=20&q=&type=Environment&subtype=Validation) is provided.
* A small sample of [raw data](/search?page=1&size=20&q=&experiment=CMS&file_type=raw) is also provided.

## <a name="disclaimer">Disclaimer</a>

* The open data are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/). Neither CMS nor CERN endorses any works, scientific or otherwise, produced using these data, even if available on, or linked from, this portal.
* All datasets will have a unique DOI that you are requested to cite in any applications or publications.
* Despite being processed, the high-level primary datasets remain complex and selection criteria need to be applied in order to analyse them, requiring some understanding of particle physics and detector functioning. The data cannot be viewed in simple data tables for spreadsheet-based analyses.
* No further development is foreseen for either the data released or the software version needed to analyse them.
    * The methods have evolved since the released data were recorded.
    * More advanced techniques are used with recent data but the software is not compatible out-of-the-box with older data samples.
* The release of 2010 data is not accompanied by any simulated data. The release of 2011 data includes simulated data. However, this is not a full set of simulations, but only those datasets that have been reprocessed with a software release compatible with the 2011 collision data. The release of 2012 data includes a larger sample of simulated data.
* If you are interested in joining the CMS Collaboration, please contact nearest [CMS university/institute](https://cms.cern/content/cms-collaboration)

## <a name="other">Other CMS open data</a>

* All [CMS publications](http://cds.cern.ch/collection/CMS?ln=en) are open access.
* [Some of the papers also include open data](https://inspirehep.net/search?p=collaboration%3A%27CMS%27+and+520__9%3Ahepdata) in the form of additional tables, plots, graphs and [Rivet](https://rivet.hepforge.org/) packages.

## <a name="policies">Policies</a>

* [Data preservation and open access policy](/record/411)
* [Papers by CMS members using public data [internal]](https://cms-docdb.cern.ch/cgi-bin/DocDB/ShowDocument?docid=12242)
