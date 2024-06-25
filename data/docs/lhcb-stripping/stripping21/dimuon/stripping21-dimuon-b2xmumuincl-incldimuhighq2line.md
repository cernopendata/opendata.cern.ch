[[stripping21 lines]](./stripping21-index)

# StrippingB2XMuMuIncl_InclDiMuHighQ2Line

## Properties:

|                |                                                                                                                                  |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2XMuMuIncl_InclDiMuHighQ2Line/Particles                                                                                    |
| Postscale      | 1.0000000                                                                                                                        |
| HLT            | HLT_PASS_RE('Hlt2DiMuonDetachedDecision')\|HLT_PASS_RE('Hlt2DiMuonDetachedHeavyDecision')\|HLT_PASS_RE('Hlt2SingleMuonDecision') |
| Prescale       | 1.0000000                                                                                                                        |
| L0DU           | None                                                                                                                             |
| ODIN           | None                                                                                                                             |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XMuMuIncl_InclDiMuHighQ2LineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/Selection_B2XMuMuIncl_HighQ2Muons

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (TRGHP \< 0.35) & (MIPCHI2DV(PRIMARY) \> 16.0) & (PIDmu\> 0.0) & (PIDmu-PIDK\> 0.0) & (PT \> 250) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                              |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/Selection_B2XMuMuIncl_HighQ2Muons/Particles                                                                       |

CombineParticles/B2XMuMuIncl_InclDiMuHighQ2Line

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMuIncl_HighQ2Muons' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                         |
| CombinationCut   | ATRUE                                                                                                  |
| MotherCut        | (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 100.0) & (VFASPF(VCHI2/VDOF) \< 4.0) & (M \> 3870.0) & (M \< 5800.0) |
| DecayDescriptor  | None                                                                                                   |
| DecayDescriptors | [ 'B0 -\> mu- mu+' ]                                                                                 |
| Output           | Phys/B2XMuMuIncl_InclDiMuHighQ2Line/Particles                                                          |
