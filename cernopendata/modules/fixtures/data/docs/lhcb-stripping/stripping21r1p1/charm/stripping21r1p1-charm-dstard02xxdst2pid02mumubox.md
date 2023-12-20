[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingDstarD02xxDst2PiD02mumuBox

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/DstarD02xxDst2PiD02mumuBox/Particles  |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | HLT_PASS_RE('Hlt2Dst2PiD02MuMu\*Decision') |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

CombineParticles/DstarD02xxseq_D02mumuforTag_selection

|                  |                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'mu-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (AMAXDOCA('')\< 0.1 \*mm) & (DAMASS('D0')\< 300 \*MeV) & (DAMASS('D0')\> -150.0 \*MeV) & (AMAXCHILD(PT)\>1100.0 \*MeV) & (APT\> 1800.0)                                                                                                                            |
| MotherCut        | (BPVDIRA\> 0.9997) & (INGENERATION( (MIPCHI2DV(PRIMARY)\>8),1 ) ) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                 |
| DecayDescriptor  | D0 -\> mu+ mu-                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> mu+ mu- ' ]                                                                                                                                                                                                                                            |
| Output           | Phys/DstarD02xxseq_D02mumuforTag_selection/Particles                                                                                                                                                                                                               |

CombineParticles/DstarD02xxDst2PiD02mumuBox

|                  |                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarD02xxseq_D02mumuforTag_selection' , 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1p1-commonparticles-stdnopidsuppions)' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'PT\>0' , 'D~0' : 'PT\>0' , 'pi+' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' , 'pi-' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' } |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<300.0 \* MeV)                                                                                                                                                                                   |
| MotherCut        | (abs(M-MAXTREE('D0'==ABSID,M)-145.42) \< 10.0 ) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                                                                                                                                 |
| Output           | Phys/DstarD02xxDst2PiD02mumuBox/Particles                                                                                                                                                                               |

AddRelatedInfo/RelatedInfo1_DstarD02xxDst2PiD02mumuBox

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02mumuBox' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_DstarD02xxDst2PiD02mumuBox/Particles |

AddRelatedInfo/RelatedInfo2_DstarD02xxDst2PiD02mumuBox

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02mumuBox' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_DstarD02xxDst2PiD02mumuBox/Particles |

AddRelatedInfo/RelatedInfo3_DstarD02xxDst2PiD02mumuBox

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02mumuBox' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_DstarD02xxDst2PiD02mumuBox/Particles |

AddRelatedInfo/RelatedInfo4_DstarD02xxDst2PiD02mumuBox

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02mumuBox' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_DstarD02xxDst2PiD02mumuBox/Particles |

AddRelatedInfo/RelatedInfo5_DstarD02xxDst2PiD02mumuBox

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02mumuBox' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo5_DstarD02xxDst2PiD02mumuBox/Particles |
