[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2D0KD2KSPi0HHDDMergedBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine/Particles                           |
| Postscale      | 1.0000000                                                                       |
| HLT1           | None                                                                            |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                       |
| L0DU           | None                                                                            |
| ODIN           | None                                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2D0KD2KSPi0HHDDMergedBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:D2HHKSPi0MergedDD

GaudiSequencer/MERGEDINPUTS:D2HHKSPi0MergedDD

GaudiSequencer/INPUT:ProtoD2pi+pi-KS0pi0DD_MergedBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

DaVinci::N4BodyDecays/ProtoD2pi+pi-KS0pi0DD_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1614.84\*MeV,AWM('pi+','pi-','KS0','pi0'),2114.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'D0 -\> pi+ pi- KS0 pi0' ]                                                                                                                                                                                                                                       |
| Output           | Phys/ProtoD2pi+pi-KS0pi0DD_MergedBeauty2Charm/Particles                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2pi+K-KS0pi0DD_MergedBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

DaVinci::N4BodyDecays/ProtoD2pi+K-KS0pi0DD_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                        |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1614.84\*MeV,AWM('pi+','K-','KS0','pi0'),2114.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ 'D0 -\> pi+ K- KS0 pi0' ]                                                                                                                                                                                                                                       |
| Output           | Phys/ProtoD2pi+K-KS0pi0DD_MergedBeauty2Charm/Particles                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+pi-KS0pi0DD_MergedBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

DaVinci::N4BodyDecays/ProtoD2K+pi-KS0pi0DD_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                        |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1614.84\*MeV,AWM('K+','pi-','KS0','pi0'),2114.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ 'D0 -\> K+ pi- KS0 pi0' ]                                                                                                                                                                                                                                       |
| Output           | Phys/ProtoD2K+pi-KS0pi0DD_MergedBeauty2Charm/Particles                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+K-KS0pi0DD_MergedBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

DaVinci::N4BodyDecays/ProtoD2K+K-KS0pi0DD_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/Pi0MergedInputsBeauty2CharmFilter' ]                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1614.84\*MeV,AWM('K+','K-','KS0','pi0'),2114.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ 'D0 -\> K+ K- KS0 pi0' ]                                                                                                                                                                                                                                       |
| Output           | Phys/ProtoD2K+K-KS0pi0DD_MergedBeauty2Charm/Particles                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHKSPi0MergedDD

|                 |                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                     |
| Inputs          | [ 'Phys/ProtoD2K+K-KS0pi0DD_MergedBeauty2Charm' , 'Phys/ProtoD2K+pi-KS0pi0DD_MergedBeauty2Charm' , 'Phys/ProtoD2pi+K-KS0pi0DD_MergedBeauty2Charm' , 'Phys/ProtoD2pi+pi-KS0pi0DD_MergedBeauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                                                                    |
| Output          | Phys/D2HHKSPi0MergedDD/Particles                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/B2D0KD2KSPi0HHDDMergedBeauty2CharmCombCutD2HHKSPi0MergedDD

|      |                                                      |
|------|------------------------------------------------------|
| Code | (CONTAINS('Phys/D2HHKSPi0MergedDD/Particles')\<2000) |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                             |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                     |

LoKi::VoidFilter/B2D0KD2KSPi0HHDDMergedBeauty2CharmCombCutKTopoInputsBeauty2CharmFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | (CONTAINS('Phys/KTopoInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/B2D0KD2KSPi0HHDDMergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHKSPi0MergedDD' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                                            |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'B+ -\> D0 K+' , 'B- -\> D0 K-' ]                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/B2D0KD2KSPi0HHDDMergedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                      |

TisTosParticleTagger/B2D0KD2KSPi0HHDDMergedBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2Charm' ]                                                                                             |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmTISTOS/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2D0KD2KSPi0HHDDMergedBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                            |
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                       |
| Output          | Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Code            | ALL                                                                      |
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                     |
| Output          | Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo1_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo2_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSPi0HHDDMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo3_B2D0KD2KSPi0HHDDMergedBeauty2CharmLine/Particles |
