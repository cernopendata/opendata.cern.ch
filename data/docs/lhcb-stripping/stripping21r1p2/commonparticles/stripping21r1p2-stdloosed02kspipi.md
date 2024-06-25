[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StdLooseD02KsPiPi

**CombineParticles/StdLooseD02KsPiPi**

|                  |                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLoosePions](./stripping21r1p2-stdloosepions) /Particles', 'Phys/ [StdLooseKsLL](./stripping21r1p2-stdlooseksll) /Particles'] |
| DaughtersCuts    | {'pi+': '(PT\>400\*MeV)', 'KS0': '(PT\>1\*GeV)'}                                                                                           |
| CombinationCut   | (ADAMASS('D0')\<80\*MeV) & (APT\>1800\*MeV)                                                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\>1)                                                                                         |
| DecayDescriptor  | [D0 -\> KS0 pi+ pi-]cc                                                                                                                   |
| DecayDescriptors | []                                                                                                                                       |
| Output           | None                                                                                                                                       |
