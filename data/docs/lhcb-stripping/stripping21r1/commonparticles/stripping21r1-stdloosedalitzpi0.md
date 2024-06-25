[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseDalitzPi0

**CombineParticles/StdLooseDalitzPi0**

|                  |                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) /Particles', 'Phys/ [StdDiElectronGamma](./stripping21r1-stddielectrongamma) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                           |
| CombinationCut   | ATRUE                                                                                                                                                        |
| MotherCut        | (MM \< 170\*MeV) & (MM \> 90\*MeV) & (1 == CHILD(1,cnv)+CHILD(2,cnv) )                                                                                       |
| DecayDescriptor  | pi0 -\> gamma gamma                                                                                                                                          |
| DecayDescriptors | []                                                                                                                                                         |
| Output           | None                                                                                                                                                         |
