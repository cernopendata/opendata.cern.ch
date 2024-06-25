[[stripping21r1 lines]](./stripping21r1-index)

# StrippingJetsDiJet20_T6PS

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/JetsDiJet20_T6PS/Particles    |
| Postscale      | 1.0000000                          |
| HLT            | HLT_PASS_RE('Hlt2Topo.\*Decision') |
| Prescale       | 1.0000000                          |
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

CombineParticles/JetsDiJet20_T6PS

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/JetsbJets' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : '(PT \> 17000.0)' }                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CombinationCut   | (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),2))\<1e-6) & (COSDPHI \< -0.8) & (( (ACHILD(PINFO(9990,0),1)\>0) & (ACHILD(PINFO(9990,0),2)\>-1)) \| ((ACHILD(PINFO(9990,0),2)\>0) & (ACHILD(PINFO(9990,0),1)\>-1))) & (( (ACHILD(PINFO(9991,0),1)\>15) & (ACHILD(PINFO(9991,0),2)\>-1)) \| ((ACHILD(PINFO(9991,0),2)\>15) & (ACHILD(PINFO(9991,0),1)\>-1))) & (( (ACHILD(PINFO(9990,0),1)\>0) & (ACHILD(PINFO(9991,0),2)\>15)) \| ((ACHILD(PINFO(9990,0),2)\>15) & (ACHILD(PINFO(9991,0),1)\>0))) |
| MotherCut        | INTREE((ABSID=='CELLjet')&(PT\>0))                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/JetsDiJet20_T6PS/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
