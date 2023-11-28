[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine/Particles                |
| Postscale      | 1.0000000                                                                    |
| HLT1           | None                                                                         |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingBc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqBC2DD-D2KSH-Beauty2Charm

GaudiSequencer/SEQ:D2KsHLLPIDBeauty2CharmFilter

GaudiSequencer/SeqD2KsHBeauty2Charm_LL

GaudiSequencer/SEQ:ProtoD+2KS0pi+LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

CombineParticles/ProtoD+2KS0pi+LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                            |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','pi+'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'D+ -\> KS0 pi+' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD+2KS0pi+LLBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD+2KS0K+LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

CombineParticles/ProtoD+2KS0K+LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                             |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','K+'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D+ -\> KS0 K+' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD+2KS0K+LLBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD-2KS0pi-LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

CombineParticles/ProtoD-2KS0pi-LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                            |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'D- -\> KS0 pi-' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD-2KS0pi-LLBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD-2KS0K-LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

CombineParticles/ProtoD-2KS0K-LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                             |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','K-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D- -\> KS0 K-' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD-2KS0K-LLBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHBeauty2Charm_LL

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                       |
| Inputs          | [ 'Phys/ProtoD+2KS0K+LLBeauty2Charm' , 'Phys/ProtoD+2KS0pi+LLBeauty2Charm' , 'Phys/ProtoD-2KS0K-LLBeauty2Charm' , 'Phys/ProtoD-2KS0pi-LLBeauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/D2KsHBeauty2Charm_LL/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHLLPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHBeauty2Charm_LL' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHLLPIDBeauty2CharmFilter/Particles                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D2KsHDDPIDBeauty2CharmFilter

GaudiSequencer/SeqD2KsHBeauty2Charm_DD

GaudiSequencer/SEQ:ProtoD+2KS0pi+DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

CombineParticles/ProtoD+2KS0pi+DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                            |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','pi+'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'D+ -\> KS0 pi+' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD+2KS0pi+DDBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD+2KS0K+DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

CombineParticles/ProtoD+2KS0K+DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                             |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','K+'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D+ -\> KS0 K+' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD+2KS0K+DDBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD-2KS0pi-DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

CombineParticles/ProtoD-2KS0pi-DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                            |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'D- -\> KS0 pi-' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD-2KS0pi-DDBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD-2KS0K-DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

CombineParticles/ProtoD-2KS0K-DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                             |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('KS0','K-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D- -\> KS0 K-' ]                                                                                                                                                                                                                                    |
| Output           | Phys/ProtoD-2KS0K-DDBeauty2Charm/Particles                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHBeauty2Charm_DD

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                       |
| Inputs          | [ 'Phys/ProtoD+2KS0K+DDBeauty2Charm' , 'Phys/ProtoD+2KS0pi+DDBeauty2Charm' , 'Phys/ProtoD-2KS0K-DDBeauty2Charm' , 'Phys/ProtoD-2KS0pi-DDBeauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/D2KsHBeauty2Charm_DD/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHDDPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHBeauty2Charm_DD' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHDDPIDBeauty2CharmFilter/Particles                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/BC2DD-D2KSH-Beauty2Charm

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/D2KsHDDPIDBeauty2CharmFilter' , 'Phys/D2KsHLLPIDBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/BC2DD-D2KSH-Beauty2Charm/Particles                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

GaudiSequencer/SeqBC2DD-Dst02D0PI0D02KSHH-Beauty2Charm

GaudiSequencer/SEQ:Dstar02D0KsHHLLPIDPi0allBeauty2Charm

GaudiSequencer/SeqD2KsHHLLBeauty2Charm

GaudiSequencer/SEQ:ProtoD2pi+pi-KS0LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

DaVinci::N3BodyDecays/ProtoD2pi+pi-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> pi+ pi- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2pi+pi-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2pi+K-KS0LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2pi+K-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ K- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2pi+K-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+pi-KS0LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2K+pi-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> K+ pi- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2K+pi-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K-KS0LLBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2K+K-KS0LLBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> K+ K- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2K+K-KS0LLBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
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
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHLLPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHHLLBeauty2Charm' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHHLLPIDBeauty2CharmFilter/Particles                                                                                                                            |

GaudiSequencer/SeqPi0AllBeauty2Charm

GaudiSequencer/SEQ:Pi0MergedInputsBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Pi0ResolvedInputsBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0ResolvedInputsBeauty2CharmFilter

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV) & (CHILD(CL,1)\>0.25) & (CHILD(CL,2)\>0.25) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ]  |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Pi0ResolvedInputsBeauty2CharmFilter/Particles                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Pi0AllBeauty2Charm

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                         |
| Inputs          | [ 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/Pi0ResolvedInputsBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Pi0AllBeauty2Charm/Particles                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Dstar02D0KsHHLLPIDPi0allBeauty2Charm

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHLLPIDBeauty2CharmFilter' , 'Phys/Pi0AllBeauty2Charm' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi0' : 'ALL' }          |
| CombinationCut   | (ADAMASS('D\*(2007)0') \< 600\*MeV)                                    |
| MotherCut        | (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV)                                 |
| DecayDescriptor  | None                                                                   |
| DecayDescriptors | [ 'D\*(2007)0 -\> D0 pi0' ]                                          |
| Output           | Phys/Dstar02D0KsHHLLPIDPi0allBeauty2Charm/Particles                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Dstar02D0KsHHDDPIDPi0allBeauty2Charm

GaudiSequencer/SeqD2KsHHDDBeauty2Charm

GaudiSequencer/SEQ:ProtoD2pi+pi-KS0DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

DaVinci::N3BodyDecays/ProtoD2pi+pi-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> pi+ pi- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2pi+pi-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2pi+K-KS0DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2pi+K-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ K- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2pi+K-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+pi-KS0DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2K+pi-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> K+ pi- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2K+pi-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K-KS0DDBeauty2Charm

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                          |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<999.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                        |

DaVinci::N3BodyDecays/ProtoD2K+K-KS0DDBeauty2Charm

|                  |                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/KS0_DDInputsBeauty2CharmFilter' ]                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-','KS0'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> K+ K- KS0' ]                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD2K+K-KS0DDBeauty2Charm/Particles                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
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
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2KsHHDDPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2KsHHDDBeauty2Charm' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2KsHHDDPIDBeauty2CharmFilter/Particles                                                                                                                            |

GaudiSequencer/SeqPi0AllBeauty2Charm

GaudiSequencer/SEQ:Pi0MergedInputsBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Pi0ResolvedInputsBeauty2CharmFilter

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0ResolvedInputsBeauty2CharmFilter

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV) & (CHILD(CL,1)\>0.25) & (CHILD(CL,2)\>0.25) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ]  |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Pi0ResolvedInputsBeauty2CharmFilter/Particles                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Pi0AllBeauty2Charm

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                         |
| Inputs          | [ 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/Pi0ResolvedInputsBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Pi0AllBeauty2Charm/Particles                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Dstar02D0KsHHDDPIDPi0allBeauty2Charm

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHDDPIDBeauty2CharmFilter' , 'Phys/Pi0AllBeauty2Charm' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi0' : 'ALL' }          |
| CombinationCut   | (ADAMASS('D\*(2007)0') \< 600\*MeV)                                    |
| MotherCut        | (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV)                                 |
| DecayDescriptor  | None                                                                   |
| DecayDescriptors | [ 'D\*(2007)0 -\> D0 pi0' ]                                          |
| Output           | Phys/Dstar02D0KsHHDDPIDPi0allBeauty2Charm/Particles                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/BC2DD-Dst02D0PI0D02KSHH-Beauty2Charm

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                             |
| Inputs          | [ 'Phys/Dstar02D0KsHHDDPIDPi0allBeauty2Charm' , 'Phys/Dstar02D0KsHHLLPIDPi0allBeauty2Charm' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/BC2DD-Dst02D0PI0D02KSHH-Beauty2Charm/Particles                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BC2DD-D2KSH-Beauty2Charm' , 'Phys/BC2DD-Dst02D0PI0D02KSHH-Beauty2Charm' ]                                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2007)0' : 'ALL' , 'D\*(2007)~0' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' }                                                                                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6800\*MeV) & (AM\>4800\*MeV)                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.05\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'B_c+ -\> D+ D\*(2007)0' , 'B_c- -\> D- D\*(2007)0' ]                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2Charm' ]                                                                               |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmTISTOS/Particles                                                                       |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                    |
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                               |
| Output          | Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | ALL                                                                              |
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                             |
| Output          | Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                       |
| Output          | Phys/RelatedInfo1_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                       |
| Output          | Phys/RelatedInfo2_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                       |
| Output          | Phys/RelatedInfo3_Bc2DDst0D2KSHDst02D0PI0D02KSHHBeauty2CharmLine/Particles |
