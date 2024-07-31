[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingDsGammaForExcitedDsSpectroscopyLine

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/DsGammaForExcitedDsSpectroscopyLine/Particles |
| Postscale      | 1.0000000                                          |
| HLT1           | None                                               |
| HLT2           | None                                               |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

LoKi::VoidFilter/StrippingDsGammaForExcitedDsSpectroscopyLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdVeryTightDsplus2KKPi_Particles

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryTightDsplus2KKPi](./stripping21r0p1-commonparticles-stdverytightdsplus2kkpi)/Particles',True)\>0 |

FilterDesktop/DsForExcitedDsSpectroscopy

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((MAXTREE('pi+'==ABSID, PIDK-PIDpi) \< 3.0) & (MINTREE('K-'==ABSID, PIDK-PIDpi) \> 7.0 ) &((in_range ( 1010.0\* MeV , M12 , 1030.0\* MeV ))\|(in_range ( 836.0\* MeV , M13 , 956.0\* MeV ) & (abs(COSPOL('[D_s+ -\> ^K- K+ pi+]CC', '[D_s+ -\> K- K+ ^pi+]CC', False)) \> 0.4)))& (SUMTREE( ISBASIC , PT ) \> 2800.0\*MeV) & (2 \<= NINGENERATION((MIPCHI2DV(PRIMARY) \> 10.0 ) , 1)) & (PT \> 1000.0) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.0) & (BPVIPCHI2() \< 9.0) ) |
| Inputs          | [ 'Phys/[StdVeryTightDsplus2KKPi](./stripping21r0p1-commonparticles-stdverytightdsplus2kkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output          | Phys/DsForExcitedDsSpectroscopy/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)/Particles',True)\>0 |

CombineParticles/DsstarForExcitedDsSpectroscopy

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DsForExcitedDsSpectroscopy' , 'Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'gamma' : '(PT \> 400.0) & (CL \> 0.1)' }                                  |
| CombinationCut   | (AM - AM1) \< 1300.0\*MeV                                                                                                   |
| MotherCut        | ALL                                                                                                                         |
| DecayDescriptor  | [D\*\_s+ -\> D_s+ gamma]cc                                                                                                |
| DecayDescriptors | [ '[D\*\_s+ -\> D_s+ gamma]cc' ]                                                                                        |
| Output           | Phys/DsstarForExcitedDsSpectroscopy/Particles                                                                               |

Pi0Veto::Tagger/DsGammaForExcitedDsSpectroscopyLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Code            | "gamma" == ID                                      |
| Inputs          | [ 'Phys/DsstarForExcitedDsSpectroscopy' ]        |
| DecayDescriptor | None                                               |
| Output          | Phys/DsGammaForExcitedDsSpectroscopyLine/Particles |
