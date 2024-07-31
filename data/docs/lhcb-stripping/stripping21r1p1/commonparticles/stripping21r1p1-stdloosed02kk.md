[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdLooseD02KK

**CombineParticles/StdLooseD02KK**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21r1p1-stdloosekaons) /Particles', 'Phys/ [StdLoosePions](./stripping21r1p1-stdloosepions) /Particles'] |
| DaughtersCuts    | {'K+': '(P\>2\*GeV)', 'pi+': '(P\>2\*GeV)'}                                                                                                  |
| CombinationCut   | (((APT\>1\*GeV) \| (ASUM(PT)\>1.2\*GeV)) & (ADAMASS('D0')\<110\*MeV) & (ADOCA(1,2)\<0.5\*mm) & (ADOCACHI2CUT(15,'')))                        |
| MotherCut        | ((VFASPF(VCHI2)\<10) & (ADMASS('D0')\<100\*MeV) & (BPVVDCHI2\>36))                                                                           |
| DecayDescriptor  | [D0 -\> K- K+]cc                                                                                                                           |
| DecayDescriptors | []                                                                                                                                         |
| Output           | None                                                                                                                                         |
