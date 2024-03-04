This page lists possible solutions to frequently encountered issues with CMS Open Data: for the virtual machine; for the CMSSW software and examples; and for the file download and access.

### Virtual machine

**I have trouble installing VirtualBox**

* Read the FAQs in [the VM installation guide](/docs/cms-virtual-machine-2011#issue). If it still fails, please contact your local system administrator.

**What is the root password for the CMS Open Data VM?**

* The root password for the CMS Open Data VM is `password`.

**The CMS Open Data VM does not open correctly**

* In some versions of VirtualBox, it has happened that the CMS Open Data VM does not open correctly. This was the case for example for VirtulBox 5.0.32, but more recent versions from [the VirtualBox website](https://www.virtualbox.org/wiki/Downloads) have been tested and are working properly. Note that it can take a while to launch the CMS Open Data VM for the first time.

* If the internet connection from the user's side is restricted, it may be that some ports and IPs need to be whitelisted so that the VM can install properly. These may change in time, please contact [opendata-support@cern.ch](mailto://opendata-support@cern.ch).

**When/after installing CERN VM, I get a message that my VM uses too much memory**

* Reduce the memory allocated to VirtualBox by clicking on System in the VirtualBox graphical user interface and adjust the base memory with the sliding bar.

### File download

**xml files do not download correctly by clicking on "Download"**

* Note that all files can be downloaded directly from the CMS Open Data VM terminal with wget e.g. you download the file `http://opendata.cern.ch/record/560/files/BuildFile.xml` in [record 560](/record/560) with
`$ wget http://opendata.cern.ch/record/560/files/BuildFile.xml`

### CMSSW software and open data examples

**When I start the CMS job, nothing happens**

* If you access the condition data (see the details in [the guide to the CMS condition database](/docs/cms-guide-for-condition-database)), the download of condition data to the local cache of your VM starts at the beginning of the job. The job will produce no output during that time. This may take up to one hour for the first time, but the next time you run the job, it will start fast as the data is already in the cache. If you observe that the cvmfs cache gets filled (see the output of `df` command) and the job also stops after the first time you run it, you should use [the CMS Open Data VM](/record/252) version with a larger cache size (CMS-OpenData-1.3.0.ova).

**While running on AOD data, my job gets "killed" by the VM without any further explanation**

* You might have exceeded the VMs available memory (use the VMs monitoring tools to check whether memory is marginal). Try one of the following:
    * do not run anything else using a lot of memory (e.g. a web browser) on the VM in parallel
    * reduce memory usage of the job (and/or check for potential memory leak)
    * increase the memory allocated to the VM by clicking on System in the VirtualBox graphical user interface and adjust the base memory with the sliding bar.

**I've done the demo example from the getting started instructions and I want to change the class name**

* Change the name of src/DemoAnalyzer.cc to the name of your choice, and replace all occurrences of `DemoAnalyzer` with the name of your choice in it and in `demoanalyzer_cfg.py`, `python/demoanalyzer_cfi`.

**After having compiled my code, I get a runtime error `An exception of category 'PluginNotFound'...`**

* It may be that your code directory is not two directories deep from `CMSSW_5_3_32/src`. If the instructions ask you to make an intermediate directory, you should do so, otherwise the CMSSW framework does not find your code even if it compiles.

**I think I've messed up my working area, how can I clean it?**

* You can clean up your working area with `scram b clean`.

**I have an example running on the 2010 data, what do I need to modify to run it on the 2011-2012 data?**

* Download [the CMS Open Data VM for 2011-2012 data](/record/252).
* Change all instances of CMSSW to the correct version (CMSSW_5_3_32 for 2011 and 2012 datasets).
* In your configuration file replace `PhysicsTools.PythonAnalysis.LumiList` with `FWCore.PythonUtilities.LumiList`.
* Download the list of validated runs for your data of interest ([2011](/record/1001) or [2012](/record/1002)) and change it in your configuration file.
* If your example accesses the condition database, set the logical links in your working directory and change the global tag definition in your configuration file as described in [the guide to the CMS condition database](/docs/cms-guide-for-condition-database)
* Change the input files to those of 2011 or 2012.
* Other changes may be needed depending on the complexity of your code, due to the change of the CMSSW version and to the type of the data.

**I have an example running on the 2011 data, what do I need to modify to run it on the 2012 data?**

* You can use the same CMS Open Data VM and the same CMSSW version (CMSSW_5_3_32).
* Download the the list of validated runs for ([2012](/record/1002) and change it in your configuration file.
* If your example accesses the condition database, set the logical links in your working directory and change the global tag definition in your configuration file as described in [the guide to the CMS condition database](/docs/cms-guide-for-condition-database).
* Change the input files to those of 2012.

**The example job prints output every event, how do I reduce frequency?**

* In the configuration file, add a line `process.MessageLogger.cerr.FwkReport.reportEvery = 1000` (or a frequency of your choice) after `process.load("FWCore.MessageService.MessageLogger_cfi")`.


### File access runtime

**When reading AOD data, I get write access warnings from eospublic on every file**

* This was a temporary 'feature' of a change in the eos software which has meanwhile been fixed. It does not affect the results.

**When reading AOD data,I get runtime Xrd error messages for some of the runs**

* Messages such as
```
170724 19:39:13 4988 Xrd: XrdClientMessage::ReadRaw: Failed to read header (8 bytes).
170724 19:40:06 5113 Xrd: CheckErrorStatus: Server [188.184.50.150:1094] declared: session not found(error code: 3011)
```
can be safely ignored, they do not affect the results.

**When reading AOD data, I get fatal access error messages from eospublic on specific files**

* According to the CERN EOS team, disk access problems to eospublic may occur occasionally and are automatically corrected within a few hours. If the access problem to a particular file lasts longer than about a day send a mail to [eos-support@cern.ch](mailto://eos-support@cern.ch), providing the file name and a log of the error message.


**Any other problem you cannot solve yourself or with the help of your local administrator(s), not related to your local setup**

> kindly contact [opendata-support@cern.ch](mailto://opendata-support@cern.ch)
