[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLb2L0Gamma

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Lb2L0Gamma/Particles                 |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | L0_CHANNEL_RE('Photon\|Electron\|Hadron') |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)/Particles',True)\>0 |

FilterDesktop/Photons_NonCnv

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 2500.0\*MeV) & (CL \> 0.2)                                                       |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p1-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Photons_NonCnv/Particles                                                           |

GaudiSequencer/SeqLooseLambda0

GaudiSequencer/SEQ:LooseLambda0LL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r0p1-commonparticles-stdlooselambdall)/Particles',True)\>0 |

FilterDesktop/LooseLambda0LL

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV) & (VFASPF(VCHI2/VDOF)\<9.0) & (MINTREE(MIPCHI2DV(PRIMARY), ISLONG) \> 16.0) & (MIPDV(PRIMARY) \> 0.05\*mm) & (ADMASS('Lambda0') \< 20.0\*MeV) & (MAXTREE(TRCHI2DOF, HASTRACK) \< 3.0) & (MINTREE(TRCHI2DOF, HASTRACK) \< 2.0) & (MAXTREE(TRGHOSTPROB, HASTRACK) \< 0.4) & (INTREE(('p+'==ABSID) & (PT \> 800.0))) & (INTREE(('pi+'==ABSID) & (PT \> 300.0))) & (INTREE(('p+'==ABSID) & (P \> 7000.0))) & (INTREE(('pi+'==ABSID) & (P \> 2000.0))) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r0p1-commonparticles-stdlooselambdall)' ]                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/LooseLambda0LL/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LooseLambda0DD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r0p1-commonparticles-stdlooselambdadd)/Particles',True)\>0 |

FilterDesktop/LooseLambda0DD

|                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV) & (VFASPF(VCHI2/VDOF)\<9.0) & (ADMASS('Lambda0') \< 30.0\*MeV) & (MAXTREE(TRCHI2DOF, HASTRACK) \< 3.0) & (MINTREE(TRCHI2DOF, HASTRACK) \< 2.0) & (MAXTREE(TRGHOSTPROB, HASTRACK) \< 0.4) & (INTREE(('p+'==ABSID) & (PT \> 800.0))) & (INTREE(('pi+'==ABSID) & (PT \> 300.0))) & (INTREE(('p+'==ABSID) & (P \> 7000.0))) & (INTREE(('pi+'==ABSID) & (P \> 2000.0))) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r0p1-commonparticles-stdlooselambdadd)' ]                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                 |
| Output          | Phys/LooseLambda0DD/Particles                                                                                                                                                                                                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/LooseLambda0

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Code            | ALL                                                 |
| Inputs          | [ 'Phys/LooseLambda0DD' , 'Phys/LooseLambda0LL' ] |
| DecayDescriptor | None                                                |
| Output          | Phys/LooseLambda0/Particles                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Lb2L0Gamma

|                  |                                                                           |
|------------------|---------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LooseLambda0' , 'Phys/Photons_NonCnv' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'gamma' : 'ALL' } |
| CombinationCut   | (ADAMASS('Lambda_b0') \< 1100.0\*MeV) & (ASUM(PT) \> 5000.0 )             |
| MotherCut        | (PT \> 1000.0\*MeV) & (MTDOCACHI2(1) \< 7.0)                              |
| DecayDescriptor  | [Lambda_b0 -\> Lambda0 gamma]cc                                         |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda0 gamma]cc' ]                                 |
| Output           | Phys/Lb2L0Gamma/Particles                                                 |

AddRelatedInfo/RelatedInfo1_Lb2L0Gamma

|                 |                                        |
|-----------------|----------------------------------------|
| Inputs          | [ 'Phys/Lb2L0Gamma' ]                |
| DecayDescriptor | None                                   |
| Output          | Phys/RelatedInfo1_Lb2L0Gamma/Particles |

AddRelatedInfo/RelatedInfo2_Lb2L0Gamma

|                 |                                        |
|-----------------|----------------------------------------|
| Inputs          | [ 'Phys/Lb2L0Gamma' ]                |
| DecayDescriptor | None                                   |
| Output          | Phys/RelatedInfo2_Lb2L0Gamma/Particles |

AddRelatedInfo/RelatedInfo3_Lb2L0Gamma

|                 |                                        |
|-----------------|----------------------------------------|
| Inputs          | [ 'Phys/Lb2L0Gamma' ]                |
| DecayDescriptor | None                                   |
| Output          | Phys/RelatedInfo3_Lb2L0Gamma/Particles |
