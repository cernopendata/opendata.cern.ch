[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2CharmlessInclusive4piAllX0SelectionLine

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/B2CharmlessInclusive4piAllX0SelectionLine/Particles |
| Postscale      | 1.0000000                                                |
| HLT1           | None                                                     |
| HLT2           | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:MergeDiTracksForCharmlessBB2CharmlessInclusive

GaudiSequencer/MERGEDINPUTS:MergeDiTracksForCharmlessBB2CharmlessInclusive

GaudiSequencer/INPUT:DiTracksForCharmlessBB2CharmlessInclusive_2body

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2CharmlessInclusive

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500)               |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2CharmlessInclusive/Particles                                    |

CombineParticles/DiTracksForCharmlessBB2CharmlessInclusive_2body

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListB2CharmlessInclusive' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                 |
| CombinationCut   | (APT\> 600) & (AM\< 1100.0)                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6.0)                                    |
| DecayDescriptor  | None                                                           |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                  |
| Output           | Phys/DiTracksForCharmlessBB2CharmlessInclusive_2body/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:DiTracksForCharmlessBB2CharmlessInclusive_gamma

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2CharmlessInclusive

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500)               |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2CharmlessInclusive/Particles                                    |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/Gamma_for_Res_ListB2CharmlessInclusive

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 400.0\*MeV) & (CL \> 0.2)                                                        |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Gamma_for_Res_ListB2CharmlessInclusive/Particles                                   |

CombineParticles/DiTracksForCharmlessBB2CharmlessInclusive_gamma

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Gamma_for_Res_ListB2CharmlessInclusive' , 'Phys/TrackListB2CharmlessInclusive' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                           |
| CombinationCut   | (APT\> 600) & (AM\< 1100.0)                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6.0)                                                                |
| DecayDescriptor  | None                                                                                       |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi- gamma' ]                                                        |
| Output           | Phys/DiTracksForCharmlessBB2CharmlessInclusive_gamma/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:DiTracksForCharmlessBB2CharmlessInclusive_pi0

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2CharmlessInclusive

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500)               |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2CharmlessInclusive/Particles                                    |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0_for_Res_ListB2CharmlessInclusive

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 600.0\*MeV)                                                                                                                                                          |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                        |
| Output          | Phys/Pi0_for_Res_ListB2CharmlessInclusive/Particles                                                                                                                         |

CombineParticles/DiTracksForCharmlessBB2CharmlessInclusive_pi0

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0_for_Res_ListB2CharmlessInclusive' , 'Phys/TrackListB2CharmlessInclusive' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                           |
| CombinationCut   | (APT\> 600) & (AM\< 1100.0)                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6.0)                                                              |
| DecayDescriptor  | None                                                                                     |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi- pi0' ]                                                        |
| Output           | Phys/DiTracksForCharmlessBB2CharmlessInclusive_pi0/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeDiTracksForCharmlessBB2CharmlessInclusive

|                 |                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                          |
| Inputs          | [ 'Phys/DiTracksForCharmlessBB2CharmlessInclusive_2body' , 'Phys/DiTracksForCharmlessBB2CharmlessInclusive_gamma' , 'Phys/DiTracksForCharmlessBB2CharmlessInclusive_pi0' ] |
| DecayDescriptor | None                                                                                                                                                                         |
| Output          | Phys/MergeDiTracksForCharmlessBB2CharmlessInclusive/Particles                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2CharmlessInclusive4piAllX0Selection

|                  |                                                             |
|------------------|-------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeDiTracksForCharmlessBB2CharmlessInclusive' ] |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)0' : 'ALL' }                        |
| CombinationCut   | in_range( 4000.0 ,AM, 5700.0 ) & ( APT \> 2500.0 )          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6.0 ) & (BPVDIRA \> 0.995)           |
| DecayDescriptor  | B0 -\> rho(770)0 rho(770)0                                  |
| DecayDescriptors | [ 'B0 -\> rho(770)0 rho(770)0' ]                          |
| Output           | Phys/B2CharmlessInclusive4piAllX0Selection/Particles        |

TisTosParticleTagger/B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0Selection' ]       |
| DecayDescriptor | None                                                     |
| Output          | Phys/B2CharmlessInclusive4piAllX0SelectionLine/Particles |
| TisTosSpecs     | { 'Hlt1(Two)?Track.\*Decision%TOS' : 0 }                 |

AddRelatedInfo/RelatedInfo1_B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo1_B2CharmlessInclusive4piAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo2_B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo2_B2CharmlessInclusive4piAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo3_B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo3_B2CharmlessInclusive4piAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo4_B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo4_B2CharmlessInclusive4piAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo5_B2CharmlessInclusive4piAllX0SelectionLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2CharmlessInclusive4piAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo5_B2CharmlessInclusive4piAllX0SelectionLine/Particles |
