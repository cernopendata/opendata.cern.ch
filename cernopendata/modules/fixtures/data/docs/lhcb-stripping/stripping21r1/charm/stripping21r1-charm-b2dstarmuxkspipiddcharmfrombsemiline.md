[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2DstarMuXKsPiPiDDCharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DstarMuXKsPiPiDDCharmFromBSemiLine/Particles                                            |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2DstarMuXKsPiPiDDCharmFromBSemiLineVOIDFilter

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

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/SelPilooseforCharmFromBSemi

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ]                             |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/SelPilooseforCharmFromBSemi/Particles                                                                |

CombineParticles/SelD02KsPiPiDDforCharmFromBSemi

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKsDDforCharmFromBSemi' , 'Phys/SelPilooseforCharmFromBSemi' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                              |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (APT \> 2000 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 1400.0 \*MeV)& (ADOCACHI2CUT( 20, ''))                                                     |
| MotherCut        | (ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (SUMTREE( PT, ISBASIC )\> 1400.0\*MeV) & (PT \> 2000 \*MeV)& (MINTREE(((ABSID=='KS0')) , VFASPF(VZ))-VFASPF(VZ) \> 10.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[D0 -\> KS0 pi+ pi-]cc' ]                                                                                                                                                            |
| Output           | Phys/SelD02KsPiPiDDforCharmFromBSemi/Particles                                                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/SelDstarPiPiDDForCharmFromBSemi

|                  |                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02KsPiPiDDforCharmFromBSemi' , 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '( PT \> 80.0 \*MeV )' , 'pi-' : '( PT \> 80.0 \*MeV )' }            |
| CombinationCut   | (AM - ACHILD(M,1) + 5 \> 0.0 \*MeV) & (AM - ACHILD(M,1) - 5 \< 170.0 \*MeV)                                                |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 8.0 ) & (M - CHILD(M,1) \> 0.0 \*MeV) & (M - CHILD(M,1) \< 170.0 \*MeV))                           |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                        |
| Output           | Phys/SelDstarPiPiDDForCharmFromBSemi/Particles                                                                             |

CombineParticles/Selb2DstarMuXKsPiPiDDCharmFromBSemi

|                  |                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarPiPiDDForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                       |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                    |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> -9999 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                               |
| DecayDescriptors | [ '[B~0 -\> D\*(2010)+ mu-]cc' , '[B~0 -\> D\*(2010)+ mu+]cc' ]                                                                                                                              |
| Output           | Phys/Selb2DstarMuXKsPiPiDDCharmFromBSemi/Particles                                                                                                                                                 |

TisTosParticleTagger/b2DstarMuXKsPiPiDDCharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DstarMuXKsPiPiDDCharmFromBSemi' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2DstarMuXKsPiPiDDCharmFromBSemiLine/Particles                                                                                                |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
