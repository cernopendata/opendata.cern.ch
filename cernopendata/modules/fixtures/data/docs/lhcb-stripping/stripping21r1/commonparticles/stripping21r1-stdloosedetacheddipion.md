[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseDetachedDipion

**CombineParticles/StdLooseDetachedDipion**

|                  |                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLoosePions](./stripping21r1-stdloosepions) /Particles']                                                                                                                                                    |
| DaughtersCuts    | {'pi+': '(PT\>150.\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.4) & (PIDK \< 8)', 'pi-': '(PT\>150.\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.4) & (PIDK \< 8)'} |
| CombinationCut   | (ANUM(PT \< 300\*MeV) \<= 1) & (ADOCAMAX('') \< 0.25\*mm) & (AM\<1670.\*MeV)                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2) \< 9.0) & (MIPCHI2DV(PRIMARY) \> 5.0) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0\*mm)                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                     |
| DecayDescriptors | ['rho(770)0 -\> pi+ pi-', '[rho(770)+ -\> pi+ pi+]cc']                                                                                                                                                               |
| Output           | None                                                                                                                                                                                                                     |
