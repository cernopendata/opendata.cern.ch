This page explains the use of global tags and the condition database with the CMS Open Data. 

A Global Tag is a coherent collection of records of additional data needed by the reconstruction and analysis software. The Global Tag is defined for each data-taking period, separately for collision and simulated data. 

These records are stored in the condition database. Condition data include non-event-related information (Alignment, Calibration, Temperature, etc.) and parameters for the simulation/reconstruction/analysis software. For 2011-2012 CMS Open Data, the condition data are provided as sqlite files in the `/cvmfs/cms-opendata-conddb.cern.ch/` directory, which is accessible to the CMS Open Data VM.

Most [physics objects](/docs/cms-physics-objects-2011) in the CMS Open Data are already calibrated and ready-to-use, and no additional corrections are needed other than selection and identification criteria, which will be applied in the analysis code. Therefore simple analyses do not need to access the condition database. Examples of such analysis are [the di-muon spectrum example](/record/5001) or [the Higgs analysis example](/record/5500).

However, the access to the condition database is necessary, for example, for jet energy corrections and trigger configuration information. Examples of such analysis are for [the PAT object production](/record/233) or [the top quark pair production analysis](/record/5000).

Note that when you need to access the condition database, the first time you run the job on the CMS Open Data VM, it will download the condition data from the `/cvmfs` area. It will take time (an example run of a 10 Mbps line took 45 mins), but it will only happen once as the files will be cached on your VM. The job will not produce any output during this time, but you can check the ongoing processes with the command 'top' and you can monitor the progress of reading the condition data to the local cache with the command 'df'.

---

**For 2011 collision data**, the global tag is FT_53_LV5_AN1. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA FT_53_LV5_AN1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db FT_53_LV5_AN1_RUNA.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2011 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db')
process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'
```

Note that two sets of condition data for 2011 data are provided:
* FT_53_LV5_AN1 valid for the full range of 2011 data taking
* FT_53_LV5_AN1_RUNA valid for the run range of 2011 RunA (public data)

It is convenient to use FT_53_LV5_AN1_RUNA as instructed above, it makes the starting time of the first job somewhat faster.

---

**For 2011 Montecarlo data**, the global tag is START53_LV6A1. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1 START53_LV6A1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1.db START53_LV6A1.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2011 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_LV6A1.db')
process.GlobalTag.globaltag = 'START53_LV6A1::All'
```

---

**For 2012 collision data**, the global tag is FT53_V21A_AN6. To access the condition database, first, set the symbolic links:

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

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2012 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT53_V21A_AN6_FULL.db')
process.GlobalTag.globaltag = 'FT53_V21A_AN6::All'
```

Note that three sets of condition data for 2011 data are provided:
* FT53_V21A_AN6_FULL valid for the full range of 2012 data taking
* FT53_V21A_AN6 valid for the run range of 2012 RunB (public data)
* FT53_V21A_AN6_RUNC valid for the run range of 2012 RunC (public data)

It is convenient to use FT53_V21A_AN6_FULL as instructed above, as you will not need to load RunB and RunC condition data separately. You should use the CMS Open Data VM version CMS-Open-Data-1.3.0.ova with a large enough cache area.

---

**For 2012 Montecarlo data**, the global tag is START53_V27. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_V27 START53_V27
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START53_V27.db START53_V27.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2012 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START53_V27.db')
process.GlobalTag.globaltag = 'START53_V27::All'
```


