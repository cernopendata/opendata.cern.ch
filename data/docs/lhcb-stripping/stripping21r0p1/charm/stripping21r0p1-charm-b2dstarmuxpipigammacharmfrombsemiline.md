[[stripping21r0p1 lines]](./stripping21r0p1-index)

# Strippingb2DstarMuXPiPiGammaCharmFromBSemiLine

## Properties:

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DstarMuXPiPiGammaCharmFromBSemiLine/Particles                              |
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

LoKi::VoidFilter/Strippingb2DstarMuXPiPiGammaCharmFromBSemiLineVOIDFilter

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
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/SelMuforCharmFromBSemi

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 3.0\*GeV)& (TRGHOSTPROB\< 0.5)& (TRCHI2DOF\< 4.0) & (MIPCHI2DV(PRIMARY)\> 4.0)& (PIDmu \> -0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' ]                                              |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/SelMuforCharmFromBSemi/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/SelPiforCharmFromBSemi

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\< 10.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                             |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/SelPiforCharmFromBSemi/Particles                                                                                     |

CombineParticles/SelX_to_PiPi_forCharmFromBSemi

|                  |                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelPiforCharmFromBSemi' ]                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4.0)&(PT \> 250.0)&(PIDK \> 4.0)' , 'pi+' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4.0)&(PT \> 250.0)&(PIDK \< 10.0)' , 'pi-' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4.0)&(PT \> 250.0)&(PIDK \< 10.0)' } |
| CombinationCut   | (in_range( 0 \* MeV, AM, 1820 \* MeV ) ) &( (APT1+APT2) \> 1800.0 )&( ACHI2DOCA(1,2) \< 10 )                                                                                                                                                                       |
| MotherCut        | ( in_range( 0 \* MeV, M, 1810 \* MeV)) &( VFASPF(VCHI2PDOF) \< 10.0)&( BPVVDCHI2 \> 1000.0 )                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                                                                                      |
| Output           | Phys/SelX_to_PiPi_forCharmFromBSemi/Particles                                                                                                                                                                                                                      |

GaudiSequencer/SeqSelAllGammasForCharmFromBSemi

GaudiSequencer/SEQ:SelGammaForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)/Particles',True)\>0 |

FilterDesktop/SelGammaForCharmFromBSemi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT\> 1500 \* MeV)                                                                      |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelGammaForCharmFromBSemi/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelGammaResLLForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaLL](./stripping21r0p1-commonparticles-stdallloosegammall)/Particles',True)\>0 |

FilterDesktop/SelGammaResLLForCharmFromBSemi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( MM \< 100 \* MeV ) &( HASVERTEX ) &( VFASPF(VCHI2/VDOF)\<9 ) &( PT \> 800 \* MeV)     |
| Inputs          | [ 'Phys/[StdAllLooseGammaLL](./stripping21r0p1-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelGammaResLLForCharmFromBSemi/Particles                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelGammaResDDForCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaDD_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaDD](./stripping21r0p1-commonparticles-stdallloosegammadd)/Particles',True)\>0 |

FilterDesktop/SelGammaResDDForCharmFromBSemi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( MM \< 100 \* MeV ) &( HASVERTEX ) &( VFASPF(VCHI2/VDOF)\<9 ) &( PT \> 800 \* MeV)     |
| Inputs          | [ 'Phys/[StdAllLooseGammaDD](./stripping21r0p1-commonparticles-stdallloosegammadd)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelGammaResDDForCharmFromBSemi/Particles                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/SelAllGammasForCharmFromBSemi

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                    |
| Inputs          | [ 'Phys/SelGammaForCharmFromBSemi' , 'Phys/SelGammaResDDForCharmFromBSemi' , 'Phys/SelGammaResLLForCharmFromBSemi' ] |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/SelAllGammasForCharmFromBSemi/Particles                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelD0_to_PiPiGamma_forCharmFromBSemi

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelAllGammasForCharmFromBSemi' , 'Phys/SelX_to_PiPi_forCharmFromBSemi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'rho(770)0' : 'ALL' }                             |
| CombinationCut   | ( ADAMASS('D0') \< 220 \*MeV) &( ACHILD(PT,1)+ACHILD(PT,2) \> 1800.0 \*MeV)        |
| MotherCut        | (ADMASS('D0') \< 210 \*MeV) &(VFASPF(VCHI2PDOF) \< 6.0)                            |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ 'D0 -\> rho(770)0 gamma' ]                                                     |
| Output           | Phys/SelD0_to_PiPiGamma_forCharmFromBSemi/Particles                                |

ConjugateNeutralPID/SelConjugateD0ForDstar_PiPiGammaForCharmFromBSemi

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelD0_to_PiPiGamma_forCharmFromBSemi' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/SelConjugateD0ForDstar_PiPiGammaForCharmFromBSemi/Particles |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r0p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

CombineParticles/SelDstar_PiPiGammaForCharmFromBSemi

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelConjugateD0ForDstar_PiPiGammaForCharmFromBSemi' , 'Phys/SelD0_to_PiPiGamma_forCharmFromBSemi' , 'Phys/[StdAllLoosePions](./stripping21r0p1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '( PT \> 80.0 \*MeV )' , 'pi-' : '( PT \> 80.0 \*MeV )' }                                                                              |
| CombinationCut   | (AM - ACHILD(M,1) + 5 \> 0.0 \*MeV) & (AM - ACHILD(M,1) - 5 \< 170.0 \*MeV)                                                                                                                  |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 8.0 ) & (M - CHILD(M,1) \> 0.0 \*MeV) & (M - CHILD(M,1) \< 170.0 \*MeV))                                                                                             |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                                                                                  |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                                                                          |
| Output           | Phys/SelDstar_PiPiGammaForCharmFromBSemi/Particles                                                                                                                                           |

CombineParticles/Selb2DstarMuXPiPiGammaCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstar_PiPiGammaForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B~0 -\> D\*(2010)+ mu-]cc' , '[B~0 -\> D\*(2010)+ mu+]cc' ]                                                                                                                          |
| Output           | Phys/Selb2DstarMuXPiPiGammaCharmFromBSemi/Particles                                                                                                                                            |

TisTosParticleTagger/b2DstarMuXPiPiGammaCharmFromBSemiLine

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DstarMuXPiPiGammaCharmFromBSemi' ]                                                                                     |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/b2DstarMuXPiPiGammaCharmFromBSemiLine/Particles                                                                                  |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |
