# Getting started with CMS data

## "I have installed the CERN Virtual Machine: now what?"

Congratulations! You have the CERN working environment up and running!

Note that in order to analyse CMS data collected in 2010, you need **CMSSW version 4.2.8 (patch7)**, supported only on Scientific Linux 5. The CMSSW command `cmsrel` you executed in the [validation stage](http://open-data.cern.ch/data/VMs#validate) ensures that you have the right version running. Make sure you are always in the **CMSSW_4_2_8patch7/src/** directory by performing the `cd CMSSW_4_2_8patch7/src/` every time you boot the VM and open the terminal.

### Visualize data with ROOT

**ROOT** is the framework used by several particle-physics experiments to work with the collected data. Although analysis is not itself performed within a ROOT file, it is instructive to understand how these files are structured and what data and collections they contain. Let's take ROOT for a spin!

* AOD (Analysis Object Data) files contain the information that is needed for analysis:
  * all the high-level [physics objects](https://twiki.cern.ch/twiki/bin/view/CMS/DPOAPublicDataReleaseStatement#Physics_objects) (such as muons, electrons, etc.);
  * tracks with associated hits, calorimetric clusters with associated hits, vertices; and
  * information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.
* It is not the final event interpretation with a simple list of particles.
  * It contains several instances of the same physics object (i.e. a jet reconstructed with different algorithms).
  * It may have double-counting (i.e. a physics object may appear as a single object of its own type, but it may also be part of a jet).
  * Additional knowledge is needed to define a "good" physics object.
  * Definition of same objects is different in each analysis.
* AOD files can be read in [ROOT](http://root.cern.ch/), but they cannot be opened (and understood) as simple data tables.
* Only the runs that are validated by data quality monitoring should be used in any analysis. The list of the validated runs is provided as a [JSON](http://json.org/) file.

* Try out:
  * Open ROOT
  * Fish through physics objects collections

## "Nice! But how do I analyse these data?"

## How is a CMS analysis performed?

* Then: Analyzer

* Reduced dataset

## What can we do with the data?

### AOD

### Applying cuts and reducing the data sample

### Analysing data sample (see previous step)
