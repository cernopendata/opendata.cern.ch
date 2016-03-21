How to install and run the demo analysis job approximately reproducing 
----------------------------------------------------------------------
the dimuon mass spectrum from MUO-10-004
----------------------------------------

This simple analysis example is set up at Research level, i.e. it requires 
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
  /Mu/Run2010B-Apr21ReReco-v1/AOD
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
    src/Demoanalyzer.cc
  by the ones from the directory
  (*** to be adjusted to proper web page address!!! ***)
  /afs/desy.de/user/g/geiser/public/CMS/opendata/MUO-10-004demo
  and read the comments in 
    src/Demoanalyzer.cc 
  if you want to understand what the program does. 

* recompile ("scram b") and rerun ("cmsRun ...") 
  exactly as before.
  You should get an output file Mu.root which contains histograms 
  for 10000 input events (small subset of data).
  These can be looked at using a Root Browser (see above).
  The most interesting histogram is 
    GM_mass_log
  In order to compare with MUO-10-004 it should be viewed with the 
  'logy' option. Of course with 10000 events the comparison is poor,
  but the J/psi (at log10(mass)=0.5), Upsilon (at log10(mass=0.98))
  and Z (at log10(mass)=1.95, one event only) peaks should be visible.

* To run over more or even the full statistics, edit the relevant parts of
  the Python file  
    demoanalyzer_cfg.py  
  (see comments therein) and rerun.
  Add up the output histograms from different (nonoverlapping) input index 
  files using Root tools.
