[[stripping21 lines]](./stripping21-index)

# StrippingBs2Phif0Line

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/Bs2Phif0Line/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/TrackListBs2Phif0

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.6) & (PT\>250.\*MeV) & (TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY) \> 16) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]              |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/TrackListBs2Phif0/Particles                                                       |

CombineParticles/TracksForPhiBs2Phif0

|                  |                                                                            |
|------------------|----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBs2Phif0' ]                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                               |
| CombinationCut   | (APT\> 900.0 \*MeV) & (AP\> 1.0 \*GeV) & in_range( 969.445 ,AM, 1069.445 ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0)                                               |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                        |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                |
| Output           | Phys/TracksForPhiBs2Phif0/Particles                                        |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/TrackList1Bs2Phif0

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.6) & (PT\>250.\*MeV) & (TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY) \> 16) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]            |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/TrackList1Bs2Phif0/Particles                                                      |

CombineParticles/TracksForf0Bs2Phif0

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackList1Bs2Phif0' ]                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                       |
| CombinationCut   | (APT\> 900.0 \*MeV) & (AP\> 1.0 \*GeV) & in_range( 0.0 ,AM, 1800.0 ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0)                                         |
| DecayDescriptor  | f_0(980) -\> pi+ pi-                                                 |
| DecayDescriptors | [ 'f_0(980) -\> pi+ pi-' ]                                         |
| Output           | Phys/TracksForf0Bs2Phif0/Particles                                   |

CombineParticles/Bs2Phif0Line

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TracksForPhiBs2Phif0' , 'Phys/TracksForf0Bs2Phif0' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'f_0(980)' : 'ALL' , 'phi(1020)' : 'ALL' }                      |
| CombinationCut   | in_range( 4800.0 ,AM, 5750.0 )                                                 |
| MotherCut        | (BPVDIRA \> 0.99) & (MIPCHI2DV(PRIMARY) \< 20) & (VFASPF(VCHI2/VDOF) \< 12.0 ) |
| DecayDescriptor  | B_s0 -\> phi(1020) f_0(980)                                                    |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) f_0(980)' ]                                            |
| Output           | Phys/Bs2Phif0Line/Particles                                                    |
