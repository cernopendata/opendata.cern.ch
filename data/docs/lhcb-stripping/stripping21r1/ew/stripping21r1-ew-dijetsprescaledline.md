[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDijetsPrescaledLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/DijetsPrescaledLine/Particles      |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS_RE('Hlt1TrackMuon.\*Decision') |
| Prescale       | 0.030000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingDijetsPrescaledLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_PFParticles_Particles

|      |                                           |
|------|-------------------------------------------|
| Code | CONTAINS('Phys/PFParticles/Particles')\>0 |

LoKi::PFJetMaker/DijetsJetsSelection

|                 |                                    |
|-----------------|------------------------------------|
| Inputs          | [ 'Phys/PFParticles' ]           |
| DecayDescriptor | None                               |
| Output          | Phys/DijetsJetsSelection/Particles |

CombineParticles/DijetsPrescaledLine

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/DijetsJetsSelection' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : 'PT \> 19000.0' } |
| CombinationCut   | COSDPHI \< -0.8                              |
| MotherCut        | ALL                                          |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                     |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]             |
| Output           | Phys/DijetsPrescaledLine/Particles           |
