[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdLooseDstarWithD02PiPi

**CombineParticles/StdLooseDstarWithD02PiPi**

|                  |                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLoosePions](./stripping21r1p1-stdallloosepions) /Particles', 'Phys/ [StdLooseD02PiPi](./stripping21r1p1-stdloosed02pipi) /Particles'] |
| DaughtersCuts    | {}                                                                                                                                                     |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<50\*MeV) & (APT\>1250\*MeV)                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (M-MAXTREE('D0'==ABSID,M)\<165.5)                                                                                           |
| DecayDescriptor  | [D\*(2010)+ -\> pi+ D0]cc                                                                                                                            |
| DecayDescriptors | []                                                                                                                                                   |
| Output           | None                                                                                                                                                   |
