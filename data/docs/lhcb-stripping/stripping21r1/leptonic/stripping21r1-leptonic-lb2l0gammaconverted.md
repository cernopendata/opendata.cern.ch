[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLb2L0GammaConverted

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Lb2L0GammaConverted/Particles        |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | L0_CHANNEL_RE('Photon\|Electron\|Hadron') |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqPhotons_Cnv_Merge

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaDD_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaLL](./stripping21r1-commonparticles-stdallloosegammall)/Particles')\>0 |

FilterDesktop/Photons_Cnv_Merge

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                     |
| Inputs          | [ 'Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)' , 'Phys/[StdAllLooseGammaLL](./stripping21r1-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Photons_Cnv_Merge/Particles                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Photons_Cnv

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (MM \< 100.0\*MeV) & (PT \> 1000.0\*MeV) & (VFASPF(VCHI2/VDOF)\<9.0) |
| Inputs          | [ 'Phys/Photons_Cnv_Merge' ]                                                     |
| DecayDescriptor | None                                                                               |
| Output          | Phys/Photons_Cnv/Particles                                                         |

GaudiSequencer/SeqLooseLambda0

GaudiSequencer/SEQ:LooseLambda0LL

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/LooseLambda0LL

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV) & (VFASPF(VCHI2/VDOF)\<9.0) & (MINTREE(MIPCHI2DV(PRIMARY), ISLONG) \> 16.0) & (MIPDV(PRIMARY) \> 0.05\*mm) & (ADMASS('Lambda0') \< 20.0\*MeV) & (MAXTREE(TRCHI2DOF, HASTRACK) \< 3.0) & (MINTREE(TRCHI2DOF, HASTRACK) \< 2.0) & (MAXTREE(TRGHOSTPROB, HASTRACK) \< 0.4) & (INTREE(('p+'==ABSID) & (PT \> 800.0))) & (INTREE(('pi+'==ABSID) & (PT \> 300.0))) & (INTREE(('p+'==ABSID) & (P \> 7000.0))) & (INTREE(('pi+'==ABSID) & (P \> 2000.0))) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ]                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/LooseLambda0LL/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LooseLambda0DD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

FilterDesktop/LooseLambda0DD

|                 |                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV) & (VFASPF(VCHI2/VDOF)\<9.0) & (ADMASS('Lambda0') \< 30.0\*MeV) & (MAXTREE(TRCHI2DOF, HASTRACK) \< 3.0) & (MINTREE(TRCHI2DOF, HASTRACK) \< 2.0) & (MAXTREE(TRGHOSTPROB, HASTRACK) \< 0.4) & (INTREE(('p+'==ABSID) & (PT \> 800.0))) & (INTREE(('pi+'==ABSID) & (PT \> 300.0))) & (INTREE(('p+'==ABSID) & (P \> 7000.0))) & (INTREE(('pi+'==ABSID) & (P \> 2000.0))) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ]                                                                                                                                                                                                                                                                                                    |
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

CombineParticles/Lb2L0GammaConverted

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LooseLambda0' , 'Phys/Photons_Cnv' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'gamma' : 'ALL' }                                                   |
| CombinationCut   | (ADAMASS('Lambda_b0') \< 1.5\*1100.0\*MeV)                                                                                  |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9.0) & (PT \> 1000.0\*MeV) & (BPVIPCHI2() \< 9.0) & (ADMASS('Lambda_b0') \< 1100.0\*MeV) |
| DecayDescriptor  | [Lambda_b0 -\> Lambda0 gamma]cc                                                                                           |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda0 gamma]cc' ]                                                                                   |
| Output           | Phys/Lb2L0GammaConverted/Particles                                                                                          |

AddRelatedInfo/RelatedInfo1_Lb2L0GammaConverted

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2L0GammaConverted' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Lb2L0GammaConverted/Particles |

AddRelatedInfo/RelatedInfo2_Lb2L0GammaConverted

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2L0GammaConverted' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Lb2L0GammaConverted/Particles |

AddRelatedInfo/RelatedInfo3_Lb2L0GammaConverted

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2L0GammaConverted' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Lb2L0GammaConverted/Particles |

AddRelatedInfo/RelatedInfo4_Lb2L0GammaConverted

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2L0GammaConverted' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_Lb2L0GammaConverted/Particles |
