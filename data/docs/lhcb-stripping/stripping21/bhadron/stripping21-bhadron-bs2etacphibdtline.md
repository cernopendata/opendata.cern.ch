[[stripping21 lines]](./stripping21-index)

# StrippingBs2EtacPhiBDTLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Bs2EtacPhiBDTLine/Particles                                             |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightPhi2KK_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightPhi2KK](./stripping21-commonparticles-stdtightphi2kk)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTSelPhi

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MAXTREE(ABSID=='K+',TRGHOSTPROB) \< 0.4) & (MM\<1.05\*GeV) & (PT\> 800\*MeV) & (MIPCHI2DV(PRIMARY) \> 2.) & (VFASPF(VCHI2) \< 9.) |
| Inputs          | [ 'Phys/[StdTightPhi2KK](./stripping21-commonparticles-stdtightphi2kk)' ]                                                        |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/Bs2EtacPhiBDTSelPhi/Particles                                                                                                 |

GaudiSequencer/SeqBs2EtacPhiBDTSelEtac

GaudiSequencer/SEQ:Bs2EtacPhiBDTSelEtac2KKPiPi

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTSelKaons

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.13) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/Bs2EtacPhiBDTSelKaons/Particles                                      |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTSelPions

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/Bs2EtacPhiBDTSelPions/Particles                                      |

DaVinci::N4BodyDecays/Bs2EtacPhiBDTSelEtac2KKPiPi

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelKaons' , 'Phys/Bs2EtacPhiBDTSelPions' ]                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                          |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 2.)                                                                                                                                                                                                          |
| DecayDescriptor  | eta_c(1S) -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'eta_c(1S) -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                   |
| Output           | Phys/Bs2EtacPhiBDTSelEtac2KKPiPi/Particles                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Bs2EtacPhiBDTSelEtac2KKKK

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTSelKaons

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.13) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                 |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/Bs2EtacPhiBDTSelKaons/Particles                                      |

DaVinci::N4BodyDecays/Bs2EtacPhiBDTSelEtac2KKKK

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelKaons' ]                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                          |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 2.)                                                                                                                                                                                                          |
| DecayDescriptor  | eta_c(1S) -\> K+ K- K+ K-                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'eta_c(1S) -\> K+ K- K+ K-' ]                                                                                                                                                                                                                                                                     |
| Output           | Phys/Bs2EtacPhiBDTSelEtac2KKKK/Particles                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Bs2EtacPhiBDTSelEtac2PiPiPiPi

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTSelPions

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/Bs2EtacPhiBDTSelPions/Particles                                      |

DaVinci::N4BodyDecays/Bs2EtacPhiBDTSelEtac2PiPiPiPi

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelPions' ]                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                        |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (in_range(2.75\*GeV, AM, 3.25\*GeV)) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 2.)                                                                                                                                                                                                          |
| DecayDescriptor  | eta_c(1S) -\> pi+ pi- pi+ pi-                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'eta_c(1S) -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                                 |
| Output           | Phys/Bs2EtacPhiBDTSelEtac2PiPiPiPi/Particles                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Bs2EtacPhiBDTSelEtac

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                |
| Inputs          | [ 'Phys/Bs2EtacPhiBDTSelEtac2KKKK' , 'Phys/Bs2EtacPhiBDTSelEtac2KKPiPi' , 'Phys/Bs2EtacPhiBDTSelEtac2PiPiPiPi' ] |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/Bs2EtacPhiBDTSelEtac/Particles                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Bs2EtacPhiBDTSelBs2EtacPhi

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelEtac' , 'Phys/Bs2EtacPhiBDTSelPhi' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'eta_c(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                       |
| CombinationCut   | (ADAMASS('B_s0') \< 500 \*MeV)                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.99) & (BPVIPCHI2()\<25) & (BPVDLS\>0) |
| DecayDescriptor  | B_s0 -\> eta_c(1S) phi(1020)                                                     |
| DecayDescriptors | [ 'B_s0 -\> eta_c(1S) phi(1020)' ]                                             |
| Output           | Phys/Bs2EtacPhiBDTSelBs2EtacPhi/Particles                                        |

FilterDesktop/Bs2EtacPhiBDTLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/Bs2EtacPhiBDTMvaBs2EtacPhi')\>0. |
| Inputs          | [ 'Phys/Bs2EtacPhiBDTSelBs2EtacPhi' ]                         |
| DecayDescriptor | None                                                            |
| Output          | Phys/Bs2EtacPhiBDTLine/Particles                                |
