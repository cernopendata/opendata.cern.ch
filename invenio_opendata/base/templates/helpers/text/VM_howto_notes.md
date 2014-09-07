# Getting started with CMS data

## "I have installed the CERN Virtual Machine: now what?"

Congratulations! You have the [CERN working environment](opendata.cern.ch/data/VMs) up and running!

Note that in order to analyse CMS data collected in 2010, you need **CMSSW version 4.2.8 (patch7)**, supported only on **Scientific Linux 5**. The CMSSW command `cmsrel` you executed in the [validation stage](http://open-data.cern.ch/data/VMs#validate) ensures that you have the right version running. Make sure you are always in the **CMSSW_4_2_8patch7/src/** directory by performing the `cd CMSSW_4_2_8patch7/src/` every time you boot the VM and open the terminal.

## "OK! Where can I get the CMS data?"

It is best if we start off with a quick introduction to **[ROOT](http://root.cern.ch)**. ROOT is the framework used by several particle-physics experiments to work with the collected data. Although analysis is not itself performed within a ROOT file, it is instructive to understand how these files are structured and what data and collections they contain.

The CMS data provided on the CERN Open Data Portal is in a format called "[Analysis Object Data](FIXME! What is AOD?)" or AOD for short. These AOD files are prepared by piecing raw data collected by various sub-detectors of CMS and contain all the information that is needed for analysis. The files cannot be opened and understood as simple data tables but require ROOT in order to be read.

So, let's see what an AOD file looks like and take ROOT for a spin!

* Making sure that you are in the **CMSSW_4_2_8patch7/src/** folder, execute the following command in your terminal to launch the CMS analysis environment:

```
$ cmsenv
```

* You can now open a CMS AOD file in ROOT. Let us open one of the files by entering the following command:

```
$ root root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
```

* You will see the ROOT logo appear on screen. You can now open the ROOT GUI by entering:

```
TBrowser t
```

* Excellent! You have successfully opened a CMS AOD file in ROOT. If this was the first time you've done so, pat yourself on the back. Now, to see what is inside this file, let us take a closer look at some collections of [physics objects](FIXME! CMS Physics Objects).

* Then on the left root window, doubleclick on the file name (the one above i.e. root://eospublic.cern.ch.... etc).
Then doubleclick on Events, and you will get all the "collections" in the AOD file.
Among those, you will find the physics object collections.


![Screenshot: After running "TBrowser t"](../images/Screenshot_001_TBrowser_t.png)


For example, the electron collection, as we are trying to explain in
https://twiki.cern.ch/twiki/bin/view/CMS/DPOAPublicDataReleaseStatement#Electrons
is recoGsfElectrons\_gsfElectrons\_\_RECO and you can look in there by doubleclicking on that line and doubleclicking on recoGsfElectrons\_gsfElectrons\_\_RECO.obj.
There, you can for example plot the transverse momentum of the electrons by doubleclicking on recoGsfElectrons\_gsfElectrons\_\_RECO.obj.pt\_

## "Nice! But how do I analyse these data?"

## How is a CMS analysis performed?

* Data collected by subdetectors, reconstructed, re-reconstructed, made into AOD
* Write analyzer that reduces the dataset, either in terms of number of events or in terms of information carried by each event.
* Run analysis code (this can be part of the analyzer stage or done afterwards: be smart about how you write your code!)

* Ana's examples go here

## What can we do with the data?

### AOD

* FILENAME nomenclature

### Applying cuts and reducing the data sample

### Analysing data sample (see previous step)

[CMS PAT Tutorials](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookPATTutorial)
