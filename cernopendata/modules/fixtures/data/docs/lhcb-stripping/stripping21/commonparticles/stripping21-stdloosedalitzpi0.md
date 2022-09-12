[[stripping21 lines]](./stripping21-index)

# StdLooseDalitzPi0

**CombineParticles/StdLooseDalitzPi0**

|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) /Particles', 'Phys/ [StdDiElectronGamma](./stripping21-stddielectrongamma) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                       |
| CombinationCut   | ATRUE                                                                                                                                                    |
| MotherCut        | (MM \< 170\*MeV) & (MM \> 90\*MeV) & (1 == CHILD(1,cnv)+CHILD(2,cnv) )                                                                                   |
| DecayDescriptor  | pi0 -\> gamma gamma                                                                                                                                      |
| DecayDescriptors | []                                                                                                                                                     |
| Output           | None                                                                                                                                                     |
