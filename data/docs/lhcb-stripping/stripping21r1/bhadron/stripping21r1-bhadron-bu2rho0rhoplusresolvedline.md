[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBu2rho0rhoPlusResolvedLine

## Properties:

|                |                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/Bu2rho0rhoPlusResolvedLine/Particles                                                       |
| Postscale      | 1.0000000                                                                                       |
| HLT            | HLT_PASS_RE('Hlt1Track(AllL0\|Photon)Decision') & HLT_PASS_RE('Hlt2Topo[23]BodyBBDTDecision') |
| Prescale       | 1.0000000                                                                                       |
| L0DU           | None                                                                                            |
| ODIN           | None                                                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2rho0rhoPlusResolvedLineVOIDFilter

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

FilterDesktop/longTracksForBu2rho0rhoPlus

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (~ISMUON) &(MIPCHI2DV(PRIMARY) \> 4) & (PROBNNpi \> 0.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                  |
| DecayDescriptor | None                                                                                                 |
| Output          | Phys/longTracksForBu2rho0rhoPlus/Particles                                                           |

CombineParticles/rho0ForBu2rho0rhoPlusResolved

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/longTracksForBu2rho0rhoPlus' ]                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                         |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                             |
| MotherCut        | (MIPCHI2DV(PRIMARY) \> 20) & (BPVVDCHI2 \> 27) & (M \> 200) & (M \< 1200) & (VFASPF(VCHI2/VDOF) \< 14) |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                  |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                          |
| Output           | Phys/rho0ForBu2rho0rhoPlusResolved/Particles                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

CombineParticles/rhoPForBu2rho0rhoPlusResolved

|                  |                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' , 'Phys/longTracksForBu2rho0rhoPlus' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \> 20)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \> 20)' , 'pi0' : '(CL \> -1000) & (P \> 3500) & (PT \> 400)' } |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                                                         |
| MotherCut        | (M \> 200) & (M \< 1200) & (P \> 7000) & (PT \> 1000)                                                                                              |
| DecayDescriptor  | [rho(770)+ -\> pi+ pi0]cc                                                                                                                        |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ pi0]cc' ]                                                                                                                |
| Output           | Phys/rhoPForBu2rho0rhoPlusResolved/Particles                                                                                                       |

CombineParticles/Bu2rho0rhoPlusResolvedLine

|                  |                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/rho0ForBu2rho0rhoPlusResolved' , 'Phys/rhoPForBu2rho0rhoPlusResolved' ]                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                                                                                                       |
| CombinationCut   | (ADAMASS('B0') \< 650) & (APT \> 1000)                                                                                                                                                                                                                 |
| MotherCut        | (SUMTREE('pi+'==ABSID,PT) \> 3800) & (ADMASS('B+') \< 600) & (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 40) & (MAXTREE('pi+'==ABSID,PT) \> 1900) & (BPVVDCHI2 \> 120) & (MIPCHI2DV(PRIMARY) \< 30) & (BPVDIRA \> 0.9998) & (VFASPF(VCHI2/VDOF) \< 8) |
| DecayDescriptor  | [B+ -\> rho(770)0 rho(770)+]cc                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B+ -\> rho(770)0 rho(770)+]cc' ]                                                                                                                                                                                                               |
| Output           | Phys/Bu2rho0rhoPlusResolvedLine/Particles                                                                                                                                                                                                              |

AddRelatedInfo/RelatedInfo1_Bu2rho0rhoPlusResolvedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusResolvedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_Bu2rho0rhoPlusResolvedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2rho0rhoPlusResolvedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusResolvedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_Bu2rho0rhoPlusResolvedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2rho0rhoPlusResolvedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusResolvedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_Bu2rho0rhoPlusResolvedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2rho0rhoPlusResolvedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusResolvedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_Bu2rho0rhoPlusResolvedLine/Particles |
