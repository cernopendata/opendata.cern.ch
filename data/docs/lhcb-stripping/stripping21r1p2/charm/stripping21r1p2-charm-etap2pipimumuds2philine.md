[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingEtap2pipimumuDs2PhiLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Etap2pipimumuDs2PhiLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLoosePions/Particles',True) |

FilterDesktop/PionsEtaForEtap2pipimumu

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P \> 0.0 \*MeV) & (PT \> 0.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 5)                    |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1p2-commonparticles-stdallloosepions)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/PionsEtaForEtap2pipimumu/Particles                                             |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseMuons/Particles',True) |

FilterDesktop/MuonsEtaForEtap2pipimumu

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P \> 0.0 \*MeV) & (PT \> 0.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 5)& (PIDmu \> -5)     |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p2-commonparticles-stdallloosemuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/MuonsEtaForEtap2pipimumu/Particles                                             |

CombineParticles/PhiForEtap2pipimumu

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsEtaForEtap2pipimumu' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                         |
| CombinationCut   | (ADAMASS('phi(1020)') \< 75 \*MeV)                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10 ) & (PT \> 100 \*MeV) & (BPVVDCHI2 \> 5 ) &(BPVIPCHI2()\> 5) |
| DecayDescriptor  | phi(1020) -\> mu+ mu-                                                                  |
| DecayDescriptors | [ 'phi(1020) -\> mu+ mu-' ]                                                          |
| Output           | Phys/PhiForEtap2pipimumu/Particles                                                     |

CombineParticles/Etap2pipimumuDs2PhiLine

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhiForEtap2pipimumu' , 'Phys/PionsEtaForEtap2pipimumu' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                |
| CombinationCut   | (ADAMASS('D_s+') \< 100 \*MeV) & ( AHASCHILD( (MIPCHI2DV(PRIMARY)\>5) & (PT\>25.0) & (P\>200.0) ) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15) & (PT \> 300 \*MeV) & (BPVVDCHI2\>10) & (BPVIPCHI2()\< 10)               |
| DecayDescriptor  | [D_s+ -\> phi(1020) pi+ pi+ pi- ]cc                                                               |
| DecayDescriptors | [ '[D_s+ -\> phi(1020) pi+ pi+ pi- ]cc' ]                                                       |
| Output           | Phys/Etap2pipimumuDs2PhiLine/Particles                                                              |

AddRelatedInfo/RelatedInfo1_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo2_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo3_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo4_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo5_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo5_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo6_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo6_Etap2pipimumuDs2PhiLine/Particles |

AddRelatedInfo/RelatedInfo7_Etap2pipimumuDs2PhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuDs2PhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo7_Etap2pipimumuDs2PhiLine/Particles |
