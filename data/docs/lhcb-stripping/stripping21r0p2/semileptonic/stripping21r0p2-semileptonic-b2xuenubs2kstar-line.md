[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuENuBs2Kstar_Line

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2XuENuBs2Kstar_Line/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuBs2Kstar_LineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseElectrons/Particles',True) |

FilterDesktop/E_forB2XuENu

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDe \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r0p2-commonparticles-stdlooseelectrons)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/E_forB2XuENu/Particles                                                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsLD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsLD/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS02PiPi_forB2XuENu

|                 |                                                                                                                                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVD \>20.0\*mm)& (MM\>456.0\*MeV)&(MM\<536.0\*MeV) & (BPVVDCHI2\> 0.0 ) & (PT \> 250.0\*MeV) & (VFASPF(VCHI2PDOF) \< 4.0) & CHILDCUT((TRCHI2DOF \< 4.0),1) & CHILDCUT((TRCHI2DOF \< 4.0),2) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),1) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),2) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p2-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLD](./stripping21r0p2-commonparticles-stdlooseksld)' , 'Phys/[StdVeryLooseKsLL](./stripping21r0p2-commonparticles-stdverylooseksll)' ]                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                               |
| Output          | Phys/KS02PiPi_forB2XuENu/Particles                                                                                                                                                                                                                                                                                 |

CombineParticles/Kstar_forB2XuENu

|                  |                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS02PiPi_forB2XuENu' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(PT\> 250.0\*MeV) &(P\> 3000.0\*MeV)& (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\>25.0)& (PIDK \< 2.0)' , 'pi-' : '(PT\> 250.0\*MeV) &(P\> 3000.0\*MeV)& (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\>25.0)& (PIDK \< 2.0)' } |
| CombinationCut   | (ADAMASS('K\*(892)+')\< 1200 )                                                                                                                                                                                                                                   |
| MotherCut        | (PT \> 800)                                                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                              |
| Output           | Phys/Kstar_forB2XuENu/Particles                                                                                                                                                                                                                                  |

CombineParticles/KstarE_forB2XuENu

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/E_forB2XuENu' , 'Phys/Kstar_forB2XuENu' ]                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                |
| CombinationCut   | ATRUE                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.99) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                    |
| DecayDescriptors | [ '[B_s~0 -\> K\*(892)+ e-]cc' ]                                                                    |
| Output           | Phys/KstarE_forB2XuENu/Particles                                                                        |

TisTosParticleTagger/B2XuENuBs2Kstar_Line

|                 |                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KstarE_forB2XuENu' ]                                                                                                      |
| DecayDescriptor | None                                                                                                                                |
| Output          | Phys/B2XuENuBs2Kstar_Line/Particles                                                                                                 |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE3Body.\*Decision%TOS' : 0 } |
