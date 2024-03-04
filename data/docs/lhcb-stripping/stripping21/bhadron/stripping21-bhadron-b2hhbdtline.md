[[stripping21 lines]](./stripping21-index)

# StrippingB2HHBDTLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/B2HHBDTLine/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/B2HHBDT

|                  |                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPDV(PRIMARY) \> 0.12 )' , 'pi-' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPDV(PRIMARY) \> 0.12 )' } |
| CombinationCut   | ( AMAXDOCA('') \< 0.1 ) & ( AM \> 4600 \* MeV ) & ( AM \< 6400 \* MeV )                                                                                                                                                      |
| MotherCut        | ( PT \> 1200 \* MeV ) & ( M \> 4800 \* MeV ) & ( M \< 6200 \* MeV ) & ( BPVIP() \< 0.12 ) & ( BPVLTIME() \> 0.0006 )                                                                                                         |
| DecayDescriptor  | B0 -\> pi+ pi-                                                                                                                                                                                                               |
| DecayDescriptors | [ 'B0 -\> pi+ pi-' ]                                                                                                                                                                                                       |
| Output           | Phys/B2HHBDT/Particles                                                                                                                                                                                                       |

FilterDesktop/B2HHBDTLine

|                 |                                    |
|-----------------|------------------------------------|
| Code            | FILTER('B2hhBDTSelection/B2hhBDT') |
| Inputs          | [ 'Phys/B2HHBDT' ]               |
| DecayDescriptor | None                               |
| Output          | Phys/B2HHBDTLine/Particles         |
