[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarD0ToKsHHPi0_Kspipipi0_DDResolved_Line

## Properties:

|                |                                                           |
|----------------|-----------------------------------------------------------|
| OutputLocation | Phys/DstarD0ToKsHHPi0_Kspipipi0_DDResolved_Line/Particles |
| Postscale      | 1.0000000                                                 |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst_hhX.\*Decision')    |
| Prescale       | 1.0000000                                                 |
| L0DU           | None                                                      |
| ODIN           | None                                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarD0ToKsHHPi0_Kspipipi0_DDResolved_LineVOIDFilter

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

FilterDesktop/PionsForDstarD0ToKsHHPi0

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \< 0)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/PionsForDstarD0ToKsHHPi0/Particles                                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/SelKsDDforDstarD0ToKsHHPi0

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 3000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/SelKsDDforDstarD0ToKsHHPi0/Particles                                                                                                                                                          |

CombineParticles/SelKstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForDstarD0ToKsHHPi0' , 'Phys/SelKsDDforDstarD0ToKsHHPi0' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                             |
| CombinationCut   | (((ACHILD(PT,1) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),1) \> 36)) \| ((ACHILD(PT,2) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),2) \> 36))) & (AM \< 1850\*MeV) & (ADOCACHI2CUT(15,'')) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 3) & (BPVVDCHI2 \> 100)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[K\*(892)0 -\> pi- pi+ KS0]cc' ]                                                                                                                                    |
| Output           | Phys/SelKstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_/Particles                                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0RForDstarD0ToKsHHPi0

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (M \> 135 - 15 \*MeV) & (M \< 135 + 15 \*MeV)                       |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Pi0RForDstarD0ToKsHHPi0/Particles                                                  |

CombineParticles/SelD0DstarD0ToKsHHPi0_Kspipipi0_DDResolved\_

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0RForDstarD0ToKsHHPi0' , 'Phys/SelKstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi0' : 'ALL' }                 |
| CombinationCut   | (ADAMASS('D0') \< 210 + 10 \*MeV) & (APT \> 1400 \*MeV)                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (DMASS('D0') \< 210 \*MeV)                                   |
| DecayDescriptor  | None                                                                                        |
| DecayDescriptors | [ '[D0 -\> K\*(892)0 pi0]cc' ]                                                          |
| Output           | Phys/SelD0DstarD0ToKsHHPi0_Kspipipi0_DDResolved\_/Particles                                 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/SlowpionsForDstarD0ToKsHHPi0

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (PT \> 300 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 5) & (MIPCHI2DV(PRIMARY)\< 9.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]    |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/SlowpionsForDstarD0ToKsHHPi0/Particles                                          |

CombineParticles/SelDstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_

|                  |                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0DstarD0ToKsHHPi0_Kspipipi0_DDResolved\_' , 'Phys/SlowpionsForDstarD0ToKsHHPi0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                   |
| CombinationCut   | (AM - ACHILD(M,1) \< 180+5 \*MeV) & (ADOCACHI2CUT(20,''))                                       |
| MotherCut        | (M - CHILD(M,1) \< 180 \*MeV) & (VFASPF(VCHI2/VDOF) \< 9.0)                                     |
| DecayDescriptor  | None                                                                                            |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                             |
| Output           | Phys/SelDstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_/Particles                                    |

TisTosParticleTagger/DstarD0ToKsHHPi0_Kspipipi0_DDResolved_Line

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/SelDstDstarD0ToKsHHPi0_Kspipipi0_DDResolved\_' ] |
| DecayDescriptor | None                                                       |
| Output          | Phys/DstarD0ToKsHHPi0_Kspipipi0_DDResolved_Line/Particles  |
| TisTosSpecs     | { 'Hlt2CharmHadD02HHXDst_hhXDecision%TOS' : 0 }            |
