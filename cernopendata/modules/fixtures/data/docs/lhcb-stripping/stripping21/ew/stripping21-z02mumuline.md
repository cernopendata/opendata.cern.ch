[[stripping21 lines]](./stripping21-index)

# StrippingZ02MuMuLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/Z02MuMuLine/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**CombineParticles/Z02MuMuLine**

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT\>3.0\*GeV)' , 'mu-' : '(PT\>3.0\*GeV)' } |
| CombinationCut   | ATRUE                                                                |
| MotherCut        | (MM\>40.0\*GeV)                                                      |
| DecayDescriptor  | Z0 -\> mu+ mu-                                                       |
| DecayDescriptors | [ 'Z0 -\> mu+ mu-' ]                                               |
| Output           | Phys/Z02MuMuLine/Particles                                           |
