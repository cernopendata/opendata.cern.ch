[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

## Properties:

|                |                                                                |
|----------------|----------------------------------------------------------------|
| OutputLocation | Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |
| Postscale      | 1.0000000                                                      |
| HLT1           | None                                                           |
| HLT2           | None                                                           |
| Prescale       | 1.0000000                                                      |
| L0DU           | None                                                           |
| ODIN           | None                                                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

DaVinci::N3BodyDecays/threepartWS_SC_B2ppipiSigmacmm_Lcpi

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' , 'Phys/[StdLooseProtons](./stripping21r0p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT\>500.0)&(P\>10000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDp-PIDpi)\>10.0) & ((PIDp-PIDK)\>0.0)' , 'pi+' : '(PT\>400.0)&(P\>5000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDK-PIDpi)\<0.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PT\>400.0)&(P\>5000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDK-PIDpi)\<0.0) & ( TRGHOSTPROB \< 0.5 )' , 'p~-' : '(PT\>500.0)&(P\>10000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDp-PIDpi)\>10.0) & ((PIDp-PIDK)\>0.0)' } |
| CombinationCut   | (AMAXDOCA('')\<0.15) & (APT\>1000.0) & (AM\<2800.0) & (AM\>1500.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MotherCut        | (PT\>1000.0) & (VFASPF(VCHI2/VDOF)\<5.0) & (VFASPF(VMINVDCHI2DV(PRIMARY))\>49.0) & (M\<2800.0) & (M\>1500.0) & (MIPCHI2DV(PRIMARY)\>6.0)                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | [D+ -\> p~- pi+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D+ -\> p~- pi+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/threepartWS_SC_B2ppipiSigmacmm_Lcpi/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/pifromSigmamm_B2ppipiSigmacmm_Lcpi

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) &(PT\>200.0)&(P\>2000.0) &(PT\<1000000.0)&(P\<10000000.0) & (MIPCHI2DV(PRIMARY)\>8.0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                  |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/pifromSigmamm_B2ppipiSigmacmm_Lcpi/Particles                                                      |

CombineParticles/fourpartWS_SCB2ppipiSigmacmm_Lcpi

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/pifromSigmamm_B2ppipiSigmacmm_Lcpi' , 'Phys/threepartWS_SC_B2ppipiSigmacmm_Lcpi' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                 |
| CombinationCut   | (AMAXDOCA('')\<0.15) & (APT\>1000.0)                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<5.0) & (MIPCHI2DV(PRIMARY)\>6.0) & (VFASPF(VMINVDCHI2DV(PRIMARY))\>49.0) & (PT\>1000.0) & ((M)\>1800.0) & ((M)\<3000.0) |
| DecayDescriptor  | [B+ -\> pi+ D+]cc                                                                                                                          |
| DecayDescriptors | [ '[B+ -\> pi+ D+]cc' ]                                                                                                                  |
| Output           | Phys/fourpartWS_SCB2ppipiSigmacmm_Lcpi/Particles                                                                                             |

TisTosParticleTagger/fourpartWS_SCB2ppipiSigmacmm_LcpiTOS

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/fourpartWS_SCB2ppipiSigmacmm_Lcpi' ]      |
| DecayDescriptor | None                                                |
| Output          | Phys/fourpartWS_SCB2ppipiSigmacmm_LcpiTOS/Particles |
| TisTosSpecs     | { 'Hlt2.\*Decision%TOS' : 0 }                       |

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdac2PKPi

|      |                                        |
|------|----------------------------------------|
| Code | 0StdLooseLambdac2PKPi/Particles',True) |

CombineParticles/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                  |                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21r0p2-commonparticles-stdlooselambdac2pkpi)' , 'Phys/fourpartWS_SCB2ppipiSigmacmm_LcpiTOS' ]                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'B+' : 'ALL' , 'B-' : 'ALL' , 'Lambda_c+' : "(ADMASS('Lambda_c~-')\<100.0) & (BPVVDCHI2\>64.0) & (VFASPF(VCHI2/VDOF)\<5.0)" , 'Lambda_c~-' : "(ADMASS('Lambda_c~-')\<100.0) & (BPVVDCHI2\>64.0) & (VFASPF(VCHI2/VDOF)\<5.0)" } |
| CombinationCut   | (AMAXDOCA('')\<0.2)                                                                                                                                                                                                                           |
| MotherCut        | (ADMASS('B+')\<200.0) & (BPVVDCHI2\>64.0) & (BPVDIRA\>0.9995) & (VFASPF(VCHI2/VDOF)\<5.0)                                                                                                                                                     |
| DecayDescriptor  | [B0 -\> Lambda_c~- B+]cc                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[B0 -\> Lambda_c~- B+]cc' ]                                                                                                                                                                                                            |
| Output           | Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo1_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo2_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo2_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo3_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo3_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo4_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo4_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo5_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo5_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo6_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo6_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo7_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo7_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |

AddRelatedInfo/RelatedInfo8_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC' ]                |
| DecayDescriptor | None                                                                        |
| Output          | Phys/RelatedInfo8_B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart_WS_SC/Particles |
