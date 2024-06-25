[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingDstarD02xxDst2PiD02emuBox

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/DstarD02xxDst2PiD02emuBox/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r0p1-commonparticles-stdnopidsuppions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseElectrons_Particles

|      |                                                                                                                   |
|------|-------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseElectrons](./stripping21r0p1-commonparticles-stdalllooseelectrons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

CombineParticles/DstarD02xxseq_D02emuforTag_selection

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseElectrons](./stripping21r0p1-commonparticles-stdalllooseelectrons)' , 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'e-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'mu+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'mu-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (AMAXDOCA('')\< 0.1 \*mm) & (ADAMASS('D0')\< 300 \*MeV) & (AMAXCHILD(PT)\>1100.0 \*MeV) & (APT\> 1800.0)                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (BPVDIRA\> 0.9997) & (INGENERATION( (MIPCHI2DV(PRIMARY)\>8),1 ) ) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'D0 -\> e+ mu- ' , 'D0 -\> e- mu+ ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/DstarD02xxseq_D02emuforTag_selection/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

CombineParticles/DstarD02xxDst2PiD02emuBox

|                  |                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarD02xxseq_D02emuforTag_selection' , 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r0p1-commonparticles-stdnopidsuppions)' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'PT\>0' , 'D~0' : 'PT\>0' , 'pi+' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' , 'pi-' : '(PT\> 110.0 \* MeV) & ( MIPCHI2DV(PRIMARY)\< 10.0) & (TRCHI2DOF\<7.0) ' } |
| CombinationCut   | (ADAMASS('D\*(2010)+')\<300.0 \* MeV)                                                                                                                                                                                   |
| MotherCut        | (abs(M-MAXTREE('D0'==ABSID,M)-145.42) \< 10.0 ) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                                                                                                                                 |
| Output           | Phys/DstarD02xxDst2PiD02emuBox/Particles                                                                                                                                                                                |
