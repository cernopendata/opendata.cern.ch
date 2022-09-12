[[stripping21r1 lines]](./stripping21r1-index)

# StdLooseDetachedDiElectron

**CombineParticles/StdLooseDetachedDiElectron**

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLooseElectrons](./stripping21r1-stdalllooseelectrons) /Particles'] |
| DaughtersCuts    | {'e+': '(PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.)'}                                 |
| CombinationCut   | (ADOCACHI2CUT(30,''))                                                               |
| MotherCut        | (VFASPF(VCHI2)\<25)                                                                 |
| DecayDescriptor  | J/psi(1S) -\> e+ e-                                                                 |
| DecayDescriptors | []                                                                                |
| Output           | None                                                                                |
