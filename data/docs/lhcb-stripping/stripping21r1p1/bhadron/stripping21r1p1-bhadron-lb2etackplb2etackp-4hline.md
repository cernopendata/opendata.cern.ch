[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingLb2EtacKpLb2EtacKp_4hLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Lb2EtacKpLb2EtacKp_4hLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelProtons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                         |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Lb2EtacKpSelProtons/Particles                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                      |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelKaons/Particles                                              |

CombineParticles/Lb2EtacKpSelLambdaS

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelKaons' , 'Phys/Lb2EtacKpSelProtons' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }              |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 900.\*MeV) & (AM \< 4.0 \*GeV) & (ADOCACHI2CUT(20., ''))   |
| MotherCut        | (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2 \> 10.) & (VFASPF(VCHI2) \< 9.) & (BPVDIRA\>0.9) |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                            |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                    |
| Output           | Phys/Lb2EtacKpSelLambdaS/Particles                                                       |

GaudiSequencer/SeqLb2EtacKpSelEtac

GaudiSequencer/SEQ:Lb2EtacKpSelEtac2KKPiPi

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                      |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelKaons/Particles                                              |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelPions

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelPions/Particles                                              |

DaVinci::N4BodyDecays/Lb2EtacKpSelEtac2KKPiPi

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelKaons' , 'Phys/Lb2EtacKpSelPions' ]                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                          |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9)                                                                                                                                                                       |
| DecayDescriptor  | eta_c(1S) -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'eta_c(1S) -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                   |
| Output           | Phys/Lb2EtacKpSelEtac2KKPiPi/Particles                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Lb2EtacKpSelEtac2KKKK

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                      |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelKaons/Particles                                              |

DaVinci::N4BodyDecays/Lb2EtacKpSelEtac2KKKK

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelKaons' ]                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                          |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9)                                                                                                                                                                       |
| DecayDescriptor  | eta_c(1S) -\> K+ K- K+ K-                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'eta_c(1S) -\> K+ K- K+ K-' ]                                                                                                                                                                                                                                                                     |
| Output           | Phys/Lb2EtacKpSelEtac2KKKK/Particles                                                                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Lb2EtacKpSelEtac2PiPiPiPi

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelPions

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelPions/Particles                                              |

DaVinci::N4BodyDecays/Lb2EtacKpSelEtac2PiPiPiPi

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelPions' ]                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                        |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9)                                                                                                                                                                       |
| DecayDescriptor  | eta_c(1S) -\> pi+ pi- pi+ pi-                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'eta_c(1S) -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                                 |
| Output           | Phys/Lb2EtacKpSelEtac2PiPiPiPi/Particles                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Lb2EtacKpSelEtac2PPbarPiPi

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelPions

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelPions/Particles                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelProtons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                         |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Lb2EtacKpSelProtons/Particles                                                |

DaVinci::N4BodyDecays/Lb2EtacKpSelEtac2PPbarPiPi

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelPions' , 'Phys/Lb2EtacKpSelProtons' ]                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                                         |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9)                                                                                                                                                                       |
| DecayDescriptor  | eta_c(1S) -\> p+ p~- pi+ pi-                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'eta_c(1S) -\> p+ p~- pi+ pi-' ]                                                                                                                                                                                                                                                                  |
| Output           | Phys/Lb2EtacKpSelEtac2PPbarPiPi/Particles                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Lb2EtacKpSelEtac

|                 |                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                        |
| Inputs          | [ 'Phys/Lb2EtacKpSelEtac2KKKK' , 'Phys/Lb2EtacKpSelEtac2KKPiPi' , 'Phys/Lb2EtacKpSelEtac2PPbarPiPi' , 'Phys/Lb2EtacKpSelEtac2PiPiPiPi' ] |
| DecayDescriptor | None                                                                                                                                       |
| Output          | Phys/Lb2EtacKpSelEtac/Particles                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Lb2EtacKpLb2EtacKp_4hLine

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelEtac' , 'Phys/Lb2EtacKpSelLambdaS' ]                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'eta_c(1S)' : 'ALL' }                                         |
| CombinationCut   | (ADAMASS('Lambda_b0') \< 500 \*MeV)                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<25) & (BPVVDCHI2\>250) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm) |
| DecayDescriptor  | [Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc                                                                                       |
| DecayDescriptors | [ '[Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc' ]                                                                               |
| Output           | Phys/Lb2EtacKpLb2EtacKp_4hLine/Particles                                                                                          |

AddRelatedInfo/RelatedInfo1_Lb2EtacKpLb2EtacKp_4hLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKpLb2EtacKp_4hLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_Lb2EtacKpLb2EtacKp_4hLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2EtacKpLb2EtacKp_4hLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKpLb2EtacKp_4hLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_Lb2EtacKpLb2EtacKp_4hLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2EtacKpLb2EtacKp_4hLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKpLb2EtacKp_4hLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_Lb2EtacKpLb2EtacKp_4hLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2EtacKpLb2EtacKp_4hLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKpLb2EtacKp_4hLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_Lb2EtacKpLb2EtacKp_4hLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2EtacKpLb2EtacKp_4hLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKpLb2EtacKp_4hLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo5_Lb2EtacKpLb2EtacKp_4hLine/Particles |
