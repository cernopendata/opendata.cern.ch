[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XGammaExclBs2PhiGammaLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2XGammaExclBs2PhiGammaLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) /Particles')\>0 |

**FilterDesktop/PhotonSelB2XGammaExcl**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\> 2600.0\*MeV)                                                      |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/PhotonSelB2XGammaExcl/Particles                                    |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21r1-stdloosephi2kk) /Particles')\>0 |

**FilterDesktop/PhiSelB2XGammaExcl**

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | goodPhi & CHILDCUT( goodKaon, 1 ) & CHILDCUT( goodKaon, 2 )     |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21r1-stdloosephi2kk) ' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/PhiSelB2XGammaExcl/Particles                               |

**CombineParticles/B2XGammaExclBs2PhiGammaLine**

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhiSelB2XGammaExcl' , 'Phys/PhotonSelB2XGammaExcl' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' }                 |
| CombinationCut   | (ADAMASS('B_s0')\<1.5\*1000.0\*MeV)                                    |
| MotherCut        | (BPVIPCHI2() \< 15.0) & (PT \> 3000.0) & (ADMASS('B_s0')\<1000.0\*MeV) |
| DecayDescriptor  | B_s0 -\> phi(1020) gamma                                               |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) gamma' ]                                       |
| Output           | Phys/B2XGammaExclBs2PhiGammaLine/Particles                             |
