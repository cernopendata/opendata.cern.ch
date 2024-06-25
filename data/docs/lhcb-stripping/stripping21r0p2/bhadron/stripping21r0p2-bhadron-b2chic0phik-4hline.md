[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2Chic0phiK_4hLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2Chic0phiK_4hLine/Particles |
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

GaudiSequencer/MERGED:B2Chic0KPiSelChic0_4h

GaudiSequencer/MERGEDINPUTS:B2Chic0KPiSelChic0_4h

GaudiSequencer/INPUT:B2Chic0KPiSelChic02KKPiPi

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/B2Chic0KPiSelKaons4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PROBNNp \< 0.9) & (PROBNNpi \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelKaons4h/Particles                                                                                |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/B2Chic0KPiSelPions4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PROBNNk \< 0.9) & (PROBNNp \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelPions4h/Particles                                                                                |

DaVinci::N4BodyDecays/B2Chic0KPiSelChic02KKPiPi

|                  |                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelKaons4h' , 'Phys/B2Chic0KPiSelPions4h' ]                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                        |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.6\*GeV, AM, 4.1\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.0 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>50) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9)                                                                                                                                                                     |
| DecayDescriptor  | chi_c0(1P) -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'chi_c0(1P) -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                |
| Output           | Phys/B2Chic0KPiSelChic02KKPiPi/Particles                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02KKKK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/B2Chic0KPiSelKaons4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PROBNNp \< 0.9) & (PROBNNpi \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelKaons4h/Particles                                                                                |

DaVinci::N4BodyDecays/B2Chic0KPiSelChic02KKKK

|                  |                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelKaons4h' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                        |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.6\*GeV, AM, 4.1\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.0 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>50) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9)                                                                                                                                                                     |
| DecayDescriptor  | chi_c0(1P) -\> K+ K- K+ K-                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'chi_c0(1P) -\> K+ K- K+ K-' ]                                                                                                                                                                                                                                                                  |
| Output           | Phys/B2Chic0KPiSelChic02KKKK/Particles                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02PiPiPiPi

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/B2Chic0KPiSelPions4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PROBNNk \< 0.9) & (PROBNNp \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelPions4h/Particles                                                                                |

DaVinci::N4BodyDecays/B2Chic0KPiSelChic02PiPiPiPi

|                  |                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelPions4h' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                      |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.6\*GeV, AM, 4.1\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.0 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>50) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9)                                                                                                                                                                     |
| DecayDescriptor  | chi_c0(1P) -\> pi+ pi- pi+ pi-                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'chi_c0(1P) -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                              |
| Output           | Phys/B2Chic0KPiSelChic02PiPiPiPi/Particles                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02PPbarPiPi

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/B2Chic0KPiSelPions4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PROBNNk \< 0.9) & (PROBNNp \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelPions4h/Particles                                                                                |

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

DaVinci::N4BodyDecays/B2Chic0KPiSelChic02PPbarPiPi

|                  |                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelPions4h' , 'Phys/B2Chic0KPiSelProtons' ]                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                                       |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.6\*GeV, AM, 4.1\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.0 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>50) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9)                                                                                                                                                                     |
| DecayDescriptor  | chi_c0(1P) -\> p+ p~- pi+ pi-                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'chi_c0(1P) -\> p+ p~- pi+ pi-' ]                                                                                                                                                                                                                                                               |
| Output           | Phys/B2Chic0KPiSelChic02PPbarPiPi/Particles                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2Chic0KPiSelChic02PPbarKK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/B2Chic0KPiSelKaons4h

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PROBNNp \< 0.9) & (PROBNNpi \< 0.9) & (MIPCHI2DV()\>6) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                      |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/B2Chic0KPiSelKaons4h/Particles                                                                                |

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

DaVinci::N4BodyDecays/B2Chic0KPiSelChic02PPbarKK

|                  |                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelKaons4h' , 'Phys/B2Chic0KPiSelProtons' ]                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                                         |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.6\*GeV, AM, 4.1\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.0 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>50) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5.) & (in_range(2.7\*GeV, MM, 4.1\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>16) & (BPVDIRA\>0.9)                                                                                                                                                                     |
| DecayDescriptor  | chi_c0(1P) -\> p+ p~- K+ K-                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'chi_c0(1P) -\> p+ p~- K+ K-' ]                                                                                                                                                                                                                                                                 |
| Output           | Phys/B2Chic0KPiSelChic02PPbarKK/Particles                                                                                                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/B2Chic0KPiSelChic0_4h

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                    |
| Inputs          | [ 'Phys/B2Chic0KPiSelChic02KKKK' , 'Phys/B2Chic0KPiSelChic02KKPiPi' , 'Phys/B2Chic0KPiSelChic02PPbarKK' , 'Phys/B2Chic0KPiSelChic02PPbarPiPi' , 'Phys/B2Chic0KPiSelChic02PiPiPiPi' ] |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/B2Chic0KPiSelChic0_4h/Particles                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2Chic0phiK_4hLine

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2Chic0KPiSelChic0_4h' , 'Phys/B2Chic0KPiSelKaons' , 'Phys/B2Chic0KPiSelPhi' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'chi_c0(1P)' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0') \< 300 \*MeV)                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<16) & (BPVVDCHI2\>49)     |
| DecayDescriptor  | [B+ -\> chi_c0(1P) phi(1020) K+]cc                                                      |
| DecayDescriptors | [ '[B+ -\> chi_c0(1P) phi(1020) K+]cc' ]                                              |
| Output           | Phys/B2Chic0phiK_4hLine/Particles                                                         |

AddRelatedInfo/RelatedInfo1_B2Chic0phiK_4hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_4hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_B2Chic0phiK_4hLine/Particles |

AddRelatedInfo/RelatedInfo2_B2Chic0phiK_4hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_4hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo2_B2Chic0phiK_4hLine/Particles |

AddRelatedInfo/RelatedInfo3_B2Chic0phiK_4hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_4hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo3_B2Chic0phiK_4hLine/Particles |

AddRelatedInfo/RelatedInfo4_B2Chic0phiK_4hLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/B2Chic0phiK_4hLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo4_B2Chic0phiK_4hLine/Particles |
