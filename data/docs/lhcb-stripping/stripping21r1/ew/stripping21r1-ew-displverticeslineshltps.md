[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDisplVerticesLinesHLTPS

## Properties:

|                |            |
|----------------|------------|
| OutputLocation | None       |
| Postscale      | 1.0000000  |
| HLT            | None       |
| Prescale       | 0.20000000 |
| L0DU           | None       |
| ODIN           | None       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/DisplVerticesLinesHLTPS

LoKi::HDRFilter/DisplVerticesLinesHLTPSHltFilterTCK0x001c0028-0x002f002c

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x001c0028, HLT_TCK % 0x40000000, 0x002f002c ) & ( HLT_PASS_RE('Hlt2DisplVerticesSinglePostScaledDecision') ) |

LoKi::HDRFilter/DisplVerticesLinesHLTPSHltFilterTCK0x00340032-0x00730035

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00340032, HLT_TCK % 0x40000000, 0x00730035 ) & ( HLT_PASS_RE('Hlt2DisplVerticesSinglePostScaledDecision') ) |

LoKi::HDRFilter/DisplVerticesLinesHLTPSHltFilterTCK0x00750037-0x007b0038

|      |                                                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00750037, HLT_TCK % 0x40000000, 0x007b0038 ) & ( HLT_PASS_RE('Hlt2DisplVertices(Single\|Double\|SingleMV)PostScaledDecision') ) |

LoKi::HDRFilter/DisplVerticesLinesHLTPSHltFilterTCK0x007e0039-0x0097003d

|      |                                                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x007e0039, HLT_TCK % 0x40000000, 0x0097003d ) & ( HLT_PASS_RE('Hlt2DisplVertices(Single\|Double\|SingleMV)PostScaledDecision') ) |

LoKi::HDRFilter/DisplVerticesLinesHLTPSHltFilterTCK0x00990042-0x40000000

|      |                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------|
| Code | in_range( 0x00990042, HLT_TCK % 0x40000000, 0x40000000 ) & ( HLT_PASS_RE('Hlt2DisplVertices(Single\|SingleLoose\|Double)PSDecision') ) |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |
