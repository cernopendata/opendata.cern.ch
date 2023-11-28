[[stripping21 lines]](./stripping21-index)

# StrippingBLVLinesB2LcmuLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/BLVLinesB2LcmuLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/BLVLinesB2LcmuLine

|                  |                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)' , 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS(5323\*MeV) \< 400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                  |
| MotherCut        | (ADMASS(5323\*MeV) \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> Lambda_c+ mu-]cc' , '[B0 -\> Lambda_c+ mu+]cc' ]                                                                                                                                             |
| Output           | Phys/BLVLinesB2LcmuLine/Particles                                                                                                                                                                             |
