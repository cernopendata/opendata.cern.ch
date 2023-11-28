[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2KstTauTau_MuMu_SameSign_Line

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KstTauTau_MuMu_SameSign_Line/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KstTauTau_MuMu_SameSign_LineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightMuons](./stripping21r1p1-commonparticles-stdtightmuons)/Particles',True)\>0 |

FilterDesktop/MuonsKMMForB2KstTauTau

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 800\*MeV) & (TRCHI2DOF \< 4) &( MIPCHI2DV(PRIMARY) \> 4)               |
| Inputs          | [ 'Phys/[StdTightMuons](./stripping21r1p1-commonparticles-stdtightmuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MuonsKMMForB2KstTauTau/Particles                                         |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)/Particles',True)\>0 |

CombineParticles/Kstar_KMMB2KstTauTau

|                  |                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' , 'Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)' ]                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2) & (MIPCHI2DV(PRIMARY) \> 4))' , 'K-' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2) & (MIPCHI2DV(PRIMARY) \> 4))' , 'pi+' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5) & (MIPCHI2DV(PRIMARY) \> 4))' , 'pi-' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5) & (MIPCHI2DV(PRIMARY) \> 4))' } |
| CombinationCut   | (AM \> 700\*MeV) & (AM \< 1100\*MeV) & (AMAXDOCA('') \<0.15\*mm)                                                                                                                                                                                                                                                                   |
| MotherCut        | (PT \> 1000\*MeV) & (VFASPF(VCHI2) \< 15) & (MIPCHI2DV(PRIMARY) \> 3) & (BPVVDCHI2 \> 120)                                                                                                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Kstar_KMMB2KstTauTau/Particles                                                                                                                                                                                                                                                                                                |

CombineParticles/B2KstTauTau_MuMu_SameSign_Line

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kstar_KMMB2KstTauTau' , 'Phys/MuonsKMMForB2KstTauTau' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM \> 1500\*MeV) & (AM \< 10000\*MeV)                                                      |
| MotherCut        | (PT \> 2000\*MeV) &(VFASPF(VCHI2) \< 100) & (BPVVD \> 3) & (BPVDIRA \>0.999)                |
| DecayDescriptor  | None                                                                                        |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 mu+ mu+]cc' , '[B0 -\> K\*(892)0 mu- mu-]cc' ]                   |
| Output           | Phys/B2KstTauTau_MuMu_SameSign_Line/Particles                                               |

AddRelatedInfo/RelatedInfo1_B2KstTauTau_MuMu_SameSign_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_MuMu_SameSign_Line' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_B2KstTauTau_MuMu_SameSign_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KstTauTau_MuMu_SameSign_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_MuMu_SameSign_Line' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_B2KstTauTau_MuMu_SameSign_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KstTauTau_MuMu_SameSign_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_MuMu_SameSign_Line' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_B2KstTauTau_MuMu_SameSign_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KstTauTau_MuMu_SameSign_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_MuMu_SameSign_Line' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo4_B2KstTauTau_MuMu_SameSign_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2KstTauTau_MuMu_SameSign_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_MuMu_SameSign_Line' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo5_B2KstTauTau_MuMu_SameSign_Line/Particles |
