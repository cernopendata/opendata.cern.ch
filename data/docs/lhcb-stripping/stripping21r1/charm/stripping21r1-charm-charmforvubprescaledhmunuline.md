[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmForVubPrescaledHMuNuLine

## Properties:

|                |                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/CharmForVubPrescaledHMuNuLine/Particles                                                                |
| Postscale      | 1.0000000                                                                                                   |
| HLT            | (HLT_PASS_RE('Hlt2CharmSemilepD02HMuNu\_.\*Decision') \| HLT_PASS_RE('Hlt2CharmHadD02HHXDst\_.\*Decision')) |
| Prescale       | 1.0000000                                                                                                   |
| L0DU           | None                                                                                                        |
| ODIN           | None                                                                                                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuonsForCharmForVubPrescaled

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ( 'mu+' == ABSID ) & ISMUON & (PT \> 800.0 \*MeV) & (PIDmu \> 0 )           |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/MuonsForCharmForVubPrescaled/Particles                                 |

GaudiSequencer/SeqMergedScalarHadronsD0HMuNuForCharmForVubPrescaled

GaudiSequencer/SEQ:PionsForCharmForVubPrescaled

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForCharmForVubPrescaled

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 600.0 ) & (PIDK \< 0 ) & ( -1.0 \< PIDpi - PIDmu)                    |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/PionsForCharmForVubPrescaled/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KaonsForCharmForVubPrescaled

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForCharmForVubPrescaled

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ( 'K+' == ABSID ) & ( 3.0 \< PIDK - PIDpi) & (PT \> 600.0 \*MeV)            |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KaonsForCharmForVubPrescaled/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergedScalarHadronsD0HMuNuForCharmForVubPrescaled

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/KaonsForCharmForVubPrescaled' , 'Phys/PionsForCharmForVubPrescaled' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/MergedScalarHadronsD0HMuNuForCharmForVubPrescaled/Particles                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/D0HMuNuForCharmForVubPrescaled

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergedScalarHadronsD0HMuNuForCharmForVubPrescaled' , 'Phys/MuonsForCharmForVubPrescaled' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                    |
| CombinationCut   | (AM \< 1950.0 \*MeV) & ((APT1+APT2) \> 2800.0 \*MeV) & (AMAXDOCA('') \< 0.07 \*mm )                                                             |
| MotherCut        | (P \> 20000.0 \*MeV) & (BPVVD \> 4.0 \*mm) & (in_range(1400.0 \*MeV ,BPVCORRM,2700.0 \*MeV)) & (BPVVDZ \> 0.0 \*mm) & (VFASPF(VCHI2/VDOF)\<9.0) |
| DecayDescriptor  | None                                                                                                                                            |
| DecayDescriptors | [ '[D0 -\> mu+ pi-]cc' , '[D0 -\> mu+ pi+]cc' , '[D0 -\> mu+ K+]cc' , '[D0 -\> mu+ K-]cc' ]                                           |
| Output           | Phys/D0HMuNuForCharmForVubPrescaled/Particles                                                                                                   |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/SlowPionsForCharmForVubPrescaled

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | ( -1.0 \< PIDpi - PIDmu)                                                          |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/SlowPionsForCharmForVubPrescaled/Particles                                   |

CombineParticles/CharmForVubPrescaledHMuNuLine

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D0HMuNuForCharmForVubPrescaled' , 'Phys/SlowPionsForCharmForVubPrescaled' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }         |
| CombinationCut   | (AM \> 300.0 \*MeV) & (AMAXDOCA('') \< 0.4 \*mm)                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9.0 ) & ( ( M - CHILD(M,1) ) \< 200.0 \*MeV )                   |
| DecayDescriptor  | None                                                                                  |
| DecayDescriptors | [ ' [D\*(2010)+ -\> D0 pi+]cc' , ' [D\*(2010)- -\> D0 pi-]cc' ]                 |
| Output           | Phys/CharmForVubPrescaledHMuNuLine/Particles                                          |
