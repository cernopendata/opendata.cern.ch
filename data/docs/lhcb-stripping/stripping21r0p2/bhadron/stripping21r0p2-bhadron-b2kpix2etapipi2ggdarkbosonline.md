[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KpiX2EtaPiPi2GGDarkBosonLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KpiX2EtaPiPi2GGDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedEta

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedEta/Particles',True) |

FilterDesktop/etaXDarkBosonFilter

|                 |                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (P\>1000\*MeV) & (MM\>450\*MeV) & (MM\<650\*MeV) & (CL\>0.2) & (MM\>450\*MeV) & (MM\<650\*MeV) & (PT\>400\*MeV) |
| Inputs          | [ 'Phys/[StdLooseResolvedEta](./stripping21r0p2-commonparticles-stdlooseresolvedeta)' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                       |
| Output          | Phys/etaXDarkBosonFilter/Particles                                                                                                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiXDarkBosonFilter

|                 |                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>3000\*MeV) & (MIPCHI2DV(PRIMARY)\>36) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                    |
| Output          | Phys/PiXDarkBosonFilter/Particles                                                                                                                                                       |

CombineParticles/X2EtaPiPi2GGDarkBosonSel

|                  |                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiXDarkBosonFilter' , 'Phys/etaXDarkBosonFilter' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'eta' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                     |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 500\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,''))                                              |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10)& (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 16),1)==0) |
| DecayDescriptor  | None                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> eta pi+ pi-' ]                                                                                                        |
| Output           | Phys/X2EtaPiPi2GGDarkBosonSel/Particles                                                                                            |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KBDarkBosonFilter

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                  |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                                                                                                      |

FilterDesktop/PiBDarkBosonFilter

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                                                                                                      |

DaVinci::N3BodyDecays/B2KpiX2EtaPiPi2GGDarkBosonLine

|                  |                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' , 'Phys/X2EtaPiPi2GGDarkBosonSel' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                          |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                        |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> K+ pi- KS0]cc' ]                                                                                                                                                                                       |
| Output           | Phys/B2KpiX2EtaPiPi2GGDarkBosonLine/Particles                                                                                                                                                                         |

AddRelatedInfo/RelatedInfo1_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo4_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo5_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo5_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo6_B2KpiX2EtaPiPi2GGDarkBosonLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EtaPiPi2GGDarkBosonLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo6_B2KpiX2EtaPiPi2GGDarkBosonLine/Particles |
