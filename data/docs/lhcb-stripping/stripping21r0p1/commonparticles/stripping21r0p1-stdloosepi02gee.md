[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StdLoosePi02gee

**CombineParticles/StdLoosePi02gee**

|                  |                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseAllPhotons](./stripping21r0p1-stdlooseallphotons) /Particles', 'Phys/ [StdAllLooseGammaLL](./stripping21r0p1-stdallloosegammall) /Particles', 'Phys/ [StdAllLooseGammaDD](./stripping21r0p1-stdallloosegammadd) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                                                                                                              |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                           |
| MotherCut        | (MM \< 170\*MeV) & (MM \> 90\*MeV) & (1 == CHILD(1,cnv)+CHILD(2,cnv) )                                                                                                                                                                          |
| DecayDescriptor  | pi0 -\> gamma gamma                                                                                                                                                                                                                             |
| DecayDescriptors | []                                                                                                                                                                                                                                            |
| Output           | None                                                                                                                                                                                                                                            |
