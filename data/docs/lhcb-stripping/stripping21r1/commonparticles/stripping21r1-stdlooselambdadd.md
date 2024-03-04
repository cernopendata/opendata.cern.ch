[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseLambdaDD

**CombineParticles/StdLooseLambdaDD**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdNoPIDsDownPions](./stripping21r1-stdnopidsdownpions) /Particles', 'Phys/ [StdNoPIDsDownProtons](./stripping21r1-stdnopidsdownprotons) /Particles'] |
| DaughtersCuts    | {'p+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>4)', 'pi+': '(P\>2\*GeV) & (MIPCHI2DV(PRIMARY)\>4)'}                                                                  |
| CombinationCut   | (ADAMASS('Lambda0')\<80\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                           |
| MotherCut        | (ADMASS('Lambda0')\<64\*MeV) & (VFASPF(VCHI2)\<25)                                                                                                               |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                         |
| DecayDescriptors | []                                                                                                                                                             |
| Output           | None                                                                                                                                                             |
