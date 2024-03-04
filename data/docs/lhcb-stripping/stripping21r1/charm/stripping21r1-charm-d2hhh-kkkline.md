[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2hhh_KKKLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/D2hhh_KKKLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingD2hhh_KKKLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KKK_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KKK](./stripping21r1-commonparticles-stdloosedplus2kkk)/Particles')\>0 |

FilterDesktop/D2hhh_KKKLine

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( (MINTREE('pi+'==ABSID, PT) \> 250.0 ) & (MINTREE('pi+'==ABSID, P ) \> 2000.0) & (MINTREE('pi+'==ABSID, MIPCHI2DV(PRIMARY)) \> 2.0 ) & (MINTREE('K-'==ABSID, PIDK-PIDpi) \> 7.0 ) & (MINTREE('K-'==ABSID, PT) \> 250.0 ) & (MINTREE('K-'==ABSID, P ) \> 2000.0) & (MINTREE('K-'==ABSID, MIPCHI2DV(PRIMARY)) \> 2.0 ) & (DOCACHI2MAX \< 50.0) & ((SUMTREE( ISBASIC , PT ) \> 2800.0\*MeV) & (2 \<= NINGENERATION((MIPCHI2DV(PRIMARY) \> 4.0 ) , 1))) & (PT \> 1000.0) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.98) & (BPVIPCHI2() \< 12.0) & (VFASPF(VMINVDCHI2DV(PRIMARY)) \> 125.0) & (in_range ( 1800.0 , M , 2040.0 )) ) |
| Inputs          | [ 'Phys/[StdLooseDplus2KKK](./stripping21r1-commonparticles-stdloosedplus2kkk)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output          | Phys/D2hhh_KKKLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

AddRelatedInfo/RelatedInfo1_D2hhh_KKKLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_KKKLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_D2hhh_KKKLine/Particles |

AddRelatedInfo/RelatedInfo2_D2hhh_KKKLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_KKKLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_D2hhh_KKKLine/Particles |

AddRelatedInfo/RelatedInfo3_D2hhh_KKKLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_KKKLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_D2hhh_KKKLine/Particles |

AddRelatedInfo/RelatedInfo4_D2hhh_KKKLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/D2hhh_KKKLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo4_D2hhh_KKKLine/Particles |
