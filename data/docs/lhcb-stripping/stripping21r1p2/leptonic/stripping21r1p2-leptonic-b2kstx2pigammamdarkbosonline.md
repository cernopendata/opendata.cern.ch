[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2KstX2PiGammaMDarkBosonLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/B2KstX2PiGammaMDarkBosonLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | HLT_PASS_RE('Hlt2Topo2Body.\*Decision')     |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingB2KstX2PiGammaMDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/gXDarkBosonFilter

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (P\>1000\*MeV) & (CL\>0.3) & (PT\>400\*MeV) |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r1p2-commonparticles-stdlooseallphotons)' ]                                |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/gXDarkBosonFilter/Particles                                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/pizMXDarkBosonFilter

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (P\>1000\*MeV) & (CL\>0.1) & (PT\>400\*MeV) |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ]                                  |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/pizMXDarkBosonFilter/Particles                                                                                    |

CombineParticles/X2PiGammaMDarkBosonSel

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| Inputs           | [ 'Phys/gXDarkBosonFilter' , 'Phys/pizMXDarkBosonFilter' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'pi0' : 'ALL' }             |
| CombinationCut   | ATRUE                                                        |
| MotherCut        | (M \< 5000\*MeV) & (PT \> 500\*MeV)                          |
| DecayDescriptor  | None                                                         |
| DecayDescriptors | [ 'eta -\> pi0 gamma' ]                                    |
| Output           | Phys/X2PiGammaMDarkBosonSel/Particles                        |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KBDarkBosonFilter

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                  |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiBDarkBosonFilter

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                                                                                                      |

CombineParticles/Kst2KPiDarkBosonSel

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ADOCACHI2CUT(30,'') & (ADAMASS('K\*(892)0') \< 100\*MeV)                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\> 16) & HASVERTEX             |
| DecayDescriptor  | None                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                           |
| Output           | Phys/Kst2KPiDarkBosonSel/Particles                                           |

CombineParticles/B2KstX2PiGammaMDarkBosonLine

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst2KPiDarkBosonSel' , 'Phys/X2PiGammaMDarkBosonSel' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'eta' : 'ALL' }                                         |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                      |
| MotherCut        | (PT\>800\*MeV) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 eta]cc' ]                                                                                  |
| Output           | Phys/B2KstX2PiGammaMDarkBosonLine/Particles                                                                         |

AddRelatedInfo/RelatedInfo1_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_B2KstX2PiGammaMDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_B2KstX2PiGammaMDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_B2KstX2PiGammaMDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo4_B2KstX2PiGammaMDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo5_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo5_B2KstX2PiGammaMDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo6_B2KstX2PiGammaMDarkBosonLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstX2PiGammaMDarkBosonLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo6_B2KstX2PiGammaMDarkBosonLine/Particles |
