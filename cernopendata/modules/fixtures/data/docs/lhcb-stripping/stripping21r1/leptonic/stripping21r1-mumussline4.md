[[stripping21r1 lines]](./stripping21r1-index)

# StrippingMuMuSSLine4

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/MuMuSSLine4/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**CombineParticles/MuMuSSLine4**

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>10.0\*GeV) & (PT\>3.0\*GeV)' , 'mu-' : '(P\>10.0\*GeV) & (PT\>3.0\*GeV)' } |
| CombinationCut   | ATRUE                                                                                                  |
| MotherCut        | (MM\>20.0\*GeV)                                                                                        |
| DecayDescriptor  | [Z0 -\> mu- mu-]cc                                                                                   |
| DecayDescriptors | [ '[Z0 -\> mu- mu-]cc' ]                                                                           |
| Output           | Phys/MuMuSSLine4/Particles                                                                             |
