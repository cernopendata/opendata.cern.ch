[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDijetsLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/DijetsLine/Particles               |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS_RE('Hlt1TrackMuon.\*Decision') |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingDijetsLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/DijetsTrksSelection

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT \> 500.0) & (P \> 5000.0) & (MIPCHI2DV(PRIMARY) \> 16) & (TRGHP \< 0.4)         |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/DijetsTrksSelection/Particles                                                  |

CombineParticles/DijetsSvrsSelection

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| Inputs           | [ 'Phys/DijetsTrksSelection' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | (ADOCACHI2CUT(8,'')) & (AM \< 7000.0) & (ASUM(PT) \> 2000.0) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100) & (VFASPF(VCHI2) \< 8)   |
| DecayDescriptor  | None                                                         |
| DecayDescriptors | [ 'D0 -\> pi- pi+' , 'D0 -\> pi- pi-' , 'D0 -\> pi+ pi+' ] |
| Output           | Phys/DijetsSvrsSelection/Particles                           |

CombineParticles/DijetsDisvrsSelection

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DijetsSvrsSelection' ]                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' }                                                        |
| CombinationCut   | (COSDALPHA \< 0.99) & (COSDPHI \< 0) & (AM \> 2000.0) & (ASUM(SUMTREE(PT,(ISBASIC),0.0)) \> 10000.0) |
| MotherCut        | INTREE(HASMUON & ISMUON & (PT \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 16))                               |
| DecayDescriptor  | None                                                                                                 |
| DecayDescriptors | [ 'B0 -\> D0 D0' ]                                                                                 |
| Output           | Phys/DijetsDisvrsSelection/Particles                                                                 |

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

CombineParticles/DijetsLine

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| Inputs           | [ 'Phys/DijetsDisvrsSelection' , 'Phys/DijetsJetsSelection' ] |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : 'PT \> 19000.0' }                    |
| CombinationCut   | COSDPHI \< -0.8                                                 |
| MotherCut        | ALL                                                             |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                                        |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                                |
| Output           | Phys/DijetsLine/Particles                                       |
