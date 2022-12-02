1. ["I have installed the CMS open data environment: now what?"](#vm)
2. ["OK! What is in the CMS data?"](#data)
3. ["Nice! But how do I analyse these data?"](#nice)

## <a name="env">"I have installed the CMS open data environment: now what?"</a>

To analyse CMS data collected in 2015, you need **version 7.6.7** of CMSSW, supported on **Scientific Linux 6**. If you are unfamiliar with Linux, take a look at [this short introduction to Linux](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBasicLinux) or try this [tutorial](https://swcarpentry.github.io/shell-novice/). Once you have installed the [CMS open data container](/docs/cms-guide-docker) or the [CMS-specific CERN Virtual Machine (VM)](/docs/cms-virtual-machine-2015), you need to open a terminal.

If you are using the VM, always use the "CMS shell" terminal available from the "CMS Shell" icon on the desktop for all CMSSW-specific commands, such as compilation and run. In VM, execute the following command in the terminal if you haven't done so before; it ensures that you have this version of CMSSW running:

```shell
$ cmsrel CMSSW_7_6_7
```

Note that if you get a warning message about the current OS not being slc6, you are using a wrong terminal ("Outer Shell") which is CERN CentOS 7 (cc7). Open a "CMS Shell" terminal as explained above and execute the cmsrel command there.

Both in CMS open data container and in the VM, make sure that you are always in the **CMSSW_7_6_7/src/** directory (and in the "CMS Shell" terminal in VM).

In VM, the CMS analysis environment needs to be properly setup by entering the following commands in the terminal (you must do so every time you boot the VM before you can proceed):

```shell
$ cd CMSSW_7_6_7/src/
$ cmsenv # do not execute this command if you are working in the container
```

## <a name="data">"OK! What is in the CMS data?"</a>

The primary data provided by CMS on the CERN Open Data Portal is in a format called "[Analysis Object Data](/docs/cms-physics-objects-2015)" or AOD for short, and from 2015 onwards, in a slimmer format called MINIAOD. These AOD files are prepared by piecing raw data collected by various sub-detectors of CMS and contain all the information that is needed for analysis. The files cannot be opened and understood as simple data tables but require specific sofware in order to be read.

So, let's see what a MINIAOD file looks like.

Make sure that you are in the **CMSSW_7_6_7/src/** folder, and, in VM, you have executed the `cmsenv` command in your terminal to launch the CMS analysis environment.

You can select a file from a dataset (a listing is available for each dataset record) and print out it contents with:

```shell
$ edmDumpEventContent root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root
```

The ouput is a list of different objects that the file contains, such as

```shell
Type                                  Module                      Label             Process
----------------------------------------------------------------------------------------------
edm::TriggerResults                   "TriggerResults"            ""                "HLT"
[...]
vector<pat::Electron>                 "slimmedElectrons"          ""                "RECO"
[...]
```

Documentation of these objects is available in [the CMS WorkBook 2015 MiniAOD page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#High_level_physics_objects). The objects are implemented as C++ classes in the CMS software package CMSSW, and detailed reference documentation of all classes is available in [the class list of the CMSSW reference manual](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/annotated.html). To see the properties of electrons, you would navigate to "pat" and find the entry for "Electron". The [pat::Electron Class Reference](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/d2/d1f/classpat_1_1Electron.html) lists all member functions through which the different properties of reconstructed electron can be accessed. Note that many of the basic propertied are "inherited" from the parent classes, and are listed separately under "Public Member Functions inherited from ... ".

These objects can be accessed in a software module which can be built with a helper script available in the CMS open data environment. If you are using the VM, this helper scripts does not work out of the box, so skip this part and go directly to [the next section](#nice). If you are using the CMS open data container, you can do the following:

```shell
$ mkdir Test
$ cd Test
$ mkedanlzr MiniAnalyzer
$ cd MiniAnalyzer
```

This will create several template files in the new MiniAnalyzer directory. For more information, have a look in [the CMS open data guide](https://cms-opendata-guide.web.cern.ch/cmssw/cmsswanalyzers/).

To access the physics object properties, add `<use name="DataFormats/PatCandidates"/>` in `plugins/BuildFile.xml`. Compile the code with:

```shell
$ scram b
```

To run over the example file, change the input file name `file:myfile.root` in `python/ConfFile_cfg.py` to `root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root`. Change the number of events from `-1` (runs over all events in the file) to `10` for testing. You can run this "empty" analyzer to see that the data are accessed properly:

```shell
$ cmsRun python/ConfFile_cfg.py
09-Dec-2021 12:00:35 CET  Initiating request to open file root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root
211209 12:00:35 722 secgsi_InitProxy: cannot access private key file: /home/cmsusr/.globus/userkey.pem
%MSG-w XrdAdaptor:  file_open 09-Dec-2021 12:00:37 CET pre-events
Data is served from cern.ch instead of original site eospublic
%MSG
09-Dec-2021 12:00:38 CET  Successfully opened file root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root
Begin processing the 1st record. Run 258434, Event 269235992, LumiSection 165 at 09-Dec-2021 12:01:10.140 CET
Begin processing the 2nd record. Run 258434, Event 269040066, LumiSection 165 at 09-Dec-2021 12:01:10.141 CET
Begin processing the 3rd record. Run 258434, Event 269567329, LumiSection 165 at 09-Dec-2021 12:01:10.142 CET
Begin processing the 4th record. Run 258434, Event 268674092, LumiSection 165 at 09-Dec-2021 12:01:10.143 CET
Begin processing the 5th record. Run 258434, Event 269416541, LumiSection 165 at 09-Dec-2021 12:01:10.143 CET
Begin processing the 6th record. Run 258434, Event 269251857, LumiSection 165 at 09-Dec-2021 12:01:10.143 CET
Begin processing the 7th record. Run 258434, Event 268739237, LumiSection 165 at 09-Dec-2021 12:01:10.144 CET
Begin processing the 8th record. Run 258434, Event 269456225, LumiSection 165 at 09-Dec-2021 12:01:10.144 CET
Begin processing the 9th record. Run 258434, Event 269845067, LumiSection 165 at 09-Dec-2021 12:01:10.144 CET
Begin processing the 10th record. Run 258434, Event 268437313, LumiSection 165 at 09-Dec-2021 12:01:10.145 CET
09-Dec-2021 12:01:10 CET  Closed file root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root

=============================================

MessageLogger Summary

 type     category        sev    module        subroutine        count    total
 ---- -------------------- -- ---------------- ----------------  -----    -----
    1 XrdAdaptor           -w file_open                              1        1
    2 fileAction           -s file_close                             1        1
    3 fileAction           -s file_open                              2        2

 type    category    Examples: run/evt        run/evt          run/evt
 ---- -------------------- ---------------- ---------------- ----------------
    1 XrdAdaptor           pre-events
    2 fileAction           PostEndRun
    3 fileAction           pre-events       pre-events

Severity    # Occurrences   Total Occurrences
--------    -------------   -----------------
Warning                 1                   1
System                  3                   3
```

To access the physics object information in the code, for example that of electrons, add the following lines in `plugins/MiniAnalyzer.cc` (the lines before and after of the line to be added are also shown):

```shell
[...]
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Electron.h" // add this line
//
[...]
      // ----------member data ---------------------------
      edm::EDGetTokenT<pat::ElectronCollection> electronToken_; // add this line
};
[...]
MiniAnalyzer::MiniAnalyzer(const edm::ParameterSet& iConfig): // add the colon to the end of this line
    electronToken_(consumes<pat::ElectronCollection>(iConfig.getParameter<edm::InputTag>("electrons"))) // add this line
{
[...]
using namespace edm;
   edm::Handle<pat::ElectronCollection> electrons; // add from this line
    iEvent.getByToken(electronToken_, electrons);
    for (const pat::Electron &el : *electrons) {
        if (el.pt() < 5) continue;
        printf("electron with pt %4.1f, eta %+5.3f, cluster eta %+5.3f, pass conversion veto %d\n",
                    el.pt(), el.eta(), el.superCluster()->eta(), el.passConversionVeto());
    }                                              // to this line

#ifdef THIS_IS_AN_EVENT_EXAMPLE
[...]
```

Replace the `process.demo` definition in `python/ConfFile_cfg.py` with the following:

```shell
process.demo = cms.EDAnalyzer("MiniAnalyzer",
    electrons = cms.InputTag("slimmedElectrons")
)
```
Compile and run again with:

```shell
$ scram b
$ cmsRun python/ConfFile_cfg.py
```

and the output gives information on the electrons in these events:

```shell
Begin processing the 1st record. Run 258434, Event 269235992, LumiSection 165 at 09-Dec-2021 12:11:17.653 CET
electron with pt 94.4, eta -1.959, cluster eta -1.969, pass conversion veto 1
Begin processing the 2nd record. Run 258434, Event 269040066, LumiSection 165 at 09-Dec-2021 12:11:17.748 CET
electron with pt 19.3, eta -0.215, cluster eta -0.236, pass conversion veto 1
electron with pt 18.1, eta -2.271, cluster eta -2.296, pass conversion veto 1
Begin processing the 3rd record. Run 258434, Event 269567329, LumiSection 165 at 09-Dec-2021 12:11:17.749 CET
electron with pt 47.2, eta +0.530, cluster eta +0.548, pass conversion veto 1
electron with pt 42.6, eta +0.362, cluster eta +0.377, pass conversion veto 1
Begin processing the 4th record. Run 258434, Event 268674092, LumiSection 165 at 09-Dec-2021 12:11:17.750 CET
electron with pt 23.3, eta +2.008, cluster eta +2.045, pass conversion veto 0
Begin processing the 5th record. Run 258434, Event 269416541, LumiSection 165 at 09-Dec-2021 12:11:17.751 CET
electron with pt 17.7, eta +2.101, cluster eta +2.081, pass conversion veto 1
Begin processing the 6th record. Run 258434, Event 269251857, LumiSection 165 at 09-Dec-2021 12:11:17.751 CET
Begin processing the 7th record. Run 258434, Event 268739237, LumiSection 165 at 09-Dec-2021 12:11:17.751 CET
Begin processing the 8th record. Run 258434, Event 269456225, LumiSection 165 at 09-Dec-2021 12:11:17.752 CET
electron with pt 23.2, eta +0.491, cluster eta +0.483, pass conversion veto 1
Begin processing the 9th record. Run 258434, Event 269845067, LumiSection 165 at 09-Dec-2021 12:11:17.752 CET
electron with pt 23.0, eta -2.378, cluster eta -2.395, pass conversion veto 1
Begin processing the 10th record. Run 258434, Event 268437313, LumiSection 165 at 09-Dec-2021 12:11:17.752 CET
```

## <a name="nice">"Nice! But how do I analyse these data?"</a>

We start off with a quick introduction to **[ROOT](http://root.cern.ch)**. ROOT is the framework used by several particle-physics experiments to work with the collected data. For a quick start on how to write the most common objects and their properties in a root file, use "Physics Object Extractor Tool (POET)" available in [this repository](https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/tree/2015MiniAOD). You can use ROOT to inspect reconstructed particles and the distributions of their properties.

Start by getting the code and compiling it. Make sure that you are back in the the **CMSSW_7_6_7/src/** folder. If you are using the VM, do the next two commands in the "Outer shell" terminal. In the container, keep using the normal container shell.

```shell
$ cd ~/CMSSW_7_6_7/src
$ git clone https://github.com/cms-opendata-analyses/PhysObjectExtractorTool.git
```

If you are using the VM, change now back to the "CMS shell" terminal. Get the 2015 MiniAOD "branch" of the repository and compile the code with:

```
$ cd ~/CMSSW_7_6_7/src
$ cd PhysObjectExtractorTool
$ git checkout 2015MiniAOD
$ scram b
```

Then produce a root file with selected objects by executing:

```shell
$ cd PhysObjectExtractor
$ cmsRun python/poet_cfg.py
```

The configuration file sets it to run over 1000 events in a simulated dataset.

If you are using the CMS open data container with the VNC application installed (see the [container guide page](/docs/cms-guide-docker)), open the graphical user interface in the container by typing

```shell
$ start_vnc
```

and then start the graphics window on your browser with the link provided and using the password `cms.cern`.

You can now open the POET output file in ROOT:

```shell
$ root myoutput.root
```

You will see the ROOT logo appear on screen. You can now open the ROOT GUI by entering:

```shell
TBrowser t
```

and you will see the ROOT browser window:

<img src="/static/docs/getting-started-with-cms-2015-data/getting_started_with_cms_2015_data_1.png" width="70%">

Now, let us take a closer look at some collections of physics objects.

On the left window of ROOT, double-click on the file name (`myoutput.root`). You should see a list of names, each corresponding to a collection of reconstructed data.

Let us take a peek, for example, at the electrons, which are found in `myelectrons`. Look in there by double-clicking on that line and then double-clicking on `Events`. Here, you can have a look at various properties of this collection, such as the transverse momentum of the electrons: `electron_pt`. Double-click on it to draw the distribution.

<img src="/static/docs/getting-started-with-cms-2015-data/getting_started_with_cms_2015_data_2.png" width="70%">

You can exit the ROOT browser through the GUI by clicking on `Browser` on the menu and then clicking on `Quit Root` or by entering `.q` in the terminal.

**NOTE**: To analyse the full event content, the analysis job may need access to the "condition data", such as event selection information. You can see how connections to the condition database are established in [the guide to the CMS condition database](/docs/cms-guide-for-condition-database) and in [the CMS Open data guide](https://cms-opendata-guide.web.cern.ch/). For simpler analyses, in which only physics objects needing no further data are used, you do not need to connect to the condition database.

Note also that in your analysis of collision data, you would need to filter only the validated events by downloading [the validated data definition file](/record/14210) and adding these lines the job configuration:

```python
import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
myLumis = LumiList.LumiList(filename='Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt').getCMSSWString().split(',')
```

Add the following statements after the `process.source` input file definition:

```python
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)
```

This selection must always be applied to any analysis on CMS open data, and to do so you must have the validation file downloaded to your local area.

That's it! Hope you enjoyed this exercise. Feel free to play around with the rest of the data and write your own analyzers and analysis code. Learn more in [the CMS Open data guide](https://cms-opendata-guide.web.cern.ch/).
