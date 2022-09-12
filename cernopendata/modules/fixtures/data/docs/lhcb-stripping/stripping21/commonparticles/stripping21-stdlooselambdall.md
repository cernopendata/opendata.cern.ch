[[stripping21 lines]](./stripping21-index)

# StdLooseLambdaLL

**CombineParticles/StdLooseLambdaLL**

|                  |                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLoosePions](./stripping21-stdloosepions) /Particles', 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles'] |
| DaughtersCuts    | {'p+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>9)', 'pi+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>9)'}                                          |
| CombinationCut   | (ADAMASS('Lambda0')\<50\*MeV) & (ADOCACHI2CUT(30, ''))                                                                                   |
| MotherCut        | (ADMASS('Lambda0')\<35\*MeV) & (VFASPF(VCHI2)\<30)                                                                                       |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                 |
| DecayDescriptors | []                                                                                                                                     |
| Output           | None                                                                                                                                     |
