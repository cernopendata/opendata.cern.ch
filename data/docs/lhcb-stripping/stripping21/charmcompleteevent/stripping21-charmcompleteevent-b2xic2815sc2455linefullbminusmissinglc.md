[[stripping21 lines]](./stripping21-index)

# StrippingB2Xic2815Sc2455LineFullBMinusMissingLc

## Properties:

|                |                                                       |
|----------------|-------------------------------------------------------|
| OutputLocation | Phys/B2Xic2815Sc2455LineFullBMinusMissingLc/Particles |
| Postscale      | 1.0000000                                             |
| HLT            | None                                                  |
| Prescale       | 1.0000000                                             |
| L0DU           | None                                                  |
| ODIN           | None                                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingB2Xic2815Sc2455LineFullBMinusMissingLcVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqB2Xic2815Sc2455CombineXi

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiLLL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                               |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                               |

FilterDesktop/B2Xic2815Sc2455FilteredPionsBase

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>200.0)& (MIPCHI2DV(PRIMARY)\>4.0) |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPions' ]                             |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsBase/Particles                       |

FilterDesktop/B2Xic2815Sc2455FilteredPionsGP

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ( TRGHOSTPROB \< 0.5 )                        |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPionsBase' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsGP/Particles |

CombineParticles/B2Xic2815Sc2455CombineXiLLL

|                  |                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                 |
| CombinationCut   | ( ADAMASS('Xi-') \< 50.0 \* MeV )                                                                                       |
| MotherCut        | ( ADMASS('Xi-') \< 35.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                  |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                               |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                       |
| Output           | Phys/B2Xic2815Sc2455CombineXiLLL/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiDDL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                               |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                               |

FilterDesktop/B2Xic2815Sc2455FilteredPionsBase

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>200.0)& (MIPCHI2DV(PRIMARY)\>4.0) |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPions' ]                             |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsBase/Particles                       |

FilterDesktop/B2Xic2815Sc2455FilteredPionsGP

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ( TRGHOSTPROB \< 0.5 )                        |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPionsBase' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsGP/Particles |

CombineParticles/B2Xic2815Sc2455CombineXiDDL

|                  |                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                 |
| CombinationCut   | ( ADAMASS('Xi-') \< 80.0 \* MeV )                                                                                       |
| MotherCut        | ( ADMASS('Xi-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                  |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                               |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                       |
| Output           | Phys/B2Xic2815Sc2455CombineXiDDL/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiDDD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsDownPions](./stripping21-commonparticles-stdnopidsdownpions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredDownstreamPions

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>100.0)& (MIPCHI2DV(PRIMARY)\>-1.0)              |
| Inputs          | [ 'Phys/[StdNoPIDsDownPions](./stripping21-commonparticles-stdnopidsdownpions)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/B2Xic2815Sc2455FilteredDownstreamPions/Particles                               |

CombineParticles/B2Xic2815Sc2455CombineXiDDD

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredDownstreamPions' , 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                         |
| CombinationCut   | ( ADAMASS('Xi-') \< 80.0 \* MeV )                                                                                               |
| MotherCut        | ( ADMASS('Xi-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                          |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                       |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                               |
| Output           | Phys/B2Xic2815Sc2455CombineXiDDD/Particles                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2Xic2815Sc2455CombineXi

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                |
| Inputs          | [ 'Phys/B2Xic2815Sc2455CombineXiDDD' , 'Phys/B2Xic2815Sc2455CombineXiDDL' , 'Phys/B2Xic2815Sc2455CombineXiLLL' ] |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Xic2815Sc2455CombineXi/Particles                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                               |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                               |

FilterDesktop/B2Xic2815Sc2455FilteredPionsBase

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>200.0)& (MIPCHI2DV(PRIMARY)\>4.0) |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPions' ]                             |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsBase/Particles                       |

FilterDesktop/B2Xic2815Sc2455FilteredPionsGP

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ( TRGHOSTPROB \< 0.5 )                        |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredPionsBase' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/B2Xic2815Sc2455FilteredPionsGP/Particles |

CombineParticles/B2Xic2815Sc2455CombineXicPlus

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXi' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'Xi-' : 'ALL' , 'Xi~+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ( ADAMASS('Xi_c0') \< 170.0 )                                                   |
| MotherCut        | (VFASPF(VCHI2)\<30.0)&(ADMASS('Xi_c0') \< 120.0)& (BPVDIRA \> 0.9)              |
| DecayDescriptor  | [Xi_c+ -\> Xi- pi+ pi+]cc                                                     |
| DecayDescriptors | [ '[Xi_c+ -\> Xi- pi+ pi+]cc' ]                                             |
| Output           | Phys/B2Xic2815Sc2455CombineXicPlus/Particles                                    |

CombineParticles/B2Xic2815Sc2455CombineXic2645Zero

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXicPlus' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                  |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (VFASPF(VCHI2)\<15.0)&(M - CHILD(M,1) - CHILD(M,2) \> -20.0) & (M - CHILD(M,1) - CHILD(M,2) \< 60.0) |
| DecayDescriptor  | [Xi_c\*0 -\> Xi_c+ pi-]cc                                                                          |
| DecayDescriptors | [ '[Xi_c\*0 -\> Xi_c+ pi-]cc' ]                                                                  |
| Output           | Phys/B2Xic2815Sc2455CombineXic2645Zero/Particles                                                     |

CombineParticles/B2Xic2815Sc2455CombineXic2815Plus

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXic2645Zero' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]               |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c\*0' : 'ALL' , 'Xi_c\*~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }              |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (VFASPF(VCHI2)\<15.0)&(M - CHILD(M,1) - CHILD(M,2) \> -20.0) & (M - CHILD(M,1) - CHILD(M,2) \< 60.0) |
| DecayDescriptor  | [Xi'\_c+ -\> Xi_c\*0 pi+]cc                                                                        |
| DecayDescriptors | [ "[Xi'\_c+ -\> Xi_c\*0 pi+]cc" ]                                                                |
| Output           | Phys/B2Xic2815Sc2455CombineXic2815Plus/Particles                                                     |

CombineParticles/B2Xic2815Sc2455CombinePartialBMinusMissingLc

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXic2815Plus' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]  |
| DaughtersCuts    | { '' : 'ALL' , "Xi'\_c+" : 'ALL' , "Xi'\_c~-" : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                   |
| MotherCut        | (VFASPF(VCHI2)\<10.0)&(BPVVDCHI2\>25.0)&(M\<4000.0)                                     |
| DecayDescriptor  | [Delta0 -\> Xi'\_c+ pi-]cc                                                            |
| DecayDescriptors | [ "[Delta0 -\> Xi'\_c+ pi-]cc" ]                                                    |
| Output           | Phys/B2Xic2815Sc2455CombinePartialBMinusMissingLc/Particles                             |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredKaons

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDK-PIDpi\>5.0)                                               |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2Xic2815Sc2455FilteredKaons/Particles                               |

FilterDesktop/B2Xic2815Sc2455FilteredKaonsBase

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>200.0)& (MIPCHI2DV(PRIMARY)\>4.0) |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredKaons' ]                             |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredKaonsBase/Particles                       |

FilterDesktop/B2Xic2815Sc2455FilteredKaonsGP

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ( TRGHOSTPROB \< 0.5 )                        |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredKaonsBase' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/B2Xic2815Sc2455FilteredKaonsGP/Particles |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredProtons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDp-PIDpi\>5.0)& (PIDp-PIDK\>0.0)                                 |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/B2Xic2815Sc2455FilteredProtons/Particles                                 |

FilterDesktop/B2Xic2815Sc2455FilteredProtonsBase

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>200.0)& (MIPCHI2DV(PRIMARY)\>4.0) |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredProtons' ]                           |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredProtonsBase/Particles                     |

FilterDesktop/B2Xic2815Sc2455FilteredProtonsGP

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | ( TRGHOSTPROB \< 0.5 )                          |
| Inputs          | [ 'Phys/B2Xic2815Sc2455FilteredProtonsBase' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/B2Xic2815Sc2455FilteredProtonsGP/Particles |

CombineParticles/B2Xic2815Sc2455FilterLc

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredKaonsGP' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/B2Xic2815Sc2455FilteredProtonsGP' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                   |
| CombinationCut   | (ADAMASS('Lambda_c+')\<1.1\*75.0)& (AMAXCHILD(MIPCHI2DV(PRIMARY))\>4.0)& (ADOCAMAX('')\<0.5)& (APT\>1000.0)                   |
| MotherCut        | (VFASPF(VCHI2) \< 30.0)& (ADMASS('Lambda_c+')\<75.0)& (BPVVDCHI2\>16.0)& (BPVDIRA\>0.9)                                       |
| DecayDescriptor  | [Lambda_c+ -\> K- p+ pi+]cc                                                                                                 |
| DecayDescriptors | [ '[Lambda_c+ -\> K- p+ pi+]cc' ]                                                                                         |
| Output           | Phys/B2Xic2815Sc2455FilterLc/Particles                                                                                        |

CombineParticles/B2Xic2815Sc2455LineFullBMinusMissingLc

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombinePartialBMinusMissingLc' , 'Phys/B2Xic2815Sc2455FilterLc' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'Delta0' : 'ALL' , 'Delta~0' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                              |
| MotherCut        | (VFASPF(VCHI2)\<15.0)                                                                              |
| DecayDescriptor  | [B- -\> Delta0 Lambda_c~-]cc                                                                     |
| DecayDescriptors | [ '[B- -\> Delta0 Lambda_c~-]cc' ]                                                             |
| Output           | Phys/B2Xic2815Sc2455LineFullBMinusMissingLc/Particles                                              |
