[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2DpMuXHHHKsCharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DpMuXHHHKsCharmFromBSemiLine/Particles                                                  |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2DpMuXHHHKsCharmFromBSemiLineVOIDFilter

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

GaudiSequencer/SeqSelAllKaonsAndPionsForCharmFromBSemi

GaudiSequencer/SEQ:SelKforCharmFromBSemi

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

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelPiforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/SelPiforCharmFromBSemi

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\< 10.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                               |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/SelPiforCharmFromBSemi/Particles                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/SelAllKaonsAndPionsForCharmFromBSemi

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | ALL                                                                |
| Inputs          | [ 'Phys/SelKforCharmFromBSemi' , 'Phys/SelPiforCharmFromBSemi' ] |
| DecayDescriptor | None                                                               |
| Output          | Phys/SelAllKaonsAndPionsForCharmFromBSemi/Particles                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelDToHHH_SEED

|                  |                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelAllKaonsAndPionsForCharmFromBSemi' ]                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                     |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 2000\*MeV)& (AM \< 2000\*MeV)& (AM - ACHILD(M,1)-ACHILD(M,2)-ACHILD(M,3) \> 50\*MeV)& (ADOCACHI2CUT(25, ''))& (ACHILD(MIPDV(PRIMARY),1)+ACHILD(MIPDV(PRIMARY),2)+ACHILD(MIPDV(PRIMARY),3) \> 1.0\*mm) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 4.0) & (BPVVD \> 5\*mm)                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[K\*(892)+ -\> pi+ pi- pi+]cc' , '[K\*(892)+ -\> K+ K- pi+]cc' , '[K\*(892)+ -\> K- pi+ pi+]cc' , '[K\*(892)+ -\> K+ pi+ pi-]cc' , '[K\*(892)+ -\> K+ K+ pi-]cc' , '[K\*(892)+ -\> K- K+ K+]cc' ]                               |
| Output           | Phys/SelDToHHH_SEED/Particles                                                                                                                                                                                                                    |

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

CombineParticles/SelCharmDToHHHKsForCharmFromBSemi

|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDToHHH_SEED' , 'Phys/SelMergedAllKsLooseForCharmFromBSemi' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'KS0' : 'ALL' }                                                                               |
| CombinationCut   | (DAMASS('D_s+') \< 90 \*MeV) & (DAMASS('D+')\> -90 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2)\> 3000\*MeV)& (ACHILD(VFASPF(VZ),2)-ACHILD(VFASPF(VZ),1) \> 5\*mm) |
| MotherCut        | (DTF_FUN(M,False,'KS0') \> 1869-80\*MeV)& (DTF_FUN(M,False,'KS0') \< 1968+80\*MeV)                                                                       |
| DecayDescriptor  | None                                                                                                                                                     |
| DecayDescriptors | [ '[D+ -\> K\*(892)+ KS0]cc' ]                                                                                                                       |
| Output           | Phys/SelCharmDToHHHKsForCharmFromBSemi/Particles                                                                                                         |

CombineParticles/Selb2D0MuX_HHHKsCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelCharmDToHHHKsForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B~0 -\> D+ mu-]cc' ]                                                                                                                                                                   |
| Output           | Phys/Selb2D0MuX_HHHKsCharmFromBSemi/Particles                                                                                                                                                  |

TisTosParticleTagger/b2DpMuXHHHKsCharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2D0MuX_HHHKsCharmFromBSemi' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2DpMuXHHHKsCharmFromBSemiLine/Particles                                                                                                      |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
