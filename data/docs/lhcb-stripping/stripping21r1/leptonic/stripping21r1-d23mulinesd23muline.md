[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD23MuLinesD23MuLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/D23MuLinesD23MuLine/Particles |
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

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21r1-stdloosemuons) /Particles')\>0 |

**DaVinci::N3BodyDecays/D23MuLinesD23MuLine**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1-stdloosemuons) ' ]                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS(1920\*MeV) \< 150\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                 |
| MotherCut        | (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 0.1\*ps)                                                  |
| DecayDescriptor  | None                                                                                                                                                             |
| DecayDescriptors | [ '[D+ -\> mu+ mu+ mu-]cc' , '[D+ -\> mu+ mu+ mu+]cc' ]                                                                                                    |
| Output           | Phys/D23MuLinesD23MuLine/Particles                                                                                                                               |
