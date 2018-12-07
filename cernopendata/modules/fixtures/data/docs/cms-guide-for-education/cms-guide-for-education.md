This page will guide you through contents of the CMS Open Data collections that are meant for educational use (or for physics enthusiasts!). It is roughly broken down into three levels of difficulty:

* Beginner: [*Visualise collisions*](#visualise-collisions)
* Intermediate: [*Make histograms with collision data*](#make-histograms-with-collision-data)
* Advanced: [*Dive deeper into the data*](#dive-deeper-into-the-data)


## Visualise collisions

If you are new to particle physics, your time is limited, or you want to do something online fairly quickly, have a look at visual displays of real particle collisions. For example, here are collision events which contributed to the discovery of the Higgs boson in 2012:

1. Go to the [CMS event display](/visualise/events/cms),
1. wait for the tool to load, and click on the `Open file` button,
1. choose `Open file(s) from web`,
1. choose `HiggsCandidates/`,
1. click on `4lepton.ig` to see candidate collisions events for a Higgs boson transforming into electrons and/or muons, or click on `diphoton.ig` to see candidate collision events for a Higgs boson transforming into two photons, and wait for the events to load to the right,
1. choose any specific event from the selection and click on `Load`.

Your collision event should now appear in the display.

* If you chose the `4lepton.ig` set and you want to see electrons, check `Electrons` under `Physics` and uncheck `Tracks (reco)` under `Tracking` in the menu to the left  (the choice is only visible if electrons are present in the collision).
* If you chose the `diphoton.ig` set, check `Photons` under `Physics` in the menu to the left (the choice is only visible if photons are present in the collision).

**Note**: If you have a VR viewer (even a simple one like [Google Cardboard](https://vr.google.com/cardboard/)), you can immerse yourself into the collision using your smartphone: click on the "Stereo View" button (shaped like binoculars), insert your phone into the viewer and have virtual tour in 3D of a real LHC collision!

The first few events of all collision datasets from CMS served on the CERN Open Data portal are available in a format suitable for the event display. In addition, many other events have been selected in specially prepared collections. Find them all in [this search query](/search?page=1&size=20&q=display&subtype=Derived&experiment=CMS).
Two examples of these specially prepared files are:

* [Higgs candidate events for use in education and outreach](/record/300), and
* [Dimuon events with invariant mass range 2-5 GeV for public education and outreach](/record/301) for J/&psi;&rarr;&mu;&mu; candidates.

You can also download these files directly from the records on this portal.

To learn how to use the [CMS event display](/visualise/events/cms), click on `Need help?` link on the top right side of the screen. For suggestions for classroom activities see [Tutorials and worksheets for CMS Event Display](/record/5103).


## Make histograms with collision data

You can get an overview of our education resources through [this search query](/search?page=1&size=20&q=learning%20school%20education&experiment=CMS) with your keyword of interest (you can change the pre-defined keywords here). Here are some highlights:

* If you already know what the basic physics quantities measured in a particle collision are and want to **play online with histograms** from different samples of open data, check out the [CMS histogram visualiser](/visualise/histograms/cms). For instructions on how to use the visualiser, click on `Need help?`.
* To learn some concepts of statistical analysis in a hands-on classroom activity, have a look at the material for an organised ["**Masterclass**" exercise](/record/53) based on CMS data and the online event display. A CMS Masterclass typically takes one day (including introductory lectures and post-analysis discussions), but the exercise itself can be done in approximately two hours. Learn more about organising your own Masterclass [on the CMS website](https://cms.cern/engage-with-cms/cms-physics-masterclass).
* You can also use **spreadsheet programs** to make a further step in the direction of data analysis, using a limited number of CMS events that are suitable for this type of exercise, see [instructions for use of CMS Open Data in spreadsheets for schools and education](/record/5100). These exercises can be done in an hour or so.
* For a first taste of real programming using physics data, consider these resources that use [**Jupyter notebooks**](https://jupyter.org/) for a browser-based introduction to data analysis (time can vary from less than an hour to several hours, depending on the scope of your exercise):
    * [A quick (completely online) hands-on demo](https://mybinder.org/v2/gh/cms-opendata-education/cms-online-notebooks-for-binder/master?filepath=quick-start-to-CMS-open-data.ipynb) to Jupyter and CMS Open Data (using python).
    * [Analysing CMS Open Data in Jupyter using **python**](/record/5101)
    * [Analysing CMS Open Data in Jupyter using **R**](/record/5102), with a brief intro to the R programming language
* All applications mentioned above use open data in simplified CSV (comma-separated values) format. See [all available CSV datasets](/search?page=1&size=20&q=&type=Dataset&experiment=CMS&subtype=Derived&file_type=csv), which have been extracted directly from the original collision datasets.
    * If you are interested in producing your own selection of open data in CSV format, see [example software ](/record/552) for the processing step.


## Dive deeper into the data

If you want a more detailed understanding of particle physics or an introduction aimed at the university level, take a look at some of the other resources in [this search query](/search?page=1&size=20&q=&keywords=education&experiment=CMS).

For example:

* [Particle Physics Playground](/record/52) provides you with further hands-on activities with open data from CMS and other experiments.
* [Computing Methods in High-Energy Physics](/record/61) is an introductory course on computing in high-energy physics.
* [CMS HEP Tutorial](/record/50) is a one-week course with a basic introduction to fundamental concepts of data analysis in HEP experiments using CMS Open Data.

Of course, you can also undertake your own explorations with CMS Open Data:

* If you want to "re-discover" the **Higgs boson** in the CMS Open Data from 2011-2012, first install the Virtual Machine (VM) as instructed in ["CMS 2011 Virtual Machines: How to install"](/docs/cms-virtual-machine-2011) and look at [this Higgs analysis example](/record/5500).
* If you want to learn how data analysis is done by CMS scientists, install the Virtual Machine (VM) as instructed in ["CMS 2011 Virtual Machines: How to install"](/docs/cms-virtual-machine-2011), follow the instructions in ["Getting Started with CMS Open Data"](/docs/cms-getting-started-2011), and then
check out our extensive overview of research activities under ["Guide for research use of CMS Open Data"](/docs/cms-guide-for-research).

Have fun!!
