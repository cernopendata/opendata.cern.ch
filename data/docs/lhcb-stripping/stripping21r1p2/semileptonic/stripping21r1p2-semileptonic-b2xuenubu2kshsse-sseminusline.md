[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuENuBu2KshSSE_SSEminusLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/B2XuENuBu2KshSSE_SSEminusLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuBu2KshSSE_SSEminusLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseElectrons/Particles',True) |

FilterDesktop/E_forB2XuENu

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDe \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r1p2-commonparticles-stdlooseelectrons)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/E_forB2XuENu/Particles                                                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/EMajorana_forB2XuENu

|                 |                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000.0) & (PT \> 100.0)& (TRGHOSTPROB \< 0.35)&(TRCHI2DOF \< 4.0 ) & (PIDe-PIDpi\> 3.0 )& (PIDe-PIDp\> 0.0 )&(PIDe-PIDK\> 0.0 )&(MIPCHI2DV(PRIMARY) \> 50.0) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r1p2-commonparticles-stdlooseelectrons)' ]                                                                              |
| DecayDescriptor | None                                                                                                                                                               |
| Output          | Phys/EMajorana_forB2XuENu/Particles                                                                                                                                |

CombineParticles/KshMajoranaSSE_forB2XuENu

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EMajorana_forB2XuENu' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : '(P \> 2000.0)& (PT \> 100.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 50.0)' , 'pi-' : '(P \> 2000.0)& (PT \> 100.0)& (TRCHI2DOF \< 4.0)& (MIPCHI2DV(PRIMARY) \> 50.0)' } |
| CombinationCut   | (ADOCACHI2CUT(25, ''))                                                                                                                                                                                                             |
| MotherCut        | (BPVVDCHI2\> 100.0 )& (VFASPF(VCHI2/VDOF) \< 4.0)&(PT \> 250.0\*MeV)                                                                                                                                                               |
| DecayDescriptor  | KS0 -\> e- pi+                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'KS0 -\> e- pi+' ]                                                                                                                                                                                                             |
| Output           | Phys/KshMajoranaSSE_forB2XuENu/Particles                                                                                                                                                                                           |

CombineParticles/B2XuENuBu2KshSSE_SSEminusLine

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/E_forB2XuENu' , 'Phys/KshMajoranaSSE_forB2XuENu' ]                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                   |
| CombinationCut   | (AM\>3000.0\*MeV) & (AM\<6500.0\*MeV)                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.99)& (MINTREE( (ABSID=='KS0') , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                           |
| DecayDescriptors | [ '[B- -\> KS0 e-]cc' ]                                                                                    |
| Output           | Phys/B2XuENuBu2KshSSE_SSEminusLine/Particles                                                                   |
