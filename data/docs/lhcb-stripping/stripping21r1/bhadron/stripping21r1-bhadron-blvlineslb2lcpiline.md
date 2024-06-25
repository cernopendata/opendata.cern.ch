[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBLVLinesLb2LcpiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/BLVLinesLb2LcpiLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/BLVLinesLb2LcpiLine

|                  |                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21r1-commonparticles-stdlooselambdac2pkpi)' , 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                             |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('Lambda_b0')\<400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                  |
| MotherCut        | (ADMASS('Lambda_b0') \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                          |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ pi-]cc' , '[Lambda_b0 -\> Lambda_c+ pi+]cc' ]                                                                                                                               |
| Output           | Phys/BLVLinesLb2LcpiLine/Particles                                                                                                                                                                            |
