[[stripping21 lines]](./stripping21-index)

# StrippingCharmForVubPrescaledVMuNuLine

## Properties:

|                |                                                                                              |
|----------------|----------------------------------------------------------------------------------------------|
| OutputLocation | Phys/CharmForVubPrescaledVMuNuLine/Particles                                                 |
| Postscale      | 1.0000000                                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2CharmSemilepD02HMuNu\_.\*Decision') \| HLT_PASS_RE('Hlt2Topo.\*Decision')) |
| Prescale       | 1.0000000                                                                                    |
| L0DU           | None                                                                                         |
| ODIN           | None                                                                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuonsForCharmForVubPrescaled

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | ( 'mu+' == ABSID ) & ISMUON & (PT \> 800.0 \*MeV) & (PIDmu \> 0 )         |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/MuonsForCharmForVubPrescaled/Particles                               |

FilterDesktop/MuonsFromBForCharmForVubPrescaled

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 6 )                       |
| Inputs          | [ 'Phys/MuonsForCharmForVubPrescaled' ]        |
| DecayDescriptor | None                                             |
| Output          | Phys/MuonsFromBForCharmForVubPrescaled/Particles |

GaudiSequencer/SeqMergedVectorHadronsDplus2VMuNuForCharmForVubPrescaled

GaudiSequencer/SEQ:KstarForCharmForVubPrescaled

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForCharmForVubPrescaled

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | ( 'K+' == ABSID ) & ( 3.0 \< PIDK - PIDpi) & (PT \> 600.0 \*MeV)          |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KaonsForCharmForVubPrescaled/Particles                               |

FilterDesktop/KaonsFromBForCharmForVubPrescaled

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 6 )                       |
| Inputs          | [ 'Phys/KaonsForCharmForVubPrescaled' ]        |
| DecayDescriptor | None                                             |
| Output          | Phys/KaonsFromBForCharmForVubPrescaled/Particles |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForCharmForVubPrescaled

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 600.0 ) & (PIDK \< 0 ) & ( -1.0 \< PIDpi - PIDmu)                  |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PionsForCharmForVubPrescaled/Particles                               |

FilterDesktop/PionsFromBForCharmForVubPrescaled

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 6 )                       |
| Inputs          | [ 'Phys/PionsForCharmForVubPrescaled' ]        |
| DecayDescriptor | None                                             |
| Output          | Phys/PionsFromBForCharmForVubPrescaled/Particles |

CombineParticles/KstarForCharmForVubPrescaled

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsFromBForCharmForVubPrescaled' , 'Phys/PionsFromBForCharmForVubPrescaled' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }              |
| CombinationCut   | (AM \< 1040.0 \*MeV) & (AM \> 750.0 \*MeV)                                                |
| MotherCut        | (PT \> 600.0 \*MeV)                                                                       |
| DecayDescriptor  | [K\*(892)0 -\> K- pi+]cc                                                                |
| DecayDescriptors | [ '[K\*(892)0 -\> K- pi+]cc' ]                                                        |
| Output           | Phys/KstarForCharmForVubPrescaled/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:RhoForCharmForVubPrescaled

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForCharmForVubPrescaled

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 600.0 ) & (PIDK \< 0 ) & ( -1.0 \< PIDpi - PIDmu)                  |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PionsForCharmForVubPrescaled/Particles                               |

FilterDesktop/PionsFromBForCharmForVubPrescaled

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 6 )                       |
| Inputs          | [ 'Phys/PionsForCharmForVubPrescaled' ]        |
| DecayDescriptor | None                                             |
| Output          | Phys/PionsFromBForCharmForVubPrescaled/Particles |

CombineParticles/RhoForCharmForVubPrescaled

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/PionsFromBForCharmForVubPrescaled' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM \< 1020 \*MeV) & (AM \> 530.0 \*MeV)       |
| MotherCut        | (PT \> 600.0 \*MeV)                            |
| DecayDescriptor  | rho(770)0 -\> pi- pi+                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi- pi+' ]                  |
| Output           | Phys/RhoForCharmForVubPrescaled/Particles      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergedVectorHadronsDplus2VMuNuForCharmForVubPrescaled

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | ALL                                                                           |
| Inputs          | [ 'Phys/KstarForCharmForVubPrescaled' , 'Phys/RhoForCharmForVubPrescaled' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MergedVectorHadronsDplus2VMuNuForCharmForVubPrescaled/Particles          |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Dplus2VMuNuForCharmForVubPrescaled

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergedVectorHadronsDplus2VMuNuForCharmForVubPrescaled' , 'Phys/MuonsFromBForCharmForVubPrescaled' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'rho(770)0' : 'ALL' }                               |
| CombinationCut   | (AM \< 1950.0 \*MeV) & ((APT1+APT2) \> 2800.0 \*MeV) & (AMAXDOCA('') \< 0.07 \*mm )                                                             |
| MotherCut        | (P \> 20000.0 \*MeV) & (BPVVD \> 4.0 \*mm) & (in_range(1400.0 \*MeV ,BPVCORRM,2700.0 \*MeV)) & (BPVVDZ \> 0.0 \*mm) & (VFASPF(VCHI2/VDOF)\<9.0) |
| DecayDescriptor  | None                                                                                                                                            |
| DecayDescriptors | [ '[D+ -\> mu+ K\*(892)0]cc' , '[D+ -\> mu+ rho(770)0]cc' ]                                                                               |
| Output           | Phys/Dplus2VMuNuForCharmForVubPrescaled/Particles                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForCharmForVubPrescaled

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 600.0 ) & (PIDK \< 0 ) & ( -1.0 \< PIDpi - PIDmu)                  |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PionsForCharmForVubPrescaled/Particles                               |

FilterDesktop/PionsFromBForCharmForVubPrescaled

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 6 )                       |
| Inputs          | [ 'Phys/PionsForCharmForVubPrescaled' ]        |
| DecayDescriptor | None                                             |
| Output          | Phys/PionsFromBForCharmForVubPrescaled/Particles |

CombineParticles/CharmForVubPrescaledVMuNuLine

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Dplus2VMuNuForCharmForVubPrescaled' , 'Phys/PionsFromBForCharmForVubPrescaled' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                         |
| CombinationCut   | ATRUE                                                                                                |
| MotherCut        | (in_range(2700.0 \*MeV ,( M - CHILD(M,1) ),3700.0 \*MeV)) & (BPVDIRA \> 0.9994) & (BPVVDCHI2 \> 100) |
| DecayDescriptor  | None                                                                                                 |
| DecayDescriptors | [ ' [B0 -\> D+ pi-]cc' , ' [B0 -\> D+ pi- pi+ pi-]cc' ]                                        |
| Output           | Phys/CharmForVubPrescaledVMuNuLine/Particles                                                         |
