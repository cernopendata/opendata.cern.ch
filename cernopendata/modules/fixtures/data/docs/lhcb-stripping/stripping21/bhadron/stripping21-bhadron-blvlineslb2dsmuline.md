[[stripping21 lines]](./stripping21-index)

# StrippingBLVLinesLb2DsmuLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/BLVLinesLb2DsmuLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/BLVLinesLb2DsmuLine

|                  |                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)' , 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : "ADMASS('D_s+') \< 100\*MeV" , 'D_s-' : "ADMASS('D_s+') \< 100\*MeV" , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('Lambda_b0')\<400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                                                     |
| MotherCut        | (ADMASS('Lambda_b0') \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Lambda_b0 -\> D_s+ mu-]cc' , '[Lambda_b0 -\> D_s+ mu+]cc' ]                                                                                                                                                                            |
| Output           | Phys/BLVLinesLb2DsmuLine/Particles                                                                                                                                                                                                               |
