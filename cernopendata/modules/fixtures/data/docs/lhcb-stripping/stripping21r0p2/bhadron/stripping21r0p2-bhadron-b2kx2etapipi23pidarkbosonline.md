[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KX2EtaPiPi23PIDarkBosonLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/B2KX2EtaPiPi23PIDarkBosonLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KX2EtaPiPi23PIDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/pizRXDarkBosonFilter

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (CL\>0.1) & (PT\>400\*MeV) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ]             |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/pizRXDarkBosonFilter/Particles                                                                   |

CombineParticles/Eta2PiPiPiForXDarkBosonSel

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiXDarkBosonFilter' , 'Phys/pizRXDarkBosonFilter' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                     |
| CombinationCut   | (AM \< 750\*MeV) & (ACHI2DOCA(1,2) \< 25)                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\> 16) & HASVERTEX & (M \< 650\*MeV) |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ 'eta -\> pi+ pi- pi0' ]                                                        |
| Output           | Phys/Eta2PiPiPiForXDarkBosonSel/Particles                                          |

CombineParticles/X2EtaPiPi23PIDarkBosonSel

|                  |                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Eta2PiPiPiForXDarkBosonSel' , 'Phys/PiXDarkBosonFilter' ]                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'eta' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                     |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 500\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,''))                                              |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10)& (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 16),1)==0) |
| DecayDescriptor  | None                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> eta pi+ pi-' ]                                                                                                        |
| Output           | Phys/X2EtaPiPi23PIDarkBosonSel/Particles                                                                                           |

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

CombineParticles/B2KX2EtaPiPi23PIDarkBosonLine

|                  |                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/X2EtaPiPi23PIDarkBosonSel' ]                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                           |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                         |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B+ -\> K+ KS0]cc' ]                                                                                                                                                                                            |
| Output           | Phys/B2KX2EtaPiPi23PIDarkBosonLine/Particles                                                                                                                                                                           |

AddRelatedInfo/RelatedInfo1_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_B2KX2EtaPiPi23PIDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_B2KX2EtaPiPi23PIDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_B2KX2EtaPiPi23PIDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo4_B2KX2EtaPiPi23PIDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo5_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo5_B2KX2EtaPiPi23PIDarkBosonLine/Particles |

AddRelatedInfo/RelatedInfo6_B2KX2EtaPiPi23PIDarkBosonLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KX2EtaPiPi23PIDarkBosonLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo6_B2KX2EtaPiPi23PIDarkBosonLine/Particles |
