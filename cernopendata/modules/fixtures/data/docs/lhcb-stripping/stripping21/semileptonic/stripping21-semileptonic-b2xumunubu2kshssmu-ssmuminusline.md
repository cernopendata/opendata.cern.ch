[[stripping21 lines]](./stripping21-index)

# StrippingB2XuMuNuBu2KshSSMu_SSMuminusLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/B2XuMuNuBu2KshSSMu_SSMuminusLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XuMuNuBu2KshSSMu_SSMuminusLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/Mu_forB2XuMuNu

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/Mu_forB2XuMuNu/Particles                                                                                                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/MuMajorana_forB2XuMuNu

|                 |                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000.0) & (PT \> 250.0)& (TRGHOSTPROB \< 0.5)&(TRCHI2DOF \< 4.0 ) & (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )&(PIDmu-PIDK\> 0.0 )&(MIPCHI2DV(PRIMARY) \> 50.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                            |
| DecayDescriptor | None                                                                                                                                                                 |
| Output          | Phys/MuMajorana_forB2XuMuNu/Particles                                                                                                                                |

CombineParticles/KshMajoranaSSMu_forB2XuMuNu

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuMajorana_forB2XuMuNu' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 50.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 250.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 50.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                               |
| MotherCut        | (BPVVDCHI2\> 100.0 )& (VFASPF(VCHI2/VDOF) \< 10.0)&(PT \> 700.0\*MeV)                                                                                                                                                                |
| DecayDescriptor  | KS0 -\> mu- pi+                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'KS0 -\> mu- pi+' ]                                                                                                                                                                                                              |
| Output           | Phys/KshMajoranaSSMu_forB2XuMuNu/Particles                                                                                                                                                                                           |

CombineParticles/B2XuMuNuBu2KshSSMu_SSMuminusLine

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KshMajoranaSSMu_forB2XuMuNu' , 'Phys/Mu_forB2XuMuNu' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                 |
| CombinationCut   | (AM\>3000.0\*MeV) & (AM\<6500.0\*MeV)                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.99)& (MINTREE( (ABSID=='KS0') , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                           |
| DecayDescriptors | [ '[B- -\> KS0 mu-]cc' ]                                                                                   |
| Output           | Phys/B2XuMuNuBu2KshSSMu_SSMuminusLine/Particles                                                                |
