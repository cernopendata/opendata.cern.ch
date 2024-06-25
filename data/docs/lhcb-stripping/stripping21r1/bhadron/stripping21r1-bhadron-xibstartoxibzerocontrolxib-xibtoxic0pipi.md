[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXibStarToXibZeroControlXib_XibToXic0PiPi

## Properties:

|                |                                                         |
|----------------|---------------------------------------------------------|
| OutputLocation | Phys/XibStarToXibZeroControlXib_XibToXic0PiPi/Particles |
| Postscale      | 1.0000000                                               |
| HLT            | None                                                    |
| Prescale       | 0.10000000                                              |
| L0DU           | None                                                    |
| ODIN           | None                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingXibStarToXibZeroControlXib_XibToXic0PiPiVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 300 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r1-commonparticles-stdlooseannprotons)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroBaseFilteredProtons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0)                |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1-commonparticles-stdlooseannprotons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/XibStarToXibZeroBaseFilteredProtons/Particles                                    |

FilterDesktop/XibStarToXibZeroGhostFilteredProtons

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.7)                                  |
| Inputs          | [ 'Phys/XibStarToXibZeroBaseFilteredProtons' ]    |
| DecayDescriptor | None                                                |
| Output          | Phys/XibStarToXibZeroGhostFilteredProtons/Particles |

FilterDesktop/XibStarToXibZeroFilteredProtons

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (HASRICH)&(PROBNNp\>0.02)                         |
| Inputs          | [ 'Phys/XibStarToXibZeroGhostFilteredProtons' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/XibStarToXibZeroFilteredProtons/Particles    |

FilterDesktop/XibStarToXibZeroTightFilteredProtons

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Code            | (PROBNNp\>0.05) & (MIPCHI2DV(PRIMARY)\>4.0)         |
| Inputs          | [ 'Phys/XibStarToXibZeroFilteredProtons' ]        |
| DecayDescriptor | None                                                |
| Output          | Phys/XibStarToXibZeroTightFilteredProtons/Particles |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroBaseFilteredKaons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0)            |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/XibStarToXibZeroBaseFilteredKaons/Particles                                  |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)/Particles')\>0 |

FilterDesktop/XibStarToXibZeroBaseFilteredPions

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0)            |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/XibStarToXibZeroBaseFilteredPions/Particles                                  |

FilterDesktop/XibStarToXibZeroGhostFilteredPions

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.7)                                |
| Inputs          | [ 'Phys/XibStarToXibZeroBaseFilteredPions' ]    |
| DecayDescriptor | None                                              |
| Output          | Phys/XibStarToXibZeroGhostFilteredPions/Particles |

FilterDesktop/XibStarToXibZeroFilteredPions

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (HASRICH)&(PROBNNpi\>0.01)                      |
| Inputs          | [ 'Phys/XibStarToXibZeroGhostFilteredPions' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/XibStarToXibZeroFilteredPions/Particles    |

FilterDesktop/XibStarToXibZeroTightFilteredPions

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (PROBNNpi\>0.04) & (MIPCHI2DV(PRIMARY)\>4.0)      |
| Inputs          | [ 'Phys/XibStarToXibZeroFilteredPions' ]        |
| DecayDescriptor | None                                              |
| Output          | Phys/XibStarToXibZeroTightFilteredPions/Particles |

CombineParticles/XibStarToXibZeroCombineXicZeroToPKKpi

|                  |                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibStarToXibZeroTightFilteredKaons' , 'Phys/XibStarToXibZeroTightFilteredPions' , 'Phys/XibStarToXibZeroTightFilteredProtons' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                               |
| CombinationCut   | ( ADAMASS('Xi_c0') \< 80.0 ) & ( APT \> 1.0\*GeV )                                                                                        |
| MotherCut        | (VFASPF(VCHI2)\<60.0)&(ADMASS('Xi_c0') \< 50.0)& (BPVDIRA \> 0.9)                                                                         |
| DecayDescriptor  | [Xi_c0 -\> p+ K- K- pi+]cc                                                                                                              |
| DecayDescriptors | [ '[Xi_c0 -\> p+ K- K- pi+]cc' ]                                                                                                      |
| Output           | Phys/XibStarToXibZeroCombineXicZeroToPKKpi/Particles                                                                                      |

CombineParticles/XibStarToXibZeroControlXib_XibToXic0PiPi

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibStarToXibZeroCombineXicZeroToPKKpi' , 'Phys/XibStarToXibZeroFilteredPions' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                   |
| CombinationCut   | ( APT \> 2000.0 ) & ( AMAXDOCA('')\<0.5\*mm ) & ( AM\>3800.0\*MeV ) & ( AM\<7200.0\*MeV )                             |
| MotherCut        | ( BPVVDCHI2 \> 36.0 ) & ( VFASPF(VCHI2PDOF)\<7.0 ) & ( MM\>5500.0\*MeV ) & ( MM\<6100.0\*MeV ) & ( BPVDIRA \> 0.995 ) |
| DecayDescriptor  | [ Xi_b0 -\> Xi_c0 pi- pi+ ]cc                                                                                       |
| DecayDescriptors | [ '[ Xi_b0 -\> Xi_c0 pi- pi+ ]cc' ]                                                                               |
| Output           | Phys/XibStarToXibZeroControlXib_XibToXic0PiPi/Particles                                                               |
