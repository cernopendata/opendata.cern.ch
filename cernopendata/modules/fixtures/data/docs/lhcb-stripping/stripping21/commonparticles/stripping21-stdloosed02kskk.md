[[stripping21 lines]](./stripping21-index)

# StdLooseD02KsKK

**CombineParticles/StdLooseD02KsKK**

|                  |                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLooseKaons](./stripping21-stdloosekaons) /Particles', 'Phys/ [StdLooseKsLL](./stripping21-stdlooseksll) /Particles'] |
| DaughtersCuts    | {'K+': '(PT\>300\*MeV)', 'KS0': '(PT\>800\*MeV)'}                                                                                  |
| CombinationCut   | (ADAMASS('D0')\<80) & (APT\>1500\*MeV)                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\>0.49)                                                                              |
| DecayDescriptor  | [D0 -\> KS0 K+ K-]cc                                                                                                             |
| DecayDescriptors | []                                                                                                                               |
| Output           | None                                                                                                                               |
