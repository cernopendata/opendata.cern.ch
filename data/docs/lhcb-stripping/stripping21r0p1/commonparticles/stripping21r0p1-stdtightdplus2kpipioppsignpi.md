[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StdTightDplus2KPiPiOppSignPi

**CombineParticles/StdTightDplus2KPiPiOppSignPi**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21r0p1-stdloosekaons) /Particles', 'Phys/ [StdLoosePions](./stripping21r0p1-stdloosepions) /Particles'] |
| DaughtersCuts    | {'K+': '(P \> 2\*GeV) & ((PIDK-PIDpi) \> 7.)', 'pi+': '(P \> 2\*GeV) & ((PIDK-PIDpi) \< 3.)'}                                                |
| CombinationCut   | ((AM\>1760.\*MeV) & (AM\<2080.\*MeV) & ((APT\>1.\*GeV) \| (ASUM(PT)\>1.\*GeV)) & (ADOCAMAX('')\<0.5\*mm))                                    |
| MotherCut        | ((VFASPF(VCHI2) \< 30 ) & (M\>1770.\*MeV) & (M \< 2070.\*MeV) & (BPVVDCHI2\>36) & (BPVDIRA\>0.98))                                           |
| DecayDescriptor  | [D+ -\> pi- pi+ K+]cc                                                                                                                      |
| DecayDescriptors | []                                                                                                                                         |
| Output           | None                                                                                                                                         |
