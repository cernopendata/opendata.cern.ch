[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingMicroDiJetsLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/MicroDiJetsLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 0.50000000                     |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_MDSTJets_Particles

|      |                                             |
|------|---------------------------------------------|
| Code | CONTAINS('Phys/MDSTJets/Particles',True)\>0 |

CombineParticles/MicroDiJetsLine

|                  |                                                   |
|------------------|---------------------------------------------------|
| Inputs           | [ 'Phys/MDSTJets' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 20000.0 ) ' } |
| CombinationCut   | AALLSAMEBPV                                       |
| MotherCut        | ALL                                               |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                          |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                  |
| Output           | Phys/MicroDiJetsLine/Particles                    |
