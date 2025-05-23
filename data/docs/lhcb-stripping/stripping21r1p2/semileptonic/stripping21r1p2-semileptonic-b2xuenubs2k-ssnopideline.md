[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuENuBs2K_SSNoPIDELine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2XuENuBs2K_SSNoPIDELine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 0.020000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuBs2K_SSNoPIDELineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsElectrons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsElectrons/Particles',True) |

FilterDesktop/ETightNoPIDCuts_forB2XuENu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdNoPIDsElectrons](./stripping21r1p2-commonparticles-stdnopidselectrons)' ]                           |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/ETightNoPIDCuts_forB2XuENu/Particles                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/K_forB2XuENu

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 10000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK \> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 36 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                     |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/K_forB2XuENu/Particles                                                                                                       |

CombineParticles/B2XuENuBs2K_SSNoPIDELine

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ETightNoPIDCuts_forB2XuENu' , 'Phys/K_forB2XuENu' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                    |
| CombinationCut   | ATRUE                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B_s~0 -\> K- e-]cc' ]                                                                                                 |
| Output           | Phys/B2XuENuBs2K_SSNoPIDELine/Particles                                                                                       |
