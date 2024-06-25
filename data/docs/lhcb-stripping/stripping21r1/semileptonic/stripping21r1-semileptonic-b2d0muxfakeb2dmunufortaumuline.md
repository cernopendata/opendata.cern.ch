[[stripping21r1 lines]](./stripping21r1-index)

# Strippingb2D0MuXFakeB2DMuNuForTauMuLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/b2D0MuXFakeB2DMuNuForTauMuLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 0.080000000                                   |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/Strippingb2D0MuXFakeB2DMuNuForTauMuLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)/Particles')\>0 |

FilterDesktop/FakeMuforB2DMuNuForTauMu

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\> 45.0) &(TRGHOSTPROB \< 0.5) & (P\> 3.0\*GeV) & (~ISMUON) & (INMUON) |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)' ]       |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/FakeMuforB2DMuNuForTauMu/Particles                                                   |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KforB2DMuNuForTauMu

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PIDK\> 4.0) & (MIPCHI2DV(PRIMARY)\> 45.0) & (P\>2.0\*GeV) & (PT \> 300.0 \*MeV) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                             |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/KforB2DMuNuForTauMu/Particles                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PiforB2DMuNuForTauMu

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (P\>2.0\*GeV) & (PT \> 300.0 \*MeV)& (MIPCHI2DV(PRIMARY)\> 45.0) & (PIDK\< 2.0) &(TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                           |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/PiforB2DMuNuForTauMu/Particles                                                                   |

CombineParticles/D02KPiforB2DMuNuForTauMu

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforB2DMuNuForTauMu' , 'Phys/PiforB2DMuNuForTauMu' ]                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                     |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2) \> 1400.0 \*MeV)                                                                     |
| MotherCut        | (SUMTREE( PT, ISBASIC )\> 1400.0 \* MeV) &(ADMASS('D0') \< 80.0 \*MeV) & (VFASPF(VCHI2/VDOF) \< 4.0) & (BPVVDCHI2 \> 250.0) & (BPVDIRA\> 0.9998) |
| DecayDescriptor  | None                                                                                                                                             |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                      |
| Output           | Phys/D02KPiforB2DMuNuForTauMu/Particles                                                                                                          |

CombineParticles/b2D0MuXFakeB2DMuNuForTauMuLine

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02KPiforB2DMuNuForTauMu' , 'Phys/FakeMuforB2DMuNuForTauMu' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }      |
| CombinationCut   | (AM\<10.2\*GeV)                                                                    |
| MotherCut        | (MM\<10.0\*GeV) & (MM\>0.0\*GeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.9995) |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ '[B- -\> D0 mu-]cc' , '[B+ -\> D0 mu+]cc' ]                                |
| Output           | Phys/b2D0MuXFakeB2DMuNuForTauMuLine/Particles                                      |
