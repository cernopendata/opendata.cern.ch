[[stripping21 lines]](./stripping21-index)

# StrippingB2TwoBaryonsBs2LambdabarLambda

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2TwoBaryonsBs2LambdabarLambda/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/Lambda0LLBLines

|                 |                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0')\<15.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ]                                                      |
| DecayDescriptor | None                                                                                                                                 |
| Output          | Phys/Lambda0LLBLines/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

FilterDesktop/Lambda0DDBLines

|                 |                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>8000.0\*MeV)&(ADMASS('Lambda0')\<20.0\*MeV)&(VFASPF(VCHI2)\<12.0) &(VFASPF(VMINVDDV(PRIMARY))\>300.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' ]                                             |
| DecayDescriptor | None                                                                                                                        |
| Output          | Phys/Lambda0DDBLines/Particles                                                                                              |

CombineParticles/B2TwoBaryonsBs2LambdabarLambda

|                  |                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0DDBLines' , 'Phys/Lambda0LLBLines' ]                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                                    |
| CombinationCut   | (ADAMASS(5.1\*GeV)\<1.1\*700.0)& (APT\>2000.0)& (ADOCAMAX('')\<5.0)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16)&(ADMASS(5.1\*GeV)\<700.0)& (BPVVDCHI2 \> 4)& (BPVIPCHI2()\< 25)& (BPVDIRA \> 0.9) |
| DecayDescriptor  | [B_s0 -\> Lambda0 Lambda~0]cc                                                                            |
| DecayDescriptors | [ '[B_s0 -\> Lambda0 Lambda~0]cc' ]                                                                    |
| Output           | Phys/B2TwoBaryonsBs2LambdabarLambda/Particles                                                              |
