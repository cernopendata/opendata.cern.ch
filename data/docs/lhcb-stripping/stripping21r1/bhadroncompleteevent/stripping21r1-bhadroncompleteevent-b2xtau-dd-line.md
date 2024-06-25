[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XTau_DD_Line

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/B2XTau_DD_Line/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsDForB2XTau

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) & (PROBNNpi \> 0.55) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                     |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/PionsDForB2XTau/Particles                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsDForB2XTau

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KaonsDForB2XTau/Particles                                                                             |

CombineParticles/DForB2XTau

|                  |                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsDForB2XTau' , 'Phys/PionsDForB2XTau' ]                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                              |
| CombinationCut   | (AM \> 1750\*MeV) & (AM \< 2080\*MeV) & (APT \> 800\*MeV) & (AMAXDOCA('') \<0.2\*mm) & (ANUM(PT \> 800\*MeV) \>= 1)                                                                       |
| MotherCut        | (PT \> 1000\*MeV) & (BPVDIRA \>0.99) & (VFASPF(VCHI2) \< 16)& (BPVVDCHI2 \> 16) & (BPVVDRHO \> 0.1\*mm) & (BPVVDRHO \< 7.0\*mm) & (BPVVDZ \> 5.0\*mm) & (M\>1800.\*MeV) & (M\<2030.\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                      |
| DecayDescriptors | [ '[D+ -\> pi+ K- pi+]cc' , '[D+ -\> K+ K- pi+]cc' ]                                                                                                                                |
| Output           | Phys/DForB2XTau/Particles                                                                                                                                                                 |

CombineParticles/B2XTau_DD_Line

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DForB2XTau' ]                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                            |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV) & (AM \> 5000)                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 90) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 225) & (BPVVD \< 90) & (PT \> 2000\*MeV) & (INGENERATION((PT \> 4000\*MeV),1)) & (INGENERATION((PT \> 2000\*MeV),2)) & (sumpt \>7000\*MeV) & (max(CHILD(ipsm,1),CHILD(ipsm,2)) \> 20) & (max(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 150) & (min(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 16) & (in_range(0\*MeV,MCOR,10000\*MeV)) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'B0 -\> D+ D-' ]                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/B2XTau_DD_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                           |

AddRelatedInfo/RelatedInfo1_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_B2XTau_DD_Line/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_DD_Line

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD_Line' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo7_B2XTau_DD_Line/Particles |
