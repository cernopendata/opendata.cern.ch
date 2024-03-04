[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingTaggedJetsEightJetLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/TaggedJetsEightJetLine/Particles |
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

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_BDTTagJets_Particles

|      |                                               |
|------|-----------------------------------------------|
| Code | CONTAINS('Phys/BDTTagJets/Particles',True)\>0 |

CombineParticles/TaggedJetsEightJetLine

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BDTTagJets' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : 'ALL' }                                               |
| CombinationCut   | ATRUE                                                                            |
| MotherCut        | ALL                                                                              |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet         |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet CELLjet' ] |
| Output           | Phys/TaggedJetsEightJetLine/Particles                                            |
