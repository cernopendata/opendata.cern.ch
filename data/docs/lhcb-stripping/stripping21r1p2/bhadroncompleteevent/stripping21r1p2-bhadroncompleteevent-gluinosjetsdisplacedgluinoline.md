[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingGluinosJetsDisplacedGluinoLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/GluinosJetsDisplacedGluinoLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

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

GaudiSequencer/MERGED:GluinosJetsDisplacedGluinoLine

GaudiSequencer/MERGEDINPUTS:GluinosJetsDisplacedGluinoLine

GaudiSequencer/INPUT:GluinosJetsDisplacedGluinoSelection

LoKi::VoidFilter/SELECT:Phys/StdJets

|      |                           |
|------|---------------------------|
| Code | 0StdJets/Particles',True) |

FilterDesktop/GluinosJetslooseJets

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT \> 20000.0)                                                   |
| Inputs          | [ 'Phys/[StdJets](./stripping21r1p2-commonparticles-stdjets)' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/GluinosJetslooseJets/Particles                               |

LoKi::VoidFilter/GluinosJetsDisplacedGluinoSelection

|      |                     |
|------|---------------------|
| Code | (DGluinoJets \>= 3) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/GluinosJetsDisplacedGluinoLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ALL                                           |
| Inputs          | [ 'Phys/GluinosJetslooseJets' ]             |
| DecayDescriptor | None                                          |
| Output          | Phys/GluinosJetsDisplacedGluinoLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
