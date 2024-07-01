[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingb2DstarMuXKsKKLLCharmFromBSemiLine

## Properties:

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DstarMuXKsKKLLCharmFromBSemiLine/Particles                                 |
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

LoKi::VoidFilter/Strippingb2DstarMuXKsKKLLCharmFromBSemiLineVOIDFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/SelKsLLforCharmFromBSemi

|                 |                                                                                                                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 2000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & CHILDCUT((TRGHOSTPROB\< 0.5),1) & CHILDCUT((TRGHOSTPROB\< 0.5),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ]                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                    |
| Output          | Phys/SelKsLLforCharmFromBSemi/Particles                                                                                                                                                                                                                                 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/SelKlooseforCharmFromBSemi

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\> -5) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                           |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/SelKlooseforCharmFromBSemi/Particles                                                                               |

CombineParticles/SelD02KsKKLLforCharmFromBSemi

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKlooseforCharmFromBSemi' , 'Phys/SelKsLLforCharmFromBSemi' ]                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (APT \> 2000 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 1400.0 \*MeV)& (ADOCACHI2CUT( 20, ''))                                                     |
| MotherCut        | (ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (SUMTREE( PT, ISBASIC )\> 1400.0\*MeV) & (PT \> 2000 \*MeV)& (MINTREE(((ABSID=='KS0')) , VFASPF(VZ))-VFASPF(VZ) \> 10.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[D0 -\> KS0 K+ K-]cc' ]                                                                                                                                                              |
| Output           | Phys/SelD02KsKKLLforCharmFromBSemi/Particles                                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

CombineParticles/SelDstarKKLLForCharmFromBSemi

|                  |                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02KsKKLLforCharmFromBSemi' , 'Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '( PT \> 80.0 \*MeV )' , 'pi-' : '( PT \> 80.0 \*MeV )' }            |
| CombinationCut   | (AM - ACHILD(M,1) + 5 \> 0.0 \*MeV) & (AM - ACHILD(M,1) - 5 \< 170.0 \*MeV)                                                |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 8.0 ) & (M - CHILD(M,1) \> 0.0 \*MeV) & (M - CHILD(M,1) \< 170.0 \*MeV))                           |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                        |
| Output           | Phys/SelDstarKKLLForCharmFromBSemi/Particles                                                                               |

CombineParticles/Selb2DstarMuXKsKKLLCharmFromBSemi

|                  |                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarKKLLForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                       |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                    |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> -9999 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                               |
| DecayDescriptors | [ '[B~0 -\> D\*(2010)+ mu-]cc' , '[B~0 -\> D\*(2010)+ mu+]cc' ]                                                                                                                              |
| Output           | Phys/Selb2DstarMuXKsKKLLCharmFromBSemi/Particles                                                                                                                                                   |

TisTosParticleTagger/b2DstarMuXKsKKLLCharmFromBSemiLine

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DstarMuXKsKKLLCharmFromBSemi' ]                                                                                        |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/b2DstarMuXKsKKLLCharmFromBSemiLine/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |
