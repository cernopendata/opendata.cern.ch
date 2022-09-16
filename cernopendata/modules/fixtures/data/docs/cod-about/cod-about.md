The CERN Open Data portal is the access point to a growing range of data produced through the research performed at CERN. It disseminates the preserved output from various research activities and includes accompanying software and documentation needed to understand and analyse the data.

The portal adheres to established global standards in data preservation and Open Science: the products are shared under open licenses; they are issued with a Digital Object Identifier (DOI) to make them citable objects.

## Data levels

Data produced by the LHC experiments are usually categorised in four different levels ([DPHEP Study Group (2009)](http://arxiv.org/abs/0912.0255)):

*   Level 1 data provides more information on published results in publications, such as extra figures and tables
*   Level 2 data includes simplified data formats for outreach and analysis training, such as basic four-vector event-level data
*   Level 3 data comprises reconstructed collision data and simulated data together with analysis-level experiment-specific software, allowing to perform complete full scientific analyses using existing reconstruction
*   Level 4 data covers basic raw data (if not yet covered as level 3 data) with accompanying reconstruction and simulation software, allowing the production of new simulated signals or even re-reconstruction of collision and simulated data

The CERN Open Data portal focuses on the release of event data from levels 2 and 3. The LHC collaborations may also provide small samples of level 4 data.

## Data policies

All four LHC experiments have approved data preservation and access policies which state that they will make their data available after a certain embargo period. For detailed information regarding embargo periods, accessibility and preservation of LHC data of various levels, please refer to the experiments [data policies](/search?page=1&size=20&q=&subtype=Policy&type=Documentation).

### How to re-use and cite these datasets

All datasets and other material available in this portal are minted with a persistent DOI identifiers that allow permanent linking to the records. The CERN Open Data portal endorses the [FORCE 11 Joint Declaration of Data Citation Principles](https://doi.org/10.25490/a97f-egyk). We thus ask you to cite the data provided on the portal when you reuse them. To make this easier for you, we provide you with a citation recommendation for every dataset as well as other suitable output formats (such as BibTeX). Citing datasets in the reference list of your paper will allow other platforms such as INSPIRE to track citations to these datasets and measure their impact.

## Technologies

This portal is built around the following technologies:

### [![](/static/img/invenio.png)](http://inveniosoftware.org)

Invenio is a digital repository framework that allows to build and run your own digital library, institutional repository, multimedia archive, or research data repository on the web. Invenio technology covers all aspects of digital repository management, from document ingestion through classification, indexing, and curation up to document dissemination. The flexible data model uses a custom JSON Schema to describe data assets. Invenio is a strong advocate of open standards.

### [![](/static/img/cernvm.png)](http://cernvm.cern.ch/)

CernVM is a baseline Virtual Software Appliance for the participants of LHC experiments. The Appliance represents a complete, portable and easy-to-configure user environment for developing and running LHC data analyses locally and on institutional and commercial clouds (OpenStack, Amazon EC2, Google Compute Engine), independently of Operating System platforms (Linux, Windows, macOS). The goal is to remove a need for the installation of the experiment software and to minimise the number of platforms (compiler-OS combinations) on which experiment software needs to be supported and tested.

### [![](/static/img/eos_cern.gif)](http://eos.cern.ch)

EOS is a disk-based service providing a low-latency storage infrastructure for physics users. EOS provides a highly-scalable hierarchical namespace implementation. Data access is provided by the XRootD protocol. The main target area for the service are physics data analysis use often cases characterised by many concurrent users, a significant fraction random data access and a large file open rate.

### Impressum

The CERN Open Data portal is developed by the CERN Information Technology group in close collaboration with LHC experiments and many researchers in the High-Energy Physics community. If you want to contact us for any request or submission, please send us an email to [opendata-support@cern.ch](mailto:opendata-support@cern.ch).
