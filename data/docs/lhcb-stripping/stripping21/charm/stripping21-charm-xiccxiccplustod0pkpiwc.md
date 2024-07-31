[[stripping21 lines]](./stripping21-index)

# StrippingXiccXiccPlusToD0PKPiWC

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/XiccXiccPlusToD0PKPiWC/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingXiccXiccPlusToD0PKPiWCVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/XiccFilteredD02KPi

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('D0')\<75.0)& (BPVVDCHI2\>64.0)                                     |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/XiccFilteredD02KPi/Particles                                           |

TisTosParticleTagger/XiccdzeroTisTos

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/XiccFilteredD02KPi' ]             |
| DecayDescriptor | None                                        |
| Output          | Phys/XiccdzeroTisTos/Particles              |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD02.\*Decision%TOS' : 0 } |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseProtons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseProtons](./stripping21-commonparticles-stdalllooseprotons)/Particles')\>0 |

FilterDesktop/XiccFilteredProtons

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDp-PIDpi\>5.0)& (HASRICH)&(PIDp-PIDK\>0.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLooseProtons](./stripping21-commonparticles-stdalllooseprotons)' ]                                             |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/XiccFilteredProtons/Particles                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

FilterDesktop/XiccFilteredKaons

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDK-PIDpi\>5.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' ]                     |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/XiccFilteredKaons/Particles                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/XiccFilteredPions

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDpi-PIDK\>0.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                     |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/XiccFilteredPions/Particles                                                                    |

CombineParticles/XiccXiccPlusToD0PKPiWC

|                  |                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XiccFilteredKaons' , 'Phys/XiccFilteredPions' , 'Phys/XiccFilteredProtons' , 'Phys/XiccdzeroTisTos' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM\<4000.0)& (APT\>2000.0)& (ADOCAMAX('')\<0.5)                                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<60.0)&(CHILD(VFASPF(VZ),1) - VFASPF(VZ) \> 0.01)& (BPVVDCHI2 \> -1.0)& (BPVDIRA \> 0.0)                                    |
| DecayDescriptor  | [Xi_cc+ -\> D0 p+ K- pi-]cc                                                                                                              |
| DecayDescriptors | [ '[Xi_cc+ -\> D0 p+ K- pi-]cc' ]                                                                                                      |
| Output           | Phys/XiccXiccPlusToD0PKPiWC/Particles                                                                                                      |
