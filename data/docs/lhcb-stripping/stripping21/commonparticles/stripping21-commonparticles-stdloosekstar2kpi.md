[[stripping21 lines]](./stripping21-index)

# StdLooseKstar2Kpi

**CombineParticles/StdLooseKstar2Kpi**

|                  |                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles', 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles'] |
| DaughtersCuts    | {}                                                                                                                                                                           |
| CombinationCut   | (APT \> 500.\*MeV) & (ADAMASS('K\*(892)0') \< 300.\*MeV) & (ADOCACHI2CUT(30, ''))                                                                                            |
| MotherCut        | (VFASPF(VCHI2) \< 25.)                                                                                                                                                       |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                                                                   |
| DecayDescriptors | []                                                                                                                                                                         |
| Output           | None                                                                                                                                                                         |
