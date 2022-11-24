[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StdLooseJpsi2MuMu

**CombineParticles/StdLooseJpsi2MuMu**

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) /Particles'] |
| DaughtersCuts    | {}                                                                            |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 100.\*MeV) & (ADOCACHI2CUT(30,''))                   |
| MotherCut        | (VFASPF(VCHI2) \< 25.)                                                        |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                         |
| DecayDescriptors | []                                                                          |
| Output           | None                                                                          |
