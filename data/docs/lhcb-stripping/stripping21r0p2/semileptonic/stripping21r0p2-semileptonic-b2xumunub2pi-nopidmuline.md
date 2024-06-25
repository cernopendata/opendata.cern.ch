[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuMuNuB2Pi_NoPIDMuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2XuMuNuB2Pi_NoPIDMuLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 0.0050000000                            |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuB2Pi_NoPIDMuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsMuons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsMuons/Particles',True) |

FilterDesktop/MuNoPID_forB2XuMuNu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdNoPIDsMuons](./stripping21r0p2-commonparticles-stdnopidsmuons)' ]                                   |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/MuNoPID_forB2XuMuNu/Particles                                                                                |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PiTight_forB2XuMuNu

|                 |                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 10000.0 \*MeV) & (PT\> 800.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (PIDK \< -2.0 )& (PIDmu \< 2 ) & (MIPCHI2DV(PRIMARY)\> 49 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                     |
| DecayDescriptor | None                                                                                                                                              |
| Output          | Phys/PiTight_forB2XuMuNu/Particles                                                                                                                |

CombineParticles/PiMuNoPIDmu_forB2XuMuNu

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuNoPID_forB2XuMuNu' , 'Phys/PiTight_forB2XuMuNu' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                |
| CombinationCut   | (AM\>1200.0\*MeV) & (AM\<5500.0\*MeV)                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> pi+ mu-]cc' ]                                                                                                  |
| Output           | Phys/PiMuNoPIDmu_forB2XuMuNu/Particles                                                                                        |

TisTosParticleTagger/B2XuMuNuB2Pi_NoPIDMuLine

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PiMuNoPIDmu_forB2XuMuNu' ]                                               |
| DecayDescriptor | None                                                                               |
| Output          | Phys/B2XuMuNuB2Pi_NoPIDMuLine/Particles                                            |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*Topo2Body.\*Decision%TOS' : 0 } |
