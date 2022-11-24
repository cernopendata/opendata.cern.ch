[[stripping21r1 lines]](./stripping21r1-index)

# StrippingJetsDiffractive

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/JetsDiffractive/Particles     |
| Postscale      | 1.0000000                          |
| HLT            | HLT_PASS_RE('Hlt2Topo.\*Decision') |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingJetsDiffractiveVOIDFilter**

|      |                                                                                                                              |
|------|------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummary(LHCb.RecSummary.nPVs, 'Rec/Vertex/Primary')\<2)& (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1-stdjets) /Particles')\>0 |

**FilterDesktop/JetsDiffractive**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (PT \> 15000.0)                                   |
| Inputs          | [ 'Phys/ [StdJets](./stripping21r1-stdjets) ' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/JetsDiffractive/Particles                    |
