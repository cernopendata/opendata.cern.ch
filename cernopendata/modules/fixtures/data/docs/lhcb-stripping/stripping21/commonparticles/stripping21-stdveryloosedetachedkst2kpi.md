[[stripping21 lines]](./stripping21-index)

# StdVeryLooseDetachedKst2Kpi

**CombineParticles/StdVeryLooseDetachedKst2Kpi**

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21-stdloosekaons) /Particles', 'Phys/ [StdLoosePions](./stripping21-stdloosepions) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                   |
| CombinationCut   | (ADAMASS('K\*(892)0')\<300\*MeV) & (ADOCACHI2CUT(30, ''))                                                                            |
| MotherCut        | (VFASPF(VCHI2)\<25)                                                                                                                  |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                           |
| DecayDescriptors | []                                                                                                                                 |
| Output           | None                                                                                                                                 |
