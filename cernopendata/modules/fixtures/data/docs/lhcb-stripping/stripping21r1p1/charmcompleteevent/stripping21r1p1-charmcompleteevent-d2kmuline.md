[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingD2KmuLine

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/D2KmuLine/Particles |
| Postscale      | 1.0000000                |
| HLT1           | None                     |
| HLT2           | None                     |
| Prescale       | 0.10000000               |
| L0DU           | None                     |
| ODIN           | None                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharmCompleteEvent

|      |                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamCharmCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingD2KmuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 160.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forD2HMuNu

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                             |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/Mu_forD2HMuNu/Particles                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/K_forD2HMuNu

|                 |                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 800.0 \*MeV)& (P\> 3000.0)& (TRGHOSTPROB \< 0.35)& (PIDK-PIDpi\> 5.0 )& (PIDK-PIDp\> 5.0 )& (PIDK-PIDmu\> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 9 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                     |
| DecayDescriptor | None                                                                                                                                              |
| Output          | Phys/K_forD2HMuNu/Particles                                                                                                                       |

CombineParticles/SelD0_forD2Kmu

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_forD2HMuNu' , 'Phys/Mu_forD2HMuNu' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }         |
| CombinationCut   | (AM\>500\*MeV) & (AM\<2000\*MeV)                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 20 )& (BPVVDCHI2 \>100.0)& (BPVDIRA \> 0.999)& (BPVVDZ \> 0.0) |
| DecayDescriptor  | None                                                                                 |
| DecayDescriptors | [ '[D0 -\> K- mu+]cc' ]                                                          |
| Output           | Phys/SelD0_forD2Kmu/Particles                                                        |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

FilterDesktop/pis_forD2HMuNu

|                 |                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------|
| Code            | (PT\> 300 \*MeV)& (P \> 1000)& (TRGHOSTPROB \< 0.35)& (PIDe \< 5) & (MIPCHI2DV(PRIMARY)\< 9.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)' ]            |
| DecayDescriptor | None                                                                                           |
| Output          | Phys/pis_forD2HMuNu/Particles                                                                  |

CombineParticles/SelDstD2Kmu

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0_forD2Kmu' , 'Phys/pis_forD2HMuNu' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM - ACHILD(M,1) \< 400+5 \*MeV) & (ADOCACHI2CUT(20,''))                     |
| MotherCut        | (M - CHILD(M,1) \< 400 \*MeV) & (VFASPF(VCHI2/VDOF) \< 9.0)                   |
| DecayDescriptor  | None                                                                          |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                           |
| Output           | Phys/SelDstD2Kmu/Particles                                                    |

TisTosParticleTagger/D2KmuLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/SelDstD2Kmu' ]                    |
| DecayDescriptor | None                                        |
| Output          | Phys/D2KmuLine/Particles                    |
| TisTosSpecs     | { 'Hlt2CharmHad.\*HHX.\*Decision%TOS' : 0 } |
