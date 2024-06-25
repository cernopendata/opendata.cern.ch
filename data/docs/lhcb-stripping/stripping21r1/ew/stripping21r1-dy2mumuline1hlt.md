[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDY2MuMuLine1Hlt

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/DY2MuMuLine1Hlt/Particles           |
| Postscale      | 1.0000000                                |
| HLT            | HLT_PASS_RE( 'Hlt2DiMuonDY.\*Decision' ) |
| Prescale       | 0.50000000                               |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**CombineParticles/DY2MuMuLine1Hlt**

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV) & (TRPCHI2\>0.001) & ((PIDmu-PIDpi)\>-3.0)' , 'mu-' : '(P\>10.0\*GeV) & (PT\>1.5\*GeV) & (TRPCHI2\>0.001) & ((PIDmu-PIDpi)\>-3.0)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                        |
| MotherCut        | (MM\>3.2\*GeV)                                                                                                                                                                               |
| DecayDescriptor  | Z0 -\> mu+ mu-                                                                                                                                                                               |
| DecayDescriptors | [ 'Z0 -\> mu+ mu-' ]                                                                                                                                                                       |
| Output           | Phys/DY2MuMuLine1Hlt/Particles                                                                                                                                                               |
