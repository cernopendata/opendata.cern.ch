[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB24pLinesB24pLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/B24pLinesB24pLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

DaVinci::N4BodyDecays/B24pLinesB24pLine

|                  |                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>0) & ((PIDp-PIDK)\>0)' , 'p~-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>0) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS(5323\*MeV) \< 500\*MeV) & (ADOCA(1,4) \< 0.3\*mm) & (ADOCA(2,4) \< 0.3\*mm) & (ADOCA(3,4) \< 0.3\*mm)                                                                                                                                |
| MotherCut        | (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> p+ p+ p~- p~-]cc' , '[B0 -\> p+ p+ p+ p~-]cc' ]                                                                                                                                                                              |
| Output           | Phys/B24pLinesB24pLine/Particles                                                                                                                                                                                                              |
