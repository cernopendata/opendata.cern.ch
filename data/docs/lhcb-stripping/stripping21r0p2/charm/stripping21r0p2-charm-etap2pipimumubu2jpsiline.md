[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingEtap2pipimumuBu2JPsiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Etap2pipimumuBu2JPsiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseKaons/Particles',True) |

FilterDesktop/KaonsBuForEtap2pipimumu

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 5)& (PIDK \> -5) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r0p2-commonparticles-stdallloosekaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KaonsBuForEtap2pipimumu/Particles                                              |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseMuons/Particles',True) |

FilterDesktop/MuonsEtaForEtap2pipimumu

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P \> 0.0 \*MeV) & (PT \> 0.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 5)& (PIDmu \> -5)     |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p2-commonparticles-stdallloosemuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/MuonsEtaForEtap2pipimumu/Particles                                             |

CombineParticles/JPsiForEtap2pipimumu

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsEtaForEtap2pipimumu' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                         |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 75 \*MeV)                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10 ) & (PT \> 100 \*MeV) & (BPVVDCHI2 \> 5 ) &(BPVIPCHI2()\> 5) |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                  |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                          |
| Output           | Phys/JPsiForEtap2pipimumu/Particles                                                    |

CombineParticles/Etap2pipimumuBu2JPsiLine

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/JPsiForEtap2pipimumu' , 'Phys/KaonsBuForEtap2pipimumu' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('B+') \< 100 \*MeV)                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8 ) & (PT \> 300 \*MeV) & (BPVVDCHI2 \> 36 ) &(BPVIPCHI2()\< 20) |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+ ]cc                                                              |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+ ]cc' ]                                                      |
| Output           | Phys/Etap2pipimumuBu2JPsiLine/Particles                                                 |

AddRelatedInfo/RelatedInfo1_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo2_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo3_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo4_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo5_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo5_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo6_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo6_Etap2pipimumuBu2JPsiLine/Particles |

AddRelatedInfo/RelatedInfo7_Etap2pipimumuBu2JPsiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Etap2pipimumuBu2JPsiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo7_Etap2pipimumuBu2JPsiLine/Particles |
