[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdLooseDalitzPi0

**CombineParticles/StdLooseDalitzPi0**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseAllPhotons](./stripping21r1p1-stdlooseallphotons) /Particles', 'Phys/ [StdDiElectronGamma](./stripping21r1p1-stddielectrongamma) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                               |
| CombinationCut   | (AM \< 200\*MeV) & (1 == ACHILD(1,cnv)+ACHILD(2,cnv) )                                                                                                           |
| MotherCut        | (MM \< 170\*MeV) & (MM \> 90\*MeV)                                                                                                                               |
| DecayDescriptor  | pi0 -\> gamma gamma                                                                                                                                              |
| DecayDescriptors | []                                                                                                                                                             |
| Output           | None                                                                                                                                                             |
