[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine/Particles                     |
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

LoKi::VoidFilter/StrippingBc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:BC2DD-Dst2D0PID02KSHH-Beauty2Charm

GaudiSequencer/MERGEDINPUTS:BC2DD-Dst2D0PID02KSHH-Beauty2Charm

GaudiSequencer/INPUT:DstarD2KSHHLLPID2D0PiBeauty2Charm

GaudiSequencer/MERGED:D2KsHHLLBeauty2Charm

GaudiSequencer/MERGEDINPUTS:D2KsHHLLBeauty2Charm

GaudiSequencer/INPUT:ProtoD2pi+pi-KS0LLBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

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

DaVinci::N3BodyDecays/ProtoD2pi+pi-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2pi+pi-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2pi+K-KS0LLBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

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

DaVinci::N3BodyDecays/ProtoD2pi+K-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> pi+ K- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2pi+K-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+pi-KS0LLBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

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

DaVinci::N3BodyDecays/ProtoD2K+pi-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> K+ pi- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2K+pi-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+K-KS0LLBeauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

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

DaVinci::N3BodyDecays/ProtoD2K+K-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2K+K-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHLLBeauty2Charm

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/ProtoD2K+K-KS0LLBeauty2Charm' , 'Phys/ProtoD2K+pi-KS0LLBeauty2Charm' , 'Phys/ProtoD2pi+K-KS0LLBeauty2Charm' , 'Phys/ProtoD2pi+pi-KS0LLBeauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/D2KsHHLLBeauty2Charm/Particles                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHLLPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHHLLBeauty2Charm' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHHLLPIDBeauty2CharmFilter/Particles                                                                                                                            |

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

CombineParticles/DstarD2KSHHLLPID2D0PiBeauty2Charm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHLLPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 600\*MeV) & (ADOCA(1,2)\<0.5\*mm)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV) |
| DecayDescriptor  | None                                                                                               |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                                            |
| Output           | Phys/DstarD2KSHHLLPID2D0PiBeauty2Charm/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:DstarD2KSHHDDPID2D0PiBeauty2Charm

GaudiSequencer/MERGED:D2KsHHDDBeauty2Charm

GaudiSequencer/MERGEDINPUTS:D2KsHHDDBeauty2Charm

GaudiSequencer/INPUT:ProtoD2pi+pi-KS0DDBeauty2Charm

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

DaVinci::N3BodyDecays/ProtoD2pi+pi-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2pi+pi-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2pi+K-KS0DDBeauty2Charm

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

DaVinci::N3BodyDecays/ProtoD2pi+K-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> pi+ K- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2pi+K-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+pi-KS0DDBeauty2Charm

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

DaVinci::N3BodyDecays/ProtoD2K+pi-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> K+ pi- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2K+pi-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+K-KS0DDBeauty2Charm

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

DaVinci::N3BodyDecays/ProtoD2K+K-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' ]                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- KS0' ]                                                                                                                                                                                                                                     |
| Output           | Phys/ProtoD2K+K-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHDDBeauty2Charm

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/ProtoD2K+K-KS0DDBeauty2Charm' , 'Phys/ProtoD2K+pi-KS0DDBeauty2Charm' , 'Phys/ProtoD2pi+K-KS0DDBeauty2Charm' , 'Phys/ProtoD2pi+pi-KS0DDBeauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/D2KsHHDDBeauty2Charm/Particles                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHDDPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHHDDBeauty2Charm' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHHDDPIDBeauty2CharmFilter/Particles                                                                                                                            |

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

CombineParticles/DstarD2KSHHDDPID2D0PiBeauty2Charm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHDDPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 600\*MeV) & (ADOCA(1,2)\<0.5\*mm)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV) |
| DecayDescriptor  | None                                                                                               |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                                            |
| Output           | Phys/DstarD2KSHHDDPID2D0PiBeauty2Charm/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/BC2DD-Dst2D0PID02KSHH-Beauty2Charm

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                       |
| Inputs          | [ 'Phys/DstarD2KSHHDDPID2D0PiBeauty2Charm' , 'Phys/DstarD2KSHHLLPID2D0PiBeauty2Charm' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/BC2DD-Dst2D0PID02KSHH-Beauty2Charm/Particles                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmCombCutBC2DD-Dst2D0PID02KSHH-Beauty2Charm

|      |                                                                       |
|------|-----------------------------------------------------------------------|
| Code | (CONTAINS('Phys/BC2DD-Dst2D0PID02KSHH-Beauty2Charm/Particles')\<2000) |

GaudiSequencer/MERGED:D2HHBeauty2Charm

GaudiSequencer/MERGEDINPUTS:D2HHBeauty2Charm

GaudiSequencer/INPUT:ProtoD2pi+pi-Beauty2Charm

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

CombineParticles/ProtoD2pi+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2pi+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+pi-Beauty2Charm

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

CombineParticles/ProtoD2K+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> K+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+K-Beauty2Charm

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

CombineParticles/ProtoD2K+K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> K+ K-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K+K-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K-pi+Beauty2Charm

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

CombineParticles/ProtoD2K-pi+Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K-','pi+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> K- pi+' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K-pi+Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHBeauty2Charm

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/ProtoD2K+K-Beauty2Charm' , 'Phys/ProtoD2K+pi-Beauty2Charm' , 'Phys/ProtoD2K-pi+Beauty2Charm' , 'Phys/ProtoD2pi+pi-Beauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/D2HHBeauty2Charm/Particles                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHBeauty2Charm' ]                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHPIDBeauty2CharmFilter/Particles                                                                                                                                |

FilterDesktop/D2HHPIDTIGHTBeauty2CharmFilter

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -5),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -5), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/D2HHPIDBeauty2CharmFilter' ]                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/D2HHPIDTIGHTBeauty2CharmFilter/Particles                                                                                                                         |

LoKi::VoidFilter/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmCombCutD2HHPIDTIGHTBeauty2CharmFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | (CONTAINS('Phys/D2HHPIDTIGHTBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BC2DD-Dst2D0PID02KSHH-Beauty2Charm' , 'Phys/D2HHPIDTIGHTBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D\*\_s+' : 'ALL' , 'D\*\_s-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' }                                                                                                                                                                                                                                                                     |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6800\*MeV) & (AM\>4800\*MeV)                                                                                                                                                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.05\*ps) & (BPVIPCHI2()\<20) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'B_c+ -\> D\*(2010)+ D0' , 'B_c- -\> D\*(2010)- D0' , 'B_c+ -\> D\*\_s+ D0' , 'B_c- -\> D\*\_s- D0' ]                                                                                                                                                                                                                                                                                               |
| Output           | Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2Charm' ]                                                                                       |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmTISTOS/Particles                                                                               |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                  |
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                             |
| Output          | Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | ALL                                                                            |
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo1_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo2_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo3_Bc2DstD0Dst2D0PID02KSHHD02HHBeauty2CharmLine/Particles |
