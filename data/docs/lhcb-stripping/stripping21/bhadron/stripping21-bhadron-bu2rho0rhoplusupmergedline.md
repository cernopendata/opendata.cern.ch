[[stripping21 lines]](./stripping21-index)

# StrippingBu2rho0rhoPlusUpMergedLine

## Properties:

|                |                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/Bu2rho0rhoPlusUpMergedLine/Particles                                                                                         |
| Postscale      | 1.0000000                                                                                                                         |
| HLT            | HLT_PASS_RE('Hlt1Track(AllL0\|Photon)Decision') & HLT_PASS_RE('Hlt2(Topo2BodyBBDT\|B2HHPi0_Merged\|RadiativeTopoPhoton)Decision') |
| Prescale       | 1.0000000                                                                                                                         |
| L0DU           | None                                                                                                                              |
| ODIN           | None                                                                                                                              |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2rho0rhoPlusUpMergedLineVOIDFilter

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0) |

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

FilterDesktop/upAndLongTracksForBu2rho0rhoPlus

|                 |                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (~ISMUON) &(MIPCHI2DV(PRIMARY) \> 8) & (PROBNNpi \> 0.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5)                                                          |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' , 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ] |
| DecayDescriptor | None                                                                                                                                                          |
| Output          | Phys/upAndLongTracksForBu2rho0rhoPlus/Particles                                                                                                               |

CombineParticles/rho0ForBu2rho0rhoPlusUpMerged

|                  |                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/upAndLongTracksForBu2rho0rhoPlus' ]                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'PT \> 0' , 'pi-' : 'PT \> 0' }                                                                                                    |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                                                                |
| MotherCut        | (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 55) & (MIPCHI2DV(PRIMARY) \> 55) & (BPVVDCHI2 \> 55) & (M \> 200) & (M \< 1200) & (VFASPF(VCHI2/VDOF) \< 14) |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                                                                     |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                             |
| Output           | Phys/rho0ForBu2rho0rhoPlusUpMerged/Particles                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0 |

CombineParticles/rhoPForBu2rho0rhoPlusUpMerged

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)' , 'Phys/upAndLongTracksForBu2rho0rhoPlus' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT \> 0)' , 'pi-' : '(PT \> 0)' , 'pi0' : '(PT \> 0)' }                                            |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                                  |
| MotherCut        | ALL                                                                                                                         |
| DecayDescriptor  | [rho(770)+ -\> pi+ pi0]cc                                                                                                 |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ pi0]cc' ]                                                                                         |
| Output           | Phys/rhoPForBu2rho0rhoPlusUpMerged/Particles                                                                                |

CombineParticles/Bu2rho0rhoPlusUpMergedLine

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/rho0ForBu2rho0rhoPlusUpMerged' , 'Phys/rhoPForBu2rho0rhoPlusUpMerged' ]                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                                                             |
| CombinationCut   | (AM \> 3900) & (AM \< 7150) & (APT \> 5000)                                                                                                                                                                  |
| MotherCut        | (INTREE( HASTRACK & ISUP )) & (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 55) & (M \> 4000) & (M \< 7000) & (BPVVDCHI2 \> 55) & (MIPCHI2DV(PRIMARY) \< 55) & (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF) \< 8) |
| DecayDescriptor  | [B+ -\> rho(770)0 rho(770)+]cc                                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> rho(770)0 rho(770)+]cc' ]                                                                                                                                                                     |
| Output           | Phys/Bu2rho0rhoPlusUpMergedLine/Particles                                                                                                                                                                    |

AddRelatedInfo/RelatedInfo1_Bu2rho0rhoPlusUpMergedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpMergedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_Bu2rho0rhoPlusUpMergedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2rho0rhoPlusUpMergedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpMergedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_Bu2rho0rhoPlusUpMergedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2rho0rhoPlusUpMergedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpMergedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_Bu2rho0rhoPlusUpMergedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2rho0rhoPlusUpMergedLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusUpMergedLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_Bu2rho0rhoPlusUpMergedLine/Particles |
