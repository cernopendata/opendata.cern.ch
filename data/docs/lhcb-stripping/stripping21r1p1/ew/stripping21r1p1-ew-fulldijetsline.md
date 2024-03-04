[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingFullDiJetsLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/FullDiJetsLine/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 0.050000000                   |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionEW

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & ~ALG_PASSED('StrippingStreamEWBadEvent') |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdJets_Particles

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdJets](./stripping21r1p1-commonparticles-stdjets)/Particles',True)\>0 |

CombineParticles/FullDiJetsLine

|                  |                                                                   |
|------------------|-------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdJets](./stripping21r1p1-commonparticles-stdjets)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 20000.0 ) ' }                 |
| CombinationCut   | AALLSAMEBPV                                                       |
| MotherCut        | ALL                                                               |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                                          |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                                  |
| Output           | Phys/FullDiJetsLine/Particles                                     |
