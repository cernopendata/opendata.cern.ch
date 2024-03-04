[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBu2rho0rhoPlusUpResolvedLine

## Properties:

|                |                                                                            |
|----------------|----------------------------------------------------------------------------|
| OutputLocation | Phys/Bu2rho0rhoPlusUpResolvedLine/Particles                                |
| Postscale      | 1.0000000                                                                  |
| HLT            | HLT_PASS('Hlt1TrackAllL0Decision') & HLT_PASS('Hlt2Topo2BodyBBDTDecision') |
| Prescale       | 1.0000000                                                                  |
| L0DU           | None                                                                       |
| ODIN           | None                                                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2rho0rhoPlusUpResolvedLineVOIDFilter

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)/Particles')\>0 |

FilterDesktop/upAndLongTracksForBu2rho0rhoPlus

|                 |                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (~ISMUON) &(MIPCHI2DV(PRIMARY) \> 8) & (PROBNNpi \> 0.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5)                                                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)' ] |
| DecayDescriptor | None                                                                                                                                                              |
| Output          | Phys/upAndLongTracksForBu2rho0rhoPlus/Particles                                                                                                                   |

CombineParticles/rho0ForBu2rho0rhoPlusUpResolved

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/upAndLongTracksForBu2rho0rhoPlus' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                         |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                             |
| MotherCut        | (MIPCHI2DV(PRIMARY) \> 55) & (BPVVDCHI2 \> 55) & (M \> 200) & (M \< 1200) & (VFASPF(VCHI2/VDOF) \< 14) |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                  |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                          |
| Output           | Phys/rho0ForBu2rho0rhoPlusUpResolved/Particles                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

CombineParticles/rhoPForBu2rho0rhoPlusUpResolved

|                  |                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' , 'Phys/upAndLongTracksForBu2rho0rhoPlus' ]                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \> 10)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \> 10)' , 'pi0' : '(CL \> -1000) & (P \> 1000) & (PT \> 400)' } |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                                                         |
| MotherCut        | (M \> 200) & (M \< 1200) & (P \> 9000) & (PT \> 1400)                                                                                              |
| DecayDescriptor  | [rho(770)+ -\> pi+ pi0]cc                                                                                                                        |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ pi0]cc' ]                                                                                                                |
| Output           | Phys/rhoPForBu2rho0rhoPlusUpResolved/Particles                                                                                                     |

CombineParticles/Bu2rho0rhoPlusUpResolvedLine

|                  |                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/rho0ForBu2rho0rhoPlusUpResolved' , 'Phys/rhoPForBu2rho0rhoPlusUpResolved' ]                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                                                                                                                                   |
| CombinationCut   | (ADAMASS('B0') \< 650) & (APT \> 1500)                                                                                                                                                                                                                                             |
| MotherCut        | (INTREE( HASTRACK & ISUP )) & (SUMTREE('pi+'==ABSID,PT) \> 3500) & (ADMASS('B+') \< 600) & (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 0) & (MAXTREE('pi+'==ABSID,PT) \> 1600) & (BPVVDCHI2 \> 55) & (MIPCHI2DV(PRIMARY) \< 20) & (BPVDIRA \> 0.9998) & (VFASPF(VCHI2/VDOF) \< 8) |
| DecayDescriptor  | [B+ -\> rho(770)0 rho(770)+]cc                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B+ -\> rho(770)0 rho(770)+]cc' ]                                                                                                                                                                                                                                           |
| Output           | Phys/Bu2rho0rhoPlusUpResolvedLine/Particles                                                                                                                                                                                                                                        |

AddRelatedInfo/RelatedInfo1_Bu2rho0rhoPlusUpResolvedLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpResolvedLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_Bu2rho0rhoPlusUpResolvedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2rho0rhoPlusUpResolvedLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpResolvedLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_Bu2rho0rhoPlusUpResolvedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2rho0rhoPlusUpResolvedLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpResolvedLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_Bu2rho0rhoPlusUpResolvedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2rho0rhoPlusUpResolvedLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpResolvedLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo4_Bu2rho0rhoPlusUpResolvedLine/Particles |
