[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2DpMuXKsKCharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DpMuXKsKCharmFromBSemiLine/Particles                                                    |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2DpMuXKsKCharmFromBSemiLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/SelMuforCharmFromBSemi

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 3.0\*GeV)& (TRGHOSTPROB\< 0.5)& (TRCHI2DOF\< 4.0) & (MIPCHI2DV(PRIMARY)\> 4.0)& (PIDmu \> -0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/SelMuforCharmFromBSemi/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/SelKforCharmFromBSemi

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                              |
| DecayDescriptor | None                                                                                                                     |
| Output          | Phys/SelKforCharmFromBSemi/Particles                                                                                     |

GaudiSequencer/SeqSelMergedAllKsLooseForCharmFromBSemi

GaudiSequencer/SEQ:SelKsLU_PosLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)/Particles')\>0 |

CombineParticles/SelKsLU_PosLongForCharmFromBSemi

|                  |                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISLONG)' , 'pi-' : '(ISUP)' }                                                                                                            |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                             |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                    |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                   |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                           |
| Output           | Phys/SelKsLU_PosLongForCharmFromBSemi/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLU_NegLongForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)/Particles')\>0 |

CombineParticles/SelKsLU_NegLongForCharmFromBSemi

|                  |                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(ISUP)' , 'pi-' : '(ISLONG)' }                                                                                                            |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                                                                                                             |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)                                                                                    |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                   |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                           |
| Output           | Phys/SelKsLU_NegLongForCharmFromBSemi/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsLLForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/SelKsLLForCharmFromBSemi

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                      |
| CombinationCut   | (ADAMASS('KS0') \< 27.\*MeV) & (ADOCACHI2CUT(25, ''))                               |
| MotherCut        | (ADMASS('KS0') \< 25.\*MeV) & ( BPVLTIME() \> 3.0\*ps) & (VFASPF(VCHI2) \< 9.)      |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                     |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                             |
| Output           | Phys/SelKsLLForCharmFromBSemi/Particles                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelKsDDforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/SelKsDDforCharmFromBSemi

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 3000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                                                                                                          |
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

CombineParticles/SelDs2KsKforCharmFromBSemi

|                  |                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKforCharmFromBSemi' , 'Phys/SelMergedAllKsLooseForCharmFromBSemi' ]                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                  |
| CombinationCut   | (DAMASS('D_s+') \< 100.0 \*MeV) & (DAMASS('D+')\> -100.0 \*MeV)& (ADOCACHI2CUT( 20, ''))                                                                                                                                                      |
| MotherCut        | (DMASS('D_s+') \< 80.0 \*MeV) & (DMASS('D+') \> -80.0 \*MeV) & (MINTREE(((ABSID=='KS0')) , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) & (CHILD(BPVLTIME(),1) \> 3.0\*ps) & (BPVLTIME() \> 0.1\*ps) & (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D+ -\> KS0 K+]cc' ]                                                                                                                                                                                                                   |
| Output           | Phys/SelDs2KsKforCharmFromBSemi/Particles                                                                                                                                                                                                     |

CombineParticles/Selb2DsMuXKsKCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDs2KsKforCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B~0 -\> D+ mu-]cc' , '[B~0 -\> D+ mu+]cc' ]                                                                                                                                          |
| Output           | Phys/Selb2DsMuXKsKCharmFromBSemi/Particles                                                                                                                                                     |

TisTosParticleTagger/b2DpMuXKsKCharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DsMuXKsKCharmFromBSemi' ]                                                                                                           |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2DpMuXKsKCharmFromBSemiLine/Particles                                                                                                        |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
