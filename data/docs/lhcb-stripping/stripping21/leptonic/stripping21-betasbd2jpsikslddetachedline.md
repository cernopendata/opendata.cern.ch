[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBd2JpsiKsLDDetachedLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiKsLDDetachedLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**FilterDesktop/NarrowJpsiForBetaSBetaS**

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV)                                              |
| Inputs          | [ 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21-stdmassconstrainedjpsi2mumu) ' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/NarrowJpsiForBetaSBetaS/Particles                                                  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsLD_Particles**

|      |                                                                            |
|------|----------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsLD](./stripping21-stdlooseksld) /Particles')\>0 |

**FilterDesktop/KsLDForBetaSBetaS**

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | (VFASPF(VCHI2)\<20) & (BPVDLS\>5)                         |
| Inputs          | [ 'Phys/ [StdLooseKsLD](./stripping21-stdlooseksld) ' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/KsLDForBetaSBetaS/Particles                          |

**CombineParticles/Bd2JpsiKSLDBetaS**

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| Inputs           | [ 'Phys/KsLDForBetaSBetaS' , 'Phys/NarrowJpsiForBetaSBetaS' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }            |
| CombinationCut   | in_range(5000,AM,5650)                                          |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF) \< 10)               |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                            |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                    |
| Output           | Phys/Bd2JpsiKSLDBetaS/Particles                                 |

**FilterDesktop/BetaSBd2JpsiKsLDDetachedLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps)                     |
| Inputs          | [ 'Phys/Bd2JpsiKSLDBetaS' ]               |
| DecayDescriptor | None                                        |
| Output          | Phys/BetaSBd2JpsiKsLDDetachedLine/Particles |
