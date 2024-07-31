[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2XTauMu_Kst_WSLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2XTauMu_Kst_WSLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 0.50000000                         |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

GaudiSequencer/SeqB2XTauMu_Kst_WS_daughters

GaudiSequencer/SEQ:Kst0MuForB2XTauMu

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

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PiforB2XTauMu

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\< 3) & (MIPCHI2DV(PRIMARY)\> 16.0) & (TRGHOSTPROB \< 0.5) & (PIDK \< 0.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]        |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/PiforB2XTauMu/Particles                                                         |

CombineParticles/Kst02KPiforB2XTauMu

|                  |                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2XTauMu' , 'Phys/PiforB2XTauMu' ]                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' , 'K-' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' , 'pi+' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' , 'pi-' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' } |
| CombinationCut   | (ADAMASS('K\*(892)0') \< 180.0 \*MeV)                                                                                                                                                                                    |
| MotherCut        | (ADMASS('K\*(892)0') \< 150.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 15.0)                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                       |
| Output           | Phys/Kst02KPiforB2XTauMu/Particles                                                                                                                                                                                       |

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

CombineParticles/Kst0MuForB2XTauMu

|                  |                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst02KPiforB2XTauMu' , 'Phys/MuforB2XTauMu' ]                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' , 'mu-' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV)' } |
| CombinationCut   | ATRUE                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15.0)                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                              |
| DecayDescriptors | [ '[K\*(1410)+ -\> K\*(892)0 mu+]cc' , '[K\*(1410)- -\> K\*(892)0 mu-]cc' ]                                                                                 |
| Output           | Phys/Kst0MuForB2XTauMu/Particles                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2XTauMu_Kst_WS_daughters

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | ALL                                      |
| Inputs          | [ 'Phys/Kst0MuForB2XTauMu' ]           |
| DecayDescriptor | None                                     |
| Output          | Phys/B2XTauMu_Kst_WS_daughters/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XTauMu_Kst_WSLine

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTauMu_Kst_WS_daughters' , 'Phys/MuforB2XTauMu' ]                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(1410)+' : 'ALL' , 'K\*(1410)-' : 'ALL' , 'mu+' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV) & (PIDmu \> 2.0) & (MIPCHI2DV(PRIMARY) \> 16.0 )' , 'mu-' : '(P \> 2.0 \*GeV) & (PT \> 500.0 \*MeV) & (PIDmu \> 2.0) & (MIPCHI2DV(PRIMARY) \> 16.0 )' } |
| CombinationCut   | (AM\<( 10000 + 200) \*MeV)                                                                                                                                                                                                                                           |
| MotherCut        | (MM \< 10000 \*MeV) & (MM\> 2000 \*MeV) & (VFASPF(VCHI2/VDOF) \< 25.0) & (BPVDIRA \> 0.95) & (BPVVDCHI2 \> 80)                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B0 -\> K\*(1410)+ mu+]cc' ]                                                                                                                                                                                                                                  |
| Output           | Phys/B2XTauMu_Kst_WSLine/Particles                                                                                                                                                                                                                                   |

AddRelatedInfo/RelatedInfo1_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo6_B2XTauMu_Kst_WSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauMu_Kst_WSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauMu_Kst_WSLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo7_B2XTauMu_Kst_WSLine/Particles |
