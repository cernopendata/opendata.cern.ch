[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseDstarWithD02KK

**CombineParticles/StdLooseDstarWithD02KK**

|                  |                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) /Particles', 'Phys/ [StdLooseD02KK](./stripping21r1-stdloosed02kk) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                             |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<50\*MeV) & (APT\>1250\*MeV)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (M-MAXTREE('D0'==ABSID,M)\<165.5)                                                                                   |
| DecayDescriptor  | [D\*(2010)+ -\> pi+ D0]cc                                                                                                                    |
| DecayDescriptors | []                                                                                                                                           |
| Output           | None                                                                                                                                           |
