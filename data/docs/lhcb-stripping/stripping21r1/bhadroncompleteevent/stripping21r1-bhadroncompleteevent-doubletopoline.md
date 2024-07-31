[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDoubleTopoLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | None                               |
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

LoKi::VoidFilter/DoubleTopoLine

|      |                                            |
|------|--------------------------------------------|
| Code | ACCEPT('DoubleTopoTool/DoubleTopoLine_DT') |
