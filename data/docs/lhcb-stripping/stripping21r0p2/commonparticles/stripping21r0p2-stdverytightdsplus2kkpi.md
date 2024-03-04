[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StdVeryTightDsplus2KKPi

**CombineParticles/StdVeryTightDsplus2KKPi**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21r0p2-stdloosekaons) /Particles', 'Phys/ [StdLoosePions](./stripping21r0p2-stdloosepions) /Particles'] |
| DaughtersCuts    | {'K+': '(P \> 2\*GeV) & ((PIDK-PIDpi) \> 5.)', 'pi+': '(P \> 2\*GeV) & ((PIDK-PIDpi) \< 5.)'}                                                |
| CombinationCut   | ((AM\>1900.\*MeV) & (AM\<2040.\*MeV) & ((APT\>1.\*GeV) \| (ASUM(PT)\>1.\*GeV)) & (ADOCAMAX('')\<0.5\*mm))                                    |
| MotherCut        | ((VFASPF(VCHI2) \< 30 ) & (M\>1920.\*MeV) & (M \< 2020.\*MeV) & (BPVVDCHI2\>36) & (BPVDIRA\>0.98))                                           |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+]cc                                                                                                                     |
| DecayDescriptors | []                                                                                                                                         |
| Output           | None                                                                                                                                         |
