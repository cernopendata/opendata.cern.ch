[[stripping21 lines]](./stripping21-index)

# StrippingBLVLinesB2DpiLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/BLVLinesB2DpiLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 0.10000000                       |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/BLVLinesB2DpiLine

|                  |                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : "ADMASS('D+') \< 100\*MeV" , 'D-' : "ADMASS('D+') \< 100\*MeV" , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('B0') \< 400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                                                  |
| MotherCut        | (ADMASS('B0') \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B0 -\> D- pi+]cc' ]                                                                                                                                                                                                              |
| Output           | Phys/BLVLinesB2DpiLine/Particles                                                                                                                                                                                                         |
