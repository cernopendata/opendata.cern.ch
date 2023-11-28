[[stripping21 lines]](./stripping21-index)

# StrippingDstarPromptWithD02HHMuMuControlLine

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/DstarPromptWithD02HHMuMuControlLine/Particles |
| Postscale      | 1.0000000                                          |
| HLT            | None                                               |
| Prescale       | 0.010000000                                        |
| L0DU           | None                                               |
| ODIN           | None                                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

GaudiSequencer/SeqD02hhhhForDstarPromptWithD02HHMuMuControl

GaudiSequencer/SEQ:D02K3PiForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02K3PiConjForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                     |

ConjugateNeutralPID/D02K3PiConjForDstarPromptWithD02HHMuMuControl

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/D02K3PiForDstarPromptWithD02HHMuMuControl' ]       |
| DecayDescriptor | None                                                         |
| Output          | Phys/D02K3PiConjForDstarPromptWithD02HHMuMuControl/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                 |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiConjForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                 |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                     |

ConjugateNeutralPID/D02FourPiConjForDstarPromptWithD02HHMuMuControl

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/D02FourPiForDstarPromptWithD02HHMuMuControl' ]       |
| DecayDescriptor | None                                                           |
| Output          | Phys/D02FourPiConjForDstarPromptWithD02HHMuMuControl/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiConjForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                   |

ConjugateNeutralPID/D02KKPiPiConjForDstarPromptWithD02HHMuMuControl

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/D02KKPiPiForDstarPromptWithD02HHMuMuControl' ]       |
| DecayDescriptor | None                                                           |
| Output          | Phys/D02KKPiPiConjForDstarPromptWithD02HHMuMuControl/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KConjForDstarPromptWithD02HHMuMuControl

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHMuMuControl

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                     |

ConjugateNeutralPID/D02Pi3KConjForDstarPromptWithD02HHMuMuControl

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/D02Pi3KForDstarPromptWithD02HHMuMuControl' ]       |
| DecayDescriptor | None                                                         |
| Output          | Phys/D02Pi3KConjForDstarPromptWithD02HHMuMuControl/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D02hhhhForDstarPromptWithD02HHMuMuControl

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Inputs          | [ 'Phys/D02FourPiConjForDstarPromptWithD02HHMuMuControl' , 'Phys/D02FourPiForDstarPromptWithD02HHMuMuControl' , 'Phys/D02K3PiConjForDstarPromptWithD02HHMuMuControl' , 'Phys/D02K3PiForDstarPromptWithD02HHMuMuControl' , 'Phys/D02KKPiPiConjForDstarPromptWithD02HHMuMuControl' , 'Phys/D02KKPiPiForDstarPromptWithD02HHMuMuControl' , 'Phys/D02Pi3KConjForDstarPromptWithD02HHMuMuControl' , 'Phys/D02Pi3KForDstarPromptWithD02HHMuMuControl' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/D02hhhhForDstarPromptWithD02HHMuMuControl/Particles                                                                                                                                                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/DstarPromptWithD02HHMuMuControlLine

|                  |                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02hhhhForDstarPromptWithD02HHMuMuControl' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3) & (PT\>120.0)' , 'pi-' : '(TRCHI2DOF\<3) & (PT\>120.0)' }       |
| CombinationCut   | (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\>-9.0) & (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\<20.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) |
| MotherCut        | (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\>-8.0) & (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\<18.0) & (VFASPF(VCHI2/VDOF)\<20)                  |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                           |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                   |
| Output           | Phys/DstarPromptWithD02HHMuMuControlLine/Particles                                                                                    |

AddRelatedInfo/RelatedInfo1_DstarPromptWithD02HHMuMuControlLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarPromptWithD02HHMuMuControlLine' ]                |
| DecayDescriptor | None                                                            |
| Output          | Phys/RelatedInfo1_DstarPromptWithD02HHMuMuControlLine/Particles |
