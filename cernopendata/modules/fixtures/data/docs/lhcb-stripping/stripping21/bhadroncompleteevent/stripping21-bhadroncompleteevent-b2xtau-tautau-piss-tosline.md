[[stripping21 lines]](./stripping21-index)

# StrippingB2XTau_TauTau_piSS_TOSLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/B2XTau_TauTau_piSS_TOSLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 0.50000000                                |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsDForB2XTau

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) & (PROBNNpi \> 0.55) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                       |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/PionsDForB2XTau/Particles                                                                                                  |

CombineParticles/TauSSForB2XTau

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsDForB2XTau' ]                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                           |
| CombinationCut   | (AM \> 400\*MeV) & (AM \< 2100\*MeV) & (APT \> 800\*MeV) & (AMAXDOCA('') \<0.2\*mm) & (ANUM(PT \> 800\*MeV) \>= 1)                                                                       |
| MotherCut        | (PT \> 1000\*MeV) & (BPVDIRA \>0.99) & (VFASPF(VCHI2) \< 16)& (BPVVDCHI2 \> 16) & (BPVVDRHO \> 0.1\*mm) & (BPVVDRHO \< 7.0\*mm) & (BPVVDZ \> 5.0\*mm) & (M\>500.\*MeV) & (M\<2000.\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                     |
| DecayDescriptors | [ '[tau+ -\> pi+ pi+ pi+]cc' ]                                                                                                                                                       |
| Output           | Phys/TauSSForB2XTau/Particles                                                                                                                                                            |

CombineParticles/B2XTau_TauTau_piSS

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TauSSForB2XTau' ]                                                                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                        |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV)                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 90) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 225) & (BPVVD \< 90) & (PT \> 2000\*MeV) & (INGENERATION((PT \> 4000\*MeV),1)) & (INGENERATION((PT \> 2000\*MeV),2)) & (sumpt \>7000\*MeV) & (max(CHILD(ipsm,1),CHILD(ipsm,2)) \> 20) & (max(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 150) & (min(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 16) & (in_range(0\*MeV,MCOR,10000\*MeV)) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'B0 -\> tau+ tau-' ]                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/B2XTau_TauTau_piSS/Particles                                                                                                                                                                                                                                                                                                                                                                                                       |

TisTosParticleTagger/B2XTau_TauTau_piSS_TOSLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS' ]                                            |
| DecayDescriptor | None                                                                       |
| Output          | Phys/B2XTau_TauTau_piSS_TOSLine/Particles                                  |
| TisTosSpecs     | { 'Hlt2(Topo2BodyBBDT\|Topo3BodyBBDT\|Topo4BodyBBDT).\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo5_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo6_B2XTau_TauTau_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_TauTau_piSS_TOSLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauTau_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo7_B2XTau_TauTau_piSS_TOSLine/Particles |
