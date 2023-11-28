[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2Chic0phiK_2hLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2Chic0phiK_2hLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/B2Chic0KPiSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PT \> 300\*MeV) & (MIPCHI2DV()\>9) & (TRGHOSTPROB\<0.4)   |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/B2Chic0KPiSelKaons/Particles                                             |

CombineParticles/B2Chic0KPiSelPhi

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelKaons' ]                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                             |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 400.\*MeV) & (AM\>970.\*MeV) &(AM \< 1070 \*MeV) & (ADOCACHI2CUT(10., '')) |
| MotherCut        | (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2 \> 9.) & (VFASPF(VCHI2) \< 9.) & (BPVDIRA\>0.9)                  |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                      |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                              |
| Output           | Phys/B2Chic0KPiSelPhi/Particles                                                                          |

GaudiSequencer/MERGED:B2Chic0KPiSelChic0_2h

GaudiSequencer/MERGEDINPUTS:B2Chic0KPiSelChic0_2h

GaudiSequencer/INPUT:B2Chic0KPiSelChic02KK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/B2Chic0KPiSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PT \> 300\*MeV) & (MIPCHI2DV()\>9) & (TRGHOSTPROB\<0.4)   |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/B2Chic0KPiSelKaons/Particles                                             |

CombineParticles/B2Chic0KPiSelChic02KK

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelKaons' ]                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                    |
| CombinationCut   | (in_range(2.6\*GeV, AM, 4.2\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2))\> 1.5 \*GeV)                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9) |
| DecayDescriptor  | chi_c0(1P) -\> K+ K-                                                                                                            |
| DecayDescriptors | [ 'chi_c0(1P) -\> K+ K-' ]                                                                                                    |
| Output           | Phys/B2Chic0KPiSelChic02KK/Particles                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02PiPi

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/B2Chic0KPiSelPions

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PT \> 300\*MeV) & (MIPCHI2DV()\>9) & (TRGHOSTPROB\<0.4)  |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/B2Chic0KPiSelPions/Particles                                             |

CombineParticles/B2Chic0KPiSelChic02PiPi

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelPions' ]                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                  |
| CombinationCut   | (in_range(2.6\*GeV, AM, 4.2\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2))\> 1.5 \*GeV)                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9) |
| DecayDescriptor  | chi_c0(1P) -\> pi+ pi-                                                                                                          |
| DecayDescriptors | [ 'chi_c0(1P) -\> pi+ pi-' ]                                                                                                  |
| Output           | Phys/B2Chic0KPiSelChic02PiPi/Particles                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02PPbar

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

FilterDesktop/B2Chic0KPiSelProtons

|                 |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp \> 0.2) & (PT \> 300\*MeV) & (MIPCHI2DV()\>9) & (P \> 10\*GeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r0p2-commonparticles-stdlooseprotons)' ]            |
| DecayDescriptor | None                                                                                         |
| Output          | Phys/B2Chic0KPiSelProtons/Particles                                                          |

CombineParticles/B2Chic0KPiSelChic02PPbar

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelProtons' ]                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                   |
| CombinationCut   | (in_range(2.6\*GeV, AM, 4.2\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2))\> 1.5 \*GeV)                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9) |
| DecayDescriptor  | chi_c0(1P) -\> p+ p~-                                                                                                           |
| DecayDescriptors | [ 'chi_c0(1P) -\> p+ p~-' ]                                                                                                   |
| Output           | Phys/B2Chic0KPiSelChic02PPbar/Particles                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/B2Chic0KPiSelChic0_2h

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                   |
| Inputs          | [ 'Phys/B2Chic0KPiSelChic02KK' , 'Phys/B2Chic0KPiSelChic02PPbar' , 'Phys/B2Chic0KPiSelChic02PiPi' ] |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/B2Chic0KPiSelChic0_2h/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2Chic0phiK_2hLine

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelChic0_2h' , 'Phys/B2Chic0KPiSelKaons' , 'Phys/B2Chic0KPiSelPhi' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'chi_c0(1P)' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0') \< 300 \*MeV)                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<16) & (BPVVDCHI2\>49)     |
| DecayDescriptor  | [B+ -\> chi_c0(1P) phi(1020) K+]cc                                                      |
| DecayDescriptors | [ '[B+ -\> chi_c0(1P) phi(1020) K+]cc' ]                                              |
| Output           | Phys/B2Chic0phiK_2hLine/Particles                                                         |

AddRelatedInfo/RelatedInfo1_B2Chic0phiK_2hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_2hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_B2Chic0phiK_2hLine/Particles |

AddRelatedInfo/RelatedInfo2_B2Chic0phiK_2hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_2hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo2_B2Chic0phiK_2hLine/Particles |

AddRelatedInfo/RelatedInfo3_B2Chic0phiK_2hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_2hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo3_B2Chic0phiK_2hLine/Particles |

AddRelatedInfo/RelatedInfo4_B2Chic0phiK_2hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_2hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo4_B2Chic0phiK_2hLine/Particles |
