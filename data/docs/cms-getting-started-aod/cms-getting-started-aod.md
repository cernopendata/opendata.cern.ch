1. ["What software environment do I need to use CMS AOD open data?"](#vm)
2. ["OK! What is in the CMS data?"](#data)
3. ["Nice! But how do I analyze these data?"](#nice)

The CMS primary data collected in 2010-2012 are provided on the CERN Open Data Portal in the Analysis Object Data (AOD) format. This page provides tutorials on how to access and analyze CMS data in this format for each year.

# <a name="vm">"What software environment do I need to use CMS AOD open data?"</a>

To analyze CMS data in AOD format, you need to use CMSSW, supported on <b>Scientific Linux</b>. If you are unfamiliar with Linux, take a look at <a href="https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBasicLinux">this short introduction to Linux</a> or <a href="https://swcarpentry.github.io/shell-novice/">tutorial</a>. To access CMSSW, you will need to install a [docker container](/docs/cms-guide-docker) or the [CMS-specific CERN Virtual Machine](https://opendata.cern.ch/search?page=1&size=20&tags=VM&experiment=CMS). Version information is available under the drop-down links below for different years of CMS data collection.

<details>
<summary>2010</summary>
<p>
To analyse CMS data collected in 2010, you need <b>version 4.2.8</b> of CMSSW, supported on Scientific Linux 5. Once you have installed the <a href="/docs/cms-guide-docker>CMS open data container</a> or the <a href="/docs/cms-virtual-machine-2010">CMS-specific CERN Virtual Machine (VM)</a>, you need to open a terminal.
</p>
<p>
If you are using the "CMS-OpenData-1.1.2" VM, always use the "CMS shell" terminal available from the "CMS Shell" icon on the desktop for all CMSSW-specific commands. (If instead you have the "CMS-OpenData-1.0.0-rc7" VM, open a terminal with the X terminal emulator from an icon in thebottom-left of the VM screen). Execute the following command in the terminal if you haven't done so before; it ensures that you have this version of CMSSW running:
</p>
```shell
$ cmsrel CMSSW_4_2_8
```
<p>
In the VM, the CMS analysis environment needs to be properly set up by entering the following commands in the terminal (you must do so every time you boot the VM before you can proceed):
</p>
```shell
$ cd CMSSW_4_2_8/src/
$ cmsenv # do not execute this command if you are working in the container
```
<br>
</details>

<details>
<summary>2011-2012</summary>
<p>
To analyse CMS data collected in 2011-2012, you need <b>version 5.3.32</b> of CMSSW, supported on Scientific Linux 6. Once you have installed the <a href="/docs/cms-guide-docker>CMS open data container</a> or the <a href="/docs/cms-virtual-machine-2011">CMS-specific CERN Virtual Machine (VM)</a>, you need to open a terminal.
</p>
<p>
If you are using the VM, always use the "CMS shell" terminal available from the "CMS Shell" icon on the desktop for all CMSSW-specific commands. In the VM, execute the following command in the terminal if you haven't done so before; it ensures that you have this version of CMSSW running:
</p>
```shell
$ cmsrel CMSSW_5_3_32
```
<p>
Note that if you get a warning message about the current OS not being slc6, you are using a wrong terminal ("Outer Shell") which is CERN CentOS 7 (cc7). Open a "CMS Shell" terminal as explained above and execute the cmsrel command there.
</p>
<p>
In the VM, the CMS analysis environment needs to be properly set up by entering the following commands in the terminal (you must do so every time you boot the VM before you can proceed):
</p>
```shell
$ cd CMSSW_5_3_32/src/
$ cmsenv # do not execute this command if you are working in the container
```
<p>
Make sure that you are always in the <b>CMSSW_5_3_32/src/</b> directory, both in the CMS open data container and in the VM (and in the "CMS Shell" terminal in VM).
</p>
<br>
</details>

# <a name="data"> "OK! What is in the CMS data?" </a>

The AOD files contain all the information that is needed for physics analysis. These files are prepared by piecing raw data collected by various sub-detectors of CMS. A list of the physics objects contained in the AOD files can be found through the links for <a href="/docs/cms-physics-objects-2010">2010</a> and for <a href="/docs/cms-physics-objects-2011">2011-2012</a>. The files cannot be opened and understood as simple data tables but require [ROOT](https://root.cern.ch), a framework used by several particle-physics experiments to work with the collected data, in order to be read.

Let's see what physics objects are contained in an AOD file. Make sure that you are in the <b>CMSSW_X_Y_Z/src/</b> folder (according to the versions described above), and, in the VM, that you are using the correct terminal and have executed the `cmsenv` command to launch the CMS analysis environment. Here we will investigate a AOD file collected in 2010 -- you may adapt the example to investigate AOD collected in other years by using these test files, or by selecting a file from a dataset. (For example, visit the <a href="/record/24404">Mu primary dataset</a> from Run2010B. Click the "Download" tab at the bottom of the page to see a list of files contained in this dataset. You can select a file from the list.)

* 2010 data: root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
* 2011-2012 data: root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root

Print out the contents of the MINIAOD file by executing:

```shell
$ edmDumpEventContent root://eospublic.cern.ch//eos/opendata/cms/Run2010B/Mu/AOD/Apr21ReReco-v1/0000/00459D48-EB70-E011-AF09-90E6BA19A252.root
```

The ouput is a list of objects that the file contains, such as

```shell
    Type                                  Module                      Label             Process
    ----------------------------------------------------------------------------------------------
    edm::TriggerResults                   "TriggerResults"            ""                "HLT"
    trigger::TriggerEvent                 "hltTriggerSummaryAOD"      ""                "HLT"
    [...]
    vector<reco::GsfElectron>             "gsfElectrons"              ""                "RECO"
    [...]
    vector<reco::Muon>                    "muons"                     ""                "RECO"
    [...]
```

Documentation of these objects is available in <a href="https://cms-opendata-guide.web.cern.ch/analysis/selection/objects/objects/">the CMS Open Data guide</a>. The objects are implemented as C++ classes in the CMS software package [CMSSW](https://github.com/cms-sw/cmssw), and detailed reference documentation of all classes is available in the class list of the CMSSW reference manual ([2010 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_4_2_8/doc/html/annotated.html), [2011-2012 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_5_3_30/doc/html/annotated.html)). To see the properties of electrons, you would navigate to the namespace "reco" and find the entry for <code>GsfElectron</code>. The <code>reco::GsfElectron</code> Class Reference ([2010 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_4_2_8/doc/html/d0/d6d/classreco_1_1GsfElectron.html), [2011-2012 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_5_3_30/doc/html/d0/d6d/classreco_1_1GsfElectron.html)) lists all member functions through which the different properties of reconstructed electron can be accessed. Note that many of the basic propertied are "inherited" from the parent classes, and are listed separately under "Public Member Functions inherited from ... ". You can find more information about each object in the CMS Open Data guide (e.g. <a href="https://cms-opendata-guide.web.cern.ch/analysis/selection/objects/electrons/">electrons</a>

# <a name="nice">"Nice! But how do I analyze these data?"</a>

You can perform analysis on the AOD dataset directly, or you can first "reduce" AOD data by applying basic event filters and perform all iterative analysis steps using this reduced (or "derived") dataset. Processing the AOD datasets is computationally heavy, so producing reduced datasets is typically preferable for large-scale analyses.

**Note: Collision data in NanoAOD format has not been filtered to contain only the validated run segments. A `json` file containing validated run segments can be found in the links on each collision dataset record.**

We will first see how to perform analysis on the primary AOD dataset, and then introduce tools for reducing AOD datasets.

## Analyzing the primary AOD dataset using EDAnalyzer

The objects contained in the AOD files can be accessed through a software module called <code>EDAnalyzer</code>, which can be built with a helper script available in the CMS open data environment.

In the CMS environment (after running <code>cmsenv</code> if you are using the VM), do the following:

```shell
$ mkdir Demo
$ cd Demo
$ mkedanlzr DemoAnalyzer
$ cd DemoAnalyzer
```

This will create several template files in the new DemoAnalyzer directory. For more information about CMSSW analyzer modules, have a look in <a href="https://cms-opendata-guide.web.cern.ch/cmssw/cmsswanalyzers/">the CMS open data guide</a>.

Compile the code with:

```shell
$ scram b
```

You can ignore the message

```
    ****WARNING: No need to export library once you have declared your library as plugin.
            Please cleanup src/Demo/DemoAnalyzer/BuildFile by removing the <export></export> section.
```

or take action and remove the indicated section from <code>BuildFile.xml</code>.

Change the file name in the configuration file <code>demoanalyzer_cfg.py</code> in the <code>DemoAnalyzer</code> directory by replacing <code>file:myfile.root</code> with your chosen file (such as a test file from the list above for 2010 or 2011-2012 data).

Change the max number of events to 10 (i.e change <code>-1</code> to <code>10</code> in <code>process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1)</code>). The default <code>-1</code> means running over all events.

Run the code with:

```shell
$ cmsRun demoanalyzer_cfg.py
```

You will get an output like the following, depending on the test file you have used:

```
    221119 18:53:23 1032 Xrd: XrdClientConn: Error resolving this host's domain name.
    221119 18:53:23 1032 secgsi_InitProxy: cannot access private key file: /home/cmsusr/.globus/userkey.pem
    221119 18:53:23 1032 Xrd: CheckErrorStatus: Server [eospublic.cern.ch] declared: (error code: 3005)
    19-Nov-2022 18:53:23 CET  Initiating request to open file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root
    19-Nov-2022 18:53:26 CET  Successfully opened file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root
    Begin processing the 1st record. Run 206401, Event 240060474, LumiSection 178 at 19-Nov-2022 18:54:37.199 CET
    Begin processing the 2nd record. Run 206401, Event 240069594, LumiSection 178 at 19-Nov-2022 18:54:37.227 CET
    Begin processing the 3rd record. Run 206401, Event 240049754, LumiSection 178 at 19-Nov-2022 18:54:37.228 CET
    Begin processing the 4th record. Run 206401, Event 240115594, LumiSection 178 at 19-Nov-2022 18:54:37.228 CET
    Begin processing the 5th record. Run 206401, Event 240154770, LumiSection 178 at 19-Nov-2022 18:54:37.229 CET
    Begin processing the 6th record. Run 206401, Event 240103386, LumiSection 178 at 19-Nov-2022 18:54:37.229 CET
    Begin processing the 7th record. Run 206401, Event 240173338, LumiSection 178 at 19-Nov-2022 18:54:37.230 CET
    Begin processing the 8th record. Run 206401, Event 240127898, LumiSection 178 at 19-Nov-2022 18:54:37.230 CET
    Begin processing the 9th record. Run 206401, Event 240103970, LumiSection 178 at 19-Nov-2022 18:54:37.231 CET
    Begin processing the 10th record. Run 206401, Event 240129066, LumiSection 178 at 19-Nov-2022 18:54:37.231 CET
    19-Nov-2022 18:54:37 CET  Closed file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root

    =============================================

    MessageLogger Summary

    type     category        sev    module        subroutine        count    total
    ---- -------------------- -- ---------------- ----------------  -----    -----
        1 fileAction           -s file_close                             1        1
        2 fileAction           -s file_open                              2        2

    type    category    Examples: run/evt        run/evt          run/evt
    ---- -------------------- ---------------- ---------------- ----------------
        1 fileAction           PostEndRun
        2 fileAction           pre-events       pre-events

    Severity    # Occurrences   Total Occurrences
    --------    -------------   -----------------
    System                  3                   3
```

This is a simple loop over the first 10 events in the file.

To access the physics object information, for example, of muons, add the following lines in <code>src/DemoAnalyzer.cc</code> (the lines before and after of the lines to be added are also shown):

```shell
[...]
#include "FWCore/ParameterSet/interface/ParameterSet.h"

//classes to extract Muon information
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include<vector>
//
// class declaration
[...]

      // ----------member data ---------------------------
      std::vector<float> muon_e; //energy values for muons in the event
};
[...]
   using namespace edm;

    //clean the container
    muon_e.clear();

    //define the handler and get by label
    Handle<reco::MuonCollection> mymuons;
    iEvent.getByLabel("muons", mymuons);

    //if collection is valid, loop over muons in event
    if(mymuons.isValid()){
        for (reco::MuonCollection::const_iterator itmuon=mymuons->begin(); itmuon!=mymuons->end(); ++itmuon){
            muon_e.push_back(itmuon->energy());
        }
    }

    //print the vector
    for(unsigned int i=0; i < muon_e.size(); i++){
        std::cout <<"Muon # "<<i<<" with E = "<<muon_e.at(i)<<" GeV."<<std::endl;
    }

#ifdef THIS_IS_AN_EVENT_EXAMPLE
[...]
```

Modify the <code>BuildFile.xml</code> to include <code>DataFormats/MuonReco</code> dependencies so that it becomes:

```shell
<use name="FWCore/Framework"/>
<use name="FWCore/PluginManager"/>
<use name="DataFormats/MuonReco"/>
<use name="FWCore/ParameterSet"/>
<flags EDM_PLUGIN="1"/>
```

Compile and run again with:

```shell
$ scram b
$ cmsRun demoanalyzer_cfg.py
```

The output gives the energy of muons in these events:

```
    19-Nov-2022 19:53:08 CET  Initiating request to open file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root
    19-Nov-2022 19:53:10 CET  Successfully opened file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root
    Begin processing the 1st record. Run 206401, Event 240060474, LumiSection 178 at 19-Nov-2022 19:53:50.971 CET
    Muon # 0 with E = 31.2151 GeV.
    Begin processing the 2nd record. Run 206401, Event 240069594, LumiSection 178 at 19-Nov-2022 19:53:51.000 CET
    Muon # 0 with E = 62.6309 GeV.
    Begin processing the 3rd record. Run 206401, Event 240049754, LumiSection 178 at 19-Nov-2022 19:53:51.001 CET
    Muon # 0 with E = 71.6465 GeV.
    Muon # 1 with E = 3.99535 GeV.
    Begin processing the 4th record. Run 206401, Event 240115594, LumiSection 178 at 19-Nov-2022 19:53:51.001 CET
    Muon # 0 with E = 137.55 GeV.
    Muon # 1 with E = 2.70864 GeV.
    Muon # 2 with E = 4.33524 GeV.
    Begin processing the 5th record. Run 206401, Event 240154770, LumiSection 178 at 19-Nov-2022 19:53:51.002 CET
    Muon # 0 with E = 87.9848 GeV.
    Muon # 1 with E = 4.34456 GeV.
    Begin processing the 6th record. Run 206401, Event 240103386, LumiSection 178 at 19-Nov-2022 19:53:51.002 CET
    Muon # 0 with E = 30.2197 GeV.
    Muon # 1 with E = 11.064 GeV.
    Muon # 2 with E = 10.8193 GeV.
    Begin processing the 7th record. Run 206401, Event 240173338, LumiSection 178 at 19-Nov-2022 19:53:51.003 CET
    Muon # 0 with E = 6.84971 GeV.
    Muon # 1 with E = 12.0909 GeV.
    Muon # 2 with E = 3.20224 GeV.
    Muon # 3 with E = 7.04104 GeV.
    Muon # 4 with E = 7.90646 GeV.
    Muon # 5 with E = 6.20379 GeV.
    Begin processing the 8th record. Run 206401, Event 240127898, LumiSection 178 at 19-Nov-2022 19:53:51.003 CET
    Muon # 0 with E = 42.8793 GeV.
    Muon # 1 with E = 3.31122 GeV.
    Muon # 2 with E = 3.85927 GeV.
    Muon # 3 with E = 3.0424 GeV.
    Begin processing the 9th record. Run 206401, Event 240103970, LumiSection 178 at 19-Nov-2022 19:53:51.003 CET
    Muon # 0 with E = 55.7221 GeV.
    Muon # 1 with E = 2.80195 GeV.
    Begin processing the 10th record. Run 206401, Event 240129066, LumiSection 178 at 19-Nov-2022 19:53:51.004 CET
    Muon # 0 with E = 33.7197 GeV.
    Muon # 1 with E = 4.90223 GeV.
    Muon # 2 with E = 5.61441 GeV.
    19-Nov-2022 19:53:51 CET  Closed file root://eospublic.cern.ch//eos/opendata/cms/Run2012D/SingleMu/AOD/22Jan2013-v1/10000/0015EC7D-EAA7-E211-A9B9-E0CB4E5536A7.root
```

<strong>NOTE</strong>: To analyze the full event content, the analysis job needs access to the "condition data", such as the jet-energy corrections. To see how the connection to the condition database is established, you can check the <a href="/docs/cms-guide-for-condition-database">Guide to the CMS condition database</a>. For simpler analyses, like the example above, where we use only physics objects needing no further data for corrections, you do not need to connect to the condition database.

For detailed examples on applying selections and analyzing the full event content of AOD files through EDAnalyzer, refer to <a href="/record/560">this CMS analysis example for 2010 data</a> and <a href="/record/5500">this CMS analysis example for 2011-2012 data</a>. Take a look at the scripts to learn how selections and extractions are done.

Next, let's see how to produce and analyze reduced datasets.

## Analyzing reduced datasets

AOD data can be reduced to simpler formats that contain ROOT trees based on standard C++ classes (integers, floats, vectors, etc) instead of custom CMS C++ classes, and thus can be read directly through ROOT without CMSSW. Within CMS, this type of data is referred to as "analysis ntuples" or, beginning in Run 2, "NanoAOD". For Open Data analyses, we can reduce the AOD data to some NanoAOD-like formats, using one of the two available production tools:

* 2010 data: <a href="https://github.com/cms-opendata-analyses/NanoAODRun1ProducerTool">NanoAODRun1 Producer</a>
* 2011 data: <a href="https://github.com/cms-opendata-analyses/NanoAODRun1ProducerTool">NanoAODRun1 Producer</a>, [Physics Object Extractor Tool](https://opendata.cern.ch/record/12501) (using the "2011" branch of the corresponding <a href="https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/tree/2011">Github repository</a>).
* 2012 data: <a href="https://github.com/cms-opendata-analyses/NanoAODRun1ProducerTool">NanoAODRun1 Producer</a>, [Physics Object Extractor Tool](https://opendata.cern.ch/record/12501)

The NanoAODRun1 producer tool is based on the CMS NanoAOD production software used in Run 2, while the Physics Object Extractor Tool (POET) is a collection of EDAnalyzers like the one we saw in the <a href="#EDAnalyzer">previous subsection</a>.

#### Reduce the AOD files to NanoAODRun1 files

The NanoAODRun1 format is a NanoAOD-like ROOT file format for CMS Run 1 data, readable with bare ROOT or other ROOT-compatible software. It contains the per-event information that is needed in most generic analyses. The goal is that about 50% of all publishable Open Data analyses can be performed using this simplified and easy-to-access data format without compromise of the quality of the scientific result. A list of variables in NanoAODRun1 MC data can be found <a href="https://twiki.cern.ch/twiki/pub/CMSPublic/WorkBookNanoAODRun1/doc_DYJetsToLL_M-50_7TeV.html">here</a>. Collision data contains the same variables, except for the generator-level information.

**Note:** the NanoAODRun1 data format should not be confused with another NanoAOD-like <a href="/record/12353">reduced format created for educational purposes rather than for analysis purposes</a>, which is sometimes also referred to as "NanoAOD" in the Open Data context.

Some datasets have already been processed as NanoAODRun1 files, and new datasets can be processed by following the <a href="https://github.com/cms-opendata-analyses/NanoAODRun1ProducerTool">instructions on Github</a>. (**Note**: User customization is not supported for NanoAODRun1, but files can be produced according to this tool.)

Analysis examples using NanoAODRun1 datasets with ROOT in C++ and Python formats for 2010, 2011, and 2012 data are available [in this Github repository](http://github.com/cms-opendata-analyses/NanoAODRun1Examples). The ROOT [docker container](/docs/cms-guide-docker/) is used to perform the example analyses.

#### Reduce the AOD files using POET (2011-2012 data)

The Physics Object Extractor Tool (POET) allows you to filter for validated data, apply selection criteria to select useful events and write out physics objects and their properties to a reduced dataset. For a quick start, check <a href="https://opendata.cern.ch/record/12501">this page</a>. After producing POET files, you can use <a href="http://root.cern.ch">ROOT</a> to inspect reconstructed particles and the distributions of their properties.

Start by getting the code and compiling it. (Note that POET is not supported for the 2010 data, which requires an older version of CMSSW) Make sure that you are back in the <b>CMSSW_5_3_32/src/</b> folder. If you are using the VM, do the git command to get the code in the "Outer shell" terminal. Go to the right folder with <code>cd ~/CMSSW_5_3_32/src</code>. In the container, keep using the normal container shell and go to the right folder with <code>cd $CMSSW_BASE/src</code>.

```shell
$ git clone https://github.com/cms-opendata-analyses/PhysObjectExtractorTool.git
```

If you are using the VM, change back now to the "CMS shell" terminal. Check out the 2011 or 2012 "branch" of the repository for analyzing 2011 or 2012 data -- while the CMSSW version is the same various algorithms to identify or correct physics objects that are provided in POET vary between years. In the following example, we use the 2012 data, so we checkout the 2012 branch. Make sure that you are always in the <b>CMSSW_5_3_32/src/</b> folder. Checkout the branch and compile the code with:

```shell
$ cd PhysObjectExtractorTool
$ git checkout 2012  # or 2011
$ scram b
```

Note how only the validated runs are selected in the configuration file. The relevant lines are:

```python
  import FWCore.ParameterSet.Config as cms
  import FWCore.PythonUtilities.LumiList as LumiList

  [...]

  goodJSON = "data/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt"
  myLumis = LumiList.LumiList(filename=goodJSON).getCMSSWString().split(",")
  process.source.lumisToProcess = CfgTypes.untracked(
        CfgTypes.VLuminosityBlockRange())
  process.source.lumisToProcess.extend(myLumis)
```

This selection must always be applied to any analysis on CMS open data, and to do so you must have the validation file downloaded to your local area.

To produce a root file with selected objects, do the following:

```shell
$ cd PhysObjectExtractor
$ cmsRun python/poet_cfg.py
```

The default configuration file is set to run over 100 events in a simulated dataset. The script runs over all the events when the `process.maxEvents` value is set to -1.

We can check the content of the output ROOT file using the ROOT command line and make basic plots through an interactive Graphical User Interface (GUI). We use this example to show how to do so with the ROOT GUI.

If you are using the CMS open data container with the VNC application installed (see the <a href="/docs/cms-guide-docker#vnc">container guide page</a>), for opening the graphical user interface, start the VNC application in the container by typing

```shell
$ start_vnc
```

Then start a VNC viewer on your local computer using the password <code>cms.cern</code>. The http option for a GUI in the browser is not guaranteed to work in the container with this CMSSW version. In the VM, X11 graphics are supported without needing VNC.

You can now open the POET output file in ROOT:

```shell
$ root myoutput.root
```

You will see the ROOT logo appear on screen. You can now open the ROOT GUI by entering:

```shell
TBrowser t
```

You will see the ROOT browser window:

<img src="/static/docs/cms-getting-started-aod/getting_started_with_cms_2011_2012_data_1.png" width="70%"><br>

Now, let us take a closer look at some collections of the physics objects.

On the left window of ROOT, double-click on the file name (<code>myoutput.root</code>). You should see a list of names, each corresponding to a collection of reconstructed data.

Let us take a peek, for example, at the muons, which are found in <code>mymuons</code>. Look in there by double-clicking on that line and then double-clicking on <code>Events</code>. Here, you can have a look at various properties of this collection, such as the transverse momentum of the muon: <code>muon_pt</code>. Double-click on it to draw the distribution.

<img src="/static/docs/cms-getting-started-aod/getting_started_with_cms_2011_2012_data_2.png" width="70%"><br>

You can exit the ROOT browser through the GUI by clicking on <code>Browser</code> on the menu and then clicking on <code>Quit Root</code> or by entering <code>.q</code> in the terminal.

POET ROOT files have a very similar structure to NanoAODRun1 files, with a separate `TTree` for each physics object. The [NanoAODRun1 Examples](http://github.com/cms-opendata-analyses/NanoAODRun1Examples) show various methods to select events and produce complex histograms using this type of ROOT file. The TTrees within POET files can be linked together using the [TTree "friend" method](https://root.cern/manual/trees/#widening-a-ttree-through-friends).

That's it! Hope you enjoyed the exercises. Feel free to play around with the rest of the data and write your own analyzers and analysis code. Learn more in <a href="https://cms-opendata-guide.web.cern.ch/">the CMS Open data guide</a>. Many tutorial lessons can be found in the <a href="https://cms-opendata-guide.web.cern.ch/cmsOpenData/workshops/">CMS Open Data Workshops</a>, particularly from 2020-2021 for AOD data.
