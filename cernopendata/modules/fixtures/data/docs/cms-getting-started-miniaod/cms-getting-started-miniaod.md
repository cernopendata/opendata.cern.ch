1. ["What software environment do I need to use CMS MiniAOD open data?"](#vm)
2. ["OK! What is in the CMS data?"](#data)
3. ["Nice! But how do I analyse these data?"](#nice)

The CMS primary data collected in 2015 and beyond are provided on the CERN Open Data Portal in a reduced ("mini") Analysis Object Data (MiniAOD) format. This page provides tutorials on how to access and analyze CMS data in this format.

## <a name="env">"What software environment do I need to use CMS MiniAOD open data?"</a>

To analyze CMS data in MiniAOD format, you need to use CMSSW, supported on <b>Scientific Linux</b>. If you are unfamiliar with Linux, take a look at <a href="https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBasicLinux">this short introduction to Linux</a>. To access CMSSW, you will need to install a [docker container](/docs/cms-guide-docker) or the [CMS-specific CERN Virtual Machine](https://opendata.cern.ch/search?page=1&size=20&tags=VM&experiment=CMS). Version information is available under the drop-down links below for different years of CMS data collection.

<details>
<summary> 2015 </summary>
<p>
To analyse CMS data collected in 2015, you need <b>version 7.6.7</b> of CMSSW, supported on Scientific Linux 6. Once you have installed the <a href="/docs/cms-guide-docker>CMS open data container</a> or the <a href="/docs/cms-virtual-machine-2015">CMS-specific CERN Virtual Machine (VM)</a>, you need to open a terminal.
</p>
If you are using the VM, always use the "CMS shell" terminal available from the "CMS Shell" icon on the desktop for all CMSSW-specific commands, such as compilation and run. In the VM, execute the following command in the terminal if you haven't done so before; it ensures that you have this version of CMSSW running:

```shell
$ cmsrel CMSSW_7_6_7
```
<p>
Note that if you get a warning message about the current OS not being slc6, you are using a wrong terminal ("Outer Shell") which is CERN CentOS 7 (cc7). Open a "CMS Shell" terminal as explained above and execute the cmsrel command there.
</p>
<p>
Both in the CMS open data container and in the VM, make sure that you are always in the <b>CMSSW_7_6_7/src/</b> directory (and in the "CMS Shell" terminal in VM).
</p>
In the VM, the CMS analysis environment needs to be properly set up by entering the following commands in the terminal (you must do so every time you boot the VM before you can proceed):

```shell
$ cd CMSSW_7_6_7/src/
$ cmsenv # do not execute this command if you are working in the container
```
<br>
</details>

<details>
<summary> 2016 </summary>
<p>
To analyse CMS data collected in 2016, you need <b>version 10.6.30</b> of CMSSW, supported on Scientific Linux 7. Once you have installed the <a href="/docs/cms-guide-docker">CMS open data container</a> or the <a href="/docs/cms-virtual-machine-cc7">CMS-specific CERN Virtual Machine (VM)</a>, you need to open a terminal.
</p>
If you are using the VM, always use the "CMS shell" terminal available from the "CMS Shell" icon on the desktop for all CMSSW-specific commands, such as compilation and run. In the VM, execute the following command in the terminal if you haven't done so before; it ensures that you have this version of CMSSW running:

```shell
$ cmsrel CMSSW_10_6_30
```
<p>
Both in the CMS open data container and in the VM, make sure that you are always in the <b>CMSSW_10_6_30/src/</b> directory (and in the "CMS Shell" terminal in VM).
</p>
<p>
In the VM, the CMS analysis environment needs to be properly set up by entering the following commands in the terminal (you must do so every time you boot the VM before you can proceed):
</p>
```shell
$ cd CMSSW_10_6_30/src/
$ cmsenv
```
<br>
</details>

## <a name="data">"OK! What is in the CMS data?"</a>

The primary data provided by CMS on the CERN Open Data Portal is in a format called <a href="/docs/cms-physics-objects-2015">Analysis Object Data</a> or AOD for short, and from 2015 onwards, in a slimmer format called MINIAOD. These AOD files are prepared by piecing raw data collected by various sub-detectors of CMS and contain all the information that is needed for analysis. The files cannot be opened and understood as simple data tables but require specific sofware in order to be read.

So, let's see what a MINIAOD file looks like. Make sure that you are in the <b>CMSSW_X_Y_Z/src/</b> folder (according to the versions described above), and, in the VM, that you have executed the `cmsenv` command in your terminal to launch the CMS analysis environment. Here we will investigate a MINIAOD file collected in 2015 -- you may adapt the example to investigate MINIAOD collected in other years by using these test files, or by selecting a file from a dataset. (For example, visit the <a href="/record/24117">Tau primary dataset</a> from Run2015D. Click one of the "Download" tabs at the bottom of the page to see a list of files contained in this dataset. You can select a file from the list.)

* 2015 data: root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root
* 2016 data: root://eospublic.cern.ch//eos/opendata/cms/Run2016G/SingleElectron/MINIAOD/UL2016_MiniAODv2-v2/120000/FF99404A-8F07-444E-B931-7B2AE327070B.root

Print out the contents of the MINIAOD file by executing:

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

Documentation of these objects is available in the CMS SWGuide Workbook MiniAOD pages ([2015 data](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#High_level_physics_objects), [2016 data](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#High_level_physics_objects)). The objects are implemented as C++ classes in the CMS software package [CMSSW](https://github.com/cms-sw/cmssw), and detailed reference documentation of all classes is available in the class list of the CMSSW reference manual ([2015 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/annotated.html), [2016 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_10_6_30//doc/html/annotatedList.html)). To see the properties of electrons, you would navigate to namespace "pat" and find the entry for "Electron". The <code>pat::Electron</code> Class Reference ([2015 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/d2/d1f/classpat_1_1Electron.html), [2016 data](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_10_6_30/doc/html/d2/d1f/classpat_1_1Electron.html)) lists all member functions through which the different properties of reconstructed electron can be accessed. Note that many of the basic propertied are "inherited" from the parent classes, and are listed separately under "Public Member Functions inherited from ... ".

These objects can be accessed in a software module called an `EDAnalyzer`. To create an example `EDAnalyzer`, follow the installation instructions below depending on your analysis environment:

<details>
<summary>2015 docker container</summary>
<p>
Create an <code>EDAnalyzer</code>using the built-in helper script <code>mkedanlzr</code>:
</p>

```shell
$ mkdir Test
$ cd Test
$ mkedanlzr MiniAnalyzer
$ cd MiniAnalyzer
```

<p>
This will create several template files in the new MiniAnalyzer directory. For more information, have a look in <a href="https://cms-opendata-guide.web.cern.ch/cmssw/cmsswanalyzers/">the CMS open data guide</a>.
</p>
<p>
To run over the example file, change the input file name <code>file:myfile.root</code>in <code>python/ConfFile_cfg.py</code>to <code>root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root</code>(or your chosen MiniAOD test file). Change the number of events from <code>-1</code>(runs over all events in the file) to <code>10</code>for testing. To access the physics object properties, add <code>&#60;use name="DataFormats/PatCandidates"/&#62;</code>in <code>plugins/BuildFile.xml</code>.
</p>
<br>
</details>

<details>
<summary>2015 VM, 2016 VM, or 2016 docker container</summary>
<p>
Download example <code>EDAnalyzer</code>scripts from <a href="https://github.com/cms-opendata-analyses/MiniAnalyzer_CMSSW_10_6_30">this Github repository</a> into a directory two levels below <code>src/</code> by executing the following command (using `Test/MiniAnalyzer/` in the command provides the directory structure needed for CMSSW to work):
</p>

```shell
$ git clone https://github.com/cms-opendata-analyses/MiniAnalyzer_CMSSW_10_6_30 Test/MiniAnalyzer/
$ cd Test/MiniAnalyzer
```

<p>
This example analyzer contains an example file from a 2016 MiniAOD data in the <code>python/ConfFile_cfg.py</code>configuration file. You can change this test file to any other 2015 or 2016 MiniAOD (or MiniAODSIM) file. The example is also set to process 10 events.
</p>
<br>
</details>
<br>
Compile the code with:

```shell
$ scram b
```
You can run this "empty" analyzer to see that the data are accessed properly:

```shell
(/code/CMSSW_10_6_30/src/Test/MiniAnalyzer) cmsRun python/ConfFile_cfg.py
26-Mar-2024 17:34:32 CET  Initiating request to open file root://eospublic.cern.ch//eos/opendata/cms/Run2016G/SingleElectron/MINIAOD/UL2016_MiniAODv2-v2/120000/FF99404A-8F07-444E-B931-7B2AE327070B.root
240326 17:34:32 865 secgsi_InitProxy: cannot access private key file: /home/cmsusr/.globus/userkey.pem
%MSG-w XrdAdaptor:  file_open 26-Mar-2024 17:34:35 CET pre-events
Data is served from cern.ch instead of original site eospublic
%MSG
26-Mar-2024 17:34:48 CET  Successfully opened file root://eospublic.cern.ch//eos/opendata/cms/Run2016G/SingleElectron/MINIAOD/UL2016_MiniAODv2-v2/120000/FF99404A-8F07-444E-B931-7B2AE327070B.root
Begin processing the 1st record. Run 280363, Event 187657341, LumiSection 116 on stream 0 at 26-Mar-2024 17:34:59.995 CET
Begin processing the 2nd record. Run 280363, Event 186936772, LumiSection 116 on stream 0 at 26-Mar-2024 17:34:59.997 CET
Begin processing the 3rd record. Run 280363, Event 186325056, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.000 CET
Begin processing the 4th record. Run 280363, Event 187418881, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.001 CET
Begin processing the 5th record. Run 280363, Event 186613060, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.001 CET
Begin processing the 6th record. Run 280363, Event 186347521, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.001 CET
Begin processing the 7th record. Run 280363, Event 186424707, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.004 CET
Begin processing the 8th record. Run 280363, Event 186377469, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.004 CET
Begin processing the 9th record. Run 280363, Event 187712063, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.004 CET
Begin processing the 10th record. Run 280363, Event 187347460, LumiSection 116 on stream 0 at 26-Mar-2024 17:35:00.004 CET
26-Mar-2024 17:35:00 CET  Closed file root://eospublic.cern.ch//eos/opendata/cms/Run2016G/SingleElectron/MINIAOD/UL2016_MiniAODv2-v2/120000/FF99404A-8F07-444E-B931-7B2AE327070B.root

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
    2 fileAction           PostGlobalEndRun
    3 fileAction           pre-events       pre-events

Severity    # Occurrences   Total Occurrences
--------    -------------   -----------------
Warning                 1                   1
System                  3                   3

dropped waiting message count 0
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
Begin processing the 1st record. Run 280363, Event 187657341, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:17.116 CET
electron with pt 30.8, eta -0.795, cluster eta -0.789, pass conversion veto 1
Begin processing the 2nd record. Run 280363, Event 186936772, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.200 CET
electron with pt 42.8, eta -2.243, cluster eta -2.252, pass conversion veto 1
electron with pt 38.5, eta -2.154, cluster eta -2.162, pass conversion veto 1
Begin processing the 3rd record. Run 280363, Event 186325056, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.202 CET
electron with pt 32.0, eta +1.864, cluster eta +1.859, pass conversion veto 1
Begin processing the 4th record. Run 280363, Event 187418881, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.205 CET
electron with pt 33.8, eta -1.882, cluster eta -1.884, pass conversion veto 1
Begin processing the 5th record. Run 280363, Event 186613060, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.206 CET
electron with pt 48.5, eta +2.082, cluster eta +2.096, pass conversion veto 1
electron with pt  5.5, eta +2.324, cluster eta +2.328, pass conversion veto 1
Begin processing the 6th record. Run 280363, Event 186347521, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.206 CET
electron with pt 27.2, eta -0.647, cluster eta -0.646, pass conversion veto 1
Begin processing the 7th record. Run 280363, Event 186424707, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.208 CET
electron with pt 142.9, eta -2.304, cluster eta -2.320, pass conversion veto 1
Begin processing the 8th record. Run 280363, Event 186377469, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.211 CET
electron with pt 23.8, eta +1.947, cluster eta +1.956, pass conversion veto 1
Begin processing the 9th record. Run 280363, Event 187712063, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.212 CET
electron with pt 132.1, eta -1.534, cluster eta -1.546, pass conversion veto 1
electron with pt 15.3, eta -0.924, cluster eta -0.938, pass conversion veto 1
electron with pt  9.2, eta -0.988, cluster eta -0.991, pass conversion veto 1
Begin processing the 10th record. Run 280363, Event 187347460, LumiSection 116 on stream 0 at 26-Mar-2024 17:51:20.212 CET
electron with pt 33.6, eta +1.325, cluster eta +1.366, pass conversion veto 1
```

Note that the specific output will look slightly different for other MiniAOD test files, but should contain the same features.

## <a name="nice">"Nice! But how do I analyse these data?"</a>

Typically, analysts prefer to process MiniAOD files using EDAnalyzers so that the data of interest can be written out into some other file format. Above, you saw an example of extracting data into text format. Within CMS, analysts often process MiniAOD to create smaller ROOT files containing TTree objects in standard C++ data types such as integers, floats, arrays, or vectors. These files can then be analyzed with ROOT or Python tools outside of CMSSW. For processing 2015 MiniAOD files, a collection of EDAnalyzers called the [Physics Object Extractor Tool](/record/12502) is available. Most 2016 MiniAOD datasets have corresponding "NanoAOD" datasets available on the portal. More details about analyzing MiniAOD from different years are given in the drop-down links below.

**Note: Collision data in MiniAOD format has not been filtered to contain only the validated run segments. A `json` file containing validated run segments can be found in the links on each collision dataset record.**

<details>
<summary> 2015 </summary>
<p>
We start off with a quick introduction to <b><a href="http://root.cern.ch">ROOT</a></b>. ROOT is the framework used by several particle-physics experiments to work with the collected data. For a quick start on how to write the most common objects and their properties in a ROOT file, use the "Physics Object Extractor Tool (POET)" available from <a href="https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/tree/2015MiniAOD">this repository</a>. You can use ROOT to inspect reconstructed particles and the distributions of their properties.
</p>
<p>
Start by getting the code and compiling it. Make sure that you are back in the the <b>CMSSW_7_6_7/src/</b> folder. If you are using the VM, do the next two commands in the "Outer shell" terminal. In the container, keep using the normal container shell.
</p>

```shell
$ cd ~/CMSSW_7_6_7/src
$ git clone https://github.com/cms-opendata-analyses/PhysObjectExtractorTool.git
```

(If you are using the VM, change now back to the "CMS shell" terminal.) Get the 2015 MiniAOD "branch" of the repository and compile the code with:

```shell
$ cd ~/CMSSW_7_6_7/src
$ cd PhysObjectExtractorTool
$ git checkout 2015MiniAOD
$ scram b
```

Then produce a ROOT file with selected objects by executing:

```shell
$ cd PhysObjectExtractor
$ cmsRun python/poet_cfg.py
```

The configuration file will run over 1000 events in a simulated MiniAOD dataset.

If you are using the CMS open data container with the VNC application installed (see the <a href="/docs/cms-guide-docker">container guide page</a>), open the graphical user interface in the container by typing

```shell
$ start_vnc
```

and then start the graphics window on your browser with the link provided and using the password <code>cms.cern</code>.

You can now open the POET output file in ROOT:

```shell
$ root myoutput.root
```

You will see the ROOT logo appear on screen. You can now open the ROOT GUI by entering:

```shell
TBrowser t
```

and you will see the ROOT browser window:<br>

<img src="/static/docs/cms-getting-started-miniaod/getting_started_with_cms_2015_data_1.png" width="70%"><br>
<p>
Now, let us take a closer look at some collections of physics objects.
</p>
<p>
On the left window of ROOT, double-click on the file name (<code>myoutput.root</code>). You should see a list of names, each corresponding to a collection of reconstructed data.
</p>
Let us take a peek, for example, at the electrons, which are found in <code>myelectrons</code>. Look in there by double-clicking on that line and then double-clicking on <code>Events</code>. Here, you can have a look at various properties of this collection, such as the transverse momentum of the electrons: <code>electron_pt</code>. Double-click on it to draw the distribution.<br>

<img src="/static/docs/cms-getting-started-miniaod/getting_started_with_cms_2015_data_2.png" width="70%"><br>

<p>
You can exit the ROOT browser through the GUI by clicking on <code>Browser</code> on the menu and then clicking on <code>Quit Root</code> or by entering <code>.q</code> in the terminal.
</p>
<p>
<b>NOTE</b>: To analyse the full event content, the analysis job may need access to the "condition data", such as event selection information. You can see how connections to the condition database are established in <a href="/docs/cms-guide-for-condition-database">the guide to the CMS condition database</a> and in <a href="https://cms-opendata-guide.web.cern.ch/">the CMS Open data guide</a>. For simpler analyses, in which only physics objects needing no further data are used, you do not need to connect to the condition database.
</p>
Note also that in your analysis of collision data, you would need to filter only the validated events by downloading <a href="/record/14210">the validated data definition file</a> and adding these lines the job configuration:

```python
import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
myLumis = LumiList.LumiList(filename='Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_v2.txt').getCMSSWString().split(',')
```

Add the following statements after the <code>process.source</code> input file definition:

```python
process.source.lumisToProcess = cms.untracked.VLuminosityBlockRange()
process.source.lumisToProcess.extend(myLumis)
```
<p>
This selection must always be applied to any analysis on CMS open data, and to do so you must have the validation file downloaded to your local area.
</p>
<br>
</details>

<details>
<summary> 2016 </summary>
<p>
The instructions for the Physics Object Extractor Tool given in the 2015 data analysis drop-down above cannot be directly applied to 2016 data, but they still represent a good example of forming a collection of EDAnalyzers for filtering validated runs and storing information of interest. CMS recommends working with the NanoAOD format of the 2016 data, which is derived from MiniAOD. Instead of holding custom C++ classes, it holds ROOT trees with standard classes that can be directly read or analyzed using ROOT or other ROOT-compatible software. See the <a href="/docs/cms-getting-started-nanoaod">NanoAOD Getting Started page</a> for more information.
</p>
<br>

That's it! Hope you enjoyed this exercise. Feel free to play around with the rest of the data and write your own analyzers and analysis code. Learn more in <a href="https://cms-opendata-guide.web.cern.ch/">the CMS Open data guide</a>.