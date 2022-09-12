[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KpiX2KKDarkBosonLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2KpiX2KKDarkBosonLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 0.25000000                            |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingB2KpiX2KKDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsKaons /Particles',True) |

**FilterDesktop/KXDarkBosonFilter**

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>3000\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r0p2-stdallnopidskaons) ' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/KXDarkBosonFilter/Particles                                                                                                                                                       |

**CombineParticles/X2KKDarkBosonSel**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KXDarkBosonFilter' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                          |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 250\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,'')) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10)                           |
| DecayDescriptor  | None                                                                                  |
| DecayDescriptors | [ 'KS0 -\> K+ K-' ]                                                                 |
| Output           | Phys/X2KKDarkBosonSel/Particles                                                       |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r0p2-stdallnopidskaons) ' ]                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                  |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                                                                                                      |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**FilterDesktop/PiBDarkBosonFilter**

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r0p2-stdallnopidspions) ' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                                                                                                      |

**DaVinci::N3BodyDecays/B2KpiX2KKDarkBosonLine**

|                  |                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' , 'Phys/X2KKDarkBosonSel' ]                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                          |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                        |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> K+ pi- KS0]cc' ]                                                                                                                                                                                       |
| Output           | Phys/B2KpiX2KKDarkBosonLine/Particles                                                                                                                                                                                 |

**AddRelatedInfo/RelatedInfo1_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2KpiX2KKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2KpiX2KKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2KpiX2KKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2KpiX2KKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_B2KpiX2KKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2KpiX2KKDarkBosonLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2KKDarkBosonLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_B2KpiX2KKDarkBosonLine/Particles |
