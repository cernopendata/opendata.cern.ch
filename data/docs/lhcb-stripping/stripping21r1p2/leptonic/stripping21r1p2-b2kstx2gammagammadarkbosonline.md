[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2KstX2GammaGammaDarkBosonLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KstX2GammaGammaDarkBosonLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | HLT_PASS_RE('Hlt2Topo2Body.\*Decision')       |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingB2KstX2GammaGammaDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**FilterDesktop/gXDarkBosonFilter**

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (P\>1000\*MeV) & (CL\>0.3) & (PT\>400\*MeV) |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21r1p2-stdlooseallphotons) ' ]                                              |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/gXDarkBosonFilter/Particles                                                                                       |

**CombineParticles/X2GammaGammaDarkBosonSel**

|                  |                                         |
|------------------|-----------------------------------------|
| Inputs           | [ 'Phys/gXDarkBosonFilter' ]          |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' }        |
| CombinationCut   | ATRUE                                   |
| MotherCut        | (M \< 5000\*MeV) & (PT \> 500\*MeV)     |
| DecayDescriptor  | None                                    |
| DecayDescriptors | [ 'pi0 -\> gamma gamma' ]             |
| Output           | Phys/X2GammaGammaDarkBosonSel/Particles |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsKaons /Particles',True) |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1p2-stdallnopidskaons) ' ]                                                                                                               |
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
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1p2-stdallnopidspions) ' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                                                                                                      |

**CombineParticles/Kst2KPiDarkBosonSel**

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ADOCACHI2CUT(30,'') & (ADAMASS('K\*(892)0') \< 100\*MeV)                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\> 16) & HASVERTEX             |
| DecayDescriptor  | None                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                           |
| Output           | Phys/Kst2KPiDarkBosonSel/Particles                                           |

**CombineParticles/B2KstX2GammaGammaDarkBosonLine**

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst2KPiDarkBosonSel' , 'Phys/X2GammaGammaDarkBosonSel' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'pi0' : 'ALL' }                                        |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                      |
| MotherCut        | (PT\>800\*MeV) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 pi0]cc' ]                                                                                  |
| Output           | Phys/B2KstX2GammaGammaDarkBosonLine/Particles                                                                       |

**AddRelatedInfo/RelatedInfo1_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_B2KstX2GammaGammaDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_B2KstX2GammaGammaDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_B2KstX2GammaGammaDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo4_B2KstX2GammaGammaDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo5_B2KstX2GammaGammaDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2KstX2GammaGammaDarkBosonLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2GammaGammaDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo6_B2KstX2GammaGammaDarkBosonLine/Particles |
