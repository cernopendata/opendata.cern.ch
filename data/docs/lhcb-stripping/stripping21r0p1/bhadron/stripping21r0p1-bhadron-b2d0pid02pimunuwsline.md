[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2D0PiD02PiMuNuWSLine

## Properties:

|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0PiD02PiMuNuWSLine/Particles                                                |
| Postscale      | 1.0000000                                                                           |
| HLT1           | None                                                                                |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision')) |
| Prescale       | 0.10000000                                                                          |
| L0DU           | None                                                                                |
| ODIN           | None                                                                                |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2D0PiD02PiMuNuWSLineVOIDFilter

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
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forB2DXD2HMuNu

|                 |                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200\* MeV)& (P\> 3000\* MeV)& (TRGHOSTPROB \< 0.4)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 4.0 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' ]                                                                         |
| DecayDescriptor | None                                                                                                                                                  |
| Output          | Phys/Mu_forB2DXD2HMuNu/Particles                                                                                                                      |

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

CombineParticles/D02PiMuNuWS_forB2DXD2HMuNu

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Mu_forB2DXD2HMuNu' , 'Phys/Pi_forB2DXD2HMuNu' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (ASUM(PT)\>1500\*MeV) & (ADOCA(1,2)\<0.2\*mm) & (AM\<1800\*MeV)                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 10 )& (cos\<0.99999)& (BPVVDCHI2 \>36)                   |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[D0 -\> pi- mu-]cc' ]                                                   |
| Output           | Phys/D02PiMuNuWS_forB2DXD2HMuNu/Particles                                      |

CombineParticles/B2D0PiD02PiMuNuWSLine

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02PiMuNuWS_forB2DXD2HMuNu' , 'Phys/Pi_forB2DXD2HMuNu' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM\<5200 \*MeV)                                                              |
| MotherCut        | (MDNDOCA(5.279,0) \< 0.02\*mm) & (lim_up\<0) & (lim_lo\>0)                    |
| DecayDescriptor  | None                                                                          |
| DecayDescriptors | [ '[B- -\> D0 pi-]cc' ]                                                   |
| Output           | Phys/B2D0PiD02PiMuNuWSLine/Particles                                          |
