This document describes the analysis of MC simulated event samples for JADE.

0. ["Stages of simulations"](#stages)
1. ["Which generators to use"](#generators)
2. ["Most important settings"](#setings)
3. ["Smearing"](#smearing)

## <a name="stages">"Stages of simulation"</a>
The simulation the events observed in the JADE detector can be split into two large stages: the simulation of the
hadronic final state and the simulation of the detector responce (detection) of the simulated hadronic final state.

The very first step of the hadronic final state simulation is the simulation of  production of partons in the final
state, i.e. quarks, gluons or other elementary particles.
This step can be described by the MC event generators precisely to some fixed order of perturbation theory.
The next step involves the simulation of radiation by the simulated particles, so called parton shower (algorithm).
This parton shower helps to improve the overall description of the physics in the final state.
After the parton shower application the hadronisation process is simulated. At this stage the produced coloured partons
(quarks and gluons)  are recombined and/or split to
form in the end colourless particles -- hadrons.
Afther the simulation of hadronisation process the decays of unstable particles are simulated.
This is the final stage of the simulation of hadronic final state. As the end result of simulation, a set of stable or relatively
long-lived particles is produced. Typically these include pions, electrons, muons, photons, protons, neutrons, kaons and
a tiny fraction of undecayed heavier hadrons.



The simulation of the detector response in JADE is done via parametric smearing.
Note that as of 2019 this tecnique is used in HEP only for the "fast" simulation of detector response, e.g. in DELPHES framework.

The basic idea of the tecnique is to establish a relation between  the properties of objects observed in the detector
(e.g. charged aprticle tracks) and the properties of particles that produces these objects.
The relation is build via distortion of the relevant parameters of the original particles, e.g. momenta, direction, etc.
The average size and type of distortion is selected  to provide best match to the data observed in the JADE detector.
For the individual object the size and type of distortion is selected randomly acording to predefined distributions.


## <a name="gen">"Which generators to use?"</a>

The most common  processes in $e^+e^-$ collisions can be simulated by many moders MC event generators.
E.g. $e^+e^-\rightarrow q\bar{q}$ can be simulated by Pythia6, Pythia8, SHERPA, Herwig6, Herwig7, WHIZARD.
For more complictaed processes that include a more complicated final states, higher order corrections,
simultions of physics processes beyond Standard Model specific generators can be used.


## <a name="settings">"Most important settings"</a>
The most important general settings are
The enegry of the beams and initial and final state radiation.
The energy of the beams should match the energy of JADE beams during the simulated datataking period.
The output of the MC event generators should be put in the HepMC2, HePMC3 or HEPEVT formats.


## <a name="smearing">"Smearing"</a>
To Smear the MC generated events, these are fed to the original JADE software.
The events should be converted forts to the format accepted by the JADE software.
That is done with the convert utility.









