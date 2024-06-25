[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLFVTau2PhiMuLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/LFVTau2PhiMuLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

CombineParticles/LFVTau2PhiMuSelPhi

|                  |                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & (PT\>300\*MeV) & (PIDK \> 0) & ( BPVIPCHI2 () \> 9 )' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & (PT\>300\*MeV) & (PIDK \> 0) & ( BPVIPCHI2 () \> 9 )' } |
| CombinationCut   | (ADAMASS('phi(1020)')\<30\*MeV)                                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 25 ) & (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                                                     |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                                                                                                            |
| Output           | Phys/LFVTau2PhiMuSelPhi/Particles                                                                                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/LFVTau2PhiMumakeTau

|                  |                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LFVTau2PhiMuSelPhi' , 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & ( BPVIPCHI2 () \> 9 )' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & ( BPVIPCHI2 () \> 9 )' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('tau-')\<150\*MeV)                                                                                                                                                                                                                  |
| MotherCut        | ( VFASPF(VCHI2) \< 25 ) & ( (BPVLTIME () \* c_light) \> 50 \* micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                          |
| DecayDescriptor  | [ tau+ -\> phi(1020) mu+ ]cc                                                                                                                                                                                                               |
| DecayDescriptors | [ ' [ tau+ -\> phi(1020) mu+ ]cc' ]                                                                                                                                                                                                      |
| Output           | Phys/LFVTau2PhiMumakeTau/Particles                                                                                                                                                                                                           |

TisTosParticleTagger/LFVTau2PhiMuLine

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMumakeTau' ]                                                                                       |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/LFVTau2PhiMuLine/Particles                                                                                        |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt1TrackMuonDecision%TOS' : 0 , 'L0Global%TIS' : 0 , 'L0MuonDecision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_LFVTau2PhiMuLine/Particles |

AddRelatedInfo/RelatedInfo2_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_LFVTau2PhiMuLine/Particles |

AddRelatedInfo/RelatedInfo3_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_LFVTau2PhiMuLine/Particles |

AddRelatedInfo/RelatedInfo4_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_LFVTau2PhiMuLine/Particles |

AddRelatedInfo/RelatedInfo5_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo5_LFVTau2PhiMuLine/Particles |

AddRelatedInfo/RelatedInfo6_LFVTau2PhiMuLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo6_LFVTau2PhiMuLine/Particles |
