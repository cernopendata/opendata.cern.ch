[[stripping21r0p1 lines]](./stripping21r0p1-index)

# Strippingb2DstarMuXHHPi0CharmFromBSemiLine

## Properties:

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DstarMuXHHPi0CharmFromBSemiLine/Particles                                  |
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

LoKi::VoidFilter/Strippingb2DstarMuXHHPi0CharmFromBSemiLineVOIDFilter

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

GaudiSequencer/SeqSelAllKaonsAndPionsForCharmFromBSemi

GaudiSequencer/SEQ:SelKforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/SelKforCharmFromBSemi

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]                                            |
| DecayDescriptor | None                                                                                                                     |
| Output          | Phys/SelKforCharmFromBSemi/Particles                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelPiforCharmFromBSemi

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

CombineParticles/SelD0ToHH_SEED_forCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelAllKaonsAndPionsForCharmFromBSemi' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                   |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 1500\*MeV)& (AM \< 2000\*MeV)& (AM - ACHILD(M,1)-ACHILD(M,2) \> 50\*MeV)& (ADOCACHI2CUT(25, ''))& (ACHILD(MIPDV(PRIMARY),1)+ACHILD(MIPDV(PRIMARY),2) \> 0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 4.0) & (BPVVD \> 3\*mm) & (BPVDIRA \> 0.99)                                                                                                                              |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ 'K\*(892)0 -\> pi+ pi-' , 'K\*(892)0 -\> K+ K-' , 'K\*(892)0 -\> K- pi+' , 'K\*(892)0 -\> K+ pi-' ]                                                                                        |
| Output           | Phys/SelD0ToHH_SEED_forCharmFromBSemi/Particles                                                                                                                                                |

GaudiSequencer/SeqSelAllPi0sForCharmFromBSemi

GaudiSequencer/SEQ:SelPi0ResolvedforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/SelPi0ResolvedforCharmFromBSemi

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT\> 1000 \*MeV) & (P\> 3000 \*MeV)& (CHILD(CL,1)\> 0.25) & (CHILD(CL,2)\> 0.25)         |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/SelPi0ResolvedforCharmFromBSemi/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelPi0MergedforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/SelPi0MergedforCharmFromBSemi

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT\> 1000 \*MeV) & (P\> 3000 \*MeV)                                                  |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/SelPi0MergedforCharmFromBSemi/Particles                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/SelAllPi0sForCharmFromBSemi

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | ALL                                                                                 |
| Inputs          | [ 'Phys/SelPi0MergedforCharmFromBSemi' , 'Phys/SelPi0ResolvedforCharmFromBSemi' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/SelAllPi0sForCharmFromBSemi/Particles                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/SelCharmDToHHPi0ForCharmFromBSemi

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelAllPi0sForCharmFromBSemi' , 'Phys/SelD0ToHH_SEED_forCharmFromBSemi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi0' : 'ALL' }        |
| CombinationCut   | (ADAMASS('D+') \< 180\*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)\> 2500\*MeV)              |
| MotherCut        | (abs(DTF_FUN(M,False,'pi0')-1865) \< 150\*MeV)                                     |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ '[D0 -\> K\*(892)0 pi0]cc' ]                                                 |
| Output           | Phys/SelCharmDToHHPi0ForCharmFromBSemi/Particles                                   |

ConjugateNeutralPID/SelConjugateD0ForDstarD0ToHHPi0ForCharmFromBSemi

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/SelCharmDToHHPi0ForCharmFromBSemi' ]                  |
| DecayDescriptor | None                                                            |
| Output          | Phys/SelConjugateD0ForDstarD0ToHHPi0ForCharmFromBSemi/Particles |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r0p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

CombineParticles/SelDstarD0ToHHPi0ForCharmFromBSemi

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelCharmDToHHPi0ForCharmFromBSemi' , 'Phys/SelConjugateD0ForDstarD0ToHHPi0ForCharmFromBSemi' , 'Phys/[StdAllLoosePions](./stripping21r0p1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '( PT \> 80.0 \*MeV )' , 'pi-' : '( PT \> 80.0 \*MeV )' }                                                                          |
| CombinationCut   | (AM - ACHILD(M,1) + 5 \> 0.0 \*MeV) & (AM - ACHILD(M,1) - 5 \< 170.0 \*MeV)                                                                                                              |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 8.0 ) & (M - CHILD(M,1) \> 0.0 \*MeV) & (M - CHILD(M,1) \< 170.0 \*MeV))                                                                                         |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                                                                              |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                                                                      |
| Output           | Phys/SelDstarD0ToHHPi0ForCharmFromBSemi/Particles                                                                                                                                        |

CombineParticles/Selb2DstarMuXHHPi0CharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarD0ToHHPi0ForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B~0 -\> D\*(2010)+ mu-]cc' , '[B~0 -\> D\*(2010)+ mu+]cc' ]                                                                                                                          |
| Output           | Phys/Selb2DstarMuXHHPi0CharmFromBSemi/Particles                                                                                                                                                |

TisTosParticleTagger/b2DstarMuXHHPi0CharmFromBSemiLine

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2DstarMuXHHPi0CharmFromBSemi' ]                                                                                         |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/b2DstarMuXHHPi0CharmFromBSemiLine/Particles                                                                                      |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |
