[[stripping21r1 lines]](./stripping21r1-index)

# StrippingJetsbJetPT15

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/JetsbJetPT15/Particles        |
| Postscale      | 1.0000000                          |
| HLT            | HLT_PASS_RE('Hlt2Topo.\*Decision') |
| Prescale       | 0.0050000000                       |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqJetsmerged

GaudiSequencer/SEQ:Jets5000.0GeVJets

LoKi::VoidFilter/SelFilterPhys_StdJets_Particles

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdJets](./stripping21r1-commonparticles-stdjets)/Particles')\>0 |

FilterDesktop/Jets5000.0GeVJets

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | (PT \> 5000.0)                                                  |
| Inputs          | [ 'Phys/[StdJets](./stripping21r1-commonparticles-stdjets)' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/Jets5000.0GeVJets/Particles                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:JetsSvrsSelection

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/JetsTrksSelection

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 500.0) & (P \> 5000.0) & (MIPCHI2DV(PRIMARY) \> 16) & (TRGHP \< 0.4) & (PPINFO(705,-1) \< 0.7) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                   |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/JetsTrksSelection/Particles                                                                      |

CombineParticles/JetsSvrsSelection

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| Inputs           | [ 'Phys/JetsTrksSelection' ]                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | (ADOCACHI2CUT(8,'')) & (AM \< 7000.0) & (ASUM(PT) \> 2000.0) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100) & (VFASPF(VCHI2) \< 8)   |
| DecayDescriptor  | None                                                         |
| DecayDescriptors | [ 'D0 -\> pi- pi+' , 'D0 -\> pi- pi-' , 'D0 -\> pi+ pi+' ] |
| Output           | Phys/JetsSvrsSelection/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Jetsmerged

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | ALL                                                       |
| Inputs          | [ 'Phys/Jets5000.0GeVJets' , 'Phys/JetsSvrsSelection' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/Jetsmerged/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

TopologicalTagging/JetsbJets

|                 |                          |
|-----------------|--------------------------|
| Inputs          | [ 'Phys/Jetsmerged' ]  |
| DecayDescriptor | None                     |
| Output          | Phys/JetsbJets/Particles |

FilterDesktop/JetsbJetPT15

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | (ABSID=='CELLjet') & (PT\> 15000.0) & (PINFO(9990,-1)\>0) |
| Inputs          | [ 'Phys/JetsbJets' ]                                    |
| DecayDescriptor | None                                                      |
| Output          | Phys/JetsbJetPT15/Particles                               |
