[[stripping21r1p1 lines]](./stripping21r1p1-index)

# Strippingb2LcMuXFakeB2DMuForTauMuLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/b2LcMuXFakeB2DMuForTauMuLine/Particles     |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | HLT_PASS_RE('Hlt2CharmHadLambdaC2PiPKDecision') |
| Prescale       | 0.10000000                                      |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/Strippingb2LcMuXFakeB2DMuForTauMuLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)/Particles',True)\>0 |

FilterDesktop/FakeMuforB2DMuForTauMu

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\> 16.0) &(TRGHOSTPROB \< 0.5) & (P\> 3.0\*GeV) & (~ISMUON) & (INMUON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)' ]     |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/FakeMuforB2DMuForTauMu/Particles                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KforB2DMuForTauMu

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (PIDK\> 4.0) & (MIPCHI2DV(PRIMARY)\> 9.0) & (P\>2.0\*GeV) & (PT \> 300.0 \*MeV) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                          |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/KforB2DMuForTauMu/Particles                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PiforB2DMuForTauMu

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 300.0 \*MeV)& (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK\< 2.0) &(TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                        |
| DecayDescriptor | None                                                                                                 |
| Output          | Phys/PiforB2DMuForTauMu/Particles                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/PforB2DMuForTauMu

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (PIDp\> 0.0) & (MIPCHI2DV(PRIMARY)\> 9.0) & (P\>2.0\*GeV) & (PT \> 300.0 \*MeV) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                      |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/PforB2DMuForTauMu/Particles                                                                       |

CombineParticles/Lc2pKPiforB2DMuForTauMu

|                  |                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuForTauMu' , 'Phys/PforB2DMuForTauMu' , 'Phys/PiforB2DMuForTauMu' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                           |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 100.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) \> 2500.0 \*MeV)                                                      |
| MotherCut        | (SUMTREE( PT, ISBASIC )\> 2500.0 \* MeV) &(ADMASS('Lambda_c+') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 4.0) & (BPVVDCHI2 \> 25.0) & (BPVDIRA\> 0.999) |
| DecayDescriptor  | None                                                                                                                                                  |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                 |
| Output           | Phys/Lc2pKPiforB2DMuForTauMu/Particles                                                                                                                |

CombineParticles/b2LcMuXFakeB2DMuForTauMuLine

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/FakeMuforB2DMuForTauMu' , 'Phys/Lc2pKPiforB2DMuForTauMu' ]                        |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | (AM\<10.2\*GeV)                                                                             |
| MotherCut        | (MM\<10.0\*GeV) & (MM\>0.0\*GeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999)           |
| DecayDescriptor  | None                                                                                        |
| DecayDescriptors | [ '[B- -\> Lambda_c+ mu-]cc' , '[B+ -\> Lambda_c+ mu+]cc' ]                           |
| Output           | Phys/b2LcMuXFakeB2DMuForTauMuLine/Particles                                                 |
