[[stripping21 lines]](./stripping21-index)

# StrippingBs2EtacPhiBDT_KsKPiLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Bs2EtacPhiBDT_KsKPiLine/Particles                                       |
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

GaudiSequencer/SeqBs2EtacPhiBDTInputKs

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/Bs2EtacPhiBDTInputKs

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Bs2EtacPhiBDTInputKs/Particles                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Bs2EtacPhiBDTSelKs

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVDLS\>5) |
| Inputs          | [ 'Phys/Bs2EtacPhiBDTInputKs' ]         |
| DecayDescriptor | None                                      |
| Output          | Phys/Bs2EtacPhiBDTSelKs/Particles         |

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

CombineParticles/Bs2EtacPhiBDTSelEtac2KsKPi

|                  |                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelKaons' , 'Phys/Bs2EtacPhiBDTSelKs' , 'Phys/Bs2EtacPhiBDTSelPions' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }  |
| CombinationCut   | (in_range(2.75\*GeV, AM, 3.25\*GeV))                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 2.)  |
| DecayDescriptor  | [eta_c(1S) -\> KS0 K+ pi-]cc                                                                |
| DecayDescriptors | [ '[eta_c(1S) -\> KS0 K+ pi-]cc' ]                                                        |
| Output           | Phys/Bs2EtacPhiBDTSelEtac2KsKPi/Particles                                                     |

CombineParticles/Bs2EtacPhiBDT_KsKPiLine

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2EtacPhiBDTSelEtac2KsKPi' , 'Phys/Bs2EtacPhiBDTSelPhi' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'eta_c(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                       |
| CombinationCut   | (ADAMASS('B_s0') \< 500 \*MeV)                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.99) & (BPVIPCHI2()\<25) & (BPVDLS\>0) |
| DecayDescriptor  | B_s0 -\> eta_c(1S) phi(1020)                                                     |
| DecayDescriptors | [ 'B_s0 -\> eta_c(1S) phi(1020)' ]                                             |
| Output           | Phys/Bs2EtacPhiBDT_KsKPiLine/Particles                                           |
