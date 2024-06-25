[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2XTauMu_K_3pi_loose_WSLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2XTauMu_K_3pi_loose_WSLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 0.50000000                                 |
| L0DU           | None                                       |
| ODIN           | None                                       |

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
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21r0p1-commonparticles-stdtightdetachedtau3pi)/Particles',True)\>0 |

GaudiSequencer/SeqB2XTauMu_K_3pi_loose_WS_daughters

GaudiSequencer/SEQ:KMuOSForB2XTauMu

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KforB2XTauMu

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDK \> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]        |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/KforB2XTauMu/Particles                                                          |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/MuforB2XTauMu

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDmu \> 2.0) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]   |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/MuforB2XTauMu/Particles                                                          |

CombineParticles/KMuOSForB2XTauMu

|                  |                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2XTauMu' , 'Phys/MuforB2XTauMu' ]                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(P \> 3.0 \*GeV) & (PIDK\> 5) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'K-' : '(P \> 3.0 \*GeV) & (PIDK\> 5) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'mu+' : ' (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'mu-' : ' (MIPCHI2DV(PRIMARY) \> 36.0 )' } |
| CombinationCut   | ((ACHILD(PT,1)+ACHILD(PT,2)) \> 2000.0)                                                                                                                                                                                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0) & (PT \>1000.0)                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[K\*(1410)0 -\> K+ mu-]cc' ]                                                                                                                                                                                                                                                                |
| Output           | Phys/KMuOSForB2XTauMu/Particles                                                                                                                                                                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KMuSSForB2XTauMu

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KforB2XTauMu

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDK \> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]        |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/KforB2XTauMu/Particles                                                          |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/MuforB2XTauMu

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDmu \> 2.0) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]   |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/MuforB2XTauMu/Particles                                                          |

CombineParticles/KMuSSForB2XTauMu

|                  |                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2XTauMu' , 'Phys/MuforB2XTauMu' ]                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(P \> 3.0 \*GeV) & (PIDK\> 5) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'K-' : '(P \> 3.0 \*GeV) & (PIDK\> 5) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'mu+' : ' (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'mu-' : ' (MIPCHI2DV(PRIMARY) \> 36.0 )' } |
| CombinationCut   | ((ACHILD(PT,1)+ACHILD(PT,2)) \> 2000.0)                                                                                                                                                                                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0) & (PT \> 1000.0)                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Delta(1600)++ -\> K+ mu+]cc' ]                                                                                                                                                                                                                                                             |
| Output           | Phys/KMuSSForB2XTauMu/Particles                                                                                                                                                                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2XTauMu_K_3pi_loose_WS_daughters

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Code            | ALL                                                     |
| Inputs          | [ 'Phys/KMuOSForB2XTauMu' , 'Phys/KMuSSForB2XTauMu' ] |
| DecayDescriptor | None                                                    |
| Output          | Phys/B2XTauMu_K_3pi_loose_WS_daughters/Particles        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XTauMu_K_3pi_loose_WSLine

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTauMu_K_3pi_loose_WS_daughters' , 'Phys/[StdTightDetachedTau3pi](./stripping21r0p1-commonparticles-stdtightdetachedtau3pi)' ]                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Delta(1600)++' : 'ALL' , 'Delta(1600)~--' : 'ALL' , 'K\*(1410)0' : 'ALL' , 'K\*(1410)~0' : 'ALL' , 'tau+' : '(P \> 5.0 \*GeV) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'tau-' : '(P \> 5.0 \*GeV) & (PT \> 800.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 36.0 )' } |
| CombinationCut   | (AM\< ( 10000 + 200) \*MeV)                                                                                                                                                                                                                                                                |
| MotherCut        | (MM \< 10000 \*MeV) & (MM\> 2000 \*MeV) & (VFASPF(VCHI2/VDOF) \< 15.0) & (PT\> 3000.0) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 400.0)                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B+ -\> K\*(1410)0 tau-]cc' , '[B+ -\> Delta(1600)++ tau+]cc' ]                                                                                                                                                                                                                   |
| Output           | Phys/B2XTauMu_K_3pi_loose_WSLine/Particles                                                                                                                                                                                                                                                 |

AddRelatedInfo/RelatedInfo1_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo4_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo5_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo6_B2XTauMu_K_3pi_loose_WSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauMu_K_3pi_loose_WSLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_K_3pi_loose_WSLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo7_B2XTauMu_K_3pi_loose_WSLine/Particles |
