
1. [Introduction to “physics objects”](#what)
2. [CMS physics objects](#list)

<br>

# <div id="what"> Introduction to “physics objects” </div>

Particle colliders are the most powerful tools we have to study the building blocks of our Universe and the laws governing them. Gigantic detectors, such as CMS, act as cameras that take "photographs" of the particle collisions, allowing us to test our understanding of Nature.

Although we cannot observe the particles created in the collisions themselves, their decay products leave signals in the CMS sub-detectors. Dedicated software then uses these signals to "reconstruct" the decay products, which we classify into families called "physics objects" (see list below). It is important to note that these reconstructed physics objects are only interpretations of the signals observed by CMS and as such are subject to various sources of uncertainty (efficiencies, misidentifications etc.).

For example, see the two events below, both belonging to a collection of muons. The first shows hits in the muon chamber segments but does not in fact contain a real muon. The second event, on the other hand, shows a clear muon flying through CMS.

<center>
<img src="/static/docs/cms-physics-objects-2010/bad_mu.gif" width="55%" align="middle">
<img src="/static/docs/cms-physics-objects-2010/good_mu.gif" width="55%" align="middle" vspace="20">
</center>

Like assembling a jigsaw puzzle, we have to put together all the individual information about the physics objects from each collision to get a picture of what took place at the collision point. Analysing several (trillions!) of collisions allow us to look for patterns in the data that may correspond to previously undiscovered particles or phenomena, or allow us to make even more precise measurements of known phenomena.

Standard collections of physics objects can be used for the vast majority of CMS analyses without further tweaking. However, different analyses may require different combinations of physics objects and information about how they are related. The trick is to balance efficiency of data selection (select as many objects of a particular type) versus the fake rate (probability of misidentification).

---

<br>

# <div id="list">  CMS physics objects </div>

<br>

The primary data provided by CMS on the CERN Open Data Portal is in a format called "Analysis Object Data" or AOD for short, and from 2015 onwards, in a slimmer format called MINIAOD. This format contains the collections of different physics objects. For a quick look, see how to print out the object collections of a data file in the [getting started guide](/docs/cms-getting-started-2015#data).

Documentation of these objects is available in [the CMS WorkBook 2015 MiniAOD page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#High_level_physics_objects). The objects are implemented as C++ classes in the CMS software package CMSSW, and detailed reference documentation of all classes is available in [the class list of the CMSSW reference manual](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/annotated.html). To see the properties of electrons, you would navigate to "pat" and find the entry for "Electron". The [pat::Electron Class Reference](https://cmsdoxygen.web.cern.ch/cmsdoxygen/CMSSW_7_6_7/doc/html/d2/d1f/classpat_1_1Electron.html) lists all member functions through which the different properties of reconstructed electron can be accessed. Note that many of the basic propertied are "inherited" from the parent classes, and are listed separately under "Public Member Functions inherited from ... ".

For a quick start on how to write the most common objects and their properties in an output file, follow the [getting started instructions](/docs/cms-getting-started-2015#data) on how to use ["Physics Object Extractor Tool (POET)"](https://github.com/cms-opendata-analyses/PhysObjectExtractorTool/tree/2015MiniAOD).
