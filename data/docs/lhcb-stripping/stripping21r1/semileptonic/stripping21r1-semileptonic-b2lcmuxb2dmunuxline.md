[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2LcMuXB2DMuNuXLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2LcMuXB2DMuNuXLine/Particles                                                             |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2LcMuXB2DMuNuXLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuforB2DMuNuX

|                 |                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 6.0\*GeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDmu \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                               |
| DecayDescriptor | None                                                                                                                      |
| Output          | Phys/MuforB2DMuNuX/Particles                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/ProtonsForB2DMuNuX

|                 |                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (P\>9.0\*GeV) & (PIDp \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                         |
| DecayDescriptor | None                                                                                                                                    |
| Output          | Phys/ProtonsForB2DMuNuX/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KforB2DMuNuX

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\> -5.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                             |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/KforB2DMuNuX/Particles                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PiforB2DMuNuX

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 250.0 \*MeV)& (TRCHI2DOF \< 4)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 4.0) & (PIDK\< 20.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                             |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/PiforB2DMuNuX/Particles                                                                                            |

CombineParticles/CharmSelForb2LcMuXB2DMuNuX

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuNuX' , 'Phys/PiforB2DMuNuX' , 'Phys/ProtonsForB2DMuNuX' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                   |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 90.0 \*MeV)& (APT \> 2000\*MeV) & (ADOCACHI2CUT( 20, ''))                                            |
| MotherCut        | (ADMASS('Lambda_c+') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (BPVVDCHI2 \> 25.0) & (PT\>2100.\*MeV) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[Lambda_c+ -\> K- p+ pi+]cc' ]                                                                                         |
| Output           | Phys/CharmSelForb2LcMuXB2DMuNuX/Particles                                                                                     |

CombineParticles/BSelForb2LcMuXB2DMuNuX

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmSelForb2LcMuXB2DMuNuX' , 'Phys/MuforB2DMuNuX' ]                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : '(PT \> 1000\*MeV) & (MIPCHI2DV(PRIMARY)\> 9)' , 'mu-' : '(PT \> 1000\*MeV) & (MIPCHI2DV(PRIMARY)\> 9)' }                 |
| CombinationCut   | (AM \> 2.2\*GeV) & (AM \< 8.0\*GeV) & (ADOCACHI2CUT( 10, ''))                                                                                                                                 |
| MotherCut        | (MM\>2.2\*GeV) & (MM\<8.0\*GeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> -0.05 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ mu-]cc' , '[Lambda_b0 -\> Lambda_c+ mu+]cc' ]                                                                                                               |
| Output           | Phys/BSelForb2LcMuXB2DMuNuX/Particles                                                                                                                                                         |

TisTosParticleTagger/b2LcMuXB2DMuNuXLine

|                 |                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/BSelForb2LcMuXB2DMuNuX' ]                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                    |
| Output          | Phys/b2LcMuXB2DMuNuXLine/Particles                                                                                                                                                      |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
