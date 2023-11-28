[[stripping21 lines]](./stripping21-index)

# Strippingb2D0MuXKsKsCharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2D0MuXKsKsCharmFromBSemiLine/Particles                                                   |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2D0MuXKsKsCharmFromBSemiLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/SelMuforCharmFromBSemi

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 3.0\*GeV)& (TRGHOSTPROB\< 0.5)& (TRCHI2DOF\< 4.0) & (MIPCHI2DV(PRIMARY)\> 4.0)& (PIDmu \> -0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                  |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/SelMuforCharmFromBSemi/Particles                                                                                      |

GaudiSequencer/SeqSelMergedAllKsLooseForCharmFromBSemi

GaudiSequencer/SEQ:SelKsLU_PosLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)/Particles')\>0 |

CombineParticles/SelKsLU_PosLongForCharmFromBSemi

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISLONG)' , 'pi-' : '(ISUP)' }                                                                                                        |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                         |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                       |
| Output           | Phys/SelKsLU_PosLongForCharmFromBSemi/Particles                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLU_NegLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)/Particles')\>0 |

CombineParticles/SelKsLU_NegLongForCharmFromBSemi

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISUP)' , 'pi-' : '(ISLONG)' }                                                                                                        |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                         |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                       |
| Output           | Phys/SelKsLU_NegLongForCharmFromBSemi/Particles                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLLForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/SelKsLLForCharmFromBSemi

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                    |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                             |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)    |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                   |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                           |
| Output           | Phys/SelKsLLForCharmFromBSemi/Particles                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsDDforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/SelKsDDforCharmFromBSemi

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 3000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                                                                                            |
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

CombineParticles/Selb2D0MuXKsKsCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02KsKsforCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                  |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B- -\> D0 mu-]cc' , '[B+ -\> D0 mu+]cc' ]                                                                                                                                            |
| Output           | Phys/Selb2D0MuXKsKsCharmFromBSemi/Particles                                                                                                                                                    |

TisTosParticleTagger/b2D0MuXKsKsCharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2D0MuXKsKsCharmFromBSemi' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2D0MuXKsKsCharmFromBSemiLine/Particles                                                                                                       |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
