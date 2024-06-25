[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2hhh_HHHIncLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/D2hhh_HHHIncLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 0.15000000                      |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

LoKi::VoidFilter/StrippingD2hhh_HHHIncLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/D2hhh_HHHIncLine

|                  |                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(((MIPCHI2DV(PRIMARY)) \> 4.0 ) & (P \> 2000.0 \*MeV) & (PT \> 250.0 \*MeV) )' , 'pi-' : '(((MIPCHI2DV(PRIMARY)) \> 4.0 ) & (P \> 2000.0 \*MeV) & (PT \> 250.0 \*MeV) )' } |
| CombinationCut   | ((ADOCACHI2CUT(50.0,'')) & (ADOCACUT(0.5\*mm,'')) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 2800.0\*MeV) & (ANUM(MIPCHI2DV(PRIMARY) \> 10.0 ) \>= 2) )                                          |
| MotherCut        | ( (PT \> 1000.0) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.98) & (BPVIPCHI2() \< 12.0) & (VFASPF(VMINVDCHI2DV(PRIMARY)) \> 125.0) & (in_range ( 600.0 , M , 2070.0 )) )                       |
| DecayDescriptor  | [D+ -\> pi- pi+ pi+]cc                                                                                                                                                                           |
| DecayDescriptors | [ '[D+ -\> pi- pi+ pi+]cc' ]                                                                                                                                                                   |
| Output           | Phys/D2hhh_HHHIncLine/Particles                                                                                                                                                                    |

AddRelatedInfo/RelatedInfo1_D2hhh_HHHIncLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_HHHIncLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_D2hhh_HHHIncLine/Particles |

AddRelatedInfo/RelatedInfo2_D2hhh_HHHIncLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_HHHIncLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_D2hhh_HHHIncLine/Particles |

AddRelatedInfo/RelatedInfo3_D2hhh_HHHIncLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_HHHIncLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_D2hhh_HHHIncLine/Particles |

AddRelatedInfo/RelatedInfo4_D2hhh_HHHIncLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_HHHIncLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_D2hhh_HHHIncLine/Particles |
