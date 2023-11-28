[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2Lambda0MuBu2LambdaSSMuLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/B2Lambda0MuBu2LambdaSSMuLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

LoKi::VoidFilter/StrippingB2Lambda0MuBu2LambdaSSMuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 300.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Muon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/Muon_forB2Lambda0Mu/Particles                                                                                                                                              |

GaudiSequencer/SeqSelection_B2Lambda0Mu_LambdaMajoranaSSMu

GaudiSequencer/SEQ:LambdaMajoranaSSMu_forB2Lambda0Mu

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Muon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/Muon_forB2Lambda0Mu/Particles                                                                                                                                              |

CombineParticles/LambdaMajoranaSSMu_forB2Lambda0Mu

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Muon_forB2Lambda0Mu' , 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                               |
| MotherCut        | ( M \> 1500.0\*MeV )&( BPVVDCHI2 \> 100.0 )&( VFASPF(VCHI2/VDOF) \< 10.0 )&( PT \> 700.0\*MeV )                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda0 -\> mu- pi+]cc' ]                                                                                                                                                                                                    |
| Output           | Phys/LambdaMajoranaSSMu_forB2Lambda0Mu/Particles                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:downLambdaMajoranaSSMu_forB2Lambda0Mu

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsDownPions](./stripping21r1p1-commonparticles-stdnopidsdownpions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseDownMuons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDownMuons](./stripping21r1p1-commonparticles-stdloosedownmuons)/Particles',True)\>0 |

FilterDesktop/downMuon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseDownMuons](./stripping21r1p1-commonparticles-stdloosedownmuons)' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/downMuon_forB2Lambda0Mu/Particles                                                                                                                                          |

CombineParticles/downLambdaMajoranaSSMu_forB2Lambda0Mu

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsDownPions](./stripping21r1p1-commonparticles-stdnopidsdownpions)' , 'Phys/downMuon_forB2Lambda0Mu' ]                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 10.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                               |
| MotherCut        | ( M \> 1500.0\*MeV )&( BPVVDCHI2 \> 100.0 )&( VFASPF(VCHI2/VDOF) \< 10.0 )&( PT \> 700.0\*MeV )                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda0 -\> mu- pi+]cc' ]                                                                                                                                                                                                    |
| Output           | Phys/downLambdaMajoranaSSMu_forB2Lambda0Mu/Particles                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2Lambda0Mu_LambdaMajoranaSSMu

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                           |
| Inputs          | [ 'Phys/LambdaMajoranaSSMu_forB2Lambda0Mu' , 'Phys/downLambdaMajoranaSSMu_forB2Lambda0Mu' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/Selection_B2Lambda0Mu_LambdaMajoranaSSMu/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2Lambda0MuBu2LambdaSSMuLine

|                  |                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Muon_forB2Lambda0Mu' , 'Phys/Selection_B2Lambda0Mu_LambdaMajoranaSSMu' ]                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                            |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<6500.0\*MeV)                                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99)& ( MINTREE((ABSID=='Lambda0'),VFASPF(VZ)) - VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                               |
| DecayDescriptors | [ '[B- -\> Lambda0 mu-]cc' ]                                                                                   |
| Output           | Phys/B2Lambda0MuBu2LambdaSSMuLine/Particles                                                                        |
