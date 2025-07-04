LHCb offers two means for exploring open data:

1. the [LHCb Ntupling
   Service](https://opendata-lhcb-ntupling-service.app.cern.ch/): a
   web service for on-demand production and publishing of custom LHCb
   open data. This amounts to over 4 PB of data to explore! For this
   option, users interact with ntuples, and no experiment specific
   software is needed.
2. The [Run 1 $pp$
   data](/search?q=&f=experiment%3ALHCb&f=type%3ADataset%2Bsubtype%3ACollision&f=file_type%3ADST&f=file_type%3AMDST&l=list&order=desc&p=1&s=10&sort=mostrecent)
   collected at LHCb is available on the CERN Open Data portal in DST format. For
   this option, users interact with DST files, and need to use LHCb specific
   software to create ntuples from the DST files.

The [LHCb Open Data Guide](https://lhcb-opendata-guide.web.cern.ch/)
provides a usage guide with examples for both of these options.

## LHCb Ntupling Service

<!-- markdownlint-disable MD033 -->
<p>
<div style="background-color: #d9edf7; color: #31708f; border: 1px solid
  #bce8f1; border-radius: 4px; padding: 15px;"> &#x25B6; Try the new <a
    href="https://opendata-lhcb-ntupling-service.app.cern.ch/" style="color:
    #245269; font-weight: bold;">LHCb Ntupling Service</a>, allowing for custom
  ntuple creation and exploration of more than 4 PB of pp data!
</div>
</p>
<!-- markdownlint-enable MD033 -->

In 2026, LHCb released the [LHCb Ntupling
Service](https://opendata-lhcb-ntupling-service.app.cern.ch/),
providing the public access to both Run 1, and for the first time, Run
2 $pp$ data collected by LHCb. This release marks a significant
advancement in the LHCb open data infrastructure, and is an exciting
step for the larger open data community, where the barrier for entry
of data analysis is lowered without the need for any experiment
specific software. Instead, custom ntuples are produced containing a
collection of physics objects and quantities based on user
specifications. The Ntupling Service serves as an all in one place for
users to request custom ntuples with LHCb data, track the request
process, communicate with the LHCb open data team, and download the
resulting ntuples.

The [Ntupling
Service](https://lhcb-opendata-guide.web.cern.ch/ntupling-service/) chapter of
the LHCb Open Data Guide contains a detailed walkthrough for request submission
and tracking, in addition to a growing list of analysis example workflows with
the resulting ntuples.

## Run 1 DSTs

By the end of 2023, LHCb released all of its Run I data, via CERN Open
Data Portal, to the general public. The data comes in `.DST` and
`.MDST` format which is the same format used by LHCb internally.

Every data set released is narrated by an "Open Data Record" accessible through
the CERN Open Data portal. Open Data Records contain various bits of
information about the selected data set (this is called metadata). An example
of the types of metadata provided in the record is:

- Number of events in the dataset
- Number of files in the dataset
- Combined size in TB of the dataset
- Production ID
- Production Type
- Detector conditions (condb, dddb tags)
- List of Trigger Configuration Keys (TCKs)
- Scripts used for each production step
- List of Logical File Names (LFNs) on [LHCb
  DIRAC](https://lhcb-dirac.readthedocs.io/en/latest/)

The [Analyzing Run 1 LHCb Open
Data](https://lhcb-opendata-guide.web.cern.ch/run1-dsts-odp/) chapter of the
LHCb Open Data Guide and the metadata provided on the Open Data Portal should
help the user to navigate, select, and work with LHCb Open Data.
