[[stripping21 lines]](./stripping21-index)

# StrippingD2HHBDTLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/D2HHBDTLine/Particles |
| Postscale      | 0.10000000                 |
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

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/D2HHBDT

|                  |                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPDV(PRIMARY) \> 0.12 )' , 'K-' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPDV(PRIMARY) \> 0.12 )' } |
| CombinationCut   | ( AMAXDOCA('') \< 0.1 ) & ( AM \> 1000 \* MeV ) & ( AM \< 2800 \* MeV )                                                                                                                                                    |
| MotherCut        | ( PT \> 1200 \* MeV ) & ( M \> 1800 \* MeV ) & ( M \< 2600 \* MeV ) & ( BPVIP() \< 0.12 ) & ( BPVLTIME() \> 0.0 )                                                                                                          |
| DecayDescriptor  | D0 -\> K+ K-                                                                                                                                                                                                               |
| DecayDescriptors | [ 'D0 -\> K+ K-' ]                                                                                                                                                                                                       |
| Output           | Phys/D2HHBDT/Particles                                                                                                                                                                                                     |

FilterDesktop/D2HHBDTLine

|                 |                                    |
|-----------------|------------------------------------|
| Code            | FILTER('D2hhBDTSelection/D2hhBDT') |
| Inputs          | [ 'Phys/D2HHBDT' ]               |
| DecayDescriptor | None                               |
| Output          | Phys/D2HHBDTLine/Particles         |
