[[stripping21 lines]](./stripping21-index)

# StrippingDstarPromptWithD02HHHHNoPIDLine

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/DstarPromptWithD02HHHHNoPIDLine/Particles |
| Postscale      | 1.0000000                                      |
| HLT            | None                                           |
| Prescale       | 0.050000000                                    |
| L0DU           | None                                           |
| ODIN           | None                                           |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarPromptWithD02HHHHNoPIDLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks,TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

GaudiSequencer/SeqD02hhhhForDstarPromptWithD02HHHHNoPID

GaudiSequencer/SEQ:D02K3PiForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02K3PiConjForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                             |

ConjugateNeutralPID/D02K3PiConjForDstarPromptWithD02HHHHNoPID

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/D02K3PiForDstarPromptWithD02HHHHNoPID' ]       |
| DecayDescriptor | None                                                     |
| Output          | Phys/D02K3PiConjForDstarPromptWithD02HHHHNoPID/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                   |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiConjForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                   |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                           |

ConjugateNeutralPID/D02FourPiConjForDstarPromptWithD02HHHHNoPID

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/D02FourPiForDstarPromptWithD02HHHHNoPID' ]       |
| DecayDescriptor | None                                                       |
| Output          | Phys/D02FourPiConjForDstarPromptWithD02HHHHNoPID/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiConjForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                           |

ConjugateNeutralPID/D02KKPiPiConjForDstarPromptWithD02HHHHNoPID

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/D02KKPiPiForDstarPromptWithD02HHHHNoPID' ]       |
| DecayDescriptor | None                                                       |
| Output          | Phys/D02KKPiPiConjForDstarPromptWithD02HHHHNoPID/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KConjForDstarPromptWithD02HHHHNoPID

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHHHNoPID

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                                             |

ConjugateNeutralPID/D02Pi3KConjForDstarPromptWithD02HHHHNoPID

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/D02Pi3KForDstarPromptWithD02HHHHNoPID' ]       |
| DecayDescriptor | None                                                     |
| Output          | Phys/D02Pi3KConjForDstarPromptWithD02HHHHNoPID/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D02hhhhForDstarPromptWithD02HHHHNoPID

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Inputs          | [ 'Phys/D02FourPiConjForDstarPromptWithD02HHHHNoPID' , 'Phys/D02FourPiForDstarPromptWithD02HHHHNoPID' , 'Phys/D02K3PiConjForDstarPromptWithD02HHHHNoPID' , 'Phys/D02K3PiForDstarPromptWithD02HHHHNoPID' , 'Phys/D02KKPiPiConjForDstarPromptWithD02HHHHNoPID' , 'Phys/D02KKPiPiForDstarPromptWithD02HHHHNoPID' , 'Phys/D02Pi3KConjForDstarPromptWithD02HHHHNoPID' , 'Phys/D02Pi3KForDstarPromptWithD02HHHHNoPID' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/D02hhhhForDstarPromptWithD02HHHHNoPID/Particles                                                                                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/DstarPromptWithD02HHHHNoPIDLine

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02hhhhForDstarPromptWithD02HHHHNoPID' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]       |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4) & (PT\>120.0)' , 'pi-' : '(TRCHI2DOF\<4) & (PT\>120.0)' }        |
| CombinationCut   | (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\>-8.0) & (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\<25.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.22) |
| MotherCut        | (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\>-7.5) & (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\<23.0) & (VFASPF(VCHI2/VDOF)\<20)                   |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                            |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                    |
| Output           | Phys/DstarPromptWithD02HHHHNoPIDLine/Particles                                                                                         |

AddRelatedInfo/RelatedInfo1_DstarPromptWithD02HHHHNoPIDLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarPromptWithD02HHHHNoPIDLine' ]                |
| DecayDescriptor | None                                                        |
| Output          | Phys/RelatedInfo1_DstarPromptWithD02HHHHNoPIDLine/Particles |
