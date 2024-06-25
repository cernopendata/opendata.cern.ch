[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XuMuNuBu2RhoWSLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2XuMuNuBu2RhoWSLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XuMuNuBu2RhoWSLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuTightCuts_forB2XuMuNu

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/MuTightCuts_forB2XuMuNu/Particles                                                                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/Rho02PiPiWS_forB2XuMuNu

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\> 300.0 \*MeV) & (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\> 9.0 )& (PIDpi-PIDK\> -10.0 ) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PT\> 300.0 \*MeV) & (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\> 9.0 )& (PIDpi-PIDK\> -10.0 ) & (TRGHOSTPROB \< 0.5)' } |
| CombinationCut   | (ADAMASS('rho(770)0')\< 150.0)                                                                                                                                                                                                                                                   |
| MotherCut        | (MAXTREE('pi+'==ABSID,PT )\>800.0 \*MeV )& (VFASPF(VCHI2/VDOF) \< 6 ) & (PT \> 500.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4 ) & (BPVDIRA\> 0.9)                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[rho(770)0 -\> pi+ pi+]cc' ]                                                                                                                                                                                                                                              |
| Output           | Phys/Rho02PiPiWS_forB2XuMuNu/Particles                                                                                                                                                                                                                                           |

CombineParticles/RhoMuWS_forB2XuMuNu

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuTightCuts_forB2XuMuNu' , 'Phys/Rho02PiPiWS_forB2XuMuNu' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'rho(770)0' : 'ALL' }                 |
| CombinationCut   | (AM\>2000.0\*MeV) & (AM\<5500.0\*MeV)                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2.0) & (BPVDIRA\> 0.999) & (BPVVDCHI2 \>120.0) & (ratio \>0.4) |
| DecayDescriptor  | None                                                                                 |
| DecayDescriptors | [ '[B+ -\> rho(770)0 mu+]cc' ]                                                   |
| Output           | Phys/RhoMuWS_forB2XuMuNu/Particles                                                   |

TisTosParticleTagger/B2XuMuNuBu2RhoWSLine

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/RhoMuWS_forB2XuMuNu' ]                                                                                               |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuBu2RhoWSLine/Particles                                                                                            |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
