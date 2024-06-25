[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingGluinosJetsSixJetsLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/GluinosJetsSixJetsLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:GluinosJetsSixJetsLine

GaudiSequencer/MERGEDINPUTS:GluinosJetsSixJetsLine

GaudiSequencer/INPUT:GluinosJetsSixJetSelection

LoKi::VoidFilter/SELECT:Phys/StdJets

|      |                           |
|------|---------------------------|
| Code | 0StdJets/Particles',True) |

FilterDesktop/GluinosJetslooseJets

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT \> 20000.0)                                                   |
| Inputs          | [ 'Phys/[StdJets](./stripping21r0p2-commonparticles-stdjets)' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/GluinosJetslooseJets/Particles                               |

LoKi::VoidFilter/GluinosJetsSixJetSelection

|      |                   |
|------|-------------------|
| Code | (lightJets \>= 6) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/GluinosJetsSixJetsLine

|                 |                                       |
|-----------------|---------------------------------------|
| Code            | ALL                                   |
| Inputs          | [ 'Phys/GluinosJetslooseJets' ]     |
| DecayDescriptor | None                                  |
| Output          | Phys/GluinosJetsSixJetsLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
