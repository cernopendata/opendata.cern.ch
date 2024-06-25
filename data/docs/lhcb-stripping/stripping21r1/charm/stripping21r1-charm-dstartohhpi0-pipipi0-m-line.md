[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarToHHPi0_pipipi0_M_Line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/DstarToHHPi0_pipipi0_M_Line/Particles             |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst_hhX.\*Decision') |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarToHHPi0_pipipi0_M_LineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForDstarToHHPi0

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \< 0)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/PionsForDstarToHHPi0/Particles                                         |

CombineParticles/SelKstDstarToHHPi0_pipipi0_M\_

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForDstarToHHPi0' ]                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                             |
| CombinationCut   | (((ACHILD(PT,1) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),1) \> 36)) \| ((ACHILD(PT,2) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),2) \> 36))) & (AM \< 1850\*MeV) & (ADOCACHI2CUT(15,'')) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 3) & (BPVVDCHI2 \> 100)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[K\*(892)0 -\> pi- pi+]cc' ]                                                                                                                                        |
| Output           | Phys/SelKstDstarToHHPi0_pipipi0_M\_/Particles                                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/Pi0MForDstarToHHPi0

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV)                                                                   |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Pi0MForDstarToHHPi0/Particles                                                  |

CombineParticles/SelD0DstarToHHPi0_pipipi0_M\_

|                  |                                                                             |
|------------------|-----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0MForDstarToHHPi0' , 'Phys/SelKstDstarToHHPi0_pipipi0_M\_' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi0' : 'ALL' } |
| CombinationCut   | (ADAMASS('D0') \< 150 + 10 \*MeV) & (APT \> 1400 \*MeV)                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (DMASS('D0') \< 150 \*MeV)                   |
| DecayDescriptor  | None                                                                        |
| DecayDescriptors | [ '[D0 -\> K\*(892)0 pi0]cc' ]                                          |
| Output           | Phys/SelD0DstarToHHPi0_pipipi0_M\_/Particles                                |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/SlowpionsForDstarToHHPi0

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (PT \> 300 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 5) & (MIPCHI2DV(PRIMARY)\< 9.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]    |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/SlowpionsForDstarToHHPi0/Particles                                              |

CombineParticles/SelDstDstarToHHPi0_pipipi0_M\_

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0DstarToHHPi0_pipipi0_M\_' , 'Phys/SlowpionsForDstarToHHPi0' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM - ACHILD(M,1) \< 180+5 \*MeV) & (ADOCACHI2CUT(20,''))                     |
| MotherCut        | (M - CHILD(M,1) \< 180 \*MeV) & (VFASPF(VCHI2/VDOF) \< 9.0)                   |
| DecayDescriptor  | None                                                                          |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                           |
| Output           | Phys/SelDstDstarToHHPi0_pipipi0_M\_/Particles                                 |

TisTosParticleTagger/DstarToHHPi0_pipipi0_M_Line

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/SelDstDstarToHHPi0_pipipi0_M\_' ]     |
| DecayDescriptor | None                                            |
| Output          | Phys/DstarToHHPi0_pipipi0_M_Line/Particles      |
| TisTosSpecs     | { 'Hlt2CharmHadD02HHXDst_hhXDecision%TOS' : 0 } |
