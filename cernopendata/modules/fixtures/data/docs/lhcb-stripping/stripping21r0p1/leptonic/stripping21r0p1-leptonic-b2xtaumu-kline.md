[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2XTauMu_KLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/B2XTauMu_KLine/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

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

GaudiSequencer/SeqB2XTauMu_K_daughters

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

FilterDesktop/B2XTauMu_K_daughters

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Code            | ALL                                                     |
| Inputs          | [ 'Phys/KMuOSForB2XTauMu' , 'Phys/KMuSSForB2XTauMu' ] |
| DecayDescriptor | None                                                    |
| Output          | Phys/B2XTauMu_K_daughters/Particles                     |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XTauMu_KLine

|                  |                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTauMu_K_daughters' , 'Phys/MuforB2XTauMu' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'Delta(1600)++' : 'ALL' , 'Delta(1600)~--' : 'ALL' , 'K\*(1410)0' : 'ALL' , 'K\*(1410)~0' : 'ALL' , 'mu+' : '(P \> 5.0 \*GeV) & (PT \> 800.0 \*MeV) & (PIDmu \> 2.0) & (MIPCHI2DV(PRIMARY) \> 36.0 )' , 'mu-' : '(P \> 5.0 \*GeV) & (PT \> 800.0 \*MeV) & (PIDmu \> 2.0) & (MIPCHI2DV(PRIMARY) \> 36.0 )' } |
| CombinationCut   | (AM\<( 10000 + 200) \*MeV)                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (MM \< 10000 \*MeV) & (MM\> 2000 \*MeV) & (VFASPF(VCHI2/VDOF) \< 15.0) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 400.0)                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B+ -\> K\*(1410)0 mu+]cc' , '[B+ -\> Delta(1600)++ mu-]cc' ]                                                                                                                                                                                                                                                     |
| Output           | Phys/B2XTauMu_KLine/Particles                                                                                                                                                                                                                                                                                              |

AddRelatedInfo/RelatedInfo1_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_B2XTauMu_KLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauMu_KLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_KLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo7_B2XTauMu_KLine/Particles |
