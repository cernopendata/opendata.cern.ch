[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StdVeryLooseDetachedKst2Kpi

**CombineParticles/StdVeryLooseDetachedKst2Kpi**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21r0p2-stdloosekaons) /Particles', 'Phys/ [StdLoosePions](./stripping21r0p2-stdloosepions) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                           |
| CombinationCut   | (ADAMASS('K\*(892)0')\<300\*MeV) & (ADOCACHI2CUT(30, ''))                                                                                    |
| MotherCut        | (VFASPF(VCHI2)\<25)                                                                                                                          |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                                   |
| DecayDescriptors | []                                                                                                                                         |
| Output           | None                                                                                                                                         |
