[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2DpMuXHHHPi0CharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2DpMuXHHHPi0CharmFromBSemiLine/Particles                                                 |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2DpMuXHHHPi0CharmFromBSemiLineVOIDFilter

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

GaudiSequencer/SeqSelAllPi0sForCharmFromBSemi

GaudiSequencer/SEQ:SelPi0ResolvedforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/SelPi0ResolvedforCharmFromBSemi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT\> 1000 \*MeV) & (P\> 3000 \*MeV)& (CHILD(CL,1)\> 0.25) & (CHILD(CL,2)\> 0.25)       |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelPi0ResolvedforCharmFromBSemi/Particles                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelPi0MergedforCharmFromBSemi

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/SelPi0MergedforCharmFromBSemi

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\> 1000 \*MeV) & (P\> 3000 \*MeV)                                                |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/SelPi0MergedforCharmFromBSemi/Particles                                        |

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

CombineParticles/SelCharmDToHHHPi0ForCharmFromBSemi

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelAllPi0sForCharmFromBSemi' , 'Phys/SelDToHHH_SEED' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'pi0' : 'ALL' }                           |
| CombinationCut   | (DAMASS('D_s+') \< 120 \*MeV) & (DAMASS('D+')\> -120 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2)\> 3000\*MeV) |
| MotherCut        | (DTF_FUN(M,False,'pi0') \> 1869-110\*MeV)& (DTF_FUN(M,False,'pi0') \< 1968+110\*MeV)                 |
| DecayDescriptor  | None                                                                                                 |
| DecayDescriptors | [ '[D+ -\> K\*(892)+ pi0]cc' ]                                                                   |
| Output           | Phys/SelCharmDToHHHPi0ForCharmFromBSemi/Particles                                                    |

CombineParticles/Selb2D0MuX_HHHPi0CharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelCharmDToHHHPi0ForCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                   |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[B~0 -\> D+ mu-]cc' ]                                                                                                                                                                   |
| Output           | Phys/Selb2D0MuX_HHHPi0CharmFromBSemi/Particles                                                                                                                                                 |

TisTosParticleTagger/b2DpMuXHHHPi0CharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2D0MuX_HHHPi0CharmFromBSemi' ]                                                                                                       |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2DpMuXHHHPi0CharmFromBSemiLine/Particles                                                                                                     |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
