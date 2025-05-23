[[stripping21r0p2 lines]](./stripping21r0p2-index)

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

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/Muon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/Muon_forB2Lambda0Mu/Particles                                                                                                                                              |

GaudiSequencer/MERGED:Selection_B2Lambda0Mu_LambdaMajoranaSSMu

GaudiSequencer/MERGEDINPUTS:Selection_B2Lambda0Mu_LambdaMajoranaSSMu

GaudiSequencer/INPUT:LambdaMajoranaSSMu_forB2Lambda0Mu

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/Muon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/Muon_forB2Lambda0Mu/Particles                                                                                                                                              |

CombineParticles/LambdaMajoranaSSMu_forB2Lambda0Mu

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Muon_forB2Lambda0Mu' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                                                           |
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

GaudiSequencer/INPUT:downLambdaMajoranaSSMu_forB2Lambda0Mu

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsDownPions

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsDownPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseDownMuons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseDownMuons/Particles',True) |

FilterDesktop/downMuon_forB2Lambda0Mu

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 250.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 0.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseDownMuons](./stripping21r0p2-commonparticles-stdloosedownmuons)' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/downMuon_forB2Lambda0Mu/Particles                                                                                                                                          |

CombineParticles/downLambdaMajoranaSSMu_forB2Lambda0Mu

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsDownPions](./stripping21r0p2-commonparticles-stdnopidsdownpions)' , 'Phys/downMuon_forB2Lambda0Mu' ]                                                                                                             |
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

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2Lambda0MuBu2LambdaSSMuLine

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Muon_forB2Lambda0Mu' , 'Phys/Selection_B2Lambda0Mu_LambdaMajoranaSSMu' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                             |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<6500.0\*MeV)                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99)& ( MINTREE((ABSID=='Lambda0'),VFASPF(VZ)) - VFASPF(VZ) \> -1.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                |
| DecayDescriptors | [ '[B- -\> Lambda0 mu-]cc' ]                                                                                    |
| Output           | Phys/B2Lambda0MuBu2LambdaSSMuLine/Particles                                                                         |
