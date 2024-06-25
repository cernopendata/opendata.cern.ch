[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2DMuNuX_Xic_FakeMuon

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2DMuNuX_Xic_FakeMuon/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | HLT_PASS_RE('Hlt1.\*Decision')       |
| HLT2           | HLT_PASS_RE('Hlt2.\*Decision')       |
| Prescale       | 0.020000000                          |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2DMuNuX_Xic_FakeMuonVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsMuons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsMuons/Particles',True) |

FilterDesktop/FakeMuonsForB2DMuNuX

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0 ) & (P\> 6000.0)& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 9.0) & (INMUON) & (PIDmu \< 0.0) |
| Inputs          | [ 'Phys/[StdNoPIDsMuons](./stripping21r1p2-commonparticles-stdnopidsmuons)' ]                                                   |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/FakeMuonsForB2DMuNuX/Particles                                                                                               |

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

FilterDesktop/ProtonsForB2DMuNuX

|                 |                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2000.0) & (PT \> 250.0 )& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 4.0)& (P\>8000.0)& (PIDp \> 0.0) & (PIDp-PIDK \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                    |
| DecayDescriptor | None                                                                                                                                                 |
| Output          | Phys/ProtonsForB2DMuNuX/Particles                                                                                                                    |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/KforB2DMuNuX

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2000.0) & (PT \> 250.0 )& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 4.0) & (P\>2000.0) & (PIDK\> -2.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                     |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/KforB2DMuNuX/Particles                                                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PiforB2DMuNuX

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2000.0) & (PT \> 250.0 )& (TRCHI2DOF \< 3.0)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 20.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                       |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/PiforB2DMuNuX/Particles                                                                                        |

CombineParticles/CharmSelForXicB2DMuNuX

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuNuX' , 'Phys/PiforB2DMuNuX' , 'Phys/ProtonsForB2DMuNuX' ]                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (ADAMASS('Xi_c+') \< 90.0 ) & (ADOCACHI2CUT( 20, ''))                                                       |
| MotherCut        | (ADMASS('Xi_c+') \< 80.0 )& (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVVDCHI2 \> 25.0) & (BPVDIRA\> 0.99)            |
| DecayDescriptor  | None                                                                                                        |
| DecayDescriptors | [ '[Xi_c+ -\> K- p+ pi+]cc' ]                                                                           |
| Output           | Phys/CharmSelForXicB2DMuNuX/Particles                                                                       |

CombineParticles/B2DMuNuX_Xic_FakeMuon

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmSelForXicB2DMuNuX' , 'Phys/FakeMuonsForB2DMuNuX' ]                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                  |
| CombinationCut   | (AM \> 2200.0) & (AM \< 8000.0) & (ADOCACHI2CUT( 10, ''))                                                                                                                                                                            |
| MotherCut        | (MM\>2200.0) & (MM\<8000.0)&(VFASPF(VCHI2/VDOF)\< 9.0) & (BPVDIRA\> 0.999)&(MINTREE(((ABSID=='D+')\|(ABSID=='D0')\|(ABSID=='Lambda_c+')\|(ABSID=='Omega_c0')\|(ABSID=='Xi_c+')\|(ABSID=='Xi_c0')), VFASPF(VZ))-VFASPF(VZ) \> -0.05 ) |
| DecayDescriptor  | None                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Xi_b0 -\> Xi_c+ mu-]cc' , '[Xi_b0 -\> Xi_c+ mu+]cc' ]                                                                                                                                                                      |
| Output           | Phys/B2DMuNuX_Xic_FakeMuon/Particles                                                                                                                                                                                                 |
