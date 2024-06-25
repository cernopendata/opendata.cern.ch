LHCb masterclass is an annual event where students from different schools and different countries get a change to work on the actual data
collected by the LHCb detector at CERN.

## About LHCb data

The following datasets for educational purposes obtained from LHCb data are provided through this portal:

- Event display datasets, containing events where a D0 meson decays into a Kaon and a Pion. These datasets can be displayed with LHCb simplified event display.
- About 60k events where a D0 meson decays into a Kaon and a Pion. This dataset can be used to study signal and background distributions of variables characterizing the D0 decay and to measure the D0 lifetime.

## LHCb Derived Datasets

- [D0 Masterclass events 1](http://lhcbproject.web.cern.ch/lhcbproject/dist/Masterclass/mclasseventv2_D0_1.root) (175 files):
  Each file contains 30 events recorded with LHCb detector. The events have been pre-selected using loose criteria to contain D0 meson candidates decaying into a Kaon and a Pion. It can be visualised with LHCb event display (link here).

- [D0 Masterclass events 2](http://lhcbproject.web.cern.ch/lhcbproject/dist/Masterclass/MasterclassData.root) (1 file):
  This file contains about 60k events pre-selected using loose criteria to contain D0 meson candidates decaying into a Kaon and a Pion. It can be accessed and analysed using LHCb D0 lifetime measurement code. (link here).

## LHCb Learning Resources

**Physics Masterclasses:** LHCb is part of the International Masterclass Programme: each year, high-school students reach their nearby universities and become LHCb physicists for a day. Their goal is to select in real LHCb events a particular decay of the D0 meson, where a Kaon and a Pion are produced. On such events, the D0 lifetime is measured. [Go to page...](http://lhcb-public.web.cern.ch/lhcb-public/en/LHCb-outreach/masterclasses/en/index.html)

## LHCb Tools

**Event Display and D0 lifetime VM image:** VM image to run LHCb event display and the analysis to measure the D0 lifetime.

LHCb software comes via a virtual machine image. The only thing you need to install by yourself on you desktop is VirtualBox. Then you just need to download the LHCb virtual machine image open it with VirtualBox and click on the LHCMasterclass icon on the desktop...

## Instructions

Learn how to use the LHCb virtual machine to have a first look at LHCb events and use analysis tools:

1. ["How do I start LHCb software?"](#start)
2. ["What kind of LHCb data will I work on?"](#data)
3. ["I have installed VirtualBox, downloaded LHCb VM image and launched it. And now?"](#vbox)
4. ["What can I learn from this exercise?"](#learn)
5. ["How does the Event display exercise work?"](#eve)
6. ["How does the D<sup>0</sup> lifetime fitting exercise work?"](#fit)

## <a name="start">"How do I start LHCb software?"</a>

LHCb software comes via a virtual machine image. The only thing you need to install by yourself on you desktop is VirtualBox. Then you just need to download the LHCb virtual machine image open it with VirtualBox and click on the LHCMasterclass icon on the desktop. (see instructions [here](../virtual-machines-lhcb/lhcb.md) )

## <a name="data">"What kind of LHCb data will I work on?"</a>

The data samples you can download from this portal consists of candidates for a type of charmed particle known as a D<sup>0</sup> particle found in a sample of randomly collected LHC interactions during 2011 data taking. A D<sup>0</sup> particle consists of a charm quark and an up anti-quark. The particles are measured decaying in the mode D<sup>0</sup>→K-π+ where the final state particles are a kaon (K-) consisting of a strange quark and an anti-up quark, and a pion (π+) that consists of a down anti-quark and an up quark. The +, - and 0 refer to the electric charge of the particle, whether it is positively charged, negatively charged or neutral.

These particles have lifetime which are long enough that, for the purpose of this exercise, they are stable within the LHCb detector. The particles have been preselected using loose criteria so that you begin in the samples you will have ith a visible signal, but background events are also present.

## <a name="vbox">"I have installed VirtualBox, downloaded LHCb VM image and launched it. And now?"</a>

The LHCbMasterclass exercise is divided into two parts: the Event Display and the D<sup>0</sup> lifetime fitting exercise, which should be executed in this order.

Once you click on the icon LHCbMasterclass you will be asked to select a language, enter your details and select the sample you want to analyse.

After clicking on the `Save` button, you can start the Event Display. If you want to move directly to the second exercise, just click on Move on to D<sup>0</sup> exercise.

## <a name="learn">"What can I learn from this exercise?"</a>

You will be working on real collisions recorded by the LHCb experiment during 2011 data taking, which contain both signal and background particles. This set of two exercises is designed to teach you how to

- Use an event display of the proton-proton collisions inside the LHCb detector to search for charmed particles and separate this signal from backgrounds.
- Fit functional forms for the signal and background to the data in order to measure the number of signal events in the data sample and their purity (defined as the fraction of signal events in the total sample).
- Obtain the distribution of signal events in a given variable by taking the combined distribution of events in the data sample (which contains both signal and background events) and subtracting the background distribution. The result of the fit in the previous step is used to find a sample of pure background events for subtraction, and to compute from the signal yield and purity the appropriate amount of background which should be subtracted.
- The signal you will be looking at decays exponentially with time, analogously to a radioactive isotope. You can now use the sample of events passing the previous step to measure the "lifetime" of the signal particle. The lifetime is defined as the time taken for (e-1)/e of the signal events to decay, where e~2.718 is the base of the natural logarithm. It is analogous to the concept of half-life in radioactive decay.

## <a name="eve">"How does the Event display exercise work?"</a>

The aim of the event display exercise is to locate displaced vertices belonging to D<sup>0</sup> particles in the vertex detector of the LHCb experiment. When you launch the exercise and load an event, you will see an image of the LHCb detector and particle trajectories ("tracks") inside it. These tracks are colour coded, and a legend at the bottom of the GUI tells you which colour corresponds to which kind of particle.

In order to make identifying vertices easier, you can view an event in three different two-dimensional projections : `y-z`, `y-x` and `x-z`, show for one event the following pictures:

<img src="/static/docs/getting-started-with-lhcb/get_started_lhcb_1.png" width="70%">

<img src="/static/docs/getting-started-with-lhcb/get_started_lhcb_2.png" width="70%">

<img src="/static/docs/getting-started-with-lhcb/get_started_lhcb_3.png" width="70%">

Different events will be clearer in different projections, so feel free to experiment with all three! Displaced vertices appear as a pair of intersecting tracks, far away from the other tracks in the event. When you click on a particle, you will see its information, including mass and momentum, in the Particle Info box. A D<sup>0</sup> particle decays into a kaon and a pion, so you will need to find a displaced vertex where a kaon track intersects with a pion track. Once you find a track which you think is part of the displaced vertex, you can save it using the `Save Particle` button. Once you have saved two particles, you can compute their mass by clicking on the `Calculate` button. If you think this combination has a mass compatible with that of the D<sup>0</sup> particle, click on Add to save it : by saving a combination for each event, you will build up a histogram of the masses of the displaced vertices in the different events.

Remember that you are looking at real data so it contains both signal and background, and the detector has a finite resolution, so not all displaced vertices will have exactly the D<sup>0</sup> mass (even the signal ones). They should, however, be within the range 1816-1914 MeV (this range is around 3% each way around the true D<sup>0</sup> mass). If you try to save a combination which is too far away from the real D<sup>0</sup> mass the exercise will warn you that you have not found the correct displaced vertex pair and won't let you save it. If you are not able to find the displaced vertex for an event after a few minutes, move on to the next event and come back to the one which was giving you trouble if you have time at the end of the exercise. Once you have looked at all events, you can examine your mass histogram by clicking the `Draw` button.

## <a name="fit">"How does the D<sup>0</sup> lifetime fitting exercise work?"</a>

Before describing the fitting part of the exercise, it will be useful to list the variables involved in this exercise :

**D<sup>0</sup> mass**: this is the invariant mass of the D<sup>0</sup> particle. The signal can be seen as a peaking structure rising above a at background. The range of masses relevant for this analysis is 1816-1914 MeV. The signal shape is described by the Gaussian (also known as "normal") distribution. The center ("mean") of this distribution is the mass of the D<sup>0</sup> particle, while the width represents the experimental resolution of the detector.

**D<sup>0</sup> TAU**: this is the distribution of decay times of the D<sup>0</sup> candidates. The signal is described by a single exponential whose slope is the D<sup>0</sup> lifetime (the object of the last exercise), while the background concentrates at short decay times.

**D<sup>0</sup> IP**: this is the D<sup>0</sup> distance of closest approach ("impact parameter") with respect to the proton-proton interaction in the event. The smaller the impact parameter, the more likely it is that the D<sup>0</sup> actually came from that primary interaction. In order to simplify the drawing, we actually plot and cut on the logarithm (base 10) of this quantity in the exercise.

**D<sup>0</sup> PT**: this is the momentum of the D<sup>0</sup> transverse to the LHC beamline.

---

**Exercise 1** : fitting the mass distribution and obtaining signal variable distributions The object of this exercise is to fit the distribution of the D<sup>0</sup> mass variable, and extract the signal yield and purity.

- Click on the `Plot` D<sup>0</sup> mass button to plot the overall mass distribution. You will see a peak (signal) on top of a at distribution (background). The peak should be described by a Gaussian function, whose mean corresponds to the mass of the D<sup>0</sup> and whose width (σ) is determined by the experimental resolution of the LHCb detector.
- Click on Fit mass distribution to fit this distribution using a Gaussian function for the signal and a linear function for the background.
- Look at the fitted mass distribution. You can split it into three regions: the signal region and two background-only "sidebands": one above the signal (the upper sideband) and one below the signal (the lower sideband). A Gaussian distribution contains 99.7% of its events within three standard deviations of the mean, so this "three σ" region around the mean is usually the definition of the signal region.
- Use the slider labelled Sig range to define the beginning and end of the signal region. All events not falling into the signal region will be said to fall into the background region.
- You can now use the definitions of the signal and background regions in the mass variable to determine the signal and background distributions in other variables. Click on the button labelled `Apply cuts and plot variables`. You will see the signal (blue) and background (red) distributions for the other three variables plotted next to the mass distribution. You should discuss the exercise with an instructor at this point.

**Exercise 2** : measuring the D<sup>0</sup> lifetime The object of this exercise is to use the signal sample which you obtained in the previous step to measure the lifetime of the D<sup>0</sup> particle. This is the same quantity as the half-life of a radioactive particle: the D<sup>0</sup> decays according to an exponential distribution, and if this exponential is fitted to a distribution of the D<sup>0</sup> decay times, the slope of this exponential is the lifetime of the D<sup>0</sup>.

- Fit the lifetime of the D<sup>0</sup>.
- Compare the slope of this exponential to the D<sup>0</sup> lifetime given by the Particle Data Group. Talk to an instructor about how well these agree with each other.
- In addition to statistical uncertainties, measurements can suffer from systematic uncertainties, caused by a miscalibrated apparatus or an incorrect modelling of the backgrounds. One basic technique for estimating these is to repeat the measurement while changing the criteria used to select signal events. If the result changes significantly when changing the criteria, we know that there is something wrong!
- Repeat your fit for the lifetime of the D<sup>0</sup> while varying the maximum allowed D<sup>0</sup> impact parameter. The allowed values range from -4:0 to 1.5 in the original fit. Move this upper value from 1.5 to -2.0 in steps of 0.25, and refit the D<sup>0</sup> lifetime at each point, saving the results as you go along.
- Plot the histogram showing the fitted value of the D<sup>0</sup> lifetime as a function of the upper cut on the impact parameter. Discuss the shape, and what it tells you about the D<sup>0</sup> lifetime, with an instructor.
- What other sources of systematic uncertainty might we need to consider when making a lifetime measurement?
