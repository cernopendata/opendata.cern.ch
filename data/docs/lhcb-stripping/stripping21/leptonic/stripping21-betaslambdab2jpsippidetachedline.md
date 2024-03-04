[[stripping21 lines]](./stripping21-index)

# StrippingBetaSLambdab2JpsippiDetachedLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/BetaSLambdab2JpsippiDetachedLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

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

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) /Particles')\>0 |

**FilterDesktop/NoPIDPionsForBetaSBetaS**

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5 )                                             |
| Inputs          | [ 'Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) ' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/NoPIDPionsForBetaSBetaS/Particles                        |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles')\>0 |

**FilterDesktop/ProtonsForBetaSBetaS**

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5 )                                               |
| Inputs          | [ 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) ' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/ProtonsForBetaSBetaS/Particles                             |

**CombineParticles/Lambdab2JpsippiBetaS**

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/NarrowJpsiForBetaSBetaS' , 'Phys/NoPIDPionsForBetaSBetaS' , 'Phys/ProtonsForBetaSBetaS' ]                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'p+' : '(PT\>500\*MeV) & (MIPCHI2DV(PRIMARY)\>9)' , 'pi+' : '(PT\>500\*MeV) & (MIPCHI2DV(PRIMARY)\>9)' , 'pi-' : '(PT\>500\*MeV) & (MIPCHI2DV(PRIMARY)\>9)' , 'p\~-' : '(PT\>500\*MeV) & (MIPCHI2DV(PRIMARY)\>9)' } |
| CombinationCut   | in_range(4800,AM,6200)                                                                                                                                                                                                                                   |
| MotherCut        | in_range(4900,M,6100) & (VFASPF(VCHI2PDOF) \< 5)                                                                                                                                                                                                         |
| DecayDescriptor  | [Lambda_b0 -\> J/psi(1S) p+ pi-]cc                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[Lambda_b0 -\> J/psi(1S) p+ pi-]cc' ]                                                                                                                                                                                                             |
| Output           | Phys/Lambdab2JpsippiBetaS/Particles                                                                                                                                                                                                                      |

**FilterDesktop/BetaSLambdab2JpsippiDetachedLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps)                         |
| Inputs          | [ 'Phys/Lambdab2JpsippiBetaS' ]               |
| DecayDescriptor | None                                            |
| Output          | Phys/BetaSLambdab2JpsippiDetachedLine/Particles |
