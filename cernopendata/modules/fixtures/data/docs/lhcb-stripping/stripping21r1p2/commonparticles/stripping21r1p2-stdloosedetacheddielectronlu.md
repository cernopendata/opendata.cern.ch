[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StdLooseDetachedDiElectronLU

**CombineParticles/StdLooseDetachedDiElectronLU**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLooseElectrons](./stripping21r1p2-stdalllooseelectrons) /Particles', 'Phys/ [StdNoPIDsUpElectrons](./stripping21r1p2-stdnopidsupelectrons) /Particles'] |
| DaughtersCuts    | {'e+': '(PT\>250\*MeV) & (MIPCHI2DV(PRIMARY) \> 4)'}                                                                                                                     |
| CombinationCut   | (AM\>30\*MeV) & (ADOCACHI2CUT(30,''))                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2)\<25)                                                                                                                                                      |
| DecayDescriptor  | J/psi(1S) -\> e+ e-                                                                                                                                                      |
| DecayDescriptors | []                                                                                                                                                                     |
| Output           | None                                                                                                                                                                     |
