[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2XuMuNuBs2KstarSSLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2XuMuNuBs2KstarSSLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuBs2KstarSSLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forB2XuMuNu

|                 |                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' ]                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                              |
| Output          | Phys/Mu_forB2XuMuNu/Particles                                                                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLD](./stripping21r0p1-commonparticles-stdlooseksld)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS02PiPi_forB2XuMuNu

|                 |                                                                                                                                                                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVD \>20.0\*mm)& (MM\>456.0\*MeV)&(MM\<536.0\*MeV) & (BPVVDCHI2\> 100.0 ) & (PT \> 700.0\*MeV) & (VFASPF(VCHI2PDOF) \< 10.0) & CHILDCUT((TRCHI2DOF \< 4.0),1) & CHILDCUT((TRCHI2DOF \< 4.0),2) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),1) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),2) & (MIPCHI2DV(PRIMARY) \> 8.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLD](./stripping21r0p1-commonparticles-stdlooseksld)' , 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                  |
| Output          | Phys/KS02PiPi_forB2XuMuNu/Particles                                                                                                                                                                                                                                                                                   |

CombineParticles/Kstar_forB2XuMuNu

|                  |                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS02PiPi_forB2XuMuNu' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(PT\> 100.0\*MeV) &(P\> 2000.0\*MeV)& (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\>9.0)& (PIDpi-PIDK\>-10.0)' , 'pi-' : '(PT\> 100.0\*MeV) &(P\> 2000.0\*MeV)& (TRCHI2DOF \< 10.0 )& (MIPCHI2DV(PRIMARY)\>9.0)& (PIDpi-PIDK\>-10.0)' } |
| CombinationCut   | (ADAMASS('K\*(892)+')\< 200)                                                                                                                                                                                                                                                 |
| MotherCut        | ALL                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                                          |
| Output           | Phys/Kstar_forB2XuMuNu/Particles                                                                                                                                                                                                                                             |

CombineParticles/KstarMuSS_forB2XuMuNu

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kstar_forB2XuMuNu' , 'Phys/Mu_forB2XuMuNu' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }              |
| CombinationCut   | ATRUE                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                    |
| DecayDescriptors | [ '[B_s~0 -\> K\*(892)- mu-]cc' ]                                                                   |
| Output           | Phys/KstarMuSS_forB2XuMuNu/Particles                                                                    |

TisTosParticleTagger/B2XuMuNuBs2KstarSSLine

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KstarMuSS_forB2XuMuNu' ]                                                                                             |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuBs2KstarSSLine/Particles                                                                                          |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
