[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2EtaMuMuAllX0SelectionLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2EtaMuMuAllX0SelectionLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

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

GaudiSequencer/MERGED:MergeDiTracksForB2EtaMuMuB2EtaMuMu

GaudiSequencer/MERGEDINPUTS:MergeDiTracksForB2EtaMuMuB2EtaMuMu

GaudiSequencer/INPUT:DiTracksForB2EtaMuMuB2EtaMuMu_2body

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2EtaMuMu

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500.0)              |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2EtaMuMu/Particles                                               |

CombineParticles/DiTracksForB2EtaMuMuB2EtaMuMu_2body

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TrackListB2EtaMuMu' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }     |
| CombinationCut   | (APT\> 600.0) & (AM\< 1100.0)                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                        |
| DecayDescriptor  | None                                               |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                      |
| Output           | Phys/DiTracksForB2EtaMuMuB2EtaMuMu_2body/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:DiTracksForB2EtaMuMuB2EtaMuMu_gamma

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2EtaMuMu

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500.0)              |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2EtaMuMu/Particles                                               |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/Gamma_for_Res_ListB2EtaMuMu

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 400.0\*MeV) & (CL \> 0.2)                                                        |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Gamma_for_Res_ListB2EtaMuMu/Particles                                              |

CombineParticles/DiTracksForB2EtaMuMuB2EtaMuMu_gamma

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/Gamma_for_Res_ListB2EtaMuMu' , 'Phys/TrackListB2EtaMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }     |
| CombinationCut   | (APT\> 600.0) & (AM\< 1100.0)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                                          |
| DecayDescriptor  | None                                                                 |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi- gamma' ]                                  |
| Output           | Phys/DiTracksForB2EtaMuMuB2EtaMuMu_gamma/Particles                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:DiTracksForB2EtaMuMuB2EtaMuMu_pi0

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TrackListB2EtaMuMu

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500.0)              |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TrackListB2EtaMuMu/Particles                                               |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0_for_Res_ListB2EtaMuMu

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 600.0\*MeV)                                                                                                                                                          |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                        |
| Output          | Phys/Pi0_for_Res_ListB2EtaMuMu/Particles                                                                                                                                    |

CombineParticles/DiTracksForB2EtaMuMuB2EtaMuMu_pi0

|                  |                                                                    |
|------------------|--------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0_for_Res_ListB2EtaMuMu' , 'Phys/TrackListB2EtaMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }     |
| CombinationCut   | (APT\> 600.0) & (AM\< 1100.0)                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                                        |
| DecayDescriptor  | None                                                               |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi- pi0' ]                                  |
| Output           | Phys/DiTracksForB2EtaMuMuB2EtaMuMu_pi0/Particles                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeDiTracksForB2EtaMuMuB2EtaMuMu

|                 |                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                      |
| Inputs          | [ 'Phys/DiTracksForB2EtaMuMuB2EtaMuMu_2body' , 'Phys/DiTracksForB2EtaMuMuB2EtaMuMu_gamma' , 'Phys/DiTracksForB2EtaMuMuB2EtaMuMu_pi0' ] |
| DecayDescriptor | None                                                                                                                                     |
| Output          | Phys/MergeDiTracksForB2EtaMuMuB2EtaMuMu/Particles                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsMuons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsMuons/Particles',True) |

FilterDesktop/Muon_for_DiMuon_ListB2EtaMuMu

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9.0) & (TRGHOSTPROB \< 0.5) & (PT \> 500.0) & (PIDmu\> -3.0)   |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r0p2-commonparticles-stdallnopidsmuons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Muon_for_DiMuon_ListB2EtaMuMu/Particles                                          |

CombineParticles/DiMuonForB2EtaMuMuB2EtaMuMu

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/Muon_for_DiMuon_ListB2EtaMuMu' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (APT\> 600.0) & (AM\< 6100.0)                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                    |
| DecayDescriptor  | None                                           |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                  |
| Output           | Phys/DiMuonForB2EtaMuMuB2EtaMuMu/Particles     |

CombineParticles/B2EtaMuMuAllX0Selection

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiMuonForB2EtaMuMuB2EtaMuMu' , 'Phys/MergeDiTracksForB2EtaMuMuB2EtaMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'rho(770)0' : 'ALL' }                           |
| CombinationCut   | in_range( 4900.0 ,AM, 6000.0 ) & ( APT \> 2500 )                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0) & (BPVDIRA \> 0.995)                                     |
| DecayDescriptor  | B0 -\> rho(770)0 J/psi(1S)                                                           |
| DecayDescriptors | [ 'B0 -\> rho(770)0 J/psi(1S)' ]                                                   |
| Output           | Phys/B2EtaMuMuAllX0Selection/Particles                                               |

TisTosParticleTagger/B2EtaMuMuAllX0SelectionLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0Selection' ]       |
| DecayDescriptor | None                                       |
| Output          | Phys/B2EtaMuMuAllX0SelectionLine/Particles |
| TisTosSpecs     | { 'Hlt1(Two)?Track.\*Decision%TOS' : 0 }   |

AddRelatedInfo/RelatedInfo1_B2EtaMuMuAllX0SelectionLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_B2EtaMuMuAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo2_B2EtaMuMuAllX0SelectionLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_B2EtaMuMuAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo3_B2EtaMuMuAllX0SelectionLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_B2EtaMuMuAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo4_B2EtaMuMuAllX0SelectionLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo4_B2EtaMuMuAllX0SelectionLine/Particles |

AddRelatedInfo/RelatedInfo5_B2EtaMuMuAllX0SelectionLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2EtaMuMuAllX0SelectionLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo5_B2EtaMuMuAllX0SelectionLine/Particles |
