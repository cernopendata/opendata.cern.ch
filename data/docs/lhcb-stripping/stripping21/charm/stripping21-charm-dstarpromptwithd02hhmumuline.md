[[stripping21 lines]](./stripping21-index)

# StrippingDstarPromptWithD02HHMuMuLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/DstarPromptWithD02HHMuMuLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

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

GaudiSequencer/SeqD02hhmumuForDstarPromptWithD02HHMuMu

GaudiSequencer/SEQ:D02KPiForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02KPiForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K- pi+ mu+ mu-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+ mu+ mu-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D02KPiForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KPiConjForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02KPiForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [D0 -\> K- pi+ mu+ mu-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+ mu+ mu-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D02KPiForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

ConjugateNeutralPID/D02KPiConjForDstarPromptWithD02HHMuMu

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/D02KPiForDstarPromptWithD02HHMuMu' ]       |
| DecayDescriptor | None                                                 |
| Output          | Phys/D02KPiConjForDstarPromptWithD02HHMuMu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02KKForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | D0 -\> K+ K- mu+ mu-                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- mu+ mu-' ]                                                                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/D02KKForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02KKConjForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

CombineParticles/D02KKForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'K-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | D0 -\> K+ K- mu+ mu-                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> K+ K- mu+ mu-' ]                                                                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/D02KKForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                              |

ConjugateNeutralPID/D02KKConjForDstarPromptWithD02HHMuMu

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/D02KKForDstarPromptWithD02HHMuMu' ]       |
| DecayDescriptor | None                                                |
| Output          | Phys/D02KKConjForDstarPromptWithD02HHMuMu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02PiPiForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02PiPiForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | D0 -\> pi+ pi- mu+ mu-                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'D0 -\> pi+ pi- mu+ mu-' ]                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/D02PiPiForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D02PiPiConjForDstarPromptWithD02HHMuMu

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D02PiPiForDstarPromptWithD02HHMuMu

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'mu-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi+' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' , 'pi-' : '(TRCHI2DOF\<3) &(PT\>300.0)&(P\>3000.0) & (MIPCHI2DV(PRIMARY)\>3.0)' } |
| CombinationCut   | (ADAMASS('D0')\<120.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) & (AHASCHILD(((ABSID=='K+') \| (ABSID=='pi+') \| (ABSID=='mu+') ) & (MIPCHI2DV(PRIMARY)\>9)))                                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20) & (BPVVDCHI2\>30) & (BPVIPCHI2()\<36) & (BPVDIRA\>0.9998) & (ADMASS('D0')\<100.0) & (PT\>2000.0)                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | D0 -\> pi+ pi- mu+ mu-                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'D0 -\> pi+ pi- mu+ mu-' ]                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/D02PiPiForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                                                                                                                                                                             |

ConjugateNeutralPID/D02PiPiConjForDstarPromptWithD02HHMuMu

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/D02PiPiForDstarPromptWithD02HHMuMu' ]       |
| DecayDescriptor | None                                                  |
| Output          | Phys/D02PiPiConjForDstarPromptWithD02HHMuMu/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D02hhmumuForDstarPromptWithD02HHMuMu

|                 |                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                               |
| Inputs          | [ 'Phys/D02KKConjForDstarPromptWithD02HHMuMu' , 'Phys/D02KKForDstarPromptWithD02HHMuMu' , 'Phys/D02KPiConjForDstarPromptWithD02HHMuMu' , 'Phys/D02KPiForDstarPromptWithD02HHMuMu' , 'Phys/D02PiPiConjForDstarPromptWithD02HHMuMu' , 'Phys/D02PiPiForDstarPromptWithD02HHMuMu' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                              |
| Output          | Phys/D02hhmumuForDstarPromptWithD02HHMuMu/Particles                                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/DstarPromptWithD02HHMuMuLine

|                  |                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02hhmumuForDstarPromptWithD02HHMuMu' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]       |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3) & (PT\>120.0)' , 'pi-' : '(TRCHI2DOF\<3) & (PT\>120.0)' }       |
| CombinationCut   | (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\>-9.0) & (AM-AMAXCHILD(M,'D0'==ABSID)-145.4\*MeV\<20.0) & (APT\>2000.0) & (AMAXDOCA('')\<0.3) |
| MotherCut        | (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\>-8.0) & (M-MAXTREE(M,'D0'==ABSID)-145.4\*MeV\<18.0) & (VFASPF(VCHI2/VDOF)\<20)                  |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                           |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                                   |
| Output           | Phys/DstarPromptWithD02HHMuMuLine/Particles                                                                                           |

AddRelatedInfo/RelatedInfo1_DstarPromptWithD02HHMuMuLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/DstarPromptWithD02HHMuMuLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_DstarPromptWithD02HHMuMuLine/Particles |
