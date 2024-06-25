[[stripping21 lines]](./stripping21-index)

# StrippingDisplVerticesLinesJetHltSingleHighMass

## Properties:

|                |                                                       |
|----------------|-------------------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesJetHltSingleHighMass/Particles |
| Postscale      | 1.0000000                                             |
| HLT            | None                                                  |
| Prescale       | 1.0000000                                             |
| L0DU           | None                                                  |
| ODIN           | None                                                  |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/DisplVerticesLinesHltCandidates

GaudiSequencer/DisplVerticesLinesHlt2CandFilterTCK0x001c0028-0x002f002c

LoKi::HDRFilter/DisplVerticesLinesHltDecisionFilterTCK0x001c0028-0x002f002c

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x001c0028, HLT_TCK % 0x40000000 , 0x002f002c ) & ( HLT_PASS('Hlt2DisplVerticesSingleDecision') ) |

HltVertexConverterS20p3/DisplVerticesLinesHltConverter0x001c0028-0x002f002c

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ ]                                     |
| DecayDescriptor | None                                      |
| Output          | Phys/DisplVerticesLinesHlt2Cand/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/DisplVerticesLinesHlt2CandFilterTCK0x00340032-0x00730035

LoKi::HDRFilter/DisplVerticesLinesHltDecisionFilterTCK0x00340032-0x00730035

|      |                                                                                                                                                                                                                                                                                   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00340032, HLT_TCK % 0x40000000 , 0x00730035 ) & ( HLT_PASS('Hlt2DisplVerticesHighFDSingleDecision') \| HLT_PASS('Hlt2DisplVerticesHighMassSingleDecision') \| HLT_PASS('Hlt2DisplVerticesLowMassSingleDecision') \| HLT_PASS('Hlt2DisplVerticesSingleDownDecision') ) |

HltVertexConverterS20p3/DisplVerticesLinesHltConverter0x00340032-0x00730035

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ ]                                     |
| DecayDescriptor | None                                      |
| Output          | Phys/DisplVerticesLinesHlt2Cand/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/DisplVerticesLinesHlt2CandFilterTCK0x00750037-0x007b0038

LoKi::HDRFilter/DisplVerticesLinesHltDecisionFilterTCK0x00750037-0x007b0038

|      |                                                                                                                                                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00750037, HLT_TCK % 0x40000000 , 0x007b0038 ) & ( HLT_PASS('Hlt2DisplVerticesSingleDecision') \| HLT_PASS('Hlt2DisplVerticesSingleDownDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighFDPostScaledDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighMassPostScaledDecision') ) |

HltVertexConverterS20p3/DisplVerticesLinesHltConverter0x00750037-0x007b0038

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ ]                                     |
| DecayDescriptor | None                                      |
| Output          | Phys/DisplVerticesLinesHlt2Cand/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/DisplVerticesLinesHlt2CandFilterTCK0x007e0039-0x0097003d

LoKi::HDRFilter/DisplVerticesLinesHltDecisionFilterTCK0x007e0039-0x0097003d

|      |                                                                                                                                                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x007e0039, HLT_TCK % 0x40000000 , 0x0097003d ) & ( HLT_PASS('Hlt2DisplVerticesSingleDecision') \| HLT_PASS('Hlt2DisplVerticesSingleDownDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighFDPostScaledDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighMassPostScaledDecision') ) |

HltVertexConverterS20p3/DisplVerticesLinesHltConverter0x007e0039-0x0097003d

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ ]                                     |
| DecayDescriptor | None                                      |
| Output          | Phys/DisplVerticesLinesHlt2Cand/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/DisplVerticesLinesHlt2CandFilterTCK0x00990042-0x40000000

LoKi::HDRFilter/DisplVerticesLinesHltDecisionFilterTCK0x00990042-0x40000000

|      |                                                                                                                                                                                                                                                                                                                                     |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00990042, HLT_TCK % 0x40000000 , 0x40000000 ) & ( HLT_PASS('Hlt2DisplVerticesSingleDecision') \| HLT_PASS('Hlt2DisplVerticesSingleDownDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighFDDecision') \| HLT_PASS('Hlt2DisplVerticesSingleHighMassDecision') \| HLT_PASS('Hlt2DisplVerticesSingleVeryHighFDDecision') ) |

HltVertexConverterS20p3/DisplVerticesLinesHltConverter0x00990042-0x40000000

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ ]                                     |
| DecayDescriptor | None                                      |
| Output          | Phys/DisplVerticesLinesHlt2Cand/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_DisplVerticesLinesHlt2Cand_Particles

|      |                                                          |
|------|----------------------------------------------------------|
| Code | CONTAINS('Phys/DisplVerticesLinesHlt2Cand/Particles')\>0 |

VeloEventShapeCutsS20p3/DisplVerticesLinesHltVeloGEC

FilterDesktop/DisplVerticesLinesHlt2CandVertices

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | ( ABSID == '~chi_10' )                            |
| Inputs          | [ 'Phys/DisplVerticesLinesHlt2Cand' ]           |
| DecayDescriptor | None                                              |
| Output          | Phys/DisplVerticesLinesHlt2CandVertices/Particles |

DisplacedVertexJetCandidateMakerS20p3/DisplVerticesLinesJetHltSingleHighMassSelectionHltJets

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesHlt2CandVertices' ]                       |
| DecayDescriptor | None                                                                  |
| Output          | Phys/DisplVerticesLinesJetHltSingleHighMassSelectionHltJets/Particles |

FilterDesktop/DisplVerticesLinesJetHltSingleHighMass

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ISLLP & ( NINTREE(ISJET) \>= 2 ) & ( MM \> 0.0 )                    |
| Inputs          | [ 'Phys/DisplVerticesLinesJetHltSingleHighMassSelectionHltJets' ] |
| DecayDescriptor | ~chi_10                                                             |
| Output          | Phys/DisplVerticesLinesJetHltSingleHighMass/Particles               |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesJetHltSingleHighMass

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetHltSingleHighMass' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesJetHltSingleHighMass/Particles |
