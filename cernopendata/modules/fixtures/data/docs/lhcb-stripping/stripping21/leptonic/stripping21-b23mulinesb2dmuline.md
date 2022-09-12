[[stripping21 lines]](./stripping21-index)

# StrippingB23MuLinesB2DMuLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B23MuLinesB2DMuLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**CombineParticles/MyD2MuMuSelection**

|                  |                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' ]                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV()\>1.0) & (TRCHI2DOF\<5.0) & (PT\>1.0\*GeV)' , 'mu-' : '(MIPCHI2DV()\>1.0) & (TRCHI2DOF\<5.0) & (PT\>1.0\*GeV)' } |
| CombinationCut   | (ADAMASS('D0') \< 110\*MeV)                                                                                                                          |
| MotherCut        | (ADMASS('D0') \< 100\*MeV) & (VFASPF(VCHI2)\<16) & (BPVLTIME(16) \> 0.1\*ps)                                                                         |
| DecayDescriptor  | None                                                                                                                                                 |
| DecayDescriptors | [ '[D0 -\> mu+ mu-]cc' , '[D0 -\> mu+ mu+]cc' ]                                                                                                |
| Output           | Phys/MyD2MuMuSelection/Particles                                                                                                                     |

**CombineParticles/B23MuLinesB2DMuLine**

|                  |                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MyD2MuMuSelection' , 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' ]                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D\~0' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                            |
| MotherCut        | (BPVVDCHI2 \> 25) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0)                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> D0 mu+]cc' ]                                                                                                                                                                      |
| Output           | Phys/B23MuLinesB2DMuLine/Particles                                                                                                                                                               |
