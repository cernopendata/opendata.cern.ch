[[stripping21 lines]](./stripping21-index)

# StrippingBLVLinesBs2DspiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/BLVLinesBs2DspiLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 0.10000000                         |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDsplus2KKPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/BLVLinesBs2DspiLine

|                  |                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : "ADMASS('D_s+') \< 100\*MeV" , 'D_s-' : "ADMASS('D_s+') \< 100\*MeV" , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('B_s0') \< 400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                                                        |
| MotherCut        | (ADMASS('B_s0') \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[B_s0 -\> D_s- pi+]cc' ]                                                                                                                                                                                                                  |
| Output           | Phys/BLVLinesBs2DspiLine/Particles                                                                                                                                                                                                               |
