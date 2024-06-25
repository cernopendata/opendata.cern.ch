[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2D0KD02KPiPiMuNuLine

## Properties:

|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0KD02KPiPiMuNuLine/Particles                                                |
| Postscale      | 1.0000000                                                                           |
| HLT1           | None                                                                                |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision')) |
| Prescale       | 1.0000000                                                                           |
| L0DU           | None                                                                                |
| ODIN           | None                                                                                |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2D0KD02KPiPiMuNuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 160.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/K_forB2DXD2HMuNu

|                 |                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV)& (P\> 3000\* MeV)& (TRGHOSTPROB \< 0.4)& (PIDK-PIDpi\> 5.0 ) & (PIDK-PIDp\> 5.0 ) & (PIDK-PIDmu\> 5.0 ) & (MIPCHI2DV(PRIMARY)\> 4.0 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]                                                                          |
| DecayDescriptor | None                                                                                                                                                   |
| Output          | Phys/K_forB2DXD2HMuNu/Particles                                                                                                                        |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Pi_forB2DXD2HMuNu

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV)& (P\> 3000\* MeV)& (TRGHOSTPROB \< 0.4)& (PIDK-PIDpi\< 0.0 ) & (PIDp \< 0.0 ) & (PIDmu \< 0.0 ) & (MIPCHI2DV(PRIMARY)\> 4.0 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/Pi_forB2DXD2HMuNu/Particles                                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forB2DXD2HMuNu

|                 |                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200\* MeV)& (P\> 3000\* MeV)& (TRGHOSTPROB \< 0.4)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 4.0 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' ]                                                                         |
| DecayDescriptor | None                                                                                                                                                  |
| Output          | Phys/Mu_forB2DXD2HMuNu/Particles                                                                                                                      |

DaVinci::N4BodyDecays/D02KPiPiMuNu_forB2DXD2HMuNu

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_forB2DXD2HMuNu' , 'Phys/Mu_forB2DXD2HMuNu' , 'Phys/Pi_forB2DXD2HMuNu' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }    |
| CombinationCut   | (ADOCA(1,4)\<0.2\*mm) & (ADOCA(2,4)\<0.2\*mm) & (ADOCA(3,4)\<0.2\*mm) & (ASUM(PT)\>1500\*MeV) & (AM\<1800\*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 10 )& (BPVVDCHI2 \>36)                                                                    |
| DecayDescriptor  | None                                                                                                            |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- mu+]cc' ]                                                                             |
| Output           | Phys/D02KPiPiMuNu_forB2DXD2HMuNu/Particles                                                                      |

CombineParticles/B2D0KD02KPiPiMuNuLine

|                  |                                                                             |
|------------------|-----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02KPiPiMuNu_forB2DXD2HMuNu' , 'Phys/K_forB2DXD2HMuNu' ]          |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' } |
| CombinationCut   | (AM\<5200 \*MeV)                                                            |
| MotherCut        | (MDNDOCA(5.279,0) \< 0.02\*mm) & (lim_up\<0) & (lim_lo\>0)                  |
| DecayDescriptor  | None                                                                        |
| DecayDescriptors | [ '[B- -\> D0 K-]cc' ]                                                  |
| Output           | Phys/B2D0KD02KPiPiMuNuLine/Particles                                        |
