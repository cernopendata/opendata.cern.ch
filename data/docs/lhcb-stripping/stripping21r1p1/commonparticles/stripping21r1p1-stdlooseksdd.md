[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdLooseKsDD

**CombineParticles/StdLooseKsDD**

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdNoPIDsDownPions](./stripping21r1p1-stdnopidsdownpions) /Particles'] |
| DaughtersCuts    | {'pi+': '(P \> 2.\*GeV) & (MIPCHI2DV(PRIMARY) \> 4.)'}                            |
| CombinationCut   | (ADAMASS('KS0') \< 80.\*MeV) & (ADOCACHI2CUT(25, ''))                             |
| MotherCut        | (ADMASS('KS0') \< 64.\*MeV) & (VFASPF(VCHI2) \< 25.)                              |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                   |
| DecayDescriptors | []                                                                              |
| Output           | None                                                                              |
