[[stripping21 lines]](./stripping21-index)

# StrippingB2pphh_kpiLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/B2pphh_kpiLine/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingB2pphh_kpiLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 200 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21-commonparticles-stdallnopidsprotons)/Particles')\>0 |

FilterDesktop/ProtonForB2pphh

|                 |                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & HASRICH & (P \> 1500\*MeV) & (PT \> 300\*MeV) & (MIPCHI2DV(PRIMARY) \> 2.0) & (TRGHOSTPROB \< 0.35) & (PROBNNp \> 0.05) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21-commonparticles-stdallnopidsprotons)' ]                                                        |
| DecayDescriptor | None                                                                                                                                         |
| Output          | Phys/ProtonForB2pphh/Particles                                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PionForB2pphh

|                 |                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & HASRICH & (P \> 1500\*MeV) & (PT \> 300\*MeV) & (MIPCHI2DV(PRIMARY) \> 6.0) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.05) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                             |
| DecayDescriptor | None                                                                                                                                          |
| Output          | Phys/PionForB2pphh/Particles                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KaonForB2pphh

|                 |                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & HASRICH & (P \> 1500\*MeV) & (PT \> 300\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRGHOSTPROB \< 0.35) & (PROBNNk \> 0.05) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ]                                                            |
| DecayDescriptor | None                                                                                                                                         |
| Output          | Phys/KaonForB2pphh/Particles                                                                                                                 |

DaVinci::N4BodyDecays/B2pphh_kpiLine

|                  |                                                                                                                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonForB2pphh' , 'Phys/PionForB2pphh' , 'Phys/ProtonForB2pphh' ]                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                               |
| CombinationCut   | ((AMAXDOCA('LoKi::TrgDistanceCalculator') \< 0.3) & (in_range (5.0 \* GeV , AM , 5.6 \* GeV)) & (ACHI2DOCA(1,4) \< 20.0 ) & (ACHI2DOCA(2,4) \< 20.0 ) & (ACHI2DOCA(3, 4) \< 20.0 ))                                                                                                       |
| MotherCut        | ((BPVDIRA \> 0.9999) & (VFASPF(VCHI2) \< 30.0) & (SUMTREE(PT,((ABSID=='p+') \|(ABSID=='p~-') \|(ABSID=='K+') \| (ABSID=='K-') \| (ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 3000.0\*MeV) & (PT \> 1000.0\*MeV) & (MIPDV(PRIMARY) \< 0.2\*mm) & (in_range (5.05 \* GeV , M , 5.55 \* GeV))) |
| DecayDescriptor  | [B0 -\> p+ p~- K+ pi-]cc                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ '[B0 -\> p+ p~- K+ pi-]cc' ]                                                                                                                                                                                                                                                        |
| Output           | Phys/B2pphh_kpiLine/Particles                                                                                                                                                                                                                                                             |
