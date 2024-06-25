[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuENuB2Pi_NoPIDELine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2XuENuB2Pi_NoPIDELine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 0.020000000                           |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuB2Pi_NoPIDELineVOIDFilter

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

FilterDesktop/ENoPID_forB2XuENu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdNoPIDsElectrons](./stripping21r0p2-commonparticles-stdnopidselectrons)' ]                           |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/ENoPID_forB2XuENu/Particles                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PiTight_forB2XuENu

|                 |                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 10000.0 \*MeV) & (PT\> 800.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK \< -2.0 )& (MIPCHI2DV(PRIMARY)\> 36 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                    |
| DecayDescriptor | None                                                                                                                             |
| Output          | Phys/PiTight_forB2XuENu/Particles                                                                                                |

CombineParticles/PiENoPIDe_forB2XuENu

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ENoPID_forB2XuENu' , 'Phys/PiTight_forB2XuENu' ]                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                  |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<5500.0\*MeV)                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> pi+ e-]cc' ]                                                                                                   |
| Output           | Phys/PiENoPIDe_forB2XuENu/Particles                                                                                           |

TisTosParticleTagger/B2XuENuB2Pi_NoPIDELine

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PiENoPIDe_forB2XuENu' ]                                                         |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/B2XuENuB2Pi_NoPIDELine/Particles                                                     |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*Topo2Body.\*Decision%TOS' : 0 } |
