[[stripping21r0p2 lines]](./stripping21r0p2-index)

# Strippingb2LcMuXFakeLb2LcMuNuX_Lc2L0PiLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/b2LcMuXFakeLb2LcMuNuX_Lc2L0PiLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT1           | HLT_PASS_RE('Hlt1.\*Decision')                   |
| HLT2           | HLT_PASS_RE('Hlt2.\*Decision')                   |
| Prescale       | 0.10000000                                       |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/Strippingb2LcMuXFakeLb2LcMuNuX_Lc2L0PiLineVOIDFilter

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

FilterDesktop/FakeMuforLb2LcMuNuX_Lc2L0Pi

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9.0 ) & (TRGHOSTPROB \< 0.35 ) & (PIDmu \< 0.0 ) & (P \> 6000.0 ) & (PT \> 1000.0 ) & (TRCHI2DOF \< 3.0) |
| Inputs          | [ 'Phys/[StdNoPIDsMuons](./stripping21r0p2-commonparticles-stdnopidsmuons)' ]                                                 |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/FakeMuforLb2LcMuNuX_Lc2L0Pi/Particles                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PiforLb2LcMuNuX_Lc2L0Pi

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 4.0 ) & (TRGHOSTPROB \< 0.35 ) & (P \> 2000.0 ) & (PT \> 250.0 ) & (TRCHI2DOF \< 3.0 ) & (PIDK \< 10.0 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                   |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/PiforLb2LcMuNuX_Lc2L0Pi/Particles                                                                                          |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseLambdaLL

|      |                                        |
|------|----------------------------------------|
| Code | 0StdVeryLooseLambdaLL/Particles',True) |

FilterDesktop/LambdaLLforLb2LcMuNuX_Lc2L0Pi

|                 |                                                                                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000.0 ) & (PT \> 500.0 ) & (BPVVDCHI2 \> 100.0) & (VFASPF(VCHI2/VDOF) \< 6.0)& (CHILDCUT((TRGHOSTPROB \< 0.35),1)) & (CHILDCUT((TRGHOSTPROB \< 0.35),2))& (CHILDCUT((TRCHI2DOF \< 3.0),1)) & (CHILDCUT((TRCHI2DOF \< 3.0),2))& (ADMASS('Lambda0') \< 30.0 ) |
| Inputs          | [ 'Phys/[StdVeryLooseLambdaLL](./stripping21r0p2-commonparticles-stdverylooselambdall)' ]                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                                               |
| Output          | Phys/LambdaLLforLb2LcMuNuX_Lc2L0Pi/Particles                                                                                                                                                                                                                       |

CombineParticles/Lc2L0PiforLb2LcMuNuX_Lc2L0Pi

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LambdaLLforLb2LcMuNuX_Lc2L0Pi' , 'Phys/PiforLb2LcMuNuX_Lc2L0Pi' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 90.0 )                                                         |
| MotherCut        | (ADMASS('Lambda_c+') \< 80.0 ) & (VFASPF(VCHI2/VDOF) \< 6.0 )                           |
| DecayDescriptor  | None                                                                                    |
| DecayDescriptors | [ '[Lambda_c+ -\> Lambda0 pi+]cc' ]                                                 |
| Output           | Phys/Lc2L0PiforLb2LcMuNuX_Lc2L0Pi/Particles                                             |

CombineParticles/b2LcMuXFakeLb2LcMuNuX_Lc2L0PiLine

|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/FakeMuforLb2LcMuNuX_Lc2L0Pi' , 'Phys/Lc2L0PiforLb2LcMuNuX_Lc2L0Pi' ]                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                              |
| CombinationCut   | (AM \> 2200.0 ) & (AM \< 8000.0) & (ADOCACHI2CUT( 10, ''))                                                                                               |
| MotherCut        | (MM \> 2200.0 ) & (MM \< 8000.0 )& (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVDIRA \> 0.999 )& (MINTREE((ABSID=='Lambda_c+'), VFASPF(VZ)) - VFASPF(VZ) \> -2.0 ) |
| DecayDescriptor  | None                                                                                                                                                     |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ mu-]cc' , '[Lambda_b0 -\> Lambda_c+ mu+]cc' ]                                                                          |
| Output           | Phys/b2LcMuXFakeLb2LcMuNuX_Lc2L0PiLine/Particles                                                                                                         |
