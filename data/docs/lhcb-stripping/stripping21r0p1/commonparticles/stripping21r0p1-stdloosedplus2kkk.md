[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StdLooseDplus2KKK

**CombineParticles/StdLooseDplus2KKK**

|                  |                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21r0p1-stdloosekaons) /Particles']                                                                                                                                                                 |
| DaughtersCuts    | {'K+': '(PT \> 250\*MeV) & (P \> 2000\*MeV) &((MIPCHI2DV(PRIMARY)) \> 2.0 ) & (PIDK-PIDpi \> 3.0)'}                                                                                                                                     |
| CombinationCut   | (AM\>1760.\*MeV) & (AM\<2080.\*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 2500\*MeV) & (ADOCACHI2CUT(50 , '' )) & (ANUM(MIPCHI2DV(PRIMARY) \> 4.0 ) \>= 2) & (AHASCHILD(MIPCHI2DV(PRIMARY) \> 10.0)) & (ADOCAMAX('') \< 0.5\*mm) |
| MotherCut        | (PT \> 1000) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.98) & (BPVIPCHI2() \< 15.0) & (VFASPF(VMINVDCHI2DV(PRIMARY)) \> 100.0)                                                                                                      |
| DecayDescriptor  | [D+ -\> K- K+ K+]cc                                                                                                                                                                                                                   |
| DecayDescriptors | []                                                                                                                                                                                                                                    |
| Output           | None                                                                                                                                                                                                                                    |
