[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBeauty2XGammapi_Ks0_Line

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Beauty2XGammapi_Ks0_Line/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

GaudiSequencer/MERGED:MergedKshorts

GaudiSequencer/MERGEDINPUTS:MergedKshorts

GaudiSequencer/INPUT:Phys/StdLooseKsDD

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdLooseKsLL

LoKi::VoidFilter/SELECT:Phys/StdLooseKsLL

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsLL/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergedKshorts

|                 |                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                 |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p2-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21r0p2-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                                |
| Output          | Phys/MergedKshorts/Particles                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/KS0SelBeauty2XGamma

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000) & (MM \> 480\*MeV) & (MM \< 515\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9) |
| Inputs          | [ 'Phys/MergedKshorts' ]                                                                 |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/KS0SelBeauty2XGamma/Particles                                                         |

CombineParticles/Track_wKs0ForRadiativeBBeauty2XGamma

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0SelBeauty2XGamma' , 'Phys/TrackListBeauty2XGamma' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }           |
| CombinationCut   | (ASUM(PT) \> 1000.0) & in_range( 0.0 , AM ,7900.0)                       |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| DecayDescriptor  | [rho(770)+ -\> pi+ KS0]cc                                              |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ KS0]cc' ]                                      |
| Output           | Phys/Track_wKs0ForRadiativeBBeauty2XGamma/Particles                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/PhotonSelBeauty2XGamma

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 2000.0) & (CL \> 0.0)                                                            |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/PhotonSelBeauty2XGamma/Particles                                                   |

CombineParticles/Beauty2XGammapi_Ks0\_

|                  |                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhotonSelBeauty2XGamma' , 'Phys/Track_wKs0ForRadiativeBBeauty2XGamma' ]                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' }                                                                                                                                                        |
| CombinationCut   | in_range( 2400.0 ,AM, 9000 ) & (ASUM(PT) \> 3000 )                                                                                                                                                                                  |
| MotherCut        | INTREE(ISBASIC & ((HASTRACK) & (P\>5000\*MeV) & (PT\>1000\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0) |
| DecayDescriptor  | [B+ -\> rho(770)+ gamma]cc                                                                                                                                                                                                        |
| DecayDescriptors | [ '[B+ -\> rho(770)+ gamma]cc' ]                                                                                                                                                                                                |
| Output           | Phys/Beauty2XGammapi_Ks0\_/Particles                                                                                                                                                                                                |

TisTosParticleTagger/Beauty2XGammapi_Ks0_Line

|                 |                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0\_' ]                                                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                      |
| Output          | Phys/Beauty2XGammapi_Ks0_Line/Particles                                                                                                                                                                                                   |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TIS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo2_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo3_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo4_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo5_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo5_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo6_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo6_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo7_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo7_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo8_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo8_Beauty2XGammapi_Ks0_Line/Particles |

AddRelatedInfo/RelatedInfo9_Beauty2XGammapi_Ks0_Line

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammapi_Ks0_Line' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo9_Beauty2XGammapi_Ks0_Line/Particles |
