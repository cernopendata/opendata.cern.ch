[[stripping21 lines]](./stripping21-index)

# StrippingB2XuMuNuBs2KSSLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2XuMuNuBs2KSSLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.50000000                        |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XuMuNuBs2KSSLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuL0TOS_forB2XuMuNu

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/MuL0TOS_forB2XuMuNu/Particles                                                                                                                                               |

TisTosParticleTagger/MuL0TOS_forB2XuMuNuTOS

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/MuL0TOS_forB2XuMuNu' ]      |
| DecayDescriptor | None                                  |
| Output          | Phys/MuL0TOS_forB2XuMuNuTOS/Particles |
| TisTosSpecs     | { 'L0.\*Muon.\*Decision%TOS' : 0 }    |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/K_forB2XuMuNu

|                 |                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 3000.0 \*MeV) & (PT\> 800.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK-PIDpi\> 5.0 )& (PIDK-PIDp\> 0.0 )& (PIDK-PIDmu\> 0.0 ) & (MIPCHI2DV(PRIMARY)\> 16 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                          |
| Output          | Phys/K_forB2XuMuNu/Particles                                                                                                                                                  |

CombineParticles/KMuSS_forB2XuMuNu

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_forB2XuMuNu' , 'Phys/MuL0TOS_forB2XuMuNuTOS' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }         |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<5500.0\*MeV)                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (ratio \> 0.4) |
| DecayDescriptor  | None                                                                                 |
| DecayDescriptors | [ '[B_s~0 -\> K- mu-]cc' ]                                                       |
| Output           | Phys/KMuSS_forB2XuMuNu/Particles                                                     |

TisTosParticleTagger/B2XuMuNuBs2KSSLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KMuSS_forB2XuMuNu' ]                                                       |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/B2XuMuNuBs2KSSLine/Particles                                                    |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
