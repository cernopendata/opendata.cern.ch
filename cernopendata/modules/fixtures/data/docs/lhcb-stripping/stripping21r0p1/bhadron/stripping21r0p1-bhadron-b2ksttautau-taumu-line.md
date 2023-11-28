[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2KstTauTau_TauMu_Line

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2KstTauTau_TauMu_Line/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KstTauTau_TauMu_LineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21r0p1-commonparticles-stdtightdetachedtau3pi)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdTightMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightMuons](./stripping21r0p1-commonparticles-stdtightmuons)/Particles',True)\>0 |

FilterDesktop/MuonsForB2KstTauTau

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (TRCHI2DOF \< 4)                                          |
| Inputs          | [ 'Phys/[StdTightMuons](./stripping21r0p1-commonparticles-stdtightmuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MuonsForB2KstTauTau/Particles                                            |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r0p1-commonparticles-stdnopidskaons)/Particles',True)\>0 |

CombineParticles/KstarB2KstTauTau

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' , 'Phys/[StdNoPIDsKaons](./stripping21r0p1-commonparticles-stdnopidskaons)' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'K-' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'pi+' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' , 'pi-' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' } |
| CombinationCut   | (AM \> 700\*MeV) & (AM \< 1100\*MeV)                                                                                                                                                                               |
| MotherCut        | (PT \> 1000\*MeV) &(BPVVD \> 3) & (VFASPF(VCHI2) \< 15)                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                 |
| Output           | Phys/KstarB2KstTauTau/Particles                                                                                                                                                                                    |

CombineParticles/B2KstTauTau_TauMu_Line

|                  |                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstarB2KstTauTau' , 'Phys/MuonsForB2KstTauTau' , 'Phys/[StdTightDetachedTau3pi](./stripping21r0p1-commonparticles-stdtightdetachedtau3pi)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                          |
| CombinationCut   | (AM \> 2000\*MeV) & (AM \< 10000\*MeV)                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2) \< 150) & (BPVVD \> 3) & (BPVVD \< 70)                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 tau+ mu-]cc' , '[B0 -\> K\*(892)0 tau- mu+]cc' ]                                                                            |
| Output           | Phys/B2KstTauTau_TauMu_Line/Particles                                                                                                                  |

AddRelatedInfo/RelatedInfo1_B2KstTauTau_TauMu_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_TauMu_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2KstTauTau_TauMu_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KstTauTau_TauMu_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_TauMu_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2KstTauTau_TauMu_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KstTauTau_TauMu_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_TauMu_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2KstTauTau_TauMu_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KstTauTau_TauMu_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_TauMu_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2KstTauTau_TauMu_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2KstTauTau_TauMu_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KstTauTau_TauMu_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_B2KstTauTau_TauMu_Line/Particles |
