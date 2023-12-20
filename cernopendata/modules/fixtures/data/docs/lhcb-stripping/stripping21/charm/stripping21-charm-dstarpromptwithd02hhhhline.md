[[stripping21 lines]](./stripping21-index)

# StrippingDstarPromptWithD02HHHHLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/DstarPromptWithD02HHHHLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarPromptWithD02HHHHLineVOIDFilter

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

GaudiSequencer/SeqD02hhhhForDstarPromptWithD02HHHH

GaudiSequencer/SEQ:D02K3PiForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02K3PiConjForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02K3PiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/D02K3PiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

ConjugateNeutralPID/D02K3PiConjForDstarPromptWithD02HHHH

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/D02K3PiForDstarPromptWithD02HHHH' ]       |
| DecayDescriptor | None                                                |
| Output          | Phys/D02K3PiConjForDstarPromptWithD02HHHH/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                   |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02FourPiConjForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02FourPiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                      |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                   |
| Output           | Phys/D02FourPiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                |

ConjugateNeutralPID/D02FourPiConjForDstarPromptWithD02HHHH

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/D02FourPiForDstarPromptWithD02HHHH' ]       |
| DecayDescriptor | None                                                  |
| Output          | Phys/D02FourPiConjForDstarPromptWithD02HHHH/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKPiPiConjForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02KKPiPiForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/D02KKPiPiForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

ConjugateNeutralPID/D02KKPiPiConjForDstarPromptWithD02HHHH

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/D02KKPiPiForDstarPromptWithD02HHHH' ]       |
| DecayDescriptor | None                                                  |
| Output          | Phys/D02KKPiPiConjForDstarPromptWithD02HHHH/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02Pi3KConjForDstarPromptWithD02HHHH

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02Pi3KForDstarPromptWithD02HHHH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PIDK\>-5.0) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PIDK\<3) & (HASRICH) & (TRCHI2DOF\<4) &(PT\>250.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('D0')\<78.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.12) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+')) & (MIPCHI2DV(PRIMARY)\>30)))                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVIPCHI2()\<1e+12) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<75.0) & (PT\>3000.0)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [D0 -\> K+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[D0 -\> K+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/D02Pi3KForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

ConjugateNeutralPID/D02Pi3KConjForDstarPromptWithD02HHHH

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/D02Pi3KForDstarPromptWithD02HHHH' ]       |
| DecayDescriptor | None                                                |
| Output          | Phys/D02Pi3KConjForDstarPromptWithD02HHHH/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D02hhhhForDstarPromptWithD02HHHH

|                 |                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                         |
| Inputs          | [ 'Phys/D02FourPiConjForDstarPromptWithD02HHHH' , 'Phys/D02FourPiForDstarPromptWithD02HHHH' , 'Phys/D02K3PiConjForDstarPromptWithD02HHHH' , 'Phys/D02K3PiForDstarPromptWithD02HHHH' , 'Phys/D02KKPiPiConjForDstarPromptWithD02HHHH' , 'Phys/D02KKPiPiForDstarPromptWithD02HHHH' , 'Phys/D02Pi3KConjForDstarPromptWithD02HHHH' , 'Phys/D02Pi3KForDstarPromptWithD02HHHH' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                        |
| Output          | Phys/D02hhhhForDstarPromptWithD02HHHH/Particles                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/DstarPromptWithD02HHHHLine

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02hhhhForDstarPromptWithD02HHHH' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4) & (PT\>120.0)' , 'pi-' : '(TRCHI2DOF\<4) & (PT\>120.0)' }        |
| CombinationCut   | (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\>-8.0) & (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\<25.0) & (APT\>3000.0) & (AMAXDOCA('')\<0.22) |
| MotherCut        | (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\>-7.5) & (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\<23.0) & (VFASPF(VCHI2/VDOF)\<20)                   |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                            |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                    |
| Output           | Phys/DstarPromptWithD02HHHHLine/Particles                                                                                              |

AddRelatedInfo/RelatedInfo1_DstarPromptWithD02HHHHLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DstarPromptWithD02HHHHLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_DstarPromptWithD02HHHHLine/Particles |
