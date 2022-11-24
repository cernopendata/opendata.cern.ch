[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB23MuLinesB23MuLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B23MuLinesB23MuLine/Particles |
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

**DaVinci::N3BodyDecays/B23MuLinesB23MuLine**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1-stdloosemuons) ' ]                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('B+') \< 500\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                      |
| MotherCut        | (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 0.0\*ps)                                                  |
| DecayDescriptor  | None                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> mu+ mu+ mu-]cc' , '[B+ -\> mu+ mu+ mu+]cc' ]                                                                                                    |
| Output           | Phys/B23MuLinesB23MuLine/Particles                                                                                                                               |
