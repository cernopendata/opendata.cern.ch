[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2CharmlessQ2B4piSelectionLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2CharmlessQ2B4piSelectionLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/TrackListB2CharmlessQ2B

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.5) & (PT \> 400.0)           |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/TrackListB2CharmlessQ2B/Particles                                        |

CombineParticles/DiTracksForCharmlessBB2CharmlessQ2B

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TrackListB2CharmlessQ2B' ]               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }     |
| CombinationCut   | (APT\> 600.0) & (AM\< 1100.0)                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6.0)                        |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                              |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                      |
| Output           | Phys/DiTracksForCharmlessBB2CharmlessQ2B/Particles |

CombineParticles/B2CharmlessQ2B4piSelection

|                  |                                                       |
|------------------|-------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracksForCharmlessBB2CharmlessQ2B' ]      |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)0' : 'ALL' }                  |
| CombinationCut   | in_range( 3500.0 ,AM, 5700.0 ) & ( APT \> 2500.0 )    |
| MotherCut        | ( BPVCORRM \< 6000.0 ) & (VFASPF(VCHI2/VDOF) \< 6.0 ) |
| DecayDescriptor  | B0 -\> rho(770)0 rho(770)0                            |
| DecayDescriptors | [ 'B0 -\> rho(770)0 rho(770)0' ]                    |
| Output           | Phys/B2CharmlessQ2B4piSelection/Particles             |

TisTosParticleTagger/B2CharmlessQ2B4piSelectionLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessQ2B4piSelection' ]       |
| DecayDescriptor | None                                          |
| Output          | Phys/B2CharmlessQ2B4piSelectionLine/Particles |
| TisTosSpecs     | { 'Hlt1Track.\*Decision%TOS' : 0 }            |
