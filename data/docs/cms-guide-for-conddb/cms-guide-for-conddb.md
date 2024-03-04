1. [What is the condition database?](#what)
2. [When is the condition database needed?](#when)
3. [How is the condition database accessed?](#how)
    1. [Accessing condition data from the CMS Open Data VM image](#vm)
    2. [Accessing condition data from the CMS Open Data containers](#containers)
4. [Global tags](#global-tags)
    1. [Proton-proton data](#proton-proton)
    2. [Heavy-ion related data](#heavy-ion)

## <a name="what">What is the condition database?</a>

This page explains the use of global tags and the condition database with the CMS Open Data.

A global tag is a coherent collection of records of additional data needed by the reconstruction and analysis software. The global tag is defined for each data-taking period, separately for collision and simulated data. These records are stored in the condition database. Condition data include non-event-related information (Alignment, Calibration, Temperature, etc.) and parameters for the simulation/reconstruction/analysis software.

## <a name="when">When is the condition database needed?</a>

Most [AOD](/docs/cms-physics-objects-2011) and [MINIAOD](/docs/cms-physics-objects-2015) physics objects in the CMS Open Data are already calibrated and ready-to-use, and no additional corrections are needed other than selection and identification criteria, which will be applied in the analysis code. Therefore, simple analyses do not need to access the condition database. Examples of such analyses are [the di-muon spectrum example](/record/5001) or [the Higgs analysis example](/record/5500).

However, access to the condition database is necessary, for example, for jet energy corrections, b-tagging variables and trigger configuration information. Examples of such analyses are the jet energy correction (JEC) reading in ["Physics Object Extractor Tool (POET)"](https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/tree/2012) or getting [the trigger information](/record/5004).

## <a name="how">How is the condition database accessed?</a>

For CMS Open Data, the condition data are provided as sqlite files in the `/cvmfs/cms-opendata-conddb.cern.ch/` file system and, if needed, are available for download from the [corresponding records](/search?page=1&size=20&q=&experiment=CMS&subtype=Condition&type=Environment) on this portal. The access to the CMS condition data depends whether you are using the CMS Open Data [VM](/docs/cms-virtual-machine-2015) or [containers](/docs/cms-guide-docker).

In both cases, the following lines are needed in the CMSSW analysis job configuration file to access the condition database:

```shell
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = '<GLOBAL TAG>'
```

Replace `<GLOBAL TAG>` with the global tag to be used in analysis indicated in each dataset record. They are listed below for all data-taking periods.

### <a name="vm">Accessing condition data from the CMS Open Data VM image</a>

The `/cvmfs/cms-opendata-conddb.cern.ch/` file system is available through the CMS Open Data VM. To make sure that it is accessible before you start a job, do the following

```shell
ls -l
ls -l /cvmfs/
```

Connect to this database area by adding the following to the job configuration file:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/<DATABASE NAME')
process.GlobalTag.globaltag = '<GLOBAL TAG>'
```

Replace `<DATABASE NAME>` with the database name given in the instructions below, and `<GLOBAL TAG>` with the global tag that corresponds to these data.

Note that the first time you run the job accessing condition data on the CMS Open Data VM, it will download them from the `/cvmfs` area. It will take time (an example run of a 10 Mbps line took 45 mins), but it will only happen once as the files will be cached on your VM. The job will not produce any output during this time, but you can check the ongoing processes with the command 'top' and you can monitor the progress of reading the condition data to the local cache with the command 'df'.

### <a name="containers">Accessing condition data from the CMS Open Data containers</a>

The CMS Open Data containers can read the condition data from predefined condition data servers. This is often slow. The most recent containers for 2011-2012 and 2015 proton-proton data have condition database files in a local `/cvmfs/cms-opendata-conddb.cern.ch` area, and the access is therefore much faster.

In these containers, to connect to the local database area instead external predefined servers, add the following to the job configuration file:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/<DATABASE NAME')
process.GlobalTag.globaltag = '<GLOBAL TAG>'
```
Replace `<DATABASE NAME>` with the database name given in the instructions below, and `<GLOBAL TAG>` with the global tag that corresponds to these data.

Note that the fast access only works for the containers that have the local `/cvmfs/cms-opendata-conddb.cern.ch` installed, and only for those global tags that have been stored there. For other case, leave out the `process.GlobalTag.connect` line, and the database information is retreived from external servers.

If you have the `/cvmfs/cms-opendata-conddb.cern.ch` mounted on your local computer and the area is shared into your container, follow the instructions for VM below.

## <a name="global-tags">Global tags</a>

The global tags for condition data are different for different data-taking periods. They are listed below for [proton-proton](#proton-proton) and [heavy-ion](#heavy-ion) data.

### <a name="proton-proton">Proton-proton data</a>

---

**For 2010 collision data**, the global tag is FT_R_42_V10A.

**VM:**

When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from `/cvmfs`. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A FT_R_42_V10A
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db FT_R_42_V10A.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2010 data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db')
process.GlobalTag.globaltag = 'FT_R_42_V10A::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2010 data
process.GlobalTag.globaltag = 'FT_R_42_V10A::All'
```

---

**For 2010 simulated data**, the global tag is START42_V17B.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START42_V17B START42_V17B
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START42_V17B.db START42_V17B.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2010 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START42_V17B.db')
process.GlobalTag.globaltag = 'START42_V17B::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2010 data
process.GlobalTag.globaltag = 'START42_V17B::All'
```

---

**For 2011 collision data**, the global tag is FT_53_LV5_AN1.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA FT_53_LV5_AN1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db FT_53_LV5_AN1_RUNA.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2011 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1.db')
process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'
```

Note that two sets of condition data for 2011 data are provided in the `/cvmfs/cms-opendata-conddb.cern.ch/` area:

* FT_53_LV5_AN1 valid for the full range of 2011 data taking
* FT_53_LV5_AN1_RUNA valid for the run range of 2011 RunA

If only accessing 2011 RunA data, using FT_53_LV5_AN1_RUNA by setting the database name to FT_53_LV5_AN1_RUNA.db in `process.GlobalTag.connect` makes the starting time of the first job somewhat faster.

**Container:**

Selected database files have been stored in the local `/cvmfs/cms-opendata-conddb.cern.ch/` area of the container to make the condition database access faster.

Define the global tag and connect to the local database in the configuration file of the job:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_data_stripped.db')
process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'
```

---

**For 2011 simulated data**, the global tag is START53_LV6A1.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1 START53_LV6A1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1.db START53_LV6A1.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2011 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1.db')
process.GlobalTag.globaltag = 'START53_LV6A1::All'
```

**Container:**

Selected database files have been stored in the local `/cvmfs/cms-opendata-conddb.cern.ch/` area of the container to make the condition database access faster.

Define the global tag and connect to the local database in the configuration file of the job:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1_data_stripped.db')
process.GlobalTag.globaltag = 'START53_LV6A1::All'
```

---

**For 2012 collision data**, the global tag is FT53_V21A_AN6.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL FT53_V21A_AN6
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL.db FT53_V21A_AN6_FULL.db
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL FT53_V21A_AN6_FULL
```
Note the third additional symbolic link, which is needed for the 2012 data. Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2012 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL.db')
process.GlobalTag.globaltag = 'FT53_V21A_AN6::All'
```

Two other sets of condition data for 2012 data are provided:

* FT53_V21A_AN6 valid for the run range of 2012 RunB
* FT53_V21A_AN6_RUNC valid for the run range of 2012 RunC

They were proviced because of the small cache area size in the earlier VM images. You should use FT53_V21A_AN6_FULL and the CMS Open Data VM version CMS-OpenData-1.5.1.ova (or CMS-Open-Data-1.3.0.ova), which has a large enough cache area.

**Container:**

Selected database files have been stored in the local `/cvmfs/cms-opendata-conddb.cern.ch/` area of the container to make the condition database access faster.

Define the global tag and connect to the local database in the configuration file of the job:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL_data_stripped.db')
process.GlobalTag.globaltag = 'FT53_V21A_AN6_FULL::All'
```

Note that when accessing the condition data from external servers, the global tag covering the full range of data taking is `FT53_V21A_AN6::All`.

---

**For 2012 simulated data**, the global tag is START53_V27.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_V27 START53_V27
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_V27.db START53_V27.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2012 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_V27.db')
process.GlobalTag.globaltag = 'START53_V27::All'
```

In addition, condition data for the global tag START53_V7N is provided. This was used to produce simulated data with dose-dependent detector characteristics, run-dependent pile-up and beam spot conditions for the Higgs boson discovery analysis. The simulated data produced with this global tag can be analysed with the other global tag above.

**Container:**

Selected database files have been stored in the local `/cvmfs/cms-opendata-conddb.cern.ch/` area of the container to make the condition database access faster.

Define the global tag and connect to the local database in the configuration file of the job:

```shell
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_V27_data_stripped.db')
process.GlobalTag.globaltag = 'START53_V27::All'
```

---
**For 2015 collision data**, the global tag is 76X_dataRun2_16Dec2015_v0.

**VM and container:**

Define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2015 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/76X_dataRun2_16Dec2015_v0.db')
process.GlobalTag.globaltag = '76X_dataRun2_16Dec2015_v0'
```

Note that when using the CMS open data software container, the `process.GlobalTag.connect` line makes the job read the condition data from the local `/cvmfs` area in the container. If it is left out, the condition data are read from predefined condition data servers and it may take longer.

---

**For 2015 simulated data**, the global tag is 76X_mcRun2_asymptotic_RunIIFall15DR76_v1.

**VM and container:**

Define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2015 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/76X_mcRun2_asymptotic_RunIIFall15DR76_v1.db')
process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'
```

Note that when using the CMS open data software container, the `process.GlobalTag.connect` line makes the job read the condition data from the local `/cvmfs` area in the container. If it is left out, the condition data are read from predefined condition data servers and it may take longer.

---

**For 2016 simulated data**, for the special data science samples, the global tag is 80X_mcRun2_asymptotic_2016_TrancheIV_v8.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/80X_mcRun2_asymptotic_2016_TrancheIV_v8.db 80X_mcRun2_asymptotic_2016_TrancheIV_v8.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2016 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/80X_mcRun2_asymptotic_2016_TrancheIV_v8.db')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
```

---

**For 2018 simulated data**, for the special data science samples, the global tag is 102X_upgrade2018_design_v9.

**VM:**

To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/102X_upgrade2018_design_v9.db 102X_upgrade2018_design_v9.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag for 2018 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/102X_upgrade2018_design_v9.db')
process.GlobalTag.globaltag = '102X_upgrade2018_design_v9'
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
```

### <a name="heavy-ion">Heavy-ion related data</a>

---

**For 2010 heavy-ion data**, the global tag is GR_R_39X_V6B.

**VM:**

When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from `/cvmfs`. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B GR_R_39X_V6B
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B.db GR_R_39X_V6B.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B.db')
process.GlobalTag.globaltag = 'GR_R_39X_V6B::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2010 data
process.GlobalTag.globaltag = 'GR_R_39X_V6B::All'
```

---

**For 2011 heavy-ion data**, the global tag is GR_R_44_V15.

**VM:**

When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from `/cvmfs`. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15 GR_R_44_V15
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15.db GR_R_44_V15.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15.db')
process.GlobalTag.globaltag = 'GR_R_44_V15::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM, which is the VM version to be used with the 2011 heavy-ion data despite of "2010" in the VM record name.

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2011 data
process.GlobalTag.globaltag = 'GR_R_44_V15::All'
```

---

**For 2013 heavy-ion and p-p reference data**, the global tag is GR_P_V43D.

**VM:**

First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_P_V43D GR_P_V43D
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_P_V43D.db GR_P_V43D.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_P_V43D.db')
process.GlobalTag.globaltag = 'GR_P_V43D::All'
```

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2013 HI data
process.GlobalTag.globaltag = 'GR_P_V43D::All'
```

---

**For 2013 heavy-ion related simulated data**, the global tags are:

- PbPb simulated data at 2.76 TeV - STARTHI53_LV1
- pp simulated reference data at 2.76 TeV - STARTHI53_V28
- pPb simulated data at 5.02 TeV - STARTHI53_V27

Replace `<GLOBAL TAG>` in the following instructions with the value from this list.

**VM:**

First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/<GLOBAL TAG> <GLOBAL TAG>
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/<GLOBAL TAG>.db <GLOBAL TAG>.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/<GLOBAL TAG>.db')
process.GlobalTag.globaltag = '<GLOBAL TAG>::All'
```

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2013 HI-related MC
process.GlobalTag.globaltag = '<GLOBAL TAG>::All'
```

---

**For 2015 p-p reference data**, the global tag is 75X_dataRun2_v13.

**VM:**

First, set the symbolic link:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/75X_dataRun2_v13.db 75X_dataRun2_v13.db
```

Then, define the correct set of condition data by mentioning the global tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/75X_dataRun2_v13.db')
process.GlobalTag.globaltag = '75X_dataRun2_v13::All'
```

**Container:**

Define the global tag in the configuration file of the job:

```shell
#globaltag for 2015 pp HI reference data
process.GlobalTag.globaltag = '75X_dataRun2_v13::All'
```

---

**Additional database files for heavy-ion software**

In addition to the regular global tags, two sets of additional database files are collected under `/cvmfs/cms-opendata-conddb.cern.ch/hi_53_add_ons/` and `/cvmfs/cms-opendata-conddb.cern.ch/hi_75_add_ons/`. These database files are used in the heavy-ion software and they modify the existing collection of the global tags when needed.
