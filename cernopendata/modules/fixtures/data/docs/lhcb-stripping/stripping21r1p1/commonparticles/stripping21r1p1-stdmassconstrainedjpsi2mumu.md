[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdMassConstrainedJpsi2MuMu

**CombineParticles/StdMassConstrainedJpsi2MuMu**

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) /Particles'] |
| DaughtersCuts    | {'mu+': '(PIDmu \> 0) & (PT \> 0.5\*GeV)'}                                    |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 150.\*MeV) & (ADOCACHI2CUT(20, ''))                  |
| MotherCut        | (VFASPF(VCHI2) \< 16.) & (MFIT)                                               |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                         |
| DecayDescriptors | []                                                                          |
| Output           | None                                                                          |
