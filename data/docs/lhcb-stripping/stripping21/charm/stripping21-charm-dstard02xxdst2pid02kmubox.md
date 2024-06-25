[[stripping21 lines]](./stripping21-index)

# StrippingDstarD02xxDst2PiD02KmuBox

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/DstarD02xxDst2PiD02KmuBox/Particles  |
| Postscale      | 1.0000000                                 |
| HLT            | HLT_PASS_RE('Hlt2Dst2PiD02KMu\*Decision') |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/DstarD02xxseq_D02KmuforTag_selection

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'mu+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'mu-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (AMAXDOCA('')\< 0.1 \*mm) & (ADAMASS('D0')\< 70.0 \*MeV) & (AMAXCHILD(PT)\>1100.0 \*MeV) & (APT\> 1800.0)                                                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (BPVDIRA\> 0.9997) & (INGENERATION( (MIPCHI2DV(PRIMARY)\>8),1 ) ) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'D0 -\> K+ mu- ' , 'D0 -\> K- mu+ ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/DstarD02xxseq_D02KmuforTag_selection/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

CombineParticles/DstarD02xxDst2PiD02KmuBox

|                  |                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarD02xxseq_D02KmuforTag_selection' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'PT\>0' , 'D~0' : 'PT\>0' , 'pi+' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' , 'pi-' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' } |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<300.0 \* MeV)                                                                                                                                                                                   |
| MotherCut        | (abs(M-MAXTREE('D0'==ABSID,M)-145.42) \< 10.0 ) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                                                                                                                                 |
| Output           | Phys/DstarD02xxDst2PiD02KmuBox/Particles                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_DstarD02xxDst2PiD02KmuBox

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02KmuBox' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_DstarD02xxDst2PiD02KmuBox/Particles |

AddRelatedInfo/RelatedInfo2_DstarD02xxDst2PiD02KmuBox

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02KmuBox' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_DstarD02xxDst2PiD02KmuBox/Particles |

AddRelatedInfo/RelatedInfo3_DstarD02xxDst2PiD02KmuBox

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02KmuBox' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_DstarD02xxDst2PiD02KmuBox/Particles |

AddRelatedInfo/RelatedInfo4_DstarD02xxDst2PiD02KmuBox

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02KmuBox' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_DstarD02xxDst2PiD02KmuBox/Particles |
