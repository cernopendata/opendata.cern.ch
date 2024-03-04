[[stripping21 lines]](./stripping21-index)

# StrippingB2XTau_TauMu_piSS_TOSLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/B2XTau_TauMu_piSS_TOSLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 0.50000000                               |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

LoKi::VoidFilter/SelFilterPhys_StdTightMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightMuons](./stripping21-commonparticles-stdtightmuons)/Particles')\>0 |

FilterDesktop/MuonsForB2XTau

|                 |                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 6000\*MeV) & (PT \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) & (HASMUON) & (PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdTightMuons](./stripping21-commonparticles-stdtightmuons)' ]                                                              |
| DecayDescriptor | None                                                                                                                                   |
| Output          | Phys/MuonsForB2XTau/Particles                                                                                                          |

CombineParticles/B2XTau_TauMu_piSS

|                  |                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForB2XTau' , 'Phys/TauSSForB2XTau' ]                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                                                                      |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV)                                                                                                                                                                            |
| MotherCut        | ((CHILD(BPVVDCHI2,1)) \< 4000) & (MIPCHI2DV(PRIMARY) \< 200) & (BPVVD \< 35) & (PT \> 5000\*MeV) & (sumpt \>2500\*MeV) & ((CHILD(VFASPF(VCHI2),1)) \< 12) & (in_range(0\*MeV,MCOR,10000\*MeV)) &((CHILD(MIPCHI2DV(PRIMARY),1)) \> 50) |
| DecayDescriptor  | None                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> tau+ mu-]cc' ]                                                                                                                                                                                                         |
| Output           | Phys/B2XTau_TauMu_piSS/Particles                                                                                                                                                                                                      |

TisTosParticleTagger/B2XTau_TauMu_piSS_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS' ]                    |
| DecayDescriptor | None                                              |
| Output          | Phys/B2XTau_TauMu_piSS_TOSLine/Particles          |
| TisTosSpecs     | { 'Hlt2(TopoMu\|SingleMuon).\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo5_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo6_B2XTau_TauMu_piSS_TOSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_TauMu_piSS_TOSLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_piSS_TOSLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo7_B2XTau_TauMu_piSS_TOSLine/Particles |
