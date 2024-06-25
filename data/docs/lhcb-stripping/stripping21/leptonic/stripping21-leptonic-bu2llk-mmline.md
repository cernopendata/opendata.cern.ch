[[stripping21 lines]](./stripping21-index)

# StrippingBu2LLK_mmLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2LLK_mmLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2LLK_mmLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/SelDiMuonsForBu2LLK

|                 |                                                                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT)\>300 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY))\>9) & (VFASPF(VCHI2/VDOF)\<9) & (BPVVDCHI2\> 16) & (MIPCHI2DV(PRIMARY) \> 0 ) & (2 == NINTREE((ABSID==13)&(HASMUON)&(ISMUON))) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)' ]                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                              |
| Output          | Phys/SelDiMuonsForBu2LLK/Particles                                                                                                                                                                                                                |

GaudiSequencer/SeqMergeBu2LLK_mm

GaudiSequencer/SEQ:KaonsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForBu2LLK

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]                                                                       |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/KaonsForBu2LLK/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KstarsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKstar2Kpi](./stripping21-commonparticles-stdloosekstar2kpi)/Particles')\>0 |

FilterDesktop/KstarsForBu2LLK

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21-commonparticles-stdloosekstar2kpi)' ]                                                               |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/KstarsForBu2LLK/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PhisForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)/Particles')\>0 |

FilterDesktop/PhisForBu2LLK

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)' ]                                                                     |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_mm

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ALL                                                                         |
| Inputs          | [ 'Phys/KaonsForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/PhisForBu2LLK' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/MergeBu2LLK_mm/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_mmLine

|                  |                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_mm' , 'Phys/SelDiMuonsForBu2LLK' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1000\*MeV                                                                                                            |
| MotherCut        | ((VFASPF(VCHI2/VDOF)\< 9 ) & (BPVIPCHI2()\< 25 ) & (BPVDIRA\> 0.9995 ) & (BPVVDCHI2\> 100 ))                                          |
| DecayDescriptor  | None                                                                                                                                  |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B_s0 -\> J/psi(1S) phi(1020)]cc' ]                    |
| Output           | Phys/Bu2LLK_mmLine/Particles                                                                                                          |

AddRelatedInfo/RelatedInfo1_Bu2LLK_mmLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_Bu2LLK_mmLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_mmLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_Bu2LLK_mmLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_mmLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_Bu2LLK_mmLine/Particles |
