[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXiccXiccPlusPlusToLcKPiPiWC

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/XiccXiccPlusPlusToLcKPiPiWC/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingXiccXiccPlusPlusToLcKPiPiWCVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/XiccFilterLc

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' , 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDK - PIDpi)\>5.0)' , 'K-' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDK - PIDpi)\>5.0)' , 'p+' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDp - PIDpi)\>5.0)&((PIDp-PIDK)\>0.0)' , 'pi+' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDpi - PIDK)\>0.0)' , 'pi-' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDpi - PIDK)\>0.0)' , 'p~-' : '(TRCHI2DOF\<5.0)& (PT\>200.0)& (P\>2000.0)&(HASRICH)&((PIDp - PIDpi)\>5.0)&((PIDp-PIDK)\>0.0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+')\<1.1\*75.0)& (AMAXCHILD(MIPCHI2DV(PRIMARY))\>4.0)& (ADOCAMAX('')\<0.5)& (APT\>1000.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2) \< 30.0)& (ADMASS('Lambda_c+')\<75.0)& (BPVVDCHI2\>16.0)& (BPVDIRA\>0.99)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [Lambda_c+ -\> K- p+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda_c+ -\> K- p+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output           | Phys/XiccFilterLc/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/XiccfilterLcTisTos

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/XiccFilterLc' ]                            |
| DecayDescriptor | None                                                 |
| Output          | Phys/XiccfilterLcTisTos/Particles                    |
| TisTosSpecs     | { 'Hlt2.\*CharmHadLambdaC2KPPi.\*Decision%TOS' : 0 } |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/XiccFilteredPions

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDpi-PIDK\>0.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]                   |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/XiccFilteredPions/Particles                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)/Particles')\>0 |

FilterDesktop/XiccFilteredKaons

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDK-PIDpi\>5.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)' ]                   |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/XiccFilteredKaons/Particles                                                                    |

CombineParticles/XiccXiccPlusPlusToLcKPiPiWC

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XiccFilteredKaons' , 'Phys/XiccFilteredPions' , 'Phys/XiccfilterLcTisTos' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM\<4000.0)& (APT\>2000.0)& (ADOCAMAX('')\<0.5)                                                                          |
| MotherCut        | (VFASPF(VCHI2)\<60.0)&(CHILD(VFASPF(VZ),1) - VFASPF(VZ) \> 0.01)& (BPVVDCHI2 \> -1.0)& (BPVDIRA \> 0.0)                   |
| DecayDescriptor  | [Xi_cc++ -\> Lambda_c+ K- pi+ pi-]cc                                                                                    |
| DecayDescriptors | [ '[Xi_cc++ -\> Lambda_c+ K- pi+ pi-]cc' ]                                                                            |
| Output           | Phys/XiccXiccPlusPlusToLcKPiPiWC/Particles                                                                                |
