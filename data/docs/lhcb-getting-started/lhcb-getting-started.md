In 2022, LHCb has released the first 200 terabytes of the data via CERN OpenData Portal, making it available to the public.

- The data comes in `.DST` and `.MDST` format, the same format is used by LHCb internally.
- Every data set released is narrated by an "Open Data Record" accessible through Open Data Portal.
- Open Data Records contain various bits of information about the selected data set (this is called metadata). An example of the types of metadata provided in the record is:
  - Number of events in the dataset
  - Number of files in the dataset
  - Combined size in TB of the dataset
  - Production ID
  - Production Type
  - Detector conditions (condb, dddb tags)
  - List of Trigger Configuration Keys (TCKs)
  - Scripts used for each production step
  - List of Logical File Names (LFNs) on [LHCb DIRAC](https://lhcb-dirac.readthedocs.io/en/latest/).

The metadata provided should help the user to navigate, select and work with with LHCb Open Data.

Index of files is accessible both via a GUI or as a machine readable file.

- Some instructions on how to use open data are pointed out in the records themselves.
- As well as the data records, an extensive list of LHCb stripping lines and their descriptions is provided as well.
- After selecting the desired stream, a stripping line description can be followed to obtain a number of cuts/conditions which could be used to filter the data further.
- Data can be accessed directly (eg. using [xrootd](https://xrootd.slac.stanford.edu/) protocol) or downloaded locally.
- It is suggested to further filter and categorize the data by writing out smaller data files in `.root` format (called ntuples).
- This is done in LHCb with the help of software called [DaVinci](https://lhcbdoc.web.cern.ch/lhcbdoc/davinci/).
- 'DaVinci' and other LHCb Software is available through [CVMFS](https://cernvm.cern.ch/fs/).
- Some initial instructions on working with DaVinci are provided in [LHCb Starterkit](https://lhcb.github.io/starterkit-lessons/first-analysis-steps/minimal-dv-job.html) web page.
