[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBs2st2KKJpsiWSLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Bs2st2KKJpsiWSLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingBs2st2KKJpsiWSLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 1000.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/K2_forBs2st2KKMuX

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.5) & (P \> 3000.0 \*MeV) & (PT \> 1000.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK-PIDpi \> 0.0) & (PIDK-PIDp \> 0) & (PIDK-PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/K2_forBs2st2KKMuX/Particles                                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                                 |
|------|---------------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r0p1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles',True)\>0 |

FilterDesktop/Jpsi_forBs2st2KKMuX

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80.0 \* MeV)                                                              |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r0p1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/Jpsi_forBs2st2KKMuX/Particles                                                                        |

CombineParticles/Bu2KJpsi_forBs2st2KKMuX

|                  |                                                                       |
|------------------|-----------------------------------------------------------------------|
| Inputs           | [ 'Phys/Jpsi_forBs2st2KKMuX' , 'Phys/K2_forBs2st2KKMuX' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }    |
| CombinationCut   | (AM \> 5050.0\*MeV) & (AM \< 5500.0\*MeV)                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 4.0) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 25.0) |
| DecayDescriptor  | None                                                                  |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                     |
| Output           | Phys/Bu2KJpsi_forBs2st2KKMuX/Particles                                |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r0p1-commonparticles-stdallloosekaons)/Particles',True)\>0 |

FilterDesktop/K1Loose_forBs2st2KKMuX

|                 |                                                                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.5) & (PT \> 250.0 \*MeV) &(MIPCHI2DV(PRIMARY) \< 9.0) & (PIDK-PIDpi \> 16.0) & (PIDK-PIDp \> 0) & (PIDK-PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r0p1-commonparticles-stdallloosekaons)' ]                                                                      |
| DecayDescriptor | None                                                                                                                                                     |
| Output          | Phys/K1Loose_forBs2st2KKMuX/Particles                                                                                                                    |

CombineParticles/Bs2st2KKJpsiWSLine

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bu2KJpsi_forBs2st2KKMuX' , 'Phys/K1Loose_forBs2st2KKMuX' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'B+' : 'ALL' , 'B-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }      |
| CombinationCut   | (AM-AM1 \< 1093.677\*MeV) & (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),2))\<1.0\*mm) |
| MotherCut        | (PT \> 50.0\*MeV)                                                               |
| DecayDescriptor  | [B\*\_s20 -\> B+ K+]cc                                                        |
| DecayDescriptors | [ '[B\*\_s20 -\> B+ K+]cc' ]                                                |
| Output           | Phys/Bs2st2KKJpsiWSLine/Particles                                               |
