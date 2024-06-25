[[stripping21 lines]](./stripping21-index)

# StdLoosePi02gee

**CombineParticles/StdLoosePi02gee**

|                  |                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) /Particles', 'Phys/ [StdAllLooseGammaLL](./stripping21-stdallloosegammall) /Particles', 'Phys/ [StdAllLooseGammaDD](./stripping21-stdallloosegammadd) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                                                                                                  |
| CombinationCut   | ATRUE                                                                                                                                                                                                                               |
| MotherCut        | (MM \< 170\*MeV) & (MM \> 90\*MeV) & (1 == CHILD(1,cnv)+CHILD(2,cnv) )                                                                                                                                                              |
| DecayDescriptor  | pi0 -\> gamma gamma                                                                                                                                                                                                                 |
| DecayDescriptors | []                                                                                                                                                                                                                                |
| Output           | None                                                                                                                                                                                                                                |
