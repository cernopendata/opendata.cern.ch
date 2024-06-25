[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XTau_DPi_Line

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/B2XTau_DPi_Line/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

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

FilterDesktop/PionsForB2XTau

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 6000\*MeV) & (PT \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                 |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/PionsForB2XTau/Particles                                                                               |

CombineParticles/B2XTau_DPi_Line

|                  |                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DForB2XTau' , 'Phys/PionsForB2XTau' ]                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                          |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV) & (AM \> 5000)                                                                                                                                                             |
| MotherCut        | ((CHILD(BPVVDCHI2,1)) \< 4000) & (MIPCHI2DV(PRIMARY) \< 200) & (BPVVD \< 35) & (PT \> 5000\*MeV) & (sumpt \>2500\*MeV) & ((CHILD(VFASPF(VCHI2),1)) \< 12) & (in_range(0\*MeV,MCOR,10000\*MeV)) &((CHILD(MIPCHI2DV(PRIMARY),1)) \> 50) |
| DecayDescriptor  | None                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> D+ pi-]cc' ]                                                                                                                                                                                                           |
| Output           | Phys/B2XTau_DPi_Line/Particles                                                                                                                                                                                                        |

AddRelatedInfo/RelatedInfo1_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo6_B2XTau_DPi_Line/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_DPi_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DPi_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo7_B2XTau_DPi_Line/Particles |
