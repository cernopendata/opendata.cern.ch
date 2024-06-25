[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2DMuNuX_Ds

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/B2DMuNuX_Ds/Particles                       |
| Postscale      | 1.0000000                                        |
| HLT1           | HLT_PASS_RE('Hlt1.\*Decision')                   |
| HLT2           | HLT_PASS_RE('Hlt2(SingleMuon\|Topo).\*Decision') |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2DMuNuX_DsVOIDFilter

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

FilterDesktop/MuforB2DMuNuX

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0 ) & (P\> 6000.0)& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDmu \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                          |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/MuforB2DMuNuX/Particles                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KforB2DMuNuX

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2000.0) & (PT \> 250.0 )& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 4.0) & (P\>2000.0) & (PIDK\> -2.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                     |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/KforB2DMuNuX/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PiforB2DMuNuX

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2000.0) & (PT \> 250.0 )& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 20.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                       |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/PiforB2DMuNuX/Particles                                                                                        |

CombineParticles/CharmSelForDsB2DMuNuX

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuNuX' , 'Phys/PiforB2DMuNuX' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                           |
| CombinationCut   | (DAMASS('D_s+') \< 90.0 )& (DAMASS('D+')\> -90.0 ) & (ADOCACHI2CUT( 20, ''))                                           |
| MotherCut        | (DMASS('D_s+') \< 80.0 )& (DMASS('D+')\> -80.0 )& (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVVDCHI2 \> 25.0) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                   |
| DecayDescriptors | [ '[D+ -\> K+ K- pi+]cc' ]                                                                                         |
| Output           | Phys/CharmSelForDsB2DMuNuX/Particles                                                                                   |

CombineParticles/BSelForDsB2DMuNuX

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmSelForDsB2DMuNuX' , 'Phys/MuforB2DMuNuX' ]                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                         |
| CombinationCut   | (AM \> 2200.0) & (AM \< 8000.0) & (ADOCACHI2CUT( 10, ''))                                                                                                                                                                            |
| MotherCut        | (MM\>2200.0) & (MM\<8000.0)&(VFASPF(VCHI2/VDOF)\< 9.0) & (BPVDIRA\> 0.999)&(MINTREE(((ABSID=='D+')\|(ABSID=='D0')\|(ABSID=='Lambda_c+')\|(ABSID=='Omega_c0')\|(ABSID=='Xi_c+')\|(ABSID=='Xi_c0')), VFASPF(VZ))-VFASPF(VZ) \> -0.05 ) |
| DecayDescriptor  | None                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B0 -\> D- mu+]cc' , '[B0 -\> D- mu-]cc' ]                                                                                                                                                                                  |
| Output           | Phys/BSelForDsB2DMuNuX/Particles                                                                                                                                                                                                     |

TisTosParticleTagger/B2DMuNuX_Ds

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/BSelForDsB2DMuNuX' ]                                                                                                     |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/B2DMuNuX_Ds/Particles                                                                                                         |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |
