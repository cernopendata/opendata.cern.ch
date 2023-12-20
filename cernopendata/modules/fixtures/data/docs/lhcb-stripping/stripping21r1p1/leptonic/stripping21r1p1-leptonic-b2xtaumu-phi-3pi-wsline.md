[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2XTauMu_Phi_3pi_WSLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2XTauMu_Phi_3pi_WSLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 0.50000000                             |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21r1p1-commonparticles-stdtightdetachedtau3pi)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/MuforB2XTauMu

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDmu \> 2.0) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]   |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/MuforB2XTauMu/Particles                                                          |

GaudiSequencer/SeqB2XTauMu_Phi_3pi_WS_daughters

GaudiSequencer/SEQ:Phi2KKforB2XTauMu

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KforB2XTauMu

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDK \> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]        |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/KforB2XTauMu/Particles                                                          |

CombineParticles/Phi2KKforB2XTauMu

|                  |                                                                    |
|------------------|--------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2XTauMu' ]                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                       |
| CombinationCut   | (ADAMASS('phi(1020)') \< 30.0 \*MeV)                               |
| MotherCut        | (ADMASS('phi(1020)') \< 25.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 20.0) |
| DecayDescriptor  | None                                                               |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                        |
| Output           | Phys/Phi2KKforB2XTauMu/Particles                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2XTauMu_Phi_3pi_WS_daughters

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | ALL                                          |
| Inputs          | [ 'Phys/Phi2KKforB2XTauMu' ]               |
| DecayDescriptor | None                                         |
| Output          | Phys/B2XTauMu_Phi_3pi_WS_daughters/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XTauMu_Phi_3pi_WSLine

|                  |                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTauMu_Phi_3pi_WS_daughters' , 'Phys/MuforB2XTauMu' , 'Phys/[StdTightDetachedTau3pi](./stripping21r1p1-commonparticles-stdtightdetachedtau3pi)' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'phi(1020)' : 'ALL' , 'tau+' : '(P \> 0 \*GeV) & (PT \> 0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 0 )' , 'tau-' : '(P \> 0 \*GeV) & (PT \> 0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 0 )' } |
| CombinationCut   | (AM\< ( 10000 + 200) \*MeV)                                                                                                                                                                                                |
| MotherCut        | (MM \< 10000 \*MeV) & (MM\> 2000 \*MeV) & (VFASPF(VCHI2/VDOF) \< 10000000000.0) & (PT\> 0) & (BPVDIRA \> 0) & (BPVVDCHI2 \> 0)                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B0 -\> phi(1020) tau+ mu+]cc' ]                                                                                                                                                                                    |
| Output           | Phys/B2XTauMu_Phi_3pi_WSLine/Particles                                                                                                                                                                                     |

AddRelatedInfo/RelatedInfo1_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo5_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo6_B2XTauMu_Phi_3pi_WSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauMu_Phi_3pi_WSLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Phi_3pi_WSLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo7_B2XTauMu_Phi_3pi_WSLine/Particles |
