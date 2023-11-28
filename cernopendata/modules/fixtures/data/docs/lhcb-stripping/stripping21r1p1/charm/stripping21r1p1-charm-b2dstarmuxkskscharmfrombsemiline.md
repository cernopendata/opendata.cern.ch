[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingb2DstarMuXKsKsCharmFromBSemiLine

## Properties:

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DstarMuXKsKsCharmFromBSemiLine/Particles                                   |
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

LoKi::VoidFilter/Strippingb2DstarMuXKsKsCharmFromBSemiLineVOIDFilter

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

GaudiSequencer/SeqSelMergedAllKsLooseForCharmFromBSemi

GaudiSequencer/SEQ:SelKsLU_PosLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)/Particles',True)\>0 |

CombineParticles/SelKsLU_PosLongForCharmFromBSemi

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISLONG)' , 'pi-' : '(ISUP)' }                                                                                                                |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                                 |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                        |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                       |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                               |
| Output           | Phys/SelKsLU_PosLongForCharmFromBSemi/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLU_NegLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)/Particles',True)\>0 |

CombineParticles/SelKsLU_NegLongForCharmFromBSemi

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISUP)' , 'pi-' : '(ISLONG)' }                                                                                                                |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                                 |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                        |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                       |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                               |
| Output           | Phys/SelKsLU_NegLongForCharmFromBSemi/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLLForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/SelKsLLForCharmFromBSemi

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                        |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                 |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)        |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                       |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                               |
| Output           | Phys/SelKsLLForCharmFromBSemi/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsDDforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/SelKsDDforCharmFromBSemi

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 3000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' ]                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/SelKsDDforCharmFromBSemi/Particles                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/SelMergedAllKsLooseForCharmFromBSemi

|                 |                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                         |
| Inputs          | [ 'Phys/SelKsDDforCharmFromBSemi' , 'Phys/SelKsLLForCharmFromBSemi' , 'Phys/SelKsLU_NegLongForCharmFromBSemi' , 'Phys/SelKsLU_PosLongForCharmFromBSemi' ] |
| DecayDescriptor | None                                                                                                                                                        |
| Output          | Phys/SelMergedAllKsLooseForCharmFromBSemi/Particles                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelD02KsKsforCharmFromBSemi

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelMergedAllKsLooseForCharmFromBSemi' ]                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                                                                               |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2) \> 1400.0 \*MeV)& (ADOCACUT( 2.\*mm, ''))                                         |
| MotherCut        | (ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (SUMTREE( PT, ISBASIC )\> 1400.0\*MeV)& (BPVVDCHI2 \> 100.0) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> KS0 KS0' ]                                                                                                                       |
| Output           | Phys/SelD02KsKsforCharmFromBSemi/Particles                                                                                                   |

ConjugateNeutralPID/SelConjugateD0ForDstar_KsKs_ForCharmFromBSemi

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/SelD02KsKsforCharmFromBSemi' ]                     |
| DecayDescriptor | None                                                         |
| Output          | Phys/SelConjugateD0ForDstar_KsKs_ForCharmFromBSemi/Particles |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

CombineParticles/SelDstar_KsKs_ForCharmFromBSemi

|                  |                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelConjugateD0ForDstar_KsKs_ForCharmFromBSemi' , 'Phys/SelD02KsKsforCharmFromBSemi' , 'Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '( PT \> 80.0 \*MeV )' , 'pi-' : '( PT \> 80.0 \*MeV )' }                                                                 |
| CombinationCut   | (AM - ACHILD(M,1) + 5 \> 0.0 \*MeV) & (AM - ACHILD(M,1) - 5 \< 170.0 \*MeV)                                                                                                     |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 8.0 ) & (M - CHILD(M,1) \> 0.0 \*MeV) & (M - CHILD(M,1) \< 170.0 \*MeV))                                                                                |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                                                                     |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                                                             |
| Output           | Phys/SelDstar_KsKs_ForCharmFromBSemi/Particles                                                                                                                                  |

CombineParticles/Selb2DstarMuXKsKsCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstar_KsKs_ForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B0 -\> D\*(2010)+ mu-]cc' , '[B0 -\> D\*(2010)+ mu+]cc' ]                                                                                                                            |
| Output           | Phys/Selb2DstarMuXKsKsCharmFromBSemi/Particles                                                                                                                                                 |

TisTosParticleTagger/b2DstarMuXKsKsCharmFromBSemiLine

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DstarMuXKsKsCharmFromBSemi' ]                                                                                          |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/b2DstarMuXKsKsCharmFromBSemiLine/Particles                                                                                       |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |
