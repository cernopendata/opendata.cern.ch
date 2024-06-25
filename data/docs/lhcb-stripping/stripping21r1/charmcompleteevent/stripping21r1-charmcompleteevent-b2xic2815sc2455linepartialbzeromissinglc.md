[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2Xic2815Sc2455LinePartialBZeroMissingLc

## Properties:

|                |                                                         |
|----------------|---------------------------------------------------------|
| OutputLocation | Phys/B2Xic2815Sc2455LinePartialBZeroMissingLc/Particles |
| Postscale      | 1.0000000                                               |
| HLT            | None                                                    |
| Prescale       | 1.0000000                                               |
| L0DU           | None                                                    |
| ODIN           | None                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingB2Xic2815Sc2455LinePartialBZeroMissingLcVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqB2Xic2815Sc2455CombineXicZero

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXicZeroToXiPi

GaudiSequencer/SeqB2Xic2815Sc2455CombineXi

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiLLL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                                 |

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

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                   |
| CombinationCut   | ( ADAMASS('Xi-') \< 50.0 \* MeV )                                                                                         |
| MotherCut        | ( ADMASS('Xi-') \< 35.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                    |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                 |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                         |
| Output           | Phys/B2Xic2815Sc2455CombineXiLLL/Particles                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiDDL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                                 |

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

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                   |
| CombinationCut   | ( ADAMASS('Xi-') \< 80.0 \* MeV )                                                                                         |
| MotherCut        | ( ADMASS('Xi-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                    |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                 |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                         |
| Output           | Phys/B2Xic2815Sc2455CombineXiDDL/Particles                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXiDDD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredDownstreamPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>100.0)& (MIPCHI2DV(PRIMARY)\>-1.0)                |
| Inputs          | [ 'Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/B2Xic2815Sc2455FilteredDownstreamPions/Particles                                 |

CombineParticles/B2Xic2815Sc2455CombineXiDDD

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredDownstreamPions' , 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                           |
| CombinationCut   | ( ADAMASS('Xi-') \< 80.0 \* MeV )                                                                                                 |
| MotherCut        | ( ADMASS('Xi-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                            |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                         |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                                 |
| Output           | Phys/B2Xic2815Sc2455CombineXiDDD/Particles                                                                                        |

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

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineXicZeroToXiPi

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXi' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'Xi-' : 'ALL' , 'Xi~+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ( ADAMASS('Xi_c0') \< 170.0 )                                                   |
| MotherCut        | (VFASPF(VCHI2)\<10.0)&(ADMASS('Xi_c0') \< 120.0)& (BPVDIRA \> 0.9)              |
| DecayDescriptor  | [Xi_c0 -\> Xi- pi+]cc                                                         |
| DecayDescriptors | [ '[Xi_c0 -\> Xi- pi+]cc' ]                                                 |
| Output           | Phys/B2Xic2815Sc2455CombineXicZeroToXiPi/Particles                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXicZeroToOmegaK

GaudiSequencer/SeqB2Xic2815Sc2455CombineOmega

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineOmegaLLL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredKaons

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDK-PIDpi\>5.0)                                                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredKaons/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineOmegaLLL

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredKaonsGP' , 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                     |
| CombinationCut   | ( ADAMASS('Omega-') \< 50.0 \* MeV )                                                                                      |
| MotherCut        | ( ADMASS('Omega-') \< 35.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                 |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                               |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                                       |
| Output           | Phys/B2Xic2815Sc2455CombineOmegaLLL/Particles                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineOmegaDDL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredKaons

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDK-PIDpi\>5.0)                                                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredKaons/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineOmegaDDL

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredKaonsGP' , 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                     |
| CombinationCut   | ( ADAMASS('Omega-') \< 80.0 \* MeV )                                                                                      |
| MotherCut        | ( ADMASS('Omega-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                 |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                               |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                                       |
| Output           | Phys/B2Xic2815Sc2455CombineOmegaDDL/Particles                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineOmegaDDD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseDownKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDownKaons](./stripping21r1-commonparticles-stdloosedownkaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredDownstreamKaons

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>100.0)& (MIPCHI2DV(PRIMARY)\>-1.0)              |
| Inputs          | [ 'Phys/[StdLooseDownKaons](./stripping21r1-commonparticles-stdloosedownkaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/B2Xic2815Sc2455FilteredDownstreamKaons/Particles                               |

CombineParticles/B2Xic2815Sc2455CombineOmegaDDD

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredDownstreamKaons' , 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                             |
| CombinationCut   | ( ADAMASS('Omega-') \< 80.0 \* MeV )                                                                                              |
| MotherCut        | ( ADMASS('Omega-') \< 50.0 \* MeV )&(VFASPF(VCHI2)\<15.0)                                                                         |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                                       |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                                               |
| Output           | Phys/B2Xic2815Sc2455CombineOmegaDDD/Particles                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2Xic2815Sc2455CombineOmega

|                 |                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                         |
| Inputs          | [ 'Phys/B2Xic2815Sc2455CombineOmegaDDD' , 'Phys/B2Xic2815Sc2455CombineOmegaDDL' , 'Phys/B2Xic2815Sc2455CombineOmegaLLL' ] |
| DecayDescriptor | None                                                                                                                        |
| Output          | Phys/B2Xic2815Sc2455CombineOmega/Particles                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredKaons

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDK-PIDpi\>5.0)                                                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredKaons/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineXicZeroToOmegaK

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineOmega' , 'Phys/B2Xic2815Sc2455FilteredKaonsGP' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Omega-' : 'ALL' , 'Omega~+' : 'ALL' } |
| CombinationCut   | ( ADAMASS('Xi_c0') \< 170.0 )                                                       |
| MotherCut        | (VFASPF(VCHI2)\<10.0)&(ADMASS('Xi_c0') \< 120.0)& (BPVDIRA \> 0.9)                  |
| DecayDescriptor  | [Xi_c0 -\> Omega- K+]cc                                                           |
| DecayDescriptors | [ '[Xi_c0 -\> Omega- K+]cc' ]                                                   |
| Output           | Phys/B2Xic2815Sc2455CombineXicZeroToOmegaK/Particles                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2Xic2815Sc2455CombineXicZeroToPKKpi

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredProtons

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDp-PIDpi\>5.0)& (PIDp-PIDK\>0.0)                                   |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/B2Xic2815Sc2455FilteredProtons/Particles                                   |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredKaons

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDK-PIDpi\>5.0)                                                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredKaons/Particles                                 |

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

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineXicZeroToPKKpi

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilteredKaonsGP' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' , 'Phys/B2Xic2815Sc2455FilteredProtonsGP' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                   |
| CombinationCut   | ( ADAMASS('Xi_c0') \< 170.0 )                                                                                                 |
| MotherCut        | (VFASPF(VCHI2)\<60.0)&(ADMASS('Xi_c0') \< 120.0)& (BPVDIRA \> 0.9)                                                            |
| DecayDescriptor  | [Xi_c0 -\> p+ K- K- pi+]cc                                                                                                  |
| DecayDescriptors | [ '[Xi_c0 -\> p+ K- K- pi+]cc' ]                                                                                          |
| Output           | Phys/B2Xic2815Sc2455CombineXicZeroToPKKpi/Particles                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2Xic2815Sc2455CombineXicZero

|                 |                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                           |
| Inputs          | [ 'Phys/B2Xic2815Sc2455CombineXicZeroToOmegaK' , 'Phys/B2Xic2815Sc2455CombineXicZeroToPKKpi' , 'Phys/B2Xic2815Sc2455CombineXicZeroToXiPi' ] |
| DecayDescriptor | None                                                                                                                                          |
| Output          | Phys/B2Xic2815Sc2455CombineXicZero/Particles                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/B2Xic2815Sc2455FilteredPions

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (HASRICH)&(PIDpi-PIDK\>0.0)                                                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2Xic2815Sc2455FilteredPions/Particles                                 |

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

CombineParticles/B2Xic2815Sc2455CombineXic2645Plus

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXicZero' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                  |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (VFASPF(VCHI2)\<15.0)&(M - CHILD(M,1) - CHILD(M,2) \> -20.0) & (M - CHILD(M,1) - CHILD(M,2) \< 60.0) |
| DecayDescriptor  | [Xi_c\*+ -\> Xi_c0 pi+]cc                                                                          |
| DecayDescriptors | [ '[Xi_c\*+ -\> Xi_c0 pi+]cc' ]                                                                  |
| Output           | Phys/B2Xic2815Sc2455CombineXic2645Plus/Particles                                                     |

CombineParticles/B2Xic2815Sc2455CombineXic2815Zero

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXic2645Plus' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]               |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c\*+' : 'ALL' , 'Xi_c\*~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }              |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (VFASPF(VCHI2)\<15.0)&(M - CHILD(M,1) - CHILD(M,2) \> -20.0) & (M - CHILD(M,1) - CHILD(M,2) \< 60.0) |
| DecayDescriptor  | [Xi'\_c0 -\> Xi_c\*+ pi-]cc                                                                        |
| DecayDescriptors | [ "[Xi'\_c0 -\> Xi_c\*+ pi-]cc" ]                                                                |
| Output           | Phys/B2Xic2815Sc2455CombineXic2815Zero/Particles                                                     |

CombineParticles/B2Xic2815Sc2455LinePartialBZeroMissingLc

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineXic2815Zero' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]  |
| DaughtersCuts    | { '' : 'ALL' , "Xi'\_c0" : 'ALL' , "Xi'\_c~0" : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                   |
| MotherCut        | (VFASPF(VCHI2)\<10.0)&(BPVVDCHI2\>25.0)&(M\<4000.0)                                     |
| DecayDescriptor  | [Delta+ -\> Xi'\_c0 pi+]cc                                                            |
| DecayDescriptors | [ "[Delta+ -\> Xi'\_c0 pi+]cc" ]                                                    |
| Output           | Phys/B2Xic2815Sc2455LinePartialBZeroMissingLc/Particles                                 |
