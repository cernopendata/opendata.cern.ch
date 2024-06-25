[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StdVeryLooseKsLL

**CombineParticles/StdVeryLooseKsLL**

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllNoPIDsPions](./stripping21r1p2-stdallnopidspions) /Particles'] |
| DaughtersCuts    | {'pi+': '(P \> 2.\*GeV) & (MIPCHI2DV(PRIMARY) \> 9.)'}                          |
| CombinationCut   | (ADAMASS('KS0') \< 50.\*MeV) & (ADOCACHI2CUT(30, ''))                           |
| MotherCut        | (ADMASS('KS0') \< 35.\*MeV) & (CHI2VX \< 30.) & (BPVVDCHI2\>4.)                 |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                 |
| DecayDescriptors | []                                                                            |
| Output           | None                                                                            |
