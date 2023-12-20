[[stripping21 lines]](./stripping21-index)

# Strippingb2Ds3PiMuXB2DMuNuXLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2Ds3PiMuXB2DMuNuXLine/Particles                                                          |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2Ds3PiMuXB2DMuNuXLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuforB2DMuNuX

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 6.0\*GeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDmu \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                 |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/MuforB2DMuNuX/Particles                                                                                              |

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

CombineParticles/CharmSelForb2Ds3PiMuXB2DMuNuX

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiforB2DMuNuX' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                  |
| CombinationCut   | (DAMASS('D_s+') \< 90.0 \*MeV) & (DAMASS('D+')\> -90.0 \*MeV)& (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 1800.\*MeV) & (ADOCACHI2CUT( 20, '')) |
| MotherCut        | (DMASS('D_s+') \< 80.0 \*MeV) & (DMASS('D+')\> -90.0 \*MeV)& (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVVDCHI2 \> 25.0)                                  |
| DecayDescriptor  | None                                                                                                                                            |
| DecayDescriptors | [ '[D+ -\> pi+ pi- pi+]cc' ]                                                                                                                |
| Output           | Phys/CharmSelForb2Ds3PiMuXB2DMuNuX/Particles                                                                                                    |

CombineParticles/BSelForb2Ds3PiMuXB2DMuNuX

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmSelForb2Ds3PiMuXB2DMuNuX' , 'Phys/MuforB2DMuNuX' ]                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 9) & (PT \> 1000\*MeV)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 9) & (PT \> 1000\*MeV)' }                              |
| CombinationCut   | (AM \> 0\*GeV) & (AM \< 9999\*GeV) & (ADOCACHI2CUT( 10, ''))                                                                                                                                |
| MotherCut        | (MM\>0\*GeV) & (MM\<9999\*GeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> -0.1 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[B0 -\> D- mu+]cc' , '[B0 -\> D- mu-]cc' ]                                                                                                                                         |
| Output           | Phys/BSelForb2Ds3PiMuXB2DMuNuX/Particles                                                                                                                                                    |

TisTosParticleTagger/b2Ds3PiMuXB2DMuNuXLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/BSelForb2Ds3PiMuXB2DMuNuX' ]                                                                                                             |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2Ds3PiMuXB2DMuNuXLine/Particles                                                                                                              |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
