Readme for "Validation code for 2010 Comissioning data sets, based on 
dimuon mass spectrum"


How to install and run the validation benchmark for the 2010 Commissioning 
--------------------------------------------------------------------------
data set based on the dimuon mass spectrum from global muons  
------------------------------------------------------------

This code for validation and benchmarking of the Commissioning 
data set, based on the dimuon mass spectrum, does NOT apply a JSON 
preselection. It therefore includes benchmarking of non-JSON selected runs.
It is set up at Research level, i.e. it requires 
university student level programming experience.
Minimal acquaintance with Linux, the Root analysis package
https://root.cern.ch/ 
and a basic text editor is assumed in the following.

* Install and run the Demo (demo analyzer) program as instructed on 
  http://opendata.cern.ch
   -> Research
   -> Explore CMS
   -> VMs
      How to Test and Validate?
  (or direct access via 
   http://opendata.cern.ch/VM/CMS  
  )

If it works successfully, 

* download the index files for the  
  /Commissioning/Run2010B-Apr21ReReco-v1/AOD
  primary data sets as instructed on 
  http://opendata.cern.ch/collection/CMS-Primary-Datasets
  and store them in Demo/DemoAnalyzer/datasets/
  (you might have to create the directory first) 

* replace the three files  
    BuildFile.xml
    demoanalyzer_cfg.py 
    src/DemoAnalyzer.cc
  by the ones from the web page
  *** to be adjusted to proper web page address ***
  http://opendata.cern.ch/record/XXX
  and read the comments in 
    src/DemoAnalyzer.cc 
  if you want to understand what the program does. 

* recompile ("scram b") and rerun ("cmsRun ...") 
  exactly as before.
  You should get an output file MuCommissioning00.root which contains 
  histograms for all the files/events in the 00 index file.
  These can be looked at using a Root Browser (see above).
  The most interesting histogram is 
    GM_mass_log

  This is the validation of a Commissioning sample, not dedicated to muon 
  final sates, so the number of events entering the mass plot is relatively
  small

* To run over the full statistics, edit the relevant parts of
  the Python file  
    demoanalyzer_cfg.py  
  (see comments therein) and rerun for each index file.

  Run job for each relevant input index file:
  - MuCommissioning00, MuCommissioning02, MuCommisioning03, MuCommissioning04
   
  Add up the output histograms from different Commissioning input index files 
  by starting ROOT and executing the ROOT program mergeCommissioning.C provided
  on the web page (assumed naming scheme is the suffix "val" for each file 
  above), i.e 
  
  root
  .x mergeCommissioning.C
  
  (Do *not* try to compile the mergMu.C file together with the other 
   files above)

  Look at output with 

  root
  new TBrowser

  and navigate to relevant file

* Reference root files for each index file, and its sum, are provided.