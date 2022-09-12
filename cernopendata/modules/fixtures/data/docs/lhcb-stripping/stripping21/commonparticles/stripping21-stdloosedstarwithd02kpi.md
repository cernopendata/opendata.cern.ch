[[stripping21 lines]](./stripping21-index)

# StdLooseDstarWithD02KPi

**CombineParticles/StdLooseDstarWithD02KPi**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) /Particles', 'Phys/ [StdLooseD02KPi](./stripping21-stdloosed02kpi) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                           |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<50\*MeV) & (APT\>1250\*MeV)                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (M-MAXTREE('D0'==ABSID,M)\<165.5)                                                                                 |
| DecayDescriptor  | [D\*(2010)+ -\> pi+ D0]cc                                                                                                                  |
| DecayDescriptors | []                                                                                                                                         |
| Output           | None                                                                                                                                         |
