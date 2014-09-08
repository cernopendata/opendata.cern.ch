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
* On the left window of ROOT (see the screenshot below), double-click on the file name (`root://eospublic.cern.ch//eos/opendata/…`), followed by `Events` and then `Collections`. You should see a list of collections of physics objects.
![Screenshot: After running "TBrowser t"](../images/Screenshot_001_TBrowser_t.png)
* Let us take a peek, for example, at the following electron collection, as shown on the list of [physics objects](FIXME! CMS Physics Objects): `recoGsfElectrons_gsfElectrons__RECO`. Look in there by double-clicking on that line and then double-clicking on `recoGsfElectrons_gsfElectrons__RECO.obj`.
Here, you can have a look at various properties of this collection, such as the plot for the transverse momentum of the electrons: `recoGsfElectrons_gsfElectrons__RECO.obj.pt_`.

## "Nice! But how do I analyse these data?"

## How is a CMS analysis performed?

* Data collected by subdetectors, reconstructed, re-reconstructed, made into AOD
* Write analyzer that reduces the dataset, either in terms of number of events or in terms of information carried by each event.
* Run analysis code (this can be part of the analyzer stage or done afterwards: be smart about how you write your code!)

### CMS analysable data

* AOD
    * FILENAME nomenclature

Note that in AOD files, reconstructed physics objects are included without cheking their "quality", i.e. in case of our electron, without applying further selection criteria, which assure that the reconstructed object is really an electron. This is something that we need to do in the analysis step.

### Applying cuts and reducing the data sample

The analysis selections can be inserted in a software module called "analyzer" written in C++. If you have followed the validation step for the virtual machine setup, you have already produced and run a simple analyzer, and this is where you can further elaborate the selections and other operations needed for the analysis. To learn more, you can follow the instructions in https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule but make sure to replace the release version (CMSSW_nnn) with the release that you are using, which is compatible with the CMS open data.

You can also pass the selection criteria through the configuration file. If you have followed the validation step for the virtual machine setup, you have already seen a configuration file, which is used to give the parameters to the cmsRun executable. You can see how this is done in the analysis example.

We have provided an analysis example in two steps. In the first step, in https://github.com/ayrodrig/pattuples2010 intermediate data files with only selected contents is produced. We have done this for you, as it takes nine days to process the data for this step. So you do not need to run this step, but have a look at the configuration file in https://github.com/ayrodrig/pattuples2010/blob/master/PAT_data_repo.py You can see that the line `removeAllPATObjectsBut(process, ['Muons','Electrons'])` removes all other "PATObjects" but muon and electrons, which will be needed in the final analysis step, and [**VALIDATIONINFO INCLUDED**]. We are using here the tools in the Physics Analysis Toolkit (PAT) which perform includes tools for analysis operations, which are common to many different analysis. You can learn more in https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookPAT but be aware that these instructions are in use in CMS and have been updated for more recent releases. With the 2010 data, you should always use the releases in the series of CMSSW_4_2 and not higher. Take also note that more recent code does not work with this older release, so whenever you see "git cms-addpkg..." in the instruction, it is likely that added code package does not work with this release. However, the material under the pages gives you a good idea what are the tools in PAT.

### Analysing data sample

Now, as the intermediate file have been produced for you, you can go directly to the next step in https://github.com/ayrodrig/OutreachExercise2010 Follow the instructions on that page. Note that running over the full, even if reduced, data sets take time, so if you want just give it a try, you can limit the number events or read only part of the files. You will find the configuration file in OutreachExercise2010/DecaysToLeptons/run/run.py It is a more complex configuration file than those that we have seen before and it reads additional information from files in the OutreachExercise2010/DecaysToLeptons/python directory. To run the example, you will need to change the path in the file names in sources.py. For example, replace file:/data2/pattuples2010/Mu/Mu_PAT_data_500files_1.root with root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/PATtuples/Mu_PAT_data_500files_1.root

After the command
ipython run.py
ipython, which is used in this example, gets configured and the job starts.
