This page explains the use of global tags and the condition database with the CMS Open Data.

A Global Tag is a coherent collection of records of additional data needed by the reconstruction and analysis software. The Global Tag is defined for each data-taking period, separately for collision and simulated data.

These records are stored in the condition database. Condition data include non-event-related information (Alignment, Calibration, Temperature, etc.) and parameters for the simulation/reconstruction/analysis software. For CMS Open Data, the condition data are provided as sqlite files in the `/cvmfs/cms-opendata-conddb.cern.ch/` directory, which is accessible through the CMS Open Data VM. Note that when using CMS Open Data docker images, connecting to this area with the command `process.GlobalTag.connect = cms.string(...` in the job configuration file is not required as the condition data can be read from predefined condition data servers.

Most [AOD](/docs/cms-physics-objects-2011) and [MINIAOD](/docs/cms-physics-objects-2015) physics objects in the CMS Open Data are already calibrated and ready-to-use, and no additional corrections are needed other than selection and identification criteria, which will be applied in the analysis code. Therefore, simple analyses do not need to access the condition database. Examples of such analyses are [the di-muon spectrum example](/record/5001) or [the Higgs analysis example](/record/5500).

However, access to the condition database is necessary, for example, for jet energy corrections and trigger configuration information. Examples of such analyses are the jet energy correction (JEC) reading in ["Physics Object Extractor Tool (POET)"](https://github.com/cms-legacydata-analyses/PhysObjectExtractorTool/tree/2012)(/record/233) or getting [the trigger information](/record/5004).

Note that when you need to access the condition database, the first time you run the job on the CMS Open Data VM, it will download the condition data from the `/cvmfs` area. It will take time (an example run of a 10 Mbps line took 45 mins), but it will only happen once as the files will be cached on your VM. The job will not produce any output during this time, but you can check the ongoing processes with the command 'top' and you can monitor the progress of reading the condition data to the local cache with the command 'df'.

The Global Tags for condition data are different for different types of data taking. Below, the instructions are given for [proton-proton](#proton-proton) and [heavy-ion](#heavy-ion) data.

## <a name="proton-proton">Proton-proton data</a>

---

**For 2010 collision data**, the global tag available in the  `/cvmfs` area is FT_R_42_V10A. When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from there. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A FT_R_42_V10A
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db FT_R_42_V10A.db
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_R_42_V10A.db')
process.GlobalTag.globaltag = 'FT_R_42_V10A::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

---

**For 2010 Montecarlo data**, the global tag is START42_V17B. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START42_V17B START42_V17B
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/START42_V17B.db START42_V17B.db
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2010 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/START42_V17B.db')
process.GlobalTag.globaltag = 'START42_V17B::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

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

Two other sets of condition data for 2012 data are provided:

* FT53_V21A_AN6 valid for the run range of 2012 RunB
* FT53_V21A_AN6_RUNC valid for the run range of 2012 RunC

They were proviced because of the small cache area size in the earlier VM images. You should use FT53_V21A_AN6_FULL and the CMS Open Data VM version CMS-OpenData-1.5.1.ova (or CMS-Open-Data-1.3.0.ova), which has a large enough cache area.

In addition, condition data for the Global Tag START53_V7N is provided. This was used to produce simulated data with dose-dependent detector characteristics, run-dependent pile-up and beam spot conditions for the Higgs boson discovery analysis. The simulated data produced with this Global Tag can be analysed with the other Global Tag above.

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

---
**For 2015 collision data**, the global tag is 76X_dataRun2_16Dec2015_v0. Define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2015 collision data
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/76X_dataRun2_16Dec2015_v0.db')
process.GlobalTag.globaltag = '76X_dataRun2_16Dec2015_v0'
```

Note that when using the CMS open data software container, the `process.GlobalTag.connect` line makes the job read the condition data from the local `/cvmfs` area in the container. If it is left out, the condition data are read from predefined condition data servers and it may take longer.

---

**For 2015 Montecarlo data**, the global tag is 76X_mcRun2_asymptotic_RunIIFall15DR76_v1. Define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2015 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/76X_mcRun2_asymptotic_RunIIFall15DR76_v1.db')
process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_RunIIFall15DR76_v1'
```

Note that when using the CMS open data software container, the `process.GlobalTag.connect` line makes the job read the condition data from the local `/cvmfs` area in the container. If it is left out, the condition data are read from predefined condition data servers and it may take longer.

---

**For 2016 Montecarlo data**, for the special data science samples, the global tag is 80X_mcRun2_asymptotic_2016_TrancheIV_v8. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/80X_mcRun2_asymptotic_2016_TrancheIV_v8.db 80X_mcRun2_asymptotic_2016_TrancheIV_v8.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2016 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/80X_mcRun2_asymptotic_2016_TrancheIV_v8.db')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_TrancheIV_v8'
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
```

---

**For 2018 Montecarlo data**, for the special data science samples, the global tag is 102X_upgrade2018_design_v9. To access the condition database, first, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/102X_upgrade2018_design_v9.db 102X_upgrade2018_design_v9.db
```
Make sure the `cms-opendata-conddb.cern.ch` directory has actually expanded in your VM. One way of doing this is executing:

```shell
ls -l
ls -l /cvmfs/
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag for 2018 MC
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/102X_upgrade2018_design_v9.db')
process.GlobalTag.globaltag = '102X_upgrade2018_design_v9'
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")
```

## <a name="heavy-ion">Heavy-ion data</a>

---

**For 2010 heavy-ion data**, the global tag available in the  `/cvmfs` area is GR_R_39X_V6B. When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from there. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B GR_R_39X_V6B
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B.db GR_R_39X_V6B.db
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_R_39X_V6B.db')
process.GlobalTag.globaltag = 'GR_R_39X_V6B::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM.

---

**For 2011 heavy-ion data**, the global tag available in the  `/cvmfs` area is GR_R_44_V15. When using the "CMS-OpenData-1.1.2" VM or a higher version, it is recommended reading the condition data from there. First, set the symbolic links:

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15 GR_R_44_V15
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15.db GR_R_44_V15.db
```

Then, define the correct set of condition data by mentioning the Global Tag in the configuration file of the job.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/GR_R_44_V15.db')
process.GlobalTag.globaltag = 'GR_R_44_V15::All'
```

Note that **this only works in the "CMS-OpenData-1.1.2" or a higher version** of the 2010 CMS Open Data VM, which is the VM version to be used with the 2011 heavy-ion data despite of "2010" in the VM record name.
