[[stripping21 lines]](./stripping21-index)

# StdLTUnbiasedJpsi2MuMu

**FilterDesktop/StdLTUnbiasedJpsi2MuMu**

|                 |                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID, PT) \> 500.\*MeV)& (MINTREE('mu+'==ABSID, PIDmu) \> -10.0)& (MAXTREE('mu+'==ABSID, PIDK) \< 10.0)& (ADMASS('J/psi(1S)') \< 50.\*MeV)& (PT \> 1000.\*MeV)& (VFASPF(VCHI2) \< 6.0) |
| Inputs          | ['Phys/ [StdLooseJpsi2MuMu](./stripping21-stdloosejpsi2mumu) /Particles']                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                    |
| Output          | None                                                                                                                                                                                                    |
