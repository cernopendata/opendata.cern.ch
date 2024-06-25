[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBeauty2XGamma2pi_wCNVDD_Line

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/Beauty2XGamma2pi_wCNVDD_Line/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/TrackListBeauty2XGamma

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (HASTRACK) & (TRCHI2DOF \< 3.0)& (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (PT \> 300.0) & (P \> 1000) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                              |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/TrackListBeauty2XGamma/Particles                                                                              |

CombineParticles/DiTracksForRadiativeBBeauty2XGamma

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBeauty2XGamma' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }     |
| CombinationCut   | (ASUM(PT) \> 1000.0) & in_range( 0.0 , AM ,7900.0) |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0)         |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                              |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                      |
| Output           | Phys/DiTracksForRadiativeBBeauty2XGamma/Particles  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseGammaDD

|      |                                      |
|------|--------------------------------------|
| Code | 0StdAllLooseGammaDD/Particles',True) |

FilterDesktop/ConvDDPhotonBeauty2XGamma

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (MM \< 100\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9) & (PT \> 1000.0)               |
| Inputs          | [ 'Phys/[StdAllLooseGammaDD](./stripping21r0p2-commonparticles-stdallloosegammadd)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/ConvDDPhotonBeauty2XGamma/Particles                                                |

CombineParticles/Beauty2XGamma2pi_wCNVDD\_

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ConvDDPhotonBeauty2XGamma' , 'Phys/DiTracksForRadiativeBBeauty2XGamma' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'rho(770)0' : 'ALL' }                                |
| CombinationCut   | in_range( 2400.0 ,AM, 9000 )& (ASUM(PT) \> 3000 )                                     |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0) |
| DecayDescriptor  | B0 -\> rho(770)0 gamma                                                                |
| DecayDescriptors | [ 'B0 -\> rho(770)0 gamma' ]                                                        |
| Output           | Phys/Beauty2XGamma2pi_wCNVDD\_/Particles                                              |

TisTosParticleTagger/Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD\_' ]                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                      |
| Output          | Phys/Beauty2XGamma2pi_wCNVDD_Line/Particles                                                                                                                                                                                               |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TIS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo2_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo3_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo4_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo4_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo5_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo5_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo6_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo6_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo7_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo7_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo8_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo8_Beauty2XGamma2pi_wCNVDD_Line/Particles |

AddRelatedInfo/RelatedInfo9_Beauty2XGamma2pi_wCNVDD_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_wCNVDD_Line' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo9_Beauty2XGamma2pi_wCNVDD_Line/Particles |
