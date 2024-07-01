[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuMuNuBu2KshOSMu_SSMuplus_Line

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/B2XuMuNuBu2KshOSMu_SSMuplus_Line/Particles |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuBu2KshOSMu_SSMuplus_LineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/Mu_forB2XuMuNu

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ]                                                      |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/Mu_forB2XuMuNu/Particles                                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/MuMajorana_forB2XuMuNu

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000.0) & (PT \> 100.0)& (TRGHOSTPROB \< 0.35)&(TRCHI2DOF \< 4.0 ) & (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )&(PIDmu-PIDK\> 0.0 )&(MIPCHI2DV(PRIMARY) \> 50.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ]                                                                                         |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/MuMajorana_forB2XuMuNu/Particles                                                                                                                                 |

CombineParticles/KshMajoranaOSMu_forB2XuMuNu

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuMajorana_forB2XuMuNu' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 100.0)&(TRCHI2DOF \< 4.0)&(MIPCHI2DV(PRIMARY) \> 50.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 100.0)&(TRCHI2DOF \< 4.0)&(MIPCHI2DV(PRIMARY) \> 50.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                           |
| MotherCut        | (BPVVDCHI2\> 100.0 )& (VFASPF(VCHI2/VDOF) \< 4.0)&(PT \> 250.0\*MeV)                                                                                                                                                             |
| DecayDescriptor  | KS0 -\> mu+ pi-                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> mu+ pi-' ]                                                                                                                                                                                                          |
| Output           | Phys/KshMajoranaOSMu_forB2XuMuNu/Particles                                                                                                                                                                                       |

CombineParticles/B2XuMuNuBu2KshOSMu_SSMuplus_Line

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KshMajoranaOSMu_forB2XuMuNu' , 'Phys/Mu_forB2XuMuNu' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                 |
| CombinationCut   | (AM\>3000.0\*MeV) & (AM\<6500.0\*MeV)                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.99)& (MINTREE( (ABSID=='KS0') , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                           |
| DecayDescriptors | [ '[B- -\> KS0 mu-]cc' ]                                                                                   |
| Output           | Phys/B2XuMuNuBu2KshOSMu_SSMuplus_Line/Particles                                                                |
