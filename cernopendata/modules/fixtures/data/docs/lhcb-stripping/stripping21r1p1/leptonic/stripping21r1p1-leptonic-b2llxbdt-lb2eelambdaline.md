[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2LLXBDT_Lb2eeLambdaLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Lb2eeLambdaLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdDiElectronFromTracks](./stripping21r1p1-commonparticles-stddielectronfromtracks)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelDiElectron

|                 |                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='e+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='e-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r1p1-commonparticles-stddielectronfromtracks)' ]                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

GaudiSequencer/SeqB2LLXBDTSelLambda

GaudiSequencer/SEQ:B2LLXBDTSelLambdaDD

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1p1-commonparticles-stdlooselambdadd)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelLambdaDD

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.\*MeV) & (BPVVDCHI2\>25)                                   |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p1-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/B2LLXBDTSelLambdaDD/Particles                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2LLXBDTSelLambdaLL

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelProtons

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                                  |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/B2LLXBDTSelProtons/Particles                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r1p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelPions4LP

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>100\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>9.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r1p1-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/B2LLXBDTSelPions4LP/Particles                                                        |

CombineParticles/B2LLXBDTSelLambdaLL

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelPions4LP' , 'Phys/B2LLXBDTSelProtons' ]                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (ADAMASS('Lambda0')\<50\*MeV) & (ADOCACHI2CUT(30, ''))                        |
| MotherCut        | (ADMASS('Lambda0') \< 30.\*MeV) & (BPVVDCHI2\>25) & (VFASPF(VCHI2) \< 25.)    |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                      |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                              |
| Output           | Phys/B2LLXBDTSelLambdaLL/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2LLXBDTSelLambda

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | ALL                                                           |
| Inputs          | [ 'Phys/B2LLXBDTSelLambdaDD' , 'Phys/B2LLXBDTSelLambdaLL' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2LLXBDTSelLambda/Particles                              |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2LLXBDTSelLb2eeLambda

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelLambda' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                          |
| CombinationCut   | (in_range(3.7\*GeV, AM, 7.1\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.8\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [Lambda_b0 -\> J/psi(1S) Lambda0]cc                                                                                  |
| DecayDescriptors | [ '[Lambda_b0 -\> J/psi(1S) Lambda0]cc' ]                                                                          |
| Output           | Phys/B2LLXBDTSelLb2eeLambda/Particles                                                                                  |

FilterDesktop/B2LLXBDT_Lb2eeLambdaLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaLb2eeLambda')\>-0.11 |
| Inputs          | [ 'Phys/B2LLXBDTSelLb2eeLambda' ]                            |
| DecayDescriptor | None                                                           |
| Output          | Phys/B2LLXBDT_Lb2eeLambdaLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Lb2eeLambdaLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Lb2eeLambdaLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Lb2eeLambdaLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Lb2eeLambdaLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Lb2eeLambdaLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Lb2eeLambdaLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eeLambdaLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Lb2eeLambdaLine/Particles |
