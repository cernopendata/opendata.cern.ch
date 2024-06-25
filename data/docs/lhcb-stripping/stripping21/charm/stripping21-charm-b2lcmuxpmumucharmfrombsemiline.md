[[stripping21 lines]](./stripping21-index)

# Strippingb2LcMuXpMuMuCharmFromBSemiLine

## Properties:

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/b2LcMuXpMuMuCharmFromBSemiLine/Particles                                                  |
| Postscale      | 1.0000000                                                                                      |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision') \| HLT_PASS_RE('Hlt2Topo(2\|3\|4)Body.\*Decision') |
| Prescale       | 1.0000000                                                                                      |
| L0DU           | None                                                                                           |
| ODIN           | None                                                                                           |

## Filter sequence:

LoKi::VoidFilter/Strippingb2LcMuXpMuMuCharmFromBSemiLineVOIDFilter

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

FilterDesktop/SelMuforCharmFromBSemi

|                 |                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (P\> 3.0\*GeV)& (TRGHOSTPROB\< 0.5)& (TRCHI2DOF\< 4.0) & (MIPCHI2DV(PRIMARY)\> 4.0)& (PIDmu \> -0.0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                  |
| DecayDescriptor | None                                                                                                                       |
| Output          | Phys/SelMuforCharmFromBSemi/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/SelProtonforCharmFromBSemi

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0) & (PT \> 250.0 \*MeV) & (P\>2.0\*GeV)& (TRGHOSTPROB\< 0.5)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDp\> 4.0) & (PIDp-PIDK\>1.0e-10) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                                                   |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/SelProtonforCharmFromBSemi/Particles                                                                                                       |

CombineParticles/SelLc2pMuMuforCharmFromBSemi

|                  |                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelProtonforCharmFromBSemi' , 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                       |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 100.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 1800.0 \*MeV)& (ADOCACHI2CUT( 20, ''))                           |
| MotherCut        | (ADMASS('Lambda_c+') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0) & (SUMTREE( PT, ISBASIC )\> 1800.0\*MeV)& (BPVVDCHI2 \> 100.0) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                                                |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ mu- mu+]cc' , '[Lambda_c+ -\> p+ mu+ mu+]cc' , '[Lambda_c+ -\> p~- mu+ mu-]cc' , '[Lambda_c+ -\> p~- mu+ mu+]cc' ]   |
| Output           | Phys/SelLc2pMuMuforCharmFromBSemi/Particles                                                                                                         |

CombineParticles/Selb2Lc2pMuMuXCharmFromBSemi

|                  |                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLc2pMuMuforCharmFromBSemi' , 'Phys/SelMuforCharmFromBSemi' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                    |
| CombinationCut   | (AM\<6200\*MeV)                                                                                                                                                                                |
| MotherCut        | (MM\> 2500 \*MeV) & (MM\<6000 \*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                           |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ mu-]cc' , '[Lambda_b0 -\> Lambda_c+ mu+]cc' ]                                                                                                                |
| Output           | Phys/Selb2Lc2pMuMuXCharmFromBSemi/Particles                                                                                                                                                    |

TisTosParticleTagger/b2LcMuXpMuMuCharmFromBSemiLine

|                 |                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Selb2Lc2pMuMuXCharmFromBSemi' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                               |
| Output          | Phys/b2LcMuXpMuMuCharmFromBSemiLine/Particles                                                                                                      |
| TisTosSpecs     | { 'Hlt1.\*Track.\*Decision%TOS' : 0 , 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2Global%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
