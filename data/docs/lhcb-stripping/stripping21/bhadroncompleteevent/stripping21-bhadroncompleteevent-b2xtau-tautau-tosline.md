[[stripping21 lines]](./stripping21-index)

# StrippingB2XTau_TauTau_TOSLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2XTau_TauTau_TOSLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21-commonparticles-stdtightdetachedtau3pi)/Particles')\>0 |

FilterDesktop/B2XTau_TauFilter

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (PT \> 0\*MeV)                                                                              |
| Inputs          | [ 'Phys/[StdTightDetachedTau3pi](./stripping21-commonparticles-stdtightdetachedtau3pi)' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/B2XTau_TauFilter/Particles                                                             |

CombineParticles/B2XTau_TauTau

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTau_TauFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                        |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV)                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 90) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 225) & (BPVVD \< 90) & (PT \> 2000\*MeV) & (INGENERATION((PT \> 4000\*MeV),1)) & (INGENERATION((PT \> 2000\*MeV),2)) & (sumpt \>7000\*MeV) & (max(CHILD(ipsm,1),CHILD(ipsm,2)) \> 20) & (max(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 150) & (min(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 16) & (in_range(0\*MeV,MCOR,10000\*MeV)) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'B0 -\> tau+ tau-' ]                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/B2XTau_TauTau/Particles                                                                                                                                                                                                                                                                                                                                                                                                            |

TisTosParticleTagger/B2XTau_TauTau_TOSLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau' ]                                                 |
| DecayDescriptor | None                                                                       |
| Output          | Phys/B2XTau_TauTau_TOSLine/Particles                                       |
| TisTosSpecs     | { 'Hlt2(Topo2BodyBBDT\|Topo3BodyBBDT\|Topo4BodyBBDT).\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_B2XTau_TauTau_TOSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_TauTau_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_TOSLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_B2XTau_TauTau_TOSLine/Particles |
