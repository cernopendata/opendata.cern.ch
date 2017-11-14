## "I have installed the CERN Virtual Machine: now what?"

To analyse CMS data collected in 2011, you need **version 5.3.32** of [CMSSW](/glossary/CMSSW), supported only on **Scientific Linux 6**. If you are unfamiliar with Linux, take a look at [this short introduction to Linux](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBasicLinux) or try this interactive [command-line bootcamp](http://rik.smith-unna.com/command_line_bootcamp/). Once you have installed the [CMS-specific CERN Virtual Machine](/VM/CMS/2011), execute the following command in the terminal if you haven't done so before; it ensures that you have this version of [CMSSW](/glossary/CMSSW) running:

```shell
$ cmsrel CMSSW_5_3_32
```

Then, make sure that you are always in the **CMSSW_5_3_32/src/** directory by entering the following command in the terminal (you must do so every time you boot the VM before you can proceed):

```shell
$ cd CMSSW_5_3_32/src/
```

## "OK! Where can I get the CMS data?"

It is best if we start off with a quick introduction to **[ROOT](http://root.cern.ch)**. ROOT is the framework used by several particle-physics experiments to work with the collected data. Although analysis is not itself performed within the ROOT GUI, it is instructive to understand how these files are structured and what data and collections they contain.

The primary data provided by CMS on the CERN Open Data Portal is in a format called "[Analysis Object Data](/about/cms)" or [AOD](/glossary/AOD) for short. These [AOD](/glossary/AOD) files are prepared by piecing raw data collected by various sub-detectors of CMS and contain all the information that is needed for analysis. The files cannot be opened and understood as simple data tables but require ROOT in order to be read.

So, let's see what an [AOD](/glossary/AOD) file looks like and take ROOT for a spin!

Making sure that you are in the **CMSSW_5_3_32/src/** folder, execute the following command in your terminal to launch the CMS analysis environment:

```shell
$ cmsenv
```

You can now open a CMS [AOD](/glossary/AOD) file in ROOT. Let us open one of the files from the CERN Open Data Portal by entering the following command:

```shell
$ root root://eospublic.cern.ch//eos/opendata/cms/[Run2011A](#)/ElectronHad/[AOD](#)/12Oct2013-v1/20001/001F9231-F141-E311-8F76-003048F00942.root
```

You will see the ROOT logo appear on screen. You can now open the ROOT GUI by entering:

```shell
TBrowser t
```

Excellent! You have successfully opened a CMS [AOD](/glossary/AOD) file in ROOT. If this was the first time you've done so, [pat](/glossary/PAT) yourself on the back. Now, to see what is inside this file, let us take a closer look at some collections of [physics objects](/about/CMS-Physics-Objects).

On the left window of ROOT (see the screenshot below), double-click on the file name (<kbd>root://eospublic.cern.ch//eos/opendata/…</kbd>). You should see a list of entries under <kbd>Events</kbd>, each corresponding to a collection of reconstructed data. We are interested in the collections containing information about reconstructed physics objects.

<img src="../../../../static/articles/getting-started-with-cms-2011-data/getting_started_with_cms_2011_data_1.png"  width="70%">

Let us take a peek, for example, at the [electrons](/glossary/electron), which are found in <kbd>recoGsfElectrons_gsfElectrons__RECO</kbd>, as shown on the list of [physics objects](/about/CMS-Physics-Objects). Look in there by double-clicking on that line and then double-clicking on <kbd>recoGsfElectrons_gsfElectrons__RECO.obj</kbd>. Here, you can have a look at various properties of this collection, such as the plot for the transverse momentum of the [electrons](/glossary/electron): <kbd>recoGsfElectrons_gsfElectrons__RECO.obj.pt_</kbd>.

You can exit the ROOT browser through the GUI by clicking on <kbd>Browser</kbd> on the menu and then clicking on <kbd>Quit Root</kbd> or by entering <kbd>.q</kbd> in the terminal.

## "Nice! But how do I analyse these data?"

In [AOD](/glossary/AOD) files, reconstructed [physics objects](/about/CMS-Physics-Objects) are included without checking their "quality", i.e. in case of our [electron](/glossary/electron) collection that you opened in ROOT, without ensuring that the reconstructed object is really an [electron](/glossary/electron). In order to analyse only the "good quality" data, you must apply some selection criteria.

With these criteria, you are in effect reducing the dataset, either in terms of the number of collisions events it contains or in terms of the information carried by each event. Following this, you run your analysis code on the reduced dataset.

Depending on the nature of your analysis you _can_ run your analysis code directly on the [AOD](/glossary/AOD) files themselves, if needed, performing the selections along the way. However, this can be resource-intensive and is done only for very specific usecases.

**NOTE**: To analyse the full event content, the analysis job needs access to the "[condition data](/glossary/tag)", such as the jet-energy corrections. You can see how connections to the [condition database](/glossary/tag) are established in the ["pattuples2011" example](/record/233). For simpler analyses, where we use only physics objects needing no further data for corrections, you do not need to connect to the [condition database](/glossary/tag). This is the case for the example for analysing the [primary datasets](/glossary/primary) below.

Your final analysis is done using a software module called an "analyzer". If you have followed the validation step for the virtual machine setup, you have already produced and run a simple analyzer. You can specify your initial selection criteria within the analyzer to perform your analysis directly on the [AOD](/glossary/AOD) files, or further elaborate the selections and other operations needed for analysing the reduced dataset. To learn more about configuring analyzers, follow [these instructions in the CMSSW WorkBook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule). Make sure, though, that you replace the release version (CMSSW_nnn) with the release that you are using, i.e. one that is compatible with the CMS open data.

You can also pass the selection criteria through the configuration file. This file activates existing tools within [CMSSW](/glossary/CMSSW) in order to perform the desired selections. If you have followed the validation step for the virtual machine setup, you have already seen a configuration file, which is used to give the parameters to the <kbd>cmsRun</kbd> executable. You can see how this is done in our analysis example.

We will now take you through these steps through a couple of specially prepared example analyses.

## Option A: Analysing the primary dataset

As mentioned above, you do not typically perform an analysis directly on the [AOD](/glossary/AOD) files. However, there may be cases when you can do so. Therefore, we have provided an example analysis to take you through the steps that you may need on the occassions that you want to analyse the [AOD](/glossary/AOD) files directly. You can find the files and instructions in [this CMS Tools entry](/record/560).

**Before you proceed**: Note that this example is tailored to the CMS data from 2010\. In order to run the same analysis on 2011 data, you need to make the following adjustments to the workflow:

1.  Different CMS VM image versions should be used for analysing 2010 and 2011 data. For 2011 data, use [CMS VM image for 2011 data](/record/252).
2.  Change all instances of [CMSSW](/glossary/CMSSW) to the correct version (<kbd>CMSSW_5_3_32</kbd> for 2011 datasets).
3.  In the <kbd>demoanalyzer_cfg.py</kbd> file, replace <kbd>PhysicsTools.PythonAnalysis.LumiList</kbd> with <kbd>FWCore.PythonUtilities.LumiList</kbd> on line 4.
4.  In the <kbd>demoanalyzer_cfg.py</kbd> file, under the section to define the input data, select any [primary dataset](/glossary/primary) with [muons](/glossary/muon) from the 2011 data (such as <kbd>SingleMu</kbd> or <kbd>DoubleMu</kbd>).
5.  Download the list of validated runs from [this record](/record/1001) and, in the <kbd>demoanalyzer_cfg.py</kbd> file, replace <kbd>goodJSON = '/home/cms-opendata/CMSSW_4_2_8/src/Demo/DemoAnalyzer/datasets/Cert_136033-149442_7TeV_Apr21ReReco_Collisions10_JSON_v2.txt'</kbd> with <kbd>goodJSON = '/home/cms-opendata/CMSSW_5_3_32/src/Demo/DemoAnalyzer/datasets/Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt'</kbd>.

## Option B: Analysing reduced datasets

We start by applying selection cuts via the configuration file and reduce the [AOD](/glossary/AOD) files into a format known as PATtuple. You can find more information about this data format (which gets its name from the CMS Physics Analysis Toolkit, or [PAT](/glossary/PAT)) on the [CMSSW PAT WorkBook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookPAT).

**Important**: Be aware that the instructions in the WorkBook are in use in CMS currently and have been updated for more recent [CMSSW](/glossary/CMSSW) releases. With the 2011 data, you should always use the releases in the series of CMSSW_5_3 and not higher. Also note that more recent code does not work with older releases, so whenever you see <kbd>git cms-addpkg…</kbd> in the instruction, it is likely that the code package this command adds does not work with the release you need. However, the material under the pages gives you a good introduction to [PAT](/glossary/PAT).

Code as well as instructions for producing PATtuples from the CMS open data can be found in [this GitHub repo](https://github.com/katilp/pattuples2011). However, since it can take a dedicated computing cluster several days to run this step and reduce the several TB of [AOD](/glossary/AOD) files to a few GB of PATtuples, we have provided you with the PATtuples in that GitHub repo, saving you quite a lot of time! So you can jump to the next step, below ("Performing your analysis…"). Although you do not need to run this step, it is worth looking at [the configuration file](https://github.com/katilp/pattuples2011/blob/master/PAT_data_repo.py):

You can see that the line <kbd>removeAllPATObjectsBut(process, ['Muons','Electrons'])</kbd> removes all "PATObjects" but [muon](/glossary/muon) and [electrons](/glossary/elctron), which will be needed in the final analysis step of this example.

Note also how only the validated runs are selected on lines:

```python
import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
myLumis = LumiList.LumiList(filename='Cert_160404-180252_7TeV_ReRecoNov08_Collisions11_JSON.txt').getCMSSWString().split(',')
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)
```

This selection must always be applied to any analysis on CMS open data, and to do so you must have the validation file downloaded to your local area.

You can also see the steps needed to use the [condition data](/glossary/tag). First, as shown in the <kbd>README</kbd>, you have to set the symbolic links to the [condition database](/glossary/tag).

```shell
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA FT_53_LV5_AN1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db FT_53_LV5_AN1_RUNA.db
```

Then, the correct set of [condition data](/glossary/tag) are defined by mentioning the [Global Tag](/glossary/tag) on lines 46–48 in the file <kbd>PAT_data_repo.py</kbd>.

```shell
#globaltag
process.GlobalTag.connect = cms.string('sqlite_file:/cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db')
process.GlobalTag.globaltag = 'FT_53_LV5_AN1::All'
```

**Important**: If you plan on running the code to produce the PATtuples needed for this analysis, note that the first time you run the job, the CERN Virtual Machine will read the [condition data](/glossary/tag) from the remote database. This process will take time (an example run of a 10 Mb/s line took 45 mins), but it will only happen once as the files will then be cached on your VM. The job will not produce any output during this time. However, you can check the ongoing processes with the command <kbd>top</kbd> and you can monitor the progress of reading the [condition data](/glossary/tag) to the local cache with the command <kbd>df</kbd>.

## Performing your analysis on the PATtuples

Now, as the intermediate PATtuple files have been produced for you, you can go directly to the next step, as described in [this second GitHub repo](https://github.com/katilp/OutreachExercise2011) and follow the instructions on that page.

Note that even though these are [derived datasets](/glossary/derived), running the analysis code over the full data can take time. So if you want just give it a try, you can limit the number events or read only part of the files. Bear in mind that running on a low number of files will not give you a meaningful plot.

Your analysis job is defined in <kbd>OutreachExercise2011/DecaysToLeptons/run/run.py</kbd>. The analysis code is in the files located in the <kbd>OutreachExercise2011/DecaysToLeptons/python</kbd> directory.

This example uses IPython, which gets configured and starts the job with the following command:

```shell
ipython run.py
```

That's it! Follow the rest of the instructions on the README and you have performed an analysis using data from CMS. Hope you enjoyed this exercise. Feel free to play around with the rest of the data and write your own analyzers and analysis code. (To exit IPython, enter <kbd>exit()</kbd>.)
