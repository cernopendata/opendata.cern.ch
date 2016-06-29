Readme for "Validation code for 2010 Mu and MuMonitor data sets, based on 
dimuon mass spectrum"


How to install and run the validation benchmark for the Mu and MuMonitor 
------------------------------------------------------------------------
data sets based on the dimuon mass spectrum from global muons  
-------------------------------------------------------------

This code for validation and benchmarking of the Mu and MuMonitor
data sets, inspired by CMS-MUO-10-004, is set up at Research level, 
i.e. it requires university student level programming experience.
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
  /Mu/Run2010B-Apr21ReReco-v1/AOD
  primary data sets and for the 
  /MuMonitor/Run2010B-Apr21ReReco-v1/AOD
  data set as instructed on 
  http://opendata.cern.ch/collection/CMS-Primary-Datasets
  and store them in Demo/DemoAnalyzer/datasets/
  (you might have to create the directory first) 

* download the JSON file as instructed in 
  http://opendata.cern.ch/record/1000
  and save it to the Demo/DemoAnalyzer/datasets directory 

* replace the three files  
    BuildFile.xml
    demoanalyzer_cfg.py 
    src/DemoAnalyzer.cc
  by the ones from the web page 
  http://opendata.cern.ch/record/460
  and read the comments in 
    src/DemoAnalyzer.cc 
  if you want to understand what the program does. 

* recompile ("scram b") and rerun ("cmsRun ...") 
  exactly as before.
  You should get an output file Mu00.root which contains histograms
  for all the files/events in the 00 index file. 
  These can be looked at using a Root Browser (see above).
  The most interesting histogram is 
    GM_mass_log
  In order to get similar appearance as the plot in MUO-10-004 it should be 
  viewed with the 
  'logy' option.
  E.g. the J/psi (at log10(mass)=0.5), Upsilon (at log10(mass=0.98))
  and Z (at log10(mass)=1.95) peaks should be visible.

* To run over the full statistics, edit the relevant parts of the Python file  
    demoanalyzer_cfg.py  
  (see comments therein) and rerun for each index file.

  Run job for each relevant input index file:
  - Mu00, Mu01, Mu02, Mu03, Mu04, Mu05  for Mu validation
  - MuMonitor for MuMonitor validation
   
  Add up the output histograms from the different Mu input index files by 
  starting ROOT and executing the ROOT program mergeMu.C provided on the 
  web page (assumed naming scheme is the suffix "val" for each file above), 
  i.e. 
  
  root
  .x mergeMu.C

  (Do *not* try to compile the mergMu.C file together with the other 
   files above)

  There is only one MuMonitor index file, so output merging is not necessary 
  in this case.
  
  Look at output with 

  root
  new TBrowser

  and navigate to relevant file

* Reference root files for each index file, and its sum, are provided.
