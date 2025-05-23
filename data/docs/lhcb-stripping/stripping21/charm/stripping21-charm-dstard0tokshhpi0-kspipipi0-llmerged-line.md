[[stripping21 lines]](./stripping21-index)

# StrippingDstarD0ToKsHHPi0_Kspipipi0_LLMerged_Line

## Properties:

|                |                                                         |
|----------------|---------------------------------------------------------|
| OutputLocation | Phys/DstarD0ToKsHHPi0_Kspipipi0_LLMerged_Line/Particles |
| Postscale      | 1.0000000                                               |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst_hhX.\*Decision')  |
| Prescale       | 1.0000000                                               |
| L0DU           | None                                                    |
| ODIN           | None                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarD0ToKsHHPi0_Kspipipi0_LLMerged_LineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForDstarD0ToKsHHPi0

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \< 0)                   |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PionsForDstarD0ToKsHHPi0/Particles                                   |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/SelKsLLforDstarD0ToKsHHPi0

|                 |                                                                                                                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\> 2000 \*MeV) & (PT\> 250 \*MeV) & (ADMASS('KS0') \< 30 \*MeV) & (BPVVDCHI2\> 100) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & CHILDCUT((TRGHOSTPROB\< 0.5),1) & CHILDCUT((TRGHOSTPROB\< 0.5),2) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> 0.99 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                                                                    |
| Output          | Phys/SelKsLLforDstarD0ToKsHHPi0/Particles                                                                                                                                                                                                                               |

CombineParticles/SelKstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForDstarD0ToKsHHPi0' , 'Phys/SelKsLLforDstarD0ToKsHHPi0' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                             |
| CombinationCut   | (((ACHILD(PT,1) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),1) \> 36)) \| ((ACHILD(PT,2) \> 1.7\*GeV) & (ACHILD(BPVIPCHI2(),2) \> 36))) & (AM \< 1850\*MeV) & (ADOCACHI2CUT(15,'')) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 3) & (BPVVDCHI2 \> 100)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[K\*(892)0 -\> pi- pi+ KS0]cc' ]                                                                                                                                    |
| Output           | Phys/SelKstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_/Particles                                                                                                                 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/Pi0MForDstarD0ToKsHHPi0

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PT \> 500 \*MeV)                                                                 |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Pi0MForDstarD0ToKsHHPi0/Particles                                            |

CombineParticles/SelD0DstarD0ToKsHHPi0_Kspipipi0_LLMerged\_

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0MForDstarD0ToKsHHPi0' , 'Phys/SelKstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi0' : 'ALL' }               |
| CombinationCut   | (ADAMASS('D0') \< 210 + 10 \*MeV) & (APT \> 1400 \*MeV)                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (DMASS('D0') \< 210 \*MeV)                                 |
| DecayDescriptor  | None                                                                                      |
| DecayDescriptors | [ '[D0 -\> K\*(892)0 pi0]cc' ]                                                        |
| Output           | Phys/SelD0DstarD0ToKsHHPi0_Kspipipi0_LLMerged\_/Particles                                 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/SlowpionsForDstarD0ToKsHHPi0

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Code            | (PT \> 300 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 5) & (MIPCHI2DV(PRIMARY)\< 9.0) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]      |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/SlowpionsForDstarD0ToKsHHPi0/Particles                                          |

CombineParticles/SelDstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_

|                  |                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0DstarD0ToKsHHPi0_Kspipipi0_LLMerged\_' , 'Phys/SlowpionsForDstarD0ToKsHHPi0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                 |
| CombinationCut   | (AM - ACHILD(M,1) \< 180+5 \*MeV) & (ADOCACHI2CUT(20,''))                                     |
| MotherCut        | (M - CHILD(M,1) \< 180 \*MeV) & (VFASPF(VCHI2/VDOF) \< 9.0)                                   |
| DecayDescriptor  | None                                                                                          |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                           |
| Output           | Phys/SelDstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_/Particles                                    |

TisTosParticleTagger/DstarD0ToKsHHPi0_Kspipipi0_LLMerged_Line

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/SelDstDstarD0ToKsHHPi0_Kspipipi0_LLMerged\_' ] |
| DecayDescriptor | None                                                     |
| Output          | Phys/DstarD0ToKsHHPi0_Kspipipi0_LLMerged_Line/Particles  |
| TisTosSpecs     | { 'Hlt2CharmHadD02HHXDst_hhXDecision%TOS' : 0 }          |
