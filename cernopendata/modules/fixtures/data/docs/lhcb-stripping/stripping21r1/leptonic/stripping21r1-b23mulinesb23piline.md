[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB23MuLinesB23PiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B23MuLinesB23PiLine/Particles |
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

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21r1-stdloosepions) /Particles')\>0 |

**DaVinci::N3BodyDecays/B23MuLinesB23PiLine**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLoosePions](./stripping21r1-stdloosepions) ' ]                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('B+') \< 100\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                      |
| MotherCut        | (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 0.0\*ps)                                                  |
| DecayDescriptor  | None                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                 |
| Output           | Phys/B23MuLinesB23PiLine/Particles                                                                                                                               |
