Ten years ago, a handful of enthusiastic researchers from the
[ALICE](https://alice.cern), [ATLAS](https://atlas.cern/),
[CMS](https://cms.cern/) and [LHCb](https://lhcb.web.cern.ch/) collaboration
open access teams, together with a handful of software engineers from the CERN
[Department of Information
Technology](https://information-technology.web.cern.ch/) and the information
specialists from the CERN [Scientific Information
Service](https://sis.web.cern.ch/), grouped together to build the CERN Open
Data portal.

Under the umbrella of the [Data Preservation in High Energy
Physics](https://dphep.web.cern.ch/), the work started in summer 2014 by
devising a metadata schema that would neatly describe the open data from the
LHC experiments in both their technical and physics-oriented facets. We had to
design the web site portal (based on the
[Invenio](https://inveniosoftware.org/) digital repository framework) to
provide web pages for general public, including visualising collision events,
all the while ensuring the best data preservation practices to describe, manage
and disseminate the data for researchers. The data needed to be made searchable
and downloadable in a way that would be attractive to both general public for
educational purposes and usable by independent researchers for referencing and
independent theoretical analysis. (Some of the technical challenges behind the
CERN Open Data portal were described in a [later
interview](https://superuser.openinfra.org/articles/cern-open-data-portal/) for
the SuperUser magazine.)

The efforts concluded in the launch of the CERN Open Data portal on [November
20th
2014](https://home.web.cern.ch/news/news/accelerators/cern-makes-public-first-data-lhc-experiments).
The portal managed of about 30 terabytes of open data from LHC experiments in a
ground-breaking service at the time. The [Reddit AskMeAnything
session](https://www.reddit.com/r/IAmA/comments/2nxwkb/a_few_days_ago_cern_launched_an_open_data_portal/)
organised alongside the release attracted large attention and many tens of
thousands of portal visitors, more than the total number of particle physicists
in the world.

Fast-forward ten years to the present time. The CERN Open Data portal now
disseminates more than 5 petabytes of open data, which is a whopping 200 times
more data than at launch. More particle physics experiments have joined the
open data portal, with [DELPHI](https://delphi-www.web.cern.ch/delphi-www/),
[OPERA](https://en.wikipedia.org/wiki/OPERA_experiment),
[PHENIX](https://www.phenix.bnl.gov/), and
[TOTEM](https://totem-experiment.web.cern.ch/) releasing data samples or even
full data collections. More experiments are in the pipeline, such as
[JADE](https://www.mpp.mpg.de/en/research/data-preservation/jade/). The CERN
Open Data portal is becoming a sort of "HEP Open Data" portal, covering not
only the LHC experiments, but the particle physics domain at large, further
demonstrating success of the original idea.

Looking back at the origins and the path travelled in the past ten years, any
sceptical concerns whether these data would be understandable and usable for
independent theoretical research have been positively answered. The [leading
publication](https://news.mit.edu/2017/first-open-access-data-large-collider-subatomic-particle-patterns-0929)
by Jesse Thaler's team in MIT analysing CMS open data showed that independent
theoretical publications are not only possible, but that they enrich the
collaboration research practices themselves, with CMS collaboration starting to
cite the independent theoretical work in their own publications. There are now
more than 70 research papers published on the CMS open data and the [number of
published papers is
growing](https://cms.cern/news/cms-celebrates-decade-open-data). Matt Strassler
published a series of blog posts [on the importance of open
data](https://profmattstrassler.com/2019/03/19/the-importance-and-challenges-of-open-data-at-the-large-hadron-collider/)
in this realm.

The independent usage of the released data for research has led to the
strengthening of published data provenance information when releasing the data
in order to provide physics context and auxiliary information about the data as
accurately and as completely as possible. The data are being published together
with analysis examples demonstrating how to extract physics objects out of the
data and how to use them in one's own analyses. The care about the data usage
patterns and the further usability and reinterpretability of data [has
naturally led](https://www.nature.com/articles/s41567-018-0342-2) to sister
projects dedicated towards facilitating [reproducible
analyses](https://www.reana.io) and [continuous
reuse](https://zenodo.org/records/10263204) of the data.

Besides independent theoretical research, the data are being used in numerous
masterclasses and education programs to train the next generation of
scientists, as well as by software engineers in the efforts to benchmark
software tools to ensure their feasibility in the forthcoming high-luminosity
experimental data-taking era.

The bottom-up efforts on preparing and releasing open data were complemented by
the top-down efforts and support from CERN laboratory management towards open
science. The efforts by CERN as the supporting hosting lab together with LHC
collaboration management boards as the data producers and owners paved the way
towards the formal establishment of the [CERN Open Data
policy](https://cds.cern.ch/record/2745133/files/CERN-OPEN-2020-013.pdf) in
2020, and, two years later, the [CERN Open Science
Policy](https://cds.cern.ch/record/2835057/files/CERN-OPEN-2022-013.pdf). It is
under these auspices that the open data pilot efforts progressively took shape
to what they are today whilst seeking the long-term sustainability of making
science open.

Looking into the future, there are clear challenges ahead. The growing number
of open data releases calls for using more efficient data publishing workflows
leveraging scientific data managers used in collaborations, such as
[Rucio](https://rucio.cern.ch/) in ATLAS and CMS and
[DIRAC](https://dirac.readthedocs.io/) in LHCb. The vast quantities of
published data calls for implementing an efficient "hot" and "cold" storage
mechanisms behind the portal in order to save on storage costs. All this
content necessitates efficient tape backups and the on-demand data staging for
users from the cold storage, when necessary. Finally, the experimental
collaborations plan to release even more data during the LHC Run-3 phase, which
calls for novel approaches to open data publishing that are going beyond the
digital repository domain, such as the nascent system allowing theorists to ask
for custom LHCb open data production via a dedicated [Ntupling
Wizard](https://arxiv.org/pdf/2302.14235v2) service.

It has been a blast working together between software engineers, information
specialists and particle physicists on fostering open and reproducible science
practices in particle physics.

Looking forward to working together in the next decennial!
