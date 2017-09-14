
# About CMS

The Compact Muon Solenoid (CMS) Experiment is one of the large particle detectors at CERN's Large Hadron Collider. The CMS Collaboration consists of more than 3000 scientists, engineers, technicians and students from 180+ institutes and universities from 40+ countries. You can find more information about the CMS [detector design](http://cms.web.cern.ch/news/cms-detector-design) and [overview](http://cms.web.cern.ch/news/detector-overview) on the official [CMS website](http://cern.ch/cms)

<br>

# About CMS data

---

## Data and analysis tools

The following are provided through this portal:

* Downloadable datasets
    * [Primary datasets](/collection/CMS-Primary-Datasets): full reconstructed collision data with no other selections. The data here are referred to as "reconstructed data"; fragmented data from various sub-detectors are processed or "reconstructed" to provide coherent information about individual [physics objects](/about/CMS-Physics-Objects) such as electrons or particle jets.
    * [Simulation data](/collection/CMS-Simulated-Datasets) (for data from 2011)
    * Examples of [simplified datasets](/collection/CMS-Derived-Datasets) derived from the primary ones for use in different applications and analyses

<br>

* Tools
    * A downloadable [Virtual Machine (VM)](/VM/CMS) image with the CMS software environment through which the primary datasets can be accessed
    * An [analysis example chain](/getting-started/CMS), reading the primary dataset and producing intermediate derived data for the final analysis
    * Ready-to-use online applications, such as [an event display](/visualise/events/CMS) and [simple histogramming software](/visualise/histograms/CMS)
    * Source code for the various examples and applications, available in the [CMS Tools](/search?cc=CMS-Tools) collection

---

## Primary and simulated datasets

* Collision data in the primary datasets are in a format known as AOD or Analysis Object Data, while simulated data are in a format called AODSIM.
* AOD/AODSIM files contain the information that is needed for analysis:
    * all the high-level [physics objects](/about/CMS-Physics-Objects) (such as muons, electrons, etc.);
    * tracks with associated hits, calorimetric clusters with associated hits, vertices; and
    * information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.

<br>

* The file is not the final event interpretation with a simple list of particles.
    * It contains several instances of the same physics object (i.e. a jet reconstructed with different algorithms).
    * It may have double-counting (i.e. a physics object may appear as a single object of its own type, but it may also be part of a jet).
    * Additional knowledge is needed to define a "good" physics object.
    * Definition of same objects is different in each analysis.

* The files can be read in [ROOT](http://root.cern.ch/), but they cannot be opened (and understood) as simple data tables.
* Only the runs that are validated by data quality monitoring should be used in any analysis. The [list of the validated runs](/collection/CMS-Validation-Utilities) is provided.

---

## Disclaimer

* The open data are released under the [Creative Commons CC0 waiver](http://creativecommons.org/publicdomain/zero/1.0/). Neither CMS or nor CERN endorse any works, scientific or otherwise, produced using these data.
* All datasets will have a unique DOI that you are requested to cite in any applications or publications.</li>
* Despite being processed, the high-level primary datasets remain complex and selection criteria need to be applied in order to analyse them, requiring some understanding of particle physics and detector functioning. The data cannot be viewed in simple data tables for spreadsheet-based analyses.
* No further development is foreseen for either the data released or the software version needed to analyse them.
    * The methods have evolved since the released data were recorded.</li>
    * More advanced techniques are used with recent data but the software is not compatible out-of-the-box with older data samples.
* The release of 2010 data is not accompanied by any simulated data. The release of 2011 data includes simulated data. However, this is not a full set of simulations, but only those datasets that have been reprocessed with a software release compatible with the 2011 collision data.</li>
* If you are interested in more, please contact nearest [CMS university/institute](http://cms.web.cern.ch/content/cms-collaboration)

---

## Other CMS open data

* All [CMS publications](http://cds.cern.ch/collection/CMS?ln=en) are open access.
* [Some of the papers also include open data](https://inspirehep.net/search?p=collaboration%3A%27CMS%27+and+520__9%3Ahepdata) in the form of additional tables, plots, graphs and [Rivet]("https://rivet.hepforge.org/) packages.

---

## Policies

* [Data preservation and open access policy](https://cms-docdb.cern.ch/cgi-bin/PublicDocDB/ShowDocument?docid=6032)
* [Papers by CMS members using public data [internal]](https://cms-docdb.cern.ch/cgi-bin/DocDB/ShowDocument?docid=12242)
