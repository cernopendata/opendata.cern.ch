[[stripping21 lines]](./stripping21-index)

# StrippingXibStarToXibZeroXibToLcK_WS

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/XibStarToXibZeroXibToLcK_WS/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingXibStarToXibZeroXibToLcK_WSVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 300 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroDisplacedLcFilt

|                 |                                                                                                                                                                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( MINTREE('pi+'==ABSID, PROBNNpi) \> 0.01 ) & ( MINTREE('K+'==ABSID, PROBNNk) \> 0.02 ) & ( MINTREE('p+'==ABSID, PROBNNp) \> 0.02 ) & ( PT \> 2.0\*GeV ) & (ADMASS('Lambda_c+')\<50\*MeV) & ( MAXTREE('pi+'==ABSID, TRGHOSTPROB) \< 0.7 ) & ( MAXTREE('K+'==ABSID, TRGHOSTPROB) \< 0.7 ) & ( MAXTREE('p+'==ABSID, TRGHOSTPROB) \< 0.7 ) |
| Inputs          | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)' ]                                                                                                                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                    |
| Output          | Phys/XibStarToXibZeroDisplacedLcFilt/Particles                                                                                                                                                                                                                                                                                          |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroBaseFilteredKaons

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0)          |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21-commonparticles-stdlooseannkaons)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/XibStarToXibZeroBaseFilteredKaons/Particles                                |

FilterDesktop/XibStarToXibZeroGhostFilteredKaons

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.7)                                |
| Inputs          | [ 'Phys/XibStarToXibZeroBaseFilteredKaons' ]    |
| DecayDescriptor | None                                              |
| Output          | Phys/XibStarToXibZeroGhostFilteredKaons/Particles |

FilterDesktop/XibStarToXibZeroFilteredKaons

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (HASRICH)&(PROBNNk\>0.02)                       |
| Inputs          | [ 'Phys/XibStarToXibZeroGhostFilteredKaons' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/XibStarToXibZeroFilteredKaons/Particles    |

FilterDesktop/XibStarToXibZeroTightFilteredKaons

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (PROBNNk\>0.04) & (MIPCHI2DV(PRIMARY)\>4.0)       |
| Inputs          | [ 'Phys/XibStarToXibZeroFilteredKaons' ]        |
| DecayDescriptor | None                                              |
| Output          | Phys/XibStarToXibZeroTightFilteredKaons/Particles |

CombineParticles/XibStarToXibZeroCombineXibToLcK

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibStarToXibZeroDisplacedLcFilt' , 'Phys/XibStarToXibZeroTightFilteredKaons' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' }                             |
| CombinationCut   | ( APT \> 2000.0 ) & ( AMAXDOCA('')\<0.5\*mm ) & ( AM\>3800.0\*MeV ) & ( AM\<7200.0\*MeV )                             |
| MotherCut        | ( BPVVDCHI2 \> 36.0 ) & ( VFASPF(VCHI2PDOF)\<7.0 ) & ( MM\>5500.0\*MeV ) & ( MM\<6100.0\*MeV ) & ( BPVDIRA \> 0.995 ) |
| DecayDescriptor  | [ Xi_b0 -\> Lambda_c+ K- ]cc                                                                                        |
| DecayDescriptors | [ '[ Xi_b0 -\> Lambda_c+ K- ]cc' ]                                                                                |
| Output           | Phys/XibStarToXibZeroCombineXibToLcK/Particles                                                                        |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroFilteredSoftPionsBase

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>1000.0)& (PT\>0.0)& (PROBNNe\<0.2)& (MIPCHI2DV(PRIMARY)\>-999.0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]      |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/XibStarToXibZeroFilteredSoftPionsBase/Particles                                   |

FilterDesktop/XibStarToXibZeroFilteredSoftPionsGP

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.7)                                 |
| Inputs          | [ 'Phys/XibStarToXibZeroFilteredSoftPionsBase' ] |
| DecayDescriptor | None                                               |
| Output          | Phys/XibStarToXibZeroFilteredSoftPionsGP/Particles |

CombineParticles/XibStarToXibZeroXibToLcK_WS

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibStarToXibZeroCombineXibToLcK' , 'Phys/XibStarToXibZeroFilteredSoftPionsGP' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_b0' : 'ALL' , 'Xi_b~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                  |
| CombinationCut   | (AM \> 5000.0\*MeV) & (AM \< 8000.0\*MeV)                                                                                            |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 20.0) & (MM - CHILD(MM,1) - CHILD(MM,2) \> -25.0) & (MM - CHILD(MM,1) - CHILD(MM,2) \< 50.0)&(PT \> 2500.0)) |
| DecayDescriptor  | [ Sigma_b+ -\> Xi_b0 pi+ ]cc                                                                                                       |
| DecayDescriptors | [ '[ Sigma_b+ -\> Xi_b0 pi+ ]cc' ]                                                                                               |
| Output           | Phys/XibStarToXibZeroXibToLcK_WS/Particles                                                                                           |
