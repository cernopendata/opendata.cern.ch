[[stripping21 lines]](./stripping21-index)

# StrippingDY2MuMuLine4

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/DY2MuMuLine4/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

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

**CombineParticles/DY2MuMuLine4**

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>10.0\*GeV) & (PT\>3.0\*GeV) & (TRPCHI2\>0.001)' , 'mu-' : '(P\>10.0\*GeV) & (PT\>3.0\*GeV) & (TRPCHI2\>0.001)' } |
| CombinationCut   | ATRUE                                                                                                                                        |
| MotherCut        | (MM\>20.0\*GeV) & (MM\<40.0\*GeV)                                                                                                            |
| DecayDescriptor  | Z0 -\> mu+ mu-                                                                                                                               |
| DecayDescriptors | [ 'Z0 -\> mu+ mu-' ]                                                                                                                       |
| Output           | Phys/DY2MuMuLine4/Particles                                                                                                                  |
