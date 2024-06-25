[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBLVLinesB2LcpLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/BLVLinesB2LcpLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 0.20000000                       |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/BLVLinesB2LcpLine

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)' , 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'p+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)& (PIDp\>5)' , 'p~-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)& (PIDp\>5)' } |
| CombinationCut   | (ADAMASS(5323\*MeV) \< 400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                                       |
| MotherCut        | (ADMASS(5323\*MeV) \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[B0 -\> Lambda_c+ p~-]cc' , '[B0 -\> Lambda_c+ p+]cc' ]                                                                                                                                                                   |
| Output           | Phys/BLVLinesB2LcpLine/Particles                                                                                                                                                                                                   |
