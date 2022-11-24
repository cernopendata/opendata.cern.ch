[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD23MuLinesD23PiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/D23MuLinesD23PiLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 0.010000000                        |
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

**DaVinci::N3BodyDecays/D23MuLinesD23PiLine**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLoosePions](./stripping21r1-stdloosepions) ' ]                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS(1920\*MeV) \< 150\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                 |
| MotherCut        | (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 0.1\*ps)                                                  |
| DecayDescriptor  | None                                                                                                                                                             |
| DecayDescriptors | [ '[D+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                 |
| Output           | Phys/D23MuLinesD23PiLine/Particles                                                                                                                               |
