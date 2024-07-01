[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSLambdab2JpsiLambdaUnbiasedLine

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/BetaSLambdab2JpsiLambdaUnbiasedLine/Particles |
| Postscale      | 1.0000000                                          |
| HLT            | None                                               |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/NarrowJpsiForBetaSBetaS

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV)                                                              |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/NarrowJpsiForBetaSBetaS/Particles                                                                  |

GaudiSequencer/SeqStdLooseLambdaMergedForBetaSBetaS

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/StdLooseLambdaMergedForBetaSBetaS

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' , 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ] |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/StdLooseLambdaMergedForBetaSBetaS/Particles                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LambdaForBetaSBetaS

|                 |                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MAXTREE('p+'==ABSID, PT) \> 500.\*MeV) & (MAXTREE('pi-'==ABSID, PT) \> 100.\*MeV) & (ADMASS('Lambda0') \< 15.\*MeV) & (VFASPF(VCHI2) \< 20) |
| Inputs          | [ 'Phys/StdLooseLambdaMergedForBetaSBetaS' ]                                                                                               |
| DecayDescriptor | None                                                                                                                                         |
| Output          | Phys/LambdaForBetaSBetaS/Particles                                                                                                           |

CombineParticles/BetaSLambdab2JpsiLambdaUnbiasedLine

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LambdaForBetaSBetaS' , 'Phys/NarrowJpsiForBetaSBetaS' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' } |
| CombinationCut   | in_range(5020,AM,6220)                                                        |
| MotherCut        | in_range(5120,M,6120) & (VFASPF(VCHI2PDOF) \< 10)                             |
| DecayDescriptor  | [Lambda_b0 -\> Lambda0 J/psi(1S) ]cc                                        |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda0 J/psi(1S) ]cc' ]                                |
| Output           | Phys/BetaSLambdab2JpsiLambdaUnbiasedLine/Particles                            |
