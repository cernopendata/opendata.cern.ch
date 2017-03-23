Readme for "Validation code for 2010 MinumumBias data sets, based on 
track and vertex spectra"


How to install and run the validation benchmark for the MinimumBias 
-------------------------------------------------------------------
data sets based on track and vertex spectra
-------------------------------------------

This code for validation and benchmarking of the MinimumBias
data sets, inspired by CMS-QCD-10-006, is set up at Research level, 
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
  /MinimumBias/Run2010B-Apr21ReReco-v1/AOD
  primary data sets as instructed on 
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
  http://opendata.cern.ch/record/XXX
  and read the comments in 
    src/DemoAnalyzer.cc 
  if you want to understand what the program does. 

* recompile ("scram b") and rerun ("cmsRun ...") 
  exactly as before.
  You should get an output file MinBias00val.root which contains histograms
  for all the files/events in the 00 index file. 
  These can be looked at using a Root Browser (see above).
  The most interesting histograms are the inclusive track pt spectra, 
  2.6pt,2.4pt, ... 0.2pt
  corresponding to the |eta| ranges 2.6-2.4, 2.4-2.2, ..., 0.2-0.0. 
  Note that no acceptance correction is applied (no MC), so the spectra 
  will look quantitatively different from the ones in QCD-10-006, although
  qualitatively similar.

* To run over the full statistics, edit the relevant parts of the Python file  
    demoanalyzer_cfg.py  
  (see comments therein) and rerun for each index file.

  Run job for each relevant input index file:
  - MinimumBias00, 01, 02, 03, 04, 05, 06 
   
  Add up the output histograms from the different MinimumBias input index files
  by starting ROOT and executing the ROOT program mergeMinBias.C provided 
  on the web page (assumed naming scheme is "MinBiasXXval" for each file 
  above), i.e. 
  
  root
  .x mergeMinBias.C

  (Do *not* try to compile the mergeMinBias.C file together with the other 
   files above)
  
  Look at output with 

  root
  new TBrowser

  and navigate to relevant file

* Reference root files for each index file, and its sum, are provided.
