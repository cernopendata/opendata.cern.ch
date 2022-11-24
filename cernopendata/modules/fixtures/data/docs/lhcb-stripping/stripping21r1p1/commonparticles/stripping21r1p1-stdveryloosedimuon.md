[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdVeryLooseDiMuon

**CombineParticles/StdVeryLooseDiMuon**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllVeryLooseMuons](./stripping21r1p1-stdallveryloosemuons) /Particles'] |
| DaughtersCuts    | {}                                                                                    |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 3000.\*MeV) & (ADOCACHI2CUT(30, ''))                         |
| MotherCut        | (VFASPF(VCHI2) \< 25.)                                                                |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                 |
| DecayDescriptors | []                                                                                  |
| Output           | None                                                                                  |
