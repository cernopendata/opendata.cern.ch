The CERN Open Data portal is the access point to a growing range of data produced through the research performed at CERN. It disseminates the preserved output from various research activities, including accompanying software and documentation which is needed to understand and analyse the data being shared.

The portal adheres to established global standards in data preservation and Open Science: the products are shared under open licenses; they are issued with a digital object identifier (DOI) to make them citable objects in the scientific discourse (see details below on how to do this).

## Data and re-use

### LHC Data

Data produced by the LHC experiments are usually categorised in four different levels ([DPHEP Study Group (2009)](http://arxiv.org/abs/0912.0255)). The Open Data portal focuses on the release of data from level 2 and 3.

*   Level 1 data comprises data that is directly related to publications which provide documentation for the published results
*   Level 2 data includes simplified data formats for analysis in outreach and training exercises
*   Level 3 data comprises reconstructed data and simulations as well as the analysis level software to allow a full scientific analysis
*   Level 4 covers basic raw level data (if not yet covered as level 3 data) and their associated software and allows access to the full potential of the experimental data


### Data Policies

All four LHC experiments have approved data preservation and access policies which state that they will make their data (except level 4 data) available. New data will enter the portal once the embargo periods for them are over. For detailed information regarding embargo periods, accessibility and preservation of LHC data, please refer to the experiments data policies.

In support of these data policies, this portal publishes and preserves data from level 2 and 3, such as simplified formats and fully reconstructed events, together with associated software and documentation needed to access and use the data.

### How to re-use and cite these datasets

All datasets and other material available in this portal are minted with a persistent identifier, a so called DOI (Digital Object Identifier) that allows permanent linking to the records. The CERN Open Data Portal endorses the [FORCE 11 Joint Declaration of Data Citation](http://www.force11.org/datacitation) Principles. Thus, we ask you to cite the data provided in the portal when you re-use them. To make this easier for you, we provide you with a citation recommendation for every dataset as well as output formats (e.g. BibTex) for common reference programs. Citing datasets in the reference list of your paper will allow other platforms such as INSPIRE to track citations to these datasets and measure their impact.

## Technologies

This portal is built around the following technologies:

### [![](/static/img/invenio.png)](http://inveniosoftware.org)


Invenio is a free software suite enabling you to run your own digital library or document repository on the web. The technology offered by the software covers all aspects of digital library management, from document ingestion through classification, indexing, and curation up to document dissemination. Invenio complies with standards such as the Open Archives Initiative and uses MARC 21 as its underlying bibliographic format. The flexibility and performance of Invenio make it a comprehensive solution for management of document repositories of moderate to large sizes.

### [![](/static/img/cernvm.png)](http://cernvm.cern.ch/)

<div class="card-body">

CernVM is a baseline Virtual Software Appliance for the participants of CERN LHC experiments. The Appliance represents a complete, portable and easy to configure user environment for developing and running LHC data analysis locally and on institutional and commercial clouds (OpenStack, Amazon EC2, Google Compute Engine), independently of Operating System software and hardware platform (Linux, Windows, MacOS). The goal is to remove a need for the installation of the experiment software and to minimise the number of platforms (compiler-OS combinations) on which experiment software needs to be supported and tested.

### [![](/static/img/eos_cern.gif)](http://eos.cern.ch)

EOS is a disk-based service providing a low latency storage infrastructure for physics users. EOS provides a highly-scalable hierarchical namespace implementation. Data access is provided by the XROOT protocol.

The main target area for the service are physics data analysis use often cases characterised by many concurrent users, a significant fraction random data access and a large file open rate.

### Impressum

The portal is a collaborative effort of the CERN groups IT-CIS and RCS-SIS in collaboration with many researchers in the High-Energy Physics community. If you want to contact us for any request or submission please send us an email to [opendata-support@cern.ch](mailto:opendata-support@cern.ch)
