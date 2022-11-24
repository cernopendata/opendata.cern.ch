[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdTightDetachedTau3pi

**CombineParticles/StdTightDetachedTau3pi**

|                  |                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdLoosePions](./stripping21r1p1-stdloosepions) /Particles']                                                                                                                                                                                                      |
| DaughtersCuts    | {'pi+': '(PT\>250.\*MeV) & (P\>2000.\*MeV) & (MIPCHI2DV(PRIMARY) \> 16.0) & (TRCHI2DOF\<4) & (TRGHOSTPROB\<0.4) & (PROBNNpi \> 0.55)', 'pi-': '(PT\>250.\*MeV) & (P\>2000.\*MeV) & (MIPCHI2DV(PRIMARY) \> 16.0) & (TRCHI2DOF\<4) & (TRGHOSTPROB\<0.4) & (PROBNNpi \> 0.55)'} |
| CombinationCut   | (APT\>800.\*MeV) & ((AM\>400.\*MeV) & (AM\<2100.\*MeV)) & (AMAXDOCA('')\<0.2\*mm) & (ANUM(PT \> 800\*MeV) \>= 1)                                                                                                                                                             |
| MotherCut        | (PT\>1000.\*MeV) & (M\>500.\*MeV) & (M\<2000.\*MeV) & (BPVDIRA\>0.99) & (VFASPF(VCHI2) \< 16) & (BPVVDCHI2\>16) & (BPVVDRHO\>0.1\*mm) & (BPVVDRHO\<7.0\*mm) & (BPVVDZ\>5.0\*mm)                                                                                              |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                         |
| DecayDescriptors | ['[tau+ -\> pi+ pi- pi+]cc']                                                                                                                                                                                                                                             |
| Output           | None                                                                                                                                                                                                                                                                         |
