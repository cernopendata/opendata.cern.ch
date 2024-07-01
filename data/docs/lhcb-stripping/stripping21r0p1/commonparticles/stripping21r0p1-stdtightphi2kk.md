[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StdTightPhi2KK

**CombineParticles/StdTightPhi2KK**

|                  |                                                                         |
|------------------|-------------------------------------------------------------------------|
| Inputs           | ['Phys/ [StdTightKaons](./stripping21r0p1-stdtightkaons) /Particles'] |
| DaughtersCuts    | {'K+': '(PT\>500\*MeV)'}                                                |
| CombinationCut   | (ADAMASS('phi(1020)')\<30\*MeV) & (ADOCACHI2CUT(30, ''))                |
| MotherCut        | (VFASPF(VCHI2) \< 25.0)                                                 |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                     |
| DecayDescriptors | []                                                                    |
| Output           | None                                                                    |
