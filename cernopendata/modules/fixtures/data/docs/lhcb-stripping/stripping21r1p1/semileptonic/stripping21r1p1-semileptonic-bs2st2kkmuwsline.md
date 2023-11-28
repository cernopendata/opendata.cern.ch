[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBs2st2KKMuWSLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Bs2st2KKMuWSLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingBs2st2KKMuWSLineVOIDFilter

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
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/K2_forBs2st2KKMuX

|                 |                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.5) & (P \> 3000.0 \*MeV) & (PT \> 1000.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK-PIDpi \> 0.0) & (PIDK-PIDp \> 0) & (PIDK-PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                            |
| Output          | Phys/K2_forBs2st2KKMuX/Particles                                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/Mu_forBs2st2KKMuX

|                 |                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.5) & (P \> 3000.0 \*MeV) & (PT \> 1000.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDmu-PIDK \> 0) & (PIDmu-PIDp \> 0) & (PIDmu-PIDpi \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                              |
| Output          | Phys/Mu_forBs2st2KKMuX/Particles                                                                                                                                                  |

CombineParticles/Bu2KMu_forBs2st2KKMuX

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K2_forBs2st2KKMuX' , 'Phys/Mu_forBs2st2KKMuX' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM \> 1800.0\*MeV) & (AM \< 5500.0\*MeV)                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 4.0) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 100.0)       |
| DecayDescriptor  | None                                                                         |
| DecayDescriptors | [ '[B+ -\> K+ mu-]cc' , '[B+ -\> K+ mu+]cc' ]                          |
| Output           | Phys/Bu2KMu_forBs2st2KKMuX/Particles                                         |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1p1-commonparticles-stdallloosekaons)/Particles',True)\>0 |

FilterDesktop/K1_forBs2st2KKMuX

|                 |                                                                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.5) & (PT \> 500.0 \*MeV) &(MIPCHI2DV(PRIMARY) \< 9.0) & (PIDK-PIDpi \> 16.0) & (PIDK-PIDp \> 0) & (PIDK-PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r1p1-commonparticles-stdallloosekaons)' ]                                                                      |
| DecayDescriptor | None                                                                                                                                                     |
| Output          | Phys/K1_forBs2st2KKMuX/Particles                                                                                                                         |

CombineParticles/Bs2st2KKMuWSLine

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bu2KMu_forBs2st2KKMuX' , 'Phys/K1_forBs2st2KKMuX' ]                  |
| DaughtersCuts    | { '' : 'ALL' , 'B+' : 'ALL' , 'B-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }     |
| CombinationCut   | (AM-AM1 \< 713.677\*MeV) & (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),2))\<1.0\*mm) |
| MotherCut        | (PT \> 50.0\*MeV)                                                              |
| DecayDescriptor  | [B\*\_s20 -\> B+ K+]cc                                                       |
| DecayDescriptors | [ '[B\*\_s20 -\> B+ K+]cc' ]                                               |
| Output           | Phys/Bs2st2KKMuWSLine/Particles                                                |

AddRelatedInfo/RelatedInfo1_Bs2st2KKMuWSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2st2KKMuWSLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_Bs2st2KKMuWSLine/Particles |
