[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBLVLinesLb2DmuLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/BLVLinesLb2DmuLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/BLVLinesLb2DmuLine

|                  |                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)' , 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : "ADMASS('D+') \< 100\*MeV" , 'D-' : "ADMASS('D+') \< 100\*MeV" , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('Lambda_b0')\<400\*MeV) & (AMAXDOCA('') \< 0.3\*mm)                                                                                                                                                                             |
| MotherCut        | (ADMASS('Lambda_b0') \< 400\*MeV ) & (BPVIPCHI2() \< 25) & (BPVVDCHI2 \> 225) & (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA \> 0.0) & (BPVLTIME() \> 1.0\*ps)                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[Lambda_b0 -\> D+ mu-]cc' , '[Lambda_b0 -\> D+ mu+]cc' ]                                                                                                                                                                        |
| Output           | Phys/BLVLinesLb2DmuLine/Particles                                                                                                                                                                                                        |
