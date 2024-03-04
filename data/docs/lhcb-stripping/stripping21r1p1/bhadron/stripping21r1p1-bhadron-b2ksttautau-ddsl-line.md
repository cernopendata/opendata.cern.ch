[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2KstTauTau_DDSL_Line

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2KstTauTau_DDSL_Line/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KstTauTau_DDSL_LineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsDForB2KstTauTau

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 4) & (TRGHOSTPROB \< 0.4) & (PROBNNpi \> 0.55) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                   |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/PionsDForB2KstTauTau/Particles                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsDForB2KstTauTau

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 4) & (TRGHOSTPROB \< 0.4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                              |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KaonsDForB2KstTauTau/Particles                                                                        |

CombineParticles/DForB2KstTauTau

|                  |                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsDForB2KstTauTau' , 'Phys/PionsDForB2KstTauTau' ]                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                              |
| CombinationCut   | (((AM \> 1840\*MeV) & (AM \< 1900\*MeV)) \| ((AM \> 1938\*MeV) & (AM \< 1998\*MeV))) & (APT \> 800\*MeV) & (AMAXDOCA('') \<0.2\*mm) & (ANUM(PT \> 800\*MeV) \>= 1)                        |
| MotherCut        | (PT \> 1000\*MeV) & (BPVDIRA \>0.99) & (VFASPF(VCHI2) \< 16)& (BPVVDCHI2 \> 16) & (BPVVDRHO \> 0.1\*mm) & (BPVVDRHO \< 7.0\*mm) & (BPVVDZ \> 5.0\*mm) & (M\>1800.\*MeV) & (M\<2030.\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                      |
| DecayDescriptors | [ '[D+ -\> pi+ K- pi+]cc' , '[D+ -\> K+ K- pi+]cc' ]                                                                                                                                |
| Output           | Phys/DForB2KstTauTau/Particles                                                                                                                                                            |

LoKi::VoidFilter/SelFilterPhys_StdTightMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightMuons](./stripping21r1p1-commonparticles-stdtightmuons)/Particles',True)\>0 |

FilterDesktop/MuonsForB2KstTauTau

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (TRCHI2DOF \< 4)                                          |
| Inputs          | [ 'Phys/[StdTightMuons](./stripping21r1p1-commonparticles-stdtightmuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MuonsForB2KstTauTau/Particles                                            |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)/Particles',True)\>0 |

CombineParticles/KstarB2KstTauTau

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' , 'Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'K-' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'pi+' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' , 'pi-' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' } |
| CombinationCut   | (AM \> 700\*MeV) & (AM \< 1100\*MeV)                                                                                                                                                                               |
| MotherCut        | (PT \> 1000\*MeV) &(BPVVD \> 3) & (VFASPF(VCHI2) \< 15)                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                 |
| Output           | Phys/KstarB2KstTauTau/Particles                                                                                                                                                                                    |

CombineParticles/B2KstTauTau_DDSL_Line

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DForB2KstTauTau' , 'Phys/KstarB2KstTauTau' , 'Phys/MuonsForB2KstTauTau' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM \> 2000\*MeV) & (AM \< 10000\*MeV)                                                                                    |
| MotherCut        | (VFASPF(VCHI2) \< 150) & (BPVVD \> 3) & (BPVVD \< 70)                                                                     |
| DecayDescriptor  | None                                                                                                                      |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 D+ mu-]cc' ]                                                                                     |
| Output           | Phys/B2KstTauTau_DDSL_Line/Particles                                                                                      |

AddRelatedInfo/RelatedInfo1_B2KstTauTau_DDSL_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_DDSL_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2KstTauTau_DDSL_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KstTauTau_DDSL_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_DDSL_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_B2KstTauTau_DDSL_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KstTauTau_DDSL_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_DDSL_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_B2KstTauTau_DDSL_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KstTauTau_DDSL_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_DDSL_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_B2KstTauTau_DDSL_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2KstTauTau_DDSL_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_DDSL_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_B2KstTauTau_DDSL_Line/Particles |
