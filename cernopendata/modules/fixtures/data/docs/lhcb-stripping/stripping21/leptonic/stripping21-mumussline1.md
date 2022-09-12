[[stripping21 lines]](./stripping21-index)

# StrippingMuMuSSLine1

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/MuMuSSLine1/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 0.10000000                 |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**CombineParticles/MuMuSSLine1**

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV)' , 'mu-' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV)' } |
| CombinationCut   | ATRUE                                                                                                  |
| MotherCut        | (MM\>3.2\*GeV) & (MM\<5.0\*GeV)                                                                        |
| DecayDescriptor  | [Z0 -\> mu- mu-]cc                                                                                   |
| DecayDescriptors | [ '[Z0 -\> mu- mu-]cc' ]                                                                           |
| Output           | Phys/MuMuSSLine1/Particles                                                                             |
