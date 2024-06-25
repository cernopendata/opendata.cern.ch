[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseRhoPlus

**CombineParticles/StdLooseRhoPlus**

|                  |                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseMergedPi0](./stripping21r1-stdloosemergedpi0) /Particles', 'Phys/ [StdLooseResolvedPi0](./stripping21r1-stdlooseresolvedpi0) /Particles', 'Phys/ [StdLoosePions](./stripping21r1-stdloosepions) /Particles', 'Phys/ [StdLooseKaons](./stripping21r1-stdloosekaons) /Particles'] |
| DaughtersCuts    | {'K+': 'ALL', 'pi0': '(PT\>1000\*MeV) & (P\> 1500\*MeV)', 'pi+': 'ALL'}                                                                                                                                                                                                                            |
| CombinationCut   | (ADAMASS('K\*(892)+')\<550\*MeV)                                                                                                                                                                                                                                                                   |
| MotherCut        | ALL                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [rho(770)- -\> pi- pi0]cc                                                                                                                                                                                                                                                                        |
| DecayDescriptors | []                                                                                                                                                                                                                                                                                               |
| Output           | None                                                                                                                                                                                                                                                                                               |
