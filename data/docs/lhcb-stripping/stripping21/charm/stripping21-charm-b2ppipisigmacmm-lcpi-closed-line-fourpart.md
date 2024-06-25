[[stripping21 lines]](./stripping21-index)

# StrippingB2ppipiSigmacmm_Lcpi_Closed_Line_FourPart

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

DaVinci::N3BodyDecays/threepart_B2ppipiSigmacmm_Lcpi

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' , 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT\>500.0)&(P\>10000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDp-PIDpi)\>5.0) & ((PIDp-PIDK)\>-5.0)' , 'pi+' : '(PT\>400.0)&(P\>5000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDK-PIDpi)\<0.0) & ( TRGHOSTPROB \< 0.3 )' , 'pi-' : '(PT\>400.0)&(P\>5000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDK-PIDpi)\<0.0) & ( TRGHOSTPROB \< 0.3 )' , 'p~-' : '(PT\>500.0)&(P\>10000.0) & (TRCHI2DOF\<3.0) & (MIPCHI2DV(PRIMARY)\>8.0) & ((PIDp-PIDpi)\>5.0) & ((PIDp-PIDK)\>-5.0)' } |
| CombinationCut   | (AMAXDOCA('')\<0.15) & (APT\>1000.0) & (AM\<2800.0) & (AM\>1500.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MotherCut        | (PT\>1000.0) & (VFASPF(VCHI2/VDOF)\<5.0) & (VFASPF(VMINVDCHI2DV(PRIMARY))\>49.0) & (M\<2800.0) & (M\>1500.0) & (MIPCHI2DV(PRIMARY)\>6.0)                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | [D+ -\> p+ pi+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[D+ -\> p+ pi+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/threepart_B2ppipiSigmacmm_Lcpi/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/pifromSigmamm_B2ppipiSigmacmm_Lcpi

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) &(PT\>150.0)&(P\>2000.0) &(PT\<1000000.0)&(P\<10000000.0) & (MIPCHI2DV(PRIMARY)\>8.0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                      |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/pifromSigmamm_B2ppipiSigmacmm_Lcpi/Particles                                                      |

CombineParticles/fourpartB2ppipiSigmacmm_Lcpi

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/pifromSigmamm_B2ppipiSigmacmm_Lcpi' , 'Phys/threepart_B2ppipiSigmacmm_Lcpi' ]                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                 |
| CombinationCut   | (AMAXDOCA('')\<0.15) & (APT\>1000.0)                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<5.0) & (MIPCHI2DV(PRIMARY)\>6.0) & (VFASPF(VMINVDCHI2DV(PRIMARY))\>49.0) & (PT\>1000.0) & ((M)\>1800.0) & ((M)\<3000.0) |
| DecayDescriptor  | [B+ -\> pi- D+]cc                                                                                                                          |
| DecayDescriptors | [ '[B+ -\> pi- D+]cc' ]                                                                                                                  |
| Output           | Phys/fourpartB2ppipiSigmacmm_Lcpi/Particles                                                                                                  |

TisTosParticleTagger/fourpartB2ppipiSigmacmm_LcpiTOS

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/fourpartB2ppipiSigmacmm_Lcpi' ]      |
| DecayDescriptor | None                                           |
| Output          | Phys/fourpartB2ppipiSigmacmm_LcpiTOS/Particles |
| TisTosSpecs     | { 'Hlt2.\*Decision%TOS' : 0 }                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

CombineParticles/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart

|                  |                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)' , 'Phys/fourpartB2ppipiSigmacmm_LcpiTOS' ]                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'B+' : 'ALL' , 'B-' : 'ALL' , 'Lambda_c+' : "(ADMASS('Lambda_c~-')\<100.0) & (BPVVDCHI2\>36.0) & (VFASPF(VCHI2/VDOF)\<5.0)" , 'Lambda_c~-' : "(ADMASS('Lambda_c~-')\<100.0) & (BPVVDCHI2\>36.0) & (VFASPF(VCHI2/VDOF)\<5.0)" } |
| CombinationCut   | (AMAXDOCA('')\<0.2)                                                                                                                                                                                                                           |
| MotherCut        | (ADMASS('B+')\<200.0) & (BPVVDCHI2\>64.0) & (BPVDIRA\>0.998) & (VFASPF(VCHI2/VDOF)\<5.0)                                                                                                                                                      |
| DecayDescriptor  | [B0 -\> Lambda_c~- B+]cc                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[B0 -\> Lambda_c~- B+]cc' ]                                                                                                                                                                                                            |
| Output           | Phys/B2ppipiSigmacmm_Lcpi_Closed_Line_FourPart/Particles                                                                                                                                                                                      |
