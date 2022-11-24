[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingHighPtMuonsZ02MuMuNoPIDsLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/HighPtMuonsZ02MuMuNoPIDsLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsMuons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsMuons /Particles',True) |

**CombineParticles/HighPtMuonsZ02MuMuNoPIDsLine**

|                  |                                                                         |
|------------------|-------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllNoPIDsMuons](./stripping21r1p2-stdallnopidsmuons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT\>3000.0)' , 'mu-' : '(PT\>3000.0)' }        |
| CombinationCut   | ATRUE                                                                   |
| MotherCut        | (MM\>40000.0) & ((CHILDCUT(ISMUON,1))\|(CHILDCUT(ISMUON,2)))            |
| DecayDescriptor  | Z0 -\> mu+ mu-                                                          |
| DecayDescriptors | [ 'Z0 -\> mu+ mu-' ]                                                  |
| Output           | Phys/HighPtMuonsZ02MuMuNoPIDsLine/Particles                             |
