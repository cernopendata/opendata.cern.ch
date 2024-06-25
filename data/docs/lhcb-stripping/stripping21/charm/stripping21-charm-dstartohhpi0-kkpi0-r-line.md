[[stripping21 lines]](./stripping21-index)

# StrippingDstarToHHPi0_KKpi0_R_Line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/DstarToHHPi0_KKpi0_R_Line/Particles               |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst_hhX.\*Decision') |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarToHHPi0_KKpi0_R_LineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForDstarToHHPi0

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \> 7)                   |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KaonsForDstarToHHPi0/Particles                                       |

CombineParticles/SelKstDstarToHHPi0_KKpi0_R\_

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForDstarToHHPi0' ]                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                               |
| CombinationCut   | (((ACHILD(PT,1) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),1) \> 36)) \| ((ACHILD(PT,2) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),2) \> 36))) & (AM \< 1850\*MeV) & (ADOCACHI2CUT(15,'')) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 3) & (BPVVDCHI2 \> 100)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[K\*(892)0 -\> K- K+]cc' ]                                                                                                                                          |
| Output           | Phys/SelKstDstarToHHPi0_KKpi0_R\_/Particles                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0RForDstarToHHPi0

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (M \> 135 - 15 \*MeV) & (M \< 135 + 15 \*MeV)                     |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Pi0RForDstarToHHPi0/Particles                                                    |

CombineParticles/SelD0DstarToHHPi0_KKpi0_R\_

|                  |                                                                             |
|------------------|-----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0RForDstarToHHPi0' , 'Phys/SelKstDstarToHHPi0_KKpi0_R\_' ]      |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi0' : 'ALL' } |
| CombinationCut   | (ADAMASS('D0') \< 150 + 10 \*MeV) & (APT \> 1400 \*MeV)                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (DMASS('D0') \< 150 \*MeV)                   |
| DecayDescriptor  | None                                                                        |
| DecayDescriptors | [ '[D0 -\> K\*(892)0 pi0]cc' ]                                          |
| Output           | Phys/SelD0DstarToHHPi0_KKpi0_R\_/Particles                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/SlowpionsForDstarToHHPi0

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (PT \> 300 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 5) & (MIPCHI2DV(PRIMARY)\< 9.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]      |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/SlowpionsForDstarToHHPi0/Particles                                              |

CombineParticles/SelDstDstarToHHPi0_KKpi0_R\_

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0DstarToHHPi0_KKpi0_R\_' , 'Phys/SlowpionsForDstarToHHPi0' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM - ACHILD(M,1) \< 180+5 \*MeV) & (ADOCACHI2CUT(20,''))                     |
| MotherCut        | (M - CHILD(M,1) \< 180 \*MeV) & (VFASPF(VCHI2/VDOF) \< 9.0)                   |
| DecayDescriptor  | None                                                                          |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                           |
| Output           | Phys/SelDstDstarToHHPi0_KKpi0_R\_/Particles                                   |

TisTosParticleTagger/DstarToHHPi0_KKpi0_R_Line

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/SelDstDstarToHHPi0_KKpi0_R\_' ]       |
| DecayDescriptor | None                                            |
| Output          | Phys/DstarToHHPi0_KKpi0_R_Line/Particles        |
| TisTosSpecs     | { 'Hlt2CharmHadD02HHXDst_hhXDecision%TOS' : 0 } |
