[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine/Particles                  |
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

LoKi::VoidFilter/StrippingBc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqD2HHHHBeauty2Charm

GaudiSequencer/SEQ:ProtoD2pi+pi+pi-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2pi+pi+pi-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+','pi-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> pi+ pi+ pi- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2pi+pi+pi-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2pi+pi+K-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2pi+pi+K-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+','K-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> pi+ pi+ K- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2pi+pi+K-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+pi+pi-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2K+pi+pi-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi+','pi-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ pi+ pi- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2K+pi+pi-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K+pi-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2K+K+pi-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K+','pi-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'D0 -\> K+ K+ pi- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2K+K+pi-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2pi+K+K-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2pi+K+K-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','K+','K-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'D0 -\> pi+ K+ K- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2pi+K+K-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2pi+pi+K-K-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2pi+pi+K-K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+','K-','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'D0 -\> pi+ pi+ K- K-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2pi+pi+K-K-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K+K-pi-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2K+K+K-pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K+','K-','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'D0 -\> K+ K+ K- pi-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2K+K+K-pi-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+pi+K-K-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2K+pi+K-K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi+','K-','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'D0 -\> K+ pi+ K- K-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2K+pi+K-K-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K+K-K-Beauty2Charm

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

DaVinci::N4BodyDecays/ProtoD2K+K+K-K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                              |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K+','K-','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'D0 -\> K+ K+ K- K-' ]                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/ProtoD2K+K+K-K-Beauty2Charm/Particles                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHHHBeauty2Charm

|                 |                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                |
| Inputs          | [ 'Phys/ProtoD2K+K+K-K-Beauty2Charm' , 'Phys/ProtoD2K+K+K-pi-Beauty2Charm' , 'Phys/ProtoD2K+K+pi-pi-Beauty2Charm' , 'Phys/ProtoD2K+pi+K-K-Beauty2Charm' , 'Phys/ProtoD2K+pi+pi-pi-Beauty2Charm' , 'Phys/ProtoD2pi+K+K-pi-Beauty2Charm' , 'Phys/ProtoD2pi+pi+K-K-Beauty2Charm' , 'Phys/ProtoD2pi+pi+K-pi-Beauty2Charm' , 'Phys/ProtoD2pi+pi+pi-pi-Beauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                               |
| Output          | Phys/D2HHHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2K3HBeauty2CharmFilter

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | NINTREE(ABSID=='K+') \> 0              |
| Inputs          | [ 'Phys/D2HHHHBeauty2Charm' ]        |
| DecayDescriptor | None                                   |
| Output          | Phys/D2K3HBeauty2CharmFilter/Particles |

FilterDesktop/D2K3HPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2K3HBeauty2CharmFilter' ]                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2K3HPIDBeauty2CharmFilter/Particles                                                                                                                               |

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

CombineParticles/DstarD2K3HPID2D0PiBeauty2Charm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2K3HPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                        |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 600\*MeV) & (ADOCA(1,2)\<0.5\*mm)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV) |
| DecayDescriptor  | None                                                                                               |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                                            |
| Output           | Phys/DstarD2K3HPID2D0PiBeauty2Charm/Particles                                                      |

GaudiSequencer/SeqD2HHBeauty2Charm

GaudiSequencer/SEQ:ProtoD2pi+pi-Beauty2Charm

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

CombineParticles/ProtoD2pi+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                            |
| Output           | Phys/ProtoD2pi+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+pi-Beauty2Charm

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

CombineParticles/ProtoD2K+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                     |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> K+ pi-' ]                                                                                                                                                                                                                                                            |
| Output           | Phys/ProtoD2K+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K+K-Beauty2Charm

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

CombineParticles/ProtoD2K+K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> K+ K-' ]                                                                                                                                                                                                                                                            |
| Output           | Phys/ProtoD2K+K-Beauty2Charm/Particles                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtoD2K-pi+Beauty2Charm

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

CombineParticles/ProtoD2K-pi+Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                     |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K-','pi+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> K- pi+' ]                                                                                                                                                                                                                                                            |
| Output           | Phys/ProtoD2K-pi+Beauty2Charm/Particles                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
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
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHBeauty2Charm' ]                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHPIDBeauty2CharmFilter/Particles                                                                                                                                |

CombineParticles/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHPIDBeauty2CharmFilter' , 'Phys/DstarD2K3HPID2D0PiBeauty2Charm' ]                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D\*\_s+' : 'ALL' , 'D\*\_s-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' }                                                                                                                                                                                                                                                                       |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6800\*MeV) & (AM\>4800\*MeV)                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.05\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'B_c+ -\> D\*(2010)+ D0' , 'B_c- -\> D\*(2010)- D0' , 'B_c+ -\> D\*\_s+ D0' , 'B_c- -\> D\*\_s- D0' ]                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                   |

TisTosParticleTagger/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2Charm' ]                                                                                 |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmTISTOS/Particles                                                                         |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                  |
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                             |
| Output          | Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | ALL                                                                            |
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo1_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo2_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                     |
| Output          | Phys/RelatedInfo3_Bc2DstD0Dst2D0PID02KHHHD02HHBeauty2CharmLine/Particles |
