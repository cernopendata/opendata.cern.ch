[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingb2D0MuXK3PiCharmFromBSemiLine

## Properties:

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| OutputLocation | Phys/b2D0MuXK3PiCharmFromBSemiLine/Particles                                      |
| Postscale      | 1.0000000                                                                         |
| HLT1           | None                                                                              |
| HLT2           | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo.\*Decision') |
| Prescale       | 1.0000000                                                                         |
| L0DU           | None                                                                              |
| ODIN           | None                                                                              |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

LoKi::VoidFilter/Strippingb2D0MuXK3PiCharmFromBSemiLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/SelMuforCharmFromBSemi

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 3.0\*GeV)& (TRGHOSTPROB\< 0.5)& (TRCHI2DOF\< 4.0) & (MIPCHI2DV(PRIMARY)\> 4.0)& (PIDmu \> -0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                              |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/SelMuforCharmFromBSemi/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/SelPiforCharmFromBSemi

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\< 10.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                             |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/SelPiforCharmFromBSemi/Particles                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/SelKforCharmFromBSemi

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                            |
| DecayDescriptor | None                                                                                                                     |
| Output          | Phys/SelKforCharmFromBSemi/Particles                                                                                     |

DaVinci::N4BodyDecays/Sel_D0_to_K3Pi_forCharmFromBSemi

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKforCharmFromBSemi' , 'Phys/SelPiforCharmFromBSemi' ]                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                 |
| CombinationCut   | (ADAMASS('D0') \< 42.0 \*MeV) &( (APT1+APT2+APT3+APT4) \> 1800.0 )&( ACHI2DOCA(1,4) \< 7 ) &( ACHI2DOCA(2,4) \< 7 ) &( ACHI2DOCA(3,4) \< 7 ) |
| MotherCut        | (ADMASS('D0') \< 40.0 \*MeV) &(VFASPF(VCHI2PDOF) \< 6.0)&(SUMTREE( PT, ISBASIC )\> 1800.0\*MeV)&(BPVVDCHI2 \> 100.0)&(BPVDIRA \> 0.99 )      |
| DecayDescriptor  | None                                                                                                                                         |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                          |
| Output           | Phys/Sel_D0_to_K3Pi_forCharmFromBSemi/Particles                                                                                              |

CombineParticles/Selb2D0MuXK3PiCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelMuforCharmFromBSemi' , 'Phys/Sel_D0_to_K3Pi_forCharmFromBSemi' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                  |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B- -\> D0 mu-]cc' , '[B+ -\> D0 mu+]cc' ]                                                                                                                                            |
| Output           | Phys/Selb2D0MuXK3PiCharmFromBSemi/Particles                                                                                                                                                    |

TisTosParticleTagger/b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2D0MuXK3PiCharmFromBSemi' ]                                                                                             |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/b2D0MuXK3PiCharmFromBSemiLine/Particles                                                                                          |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/b2D0MuXK3PiCharmFromBSemiLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_b2D0MuXK3PiCharmFromBSemiLine/Particles |

AddRelatedInfo/RelatedInfo2_b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/b2D0MuXK3PiCharmFromBSemiLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_b2D0MuXK3PiCharmFromBSemiLine/Particles |

AddRelatedInfo/RelatedInfo3_b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/b2D0MuXK3PiCharmFromBSemiLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_b2D0MuXK3PiCharmFromBSemiLine/Particles |

AddRelatedInfo/RelatedInfo4_b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/b2D0MuXK3PiCharmFromBSemiLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo4_b2D0MuXK3PiCharmFromBSemiLine/Particles |

AddRelatedInfo/RelatedInfo5_b2D0MuXK3PiCharmFromBSemiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/b2D0MuXK3PiCharmFromBSemiLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo5_b2D0MuXK3PiCharmFromBSemiLine/Particles |
