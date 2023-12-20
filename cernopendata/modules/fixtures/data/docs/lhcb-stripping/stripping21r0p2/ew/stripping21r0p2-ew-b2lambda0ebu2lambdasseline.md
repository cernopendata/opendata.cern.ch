[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2Lambda0EBu2LambdaSSELine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/B2Lambda0EBu2LambdaSSELine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionEW

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & ~ALG_PASSED('StrippingStreamEWBadEvent') |

LoKi::VoidFilter/StrippingB2Lambda0EBu2LambdaSSELineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 300.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseElectrons/Particles',True) |

FilterDesktop/Electron_forB2Lambda0E

|                 |                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDe-PIDpi\> 3.0 )& (PIDe-PIDp\> 3.0 )& (PIDe-PIDK\> 3.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r0p2-commonparticles-stdlooseelectrons)' ]                                                                                        |
| DecayDescriptor | None                                                                                                                                                                         |
| Output          | Phys/Electron_forB2Lambda0E/Particles                                                                                                                                        |

GaudiSequencer/MERGED:Selection_B2Lambda0E_LambdaMajoranaSSE

GaudiSequencer/MERGEDINPUTS:Selection_B2Lambda0E_LambdaMajoranaSSE

GaudiSequencer/INPUT:LambdaMajoranaSSE_forB2Lambda0E

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseElectrons/Particles',True) |

FilterDesktop/Electron_forB2Lambda0E

|                 |                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDe-PIDpi\> 3.0 )& (PIDe-PIDp\> 3.0 )& (PIDe-PIDK\> 3.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r0p2-commonparticles-stdlooseelectrons)' ]                                                                                        |
| DecayDescriptor | None                                                                                                                                                                         |
| Output          | Phys/Electron_forB2Lambda0E/Particles                                                                                                                                        |

CombineParticles/LambdaMajoranaSSE_forB2Lambda0E

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Electron_forB2Lambda0E' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                             |
| MotherCut        | ( M \> 1500.0\*MeV )&( BPVVDCHI2 \> 100.0 )&( VFASPF(VCHI2/VDOF) \< 10.0 )&( PT \> 700.0\*MeV )                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda0 -\> e- pi+]cc' ]                                                                                                                                                                                                   |
| Output           | Phys/LambdaMajoranaSSE_forB2Lambda0E/Particles                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:downLambdaMajoranaSSE_forB2Lambda0E

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsDownPions

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsDownPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsDownElectrons

|      |                                          |
|------|------------------------------------------|
| Code | 0StdNoPIDsDownElectrons/Particles',True) |

FilterDesktop/downElectron_forB2Lambda0E

|                 |                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDe-PIDpi\> 3.0 )& (PIDe-PIDp\> 3.0 )& (PIDe-PIDK\> 3.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdNoPIDsDownElectrons](./stripping21r0p2-commonparticles-stdnopidsdownelectrons)' ]                                                                              |
| DecayDescriptor | None                                                                                                                                                                         |
| Output          | Phys/downElectron_forB2Lambda0E/Particles                                                                                                                                    |

CombineParticles/downLambdaMajoranaSSE_forB2Lambda0E

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsDownPions](./stripping21r0p2-commonparticles-stdnopidsdownpions)' , 'Phys/downElectron_forB2Lambda0E' ]                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                             |
| MotherCut        | ( M \> 1500.0\*MeV )&( BPVVDCHI2 \> 100.0 )&( VFASPF(VCHI2/VDOF) \< 10.0 )&( PT \> 700.0\*MeV )                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda0 -\> e- pi+]cc' ]                                                                                                                                                                                                   |
| Output           | Phys/downLambdaMajoranaSSE_forB2Lambda0E/Particles                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2Lambda0E_LambdaMajoranaSSE

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                       |
| Inputs          | [ 'Phys/LambdaMajoranaSSE_forB2Lambda0E' , 'Phys/downLambdaMajoranaSSE_forB2Lambda0E' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2Lambda0E_LambdaMajoranaSSE/Particles                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2Lambda0EBu2LambdaSSELine

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Electron_forB2Lambda0E' , 'Phys/Selection_B2Lambda0E_LambdaMajoranaSSE' ]                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                               |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<6500.0\*MeV)                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99)& ( MINTREE((ABSID=='Lambda0'),VFASPF(VZ)) - VFASPF(VZ) \> -1.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                |
| DecayDescriptors | [ '[B- -\> Lambda0 e-]cc' ]                                                                                     |
| Output           | Phys/B2Lambda0EBu2LambdaSSELine/Particles                                                                           |
