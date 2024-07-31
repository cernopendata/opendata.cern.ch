[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDstarD2XGammaDstarD2PiPiGamma_CNVLLLine

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLLine/Particles |
| Postscale      | 1.0000000                                              |
| HLT1           | None                                                   |
| HLT2           | None                                                   |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharmCompleteEvent

|      |                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamCharmCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsKaons/Particles',True) |

CombineParticles/DstarD2XGammaHHForD2PiPiGamma

|                  |                                                                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsKaons](./stripping21r0p2-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4)&(PT \> 250.0)&(MIPCHI2DV(PRIMARY) \> 3 )&(PIDK \> 5)' , 'pi+' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4)&(PT \> 250.0)&(MIPCHI2DV(PRIMARY) \> 3 )&(PIDK \< 0)' , 'pi-' : ' (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4)&(PT \> 250.0)&(MIPCHI2DV(PRIMARY) \> 3 )&(PIDK \< 0)' } |
| CombinationCut   | (in_range( 0.0, AM, 1865.0 ) ) &( (APT1+APT2) \> 0.0 )&( ACHI2DOCA(1,2) \< 10.0 )                                                                                                                                                                                                                                                     |
| MotherCut        | (in_range( 0.0, M, 1865.0 )) &(VFASPF(VCHI2PDOF) \< 16.0)&( BPVVDCHI2 \> 100.0 )                                                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/DstarD2XGammaHHForD2PiPiGamma/Particles                                                                                                                                                                                                                                                                                          |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseGammaLL

|      |                                      |
|------|--------------------------------------|
| Code | 0StdAllLooseGammaLL/Particles',True) |

FilterDesktop/CNVGammaLLForDstarD2XGamma

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( MM \< 100.0 \* MeV ) &( HASVERTEX ) &( VFASPF(VCHI2/VDOF)\<9 ) &( PT \> 1000.0)       |
| Inputs          | [ 'Phys/[StdAllLooseGammaLL](./stripping21r0p2-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/CNVGammaLLForDstarD2XGamma/Particles                                               |

CombineParticles/DstarD2XGammaD2PiPiGamma_CNVLL

|                  |                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CNVGammaLLForDstarD2XGamma' , 'Phys/DstarD2XGammaHHForD2PiPiGamma' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                               |
| CombinationCut   | (in_range( 1610.0, AM, 2130.0 ))                                                                                                                     |
| MotherCut        | (in_range( 1610.0\* MeV, M, 2100.0 )) &(PT \> 2000.0)&(VFASPF(VCHI2PDOF) \< 12.0)&(BPVDIRA \> 0.9995 )&(BPVLTIME() \> 0.0001 )&(BPVIPCHI2() \< 35.0) |
| DecayDescriptor  | None                                                                                                                                                 |
| DecayDescriptors | [ 'D0 -\> rho(770)0 gamma' ]                                                                                                                       |
| Output           | Phys/DstarD2XGammaD2PiPiGamma_CNVLL/Particles                                                                                                        |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/DstarD2XGammaDstarD2PiPiGamma_CNVLLSel

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarD2XGammaD2PiPiGamma_CNVLL' , 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF \< 3)' , 'pi-' : '(TRCHI2DOF \< 3)' }                       |
| CombinationCut   | ((AM - AM1) \< 180.0)                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15.0)&((M - M1) \< 163.0)                                                                              |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                                       |
| Output           | Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLSel/Particles                                                                         |

TisTosParticleTagger/DstarD2XGammaDstarD2PiPiGamma_CNVLLDstarHlt1TOS

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLSel' ]            |
| DecayDescriptor | None                                                           |
| Output          | Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLDstarHlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1Track.\*Decision%TOS' : 0 }                             |

TisTosParticleTagger/DstarD2XGammaDstarD2PiPiGamma_CNVLLLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLDstarHlt1TOS' ]                         |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/DstarD2XGammaDstarD2PiPiGamma_CNVLLLine/Particles                               |
| TisTosSpecs     | { 'Hlt2CharmHadD02HHXDst_hhX.\*Decision%TOS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 } |
