[[stripping21 lines]](./stripping21-index)

# StrippingJetsMB

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/JetsMB/Particles            |
| Postscale      | 1.0000000                        |
| HLT            | HLT_PASS('Hlt1MBNoBiasDecision') |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21-stdjets) /Particles')\>0 |

**FilterDesktop/JetsMB**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (PT \> 15000.0)                                 |
| Inputs          | [ 'Phys/ [StdJets](./stripping21-stdjets) ' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/JetsMB/Particles                           |
