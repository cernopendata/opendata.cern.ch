[[stripping21 lines]](./stripping21-index)

# Strippingb2D0eXB2DMuNuXLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2D0eXB2DMuNuXLine/Particles                                                              |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2D0eXB2DMuNuXLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseElectrons](./stripping21-commonparticles-stdlooseelectrons)/Particles')\>0 |

FilterDesktop/eforB2DMuNuX

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 6.0\*GeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDe \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21-commonparticles-stdlooseelectrons)' ]                                        |
| DecayDescriptor | None                                                                                                                     |
| Output          | Phys/eforB2DMuNuX/Particles                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KforB2DMuNuX

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\> -5.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]                                               |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/KforB2DMuNuX/Particles                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PiforB2DMuNuX

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 20.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                               |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/PiforB2DMuNuX/Particles                                                                                            |

CombineParticles/CharmSelForb2D0eXB2DMuNuX

|                  |                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuNuX' , 'Phys/PiforB2DMuNuX' ]                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK \> 4) & (PT \> 300\*MeV)' , 'K-' : '(PIDK \> 4) & (PT \> 300\*MeV)' , 'pi+' : '(PIDK \< 10) & (PT \> 300\*MeV)' , 'pi-' : '(PIDK \< 10) & (PT \> 300\*MeV)' } |
| CombinationCut   | (ADAMASS('D0') \< 90.0 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2) \> 1400.\*MeV) & (ADOCACHI2CUT( 20, ''))                                                                                         |
| MotherCut        | (ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVVDCHI2 \> 25.0) & (BPVDIRA\> 0.99)                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                       |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                |
| Output           | Phys/CharmSelForb2D0eXB2DMuNuX/Particles                                                                                                                                                   |

CombineParticles/BSelForb2D0eXB2DMuNuX

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmSelForb2D0eXB2DMuNuX' , 'Phys/eforB2DMuNuX' ]                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'e+' : '(PT\>1.2\*GeV) & (MIPCHI2DV(PRIMARY)\> 9.0)' , 'e-' : '(PT\>1.2\*GeV) & (MIPCHI2DV(PRIMARY)\> 9.0)' }                                 |
| CombinationCut   | (AM \> 2.2\*GeV) & (AM \< 8.0\*GeV) & (ADOCACHI2CUT( 10, ''))                                                                                                                               |
| MotherCut        | (MM\>2.2\*GeV) & (MM\<8.0\*GeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[B- -\> D0 e-]cc' ]                                                                                                                                                                  |
| Output           | Phys/BSelForb2D0eXB2DMuNuX/Particles                                                                                                                                                        |

TisTosParticleTagger/b2D0eXB2DMuNuXLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/BSelForb2D0eXB2DMuNuX' ]                                                                                                                 |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2D0eXB2DMuNuXLine/Particles                                                                                                                  |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
