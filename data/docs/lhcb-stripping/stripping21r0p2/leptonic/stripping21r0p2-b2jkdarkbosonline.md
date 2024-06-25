[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2JKDarkBosonLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/B2JKDarkBosonLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingB2JKDarkBosonLineVOIDFilter**

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
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ]                                                                                                            |
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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsKaons /Particles',True) |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r0p2-stdallnopidskaons) ' ]                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                  |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                                                                                                      |

**CombineParticles/B2JKDarkBosonLine**

|                  |                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/J2MuMuDarkBosonSel' , 'Phys/KBDarkBosonFilter' ]                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                     |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                         |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                                                                                                                                      |
| Output           | Phys/B2JKDarkBosonLine/Particles                                                                                                                                                                                       |

**AddRelatedInfo/RelatedInfo1_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_B2JKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_B2JKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_B2JKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_B2JKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_B2JKDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2JKDarkBosonLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2JKDarkBosonLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo6_B2JKDarkBosonLine/Particles |
