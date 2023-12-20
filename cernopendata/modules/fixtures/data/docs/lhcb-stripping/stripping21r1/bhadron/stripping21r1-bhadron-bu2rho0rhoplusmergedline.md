[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBu2rho0rhoPlusMergedLine

## Properties:

|                |                                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/Bu2rho0rhoPlusMergedLine/Particles                                                                                                |
| Postscale      | 1.0000000                                                                                                                              |
| HLT            | HLT_PASS_RE('Hlt1Track(AllL0\|Photon)Decision') & HLT_PASS_RE('Hlt2(Topo[23]BodyBBDT\|B2HHPi0_Merged\|RadiativeTopoPhoton)Decision') |
| Prescale       | 1.0000000                                                                                                                              |
| L0DU           | None                                                                                                                                   |
| ODIN           | None                                                                                                                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2rho0rhoPlusMergedLineVOIDFilter

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0) |

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

CombineParticles/rho0ForBu2rho0rhoPlusMerged

|                  |                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/longTracksForBu2rho0rhoPlus' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'PT \> 100' , 'pi-' : 'PT \> 100' }                                                                                                |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                                                                |
| MotherCut        | (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 20) & (MIPCHI2DV(PRIMARY) \> 33) & (BPVVDCHI2 \> 25) & (M \> 200) & (M \< 1200) & (VFASPF(VCHI2/VDOF) \< 14) |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                                                                     |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                             |
| Output           | Phys/rho0ForBu2rho0rhoPlusMerged/Particles                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

CombineParticles/rhoPForBu2rho0rhoPlusMerged

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' , 'Phys/longTracksForBu2rho0rhoPlus' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT \> 960)' , 'pi-' : '(PT \> 960)' , 'pi0' : '(PT \> 1900)' }                                  |
| CombinationCut   | (AM \> 100) & (AM \< 1300)                                                                                               |
| MotherCut        | ALL                                                                                                                      |
| DecayDescriptor  | [rho(770)+ -\> pi+ pi0]cc                                                                                              |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ pi0]cc' ]                                                                                      |
| Output           | Phys/rhoPForBu2rho0rhoPlusMerged/Particles                                                                               |

CombineParticles/Bu2rho0rhoPlusMergedLine

|                  |                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/rho0ForBu2rho0rhoPlusMerged' , 'Phys/rhoPForBu2rho0rhoPlusMerged' ]                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                                  |
| CombinationCut   | (AM \> 3900) & (AM \< 7150) & (APT \> 4000)                                                                                                                                       |
| MotherCut        | (MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY)) \> 20) & (M \> 4000) & (M \< 7000) & (BPVVDCHI2 \> 120) & (MIPCHI2DV(PRIMARY) \< 450) & (BPVDIRA \> 0.9997) & (VFASPF(VCHI2/VDOF) \< 8) |
| DecayDescriptor  | [B+ -\> rho(770)0 rho(770)+]cc                                                                                                                                                  |
| DecayDescriptors | [ '[B+ -\> rho(770)0 rho(770)+]cc' ]                                                                                                                                          |
| Output           | Phys/Bu2rho0rhoPlusMergedLine/Particles                                                                                                                                           |

AddRelatedInfo/RelatedInfo1_Bu2rho0rhoPlusMergedLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusMergedLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_Bu2rho0rhoPlusMergedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2rho0rhoPlusMergedLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusMergedLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_Bu2rho0rhoPlusMergedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2rho0rhoPlusMergedLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusMergedLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_Bu2rho0rhoPlusMergedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2rho0rhoPlusMergedLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bu2rho0rhoPlusMergedLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_Bu2rho0rhoPlusMergedLine/Particles |
