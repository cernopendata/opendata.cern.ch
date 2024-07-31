[[stripping21 lines]](./stripping21-index)

# StrippingDY2MuMuLine1

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/DY2MuMuLine1/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 0.050000000                 |
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

**CombineParticles/DY2MuMuLine1**

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV) & (TRPCHI2\>0.001) & ((PIDmu-PIDpi)\>-3.0)' , 'mu-' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV) & (TRPCHI2\>0.001) & ((PIDmu-PIDpi)\>-3.0)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                        |
| MotherCut        | (MM\>3.2\*GeV) & (MM\<5.0\*GeV)                                                                                                                                                              |
| DecayDescriptor  | Z0 -\> mu+ mu-                                                                                                                                                                               |
| DecayDescriptors | [ 'Z0 -\> mu+ mu-' ]                                                                                                                                                                       |
| Output           | Phys/DY2MuMuLine1/Particles                                                                                                                                                                  |
