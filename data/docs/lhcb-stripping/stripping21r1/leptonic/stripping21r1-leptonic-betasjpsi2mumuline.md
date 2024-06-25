[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSJpsi2MuMuLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/BetaSJpsi2MuMuLine/Particles     |
| Postscale      | 1.0000000                             |
| HLT            | HLT_PASS_RE('Hlt2DiMuonJPsiDecision') |
| Prescale       | 0.14000000                            |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqBetaSJpsi2MuMuLine

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/BetaSJpsi2MuMuLine

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                     |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/BetaSJpsi2MuMuLine/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |
