[[stripping21r1 lines]](./stripping21r1-index)

# StdVeryLooseLambdaLL

**CombineParticles/StdVeryLooseLambdaLL**

|                  |                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) /Particles', 'Phys/ [StdAllNoPIDsProtons](./stripping21r1-stdallnopidsprotons) /Particles'] |
| DaughtersCuts    | {'p+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>9)', 'pi+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>9)'}                                                              |
| CombinationCut   | (ADAMASS('Lambda0')\<50\*MeV) & (ADOCACHI2CUT(30, ''))                                                                                                       |
| MotherCut        | (ADMASS('Lambda0')\<35\*MeV) & (VFASPF(VCHI2)\<30) & (BPVVDCHI2 \> 4.)                                                                                       |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                     |
| DecayDescriptors | []                                                                                                                                                         |
| Output           | None                                                                                                                                                         |
