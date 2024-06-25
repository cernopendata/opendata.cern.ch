[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2JKstDarkBosonLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2JKstDarkBosonLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingB2JKstDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**FilterDesktop/MuJDarkBosonFilter**

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (PIDmu\>-4) & (TRCHI2DOF\<4) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>125\*MeV) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/MuJDarkBosonFilter/Particles                                                                                                                                                |

**CombineParticles/J2MuMuDarkBosonSel**

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuJDarkBosonFilter' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                     |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 100\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,'')) |
| MotherCut        | (BPVDIRA \> 0) & (VFASPF(VCHI2/VDOF)\<12)                                          |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                      |
| Output           | Phys/J2MuMuDarkBosonSel/Particles                                                  |

**LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedKst2Kpi**

|      |                                             |
|------|---------------------------------------------|
| Code | 0 StdLooseDetachedKst2Kpi /Particles',True) |

**FilterDesktop/KstDarkBosonFilter**

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 25)                                                          |
| Inputs          | [ 'Phys/ [StdLooseDetachedKst2Kpi](./stripping21r1p2-stdloosedetachedkst2kpi) ' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KstDarkBosonFilter/Particles                                                   |

**CombineParticles/B2JKstDarkBosonLine**

|                  |                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/J2MuMuDarkBosonSel' , 'Phys/KstDarkBosonFilter' ]                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }                                                                                                                                     |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                         |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                                                                                                                                                               |
| Output           | Phys/B2JKstDarkBosonLine/Particles                                                                                                                                                                                     |

**AddRelatedInfo/RelatedInfo1_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_B2JKstDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_B2JKstDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_B2JKstDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_B2JKstDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_B2JKstDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2JKstDarkBosonLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2JKstDarkBosonLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo6_B2JKstDarkBosonLine/Particles |
