[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2Xic2815Sc2455LinePartialBZeroMissingXic

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/B2Xic2815Sc2455LinePartialBZeroMissingXic/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingB2Xic2815Sc2455LinePartialBZeroMissingXicVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

CombineParticles/B2Xic2815Sc2455CombineScZero

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455FilterLc' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }          |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (VFASPF(VCHI2)\<15.0)&(M - CHILD(M,1) - CHILD(M,2) \> -20.0) & (M - CHILD(M,1) - CHILD(M,2) \< 60.0) |
| DecayDescriptor  | [Sigma_c0 -\> Lambda_c+ pi-]cc                                                                     |
| DecayDescriptors | [ '[Sigma_c0 -\> Lambda_c+ pi-]cc' ]                                                             |
| Output           | Phys/B2Xic2815Sc2455CombineScZero/Particles                                                          |

CombineParticles/B2Xic2815Sc2455LinePartialBZeroMissingXic

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Xic2815Sc2455CombineScZero' , 'Phys/B2Xic2815Sc2455FilteredPionsGP' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'Sigma_c0' : 'ALL' , 'Sigma_c~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                     |
| MotherCut        | (VFASPF(VCHI2)\<30.0)&(BPVVDCHI2\>25.0)&(M\<4000.0)                                       |
| DecayDescriptor  | [Delta0 -\> Sigma_c0 pi+ pi-]cc                                                         |
| DecayDescriptors | [ '[Delta0 -\> Sigma_c0 pi+ pi-]cc' ]                                                 |
| Output           | Phys/B2Xic2815Sc2455LinePartialBZeroMissingXic/Particles                                  |
