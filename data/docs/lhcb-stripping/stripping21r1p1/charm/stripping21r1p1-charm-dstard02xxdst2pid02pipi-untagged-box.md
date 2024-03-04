[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingDstarD02xxDst2PiD02pipi_untagged_Box

## Properties:

|                |                                                     |
|----------------|-----------------------------------------------------|
| OutputLocation | Phys/DstarD02xxDst2PiD02pipi_untagged_Box/Particles |
| Postscale      | 1.0000000                                           |
| HLT1           | None                                                |
| HLT2           | HLT_PASS_RE('Hlt2Dst2PiD02PiPi\*Decision')          |
| Prescale       | 1.0000000                                           |
| L0DU           | None                                                |
| ODIN           | None                                                |

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

CombineParticles/DstarD02xxDst2PiD02pipi_untagged_Box

|                  |                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (AMAXDOCA('')\< 0.1 \*mm) & (ADAMASS('D0')\< 70.0 \*MeV) & (AMAXCHILD(PT)\>1100.0 \*MeV) & (APT\> 1800.0)                                                                                                                                                          |
| MotherCut        | (BPVDIRA\> 0.9997) & (INGENERATION( (MIPCHI2DV(PRIMARY)\>8),1 ) ) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                 |
| DecayDescriptor  | D0 -\> pi+ pi-                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi+ pi- ' ]                                                                                                                                                                                                                                            |
| Output           | Phys/DstarD02xxDst2PiD02pipi_untagged_Box/Particles                                                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_DstarD02xxDst2PiD02pipi_untagged_Box

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02pipi_untagged_Box' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/RelatedInfo1_DstarD02xxDst2PiD02pipi_untagged_Box/Particles |

AddRelatedInfo/RelatedInfo2_DstarD02xxDst2PiD02pipi_untagged_Box

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02pipi_untagged_Box' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/RelatedInfo2_DstarD02xxDst2PiD02pipi_untagged_Box/Particles |

AddRelatedInfo/RelatedInfo3_DstarD02xxDst2PiD02pipi_untagged_Box

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02pipi_untagged_Box' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/RelatedInfo3_DstarD02xxDst2PiD02pipi_untagged_Box/Particles |

AddRelatedInfo/RelatedInfo4_DstarD02xxDst2PiD02pipi_untagged_Box

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02pipi_untagged_Box' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/RelatedInfo4_DstarD02xxDst2PiD02pipi_untagged_Box/Particles |

AddRelatedInfo/RelatedInfo5_DstarD02xxDst2PiD02pipi_untagged_Box

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02pipi_untagged_Box' ]                |
| DecayDescriptor | None                                                             |
| Output          | Phys/RelatedInfo5_DstarD02xxDst2PiD02pipi_untagged_Box/Particles |
