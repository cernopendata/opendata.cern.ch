[[stripping21 lines]](./stripping21-index)

# StrippingButo5h_5pi_exclLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Buto5h_5pi_exclLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/Buto5hGlobalEVventCutFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 200 ) |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/Buto5h_5pi_exclLine

|                  |                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : ' (PT \> 250.0\*MeV) & (TRCHI2DOF \< 1.7) & (MIPCHI2DV(PRIMARY) \> 6.0) & (PROBNNpi \> 0.15) & (TRGHP \< 0.2) ' , 'pi-' : ' (PT \> 250.0\*MeV) & (TRCHI2DOF \< 1.7) & (MIPCHI2DV(PRIMARY) \> 6.0) & (PROBNNpi \> 0.15) & (TRGHP \< 0.2) ' } |
| CombinationCut   | (AM \< 5679.0\*MeV) & (AM \> 5079.0\*MeV) & (AMAXDOCA('LoKi::TrgDistanceCalculator') \< 0.14)                                                                                                                                                                      |
| MotherCut        | (BPVDIRA \> 0.99999) & (BPVVDCHI2 \> 500.0) & (VFASPF(VCHI2) \< 12.0) & (PT \> 1000.0\*MeV) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 400.0)                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[B+ -\> pi+ pi+ pi+ pi- pi-]cc' ]                                                                                                                                                                                                                           |
| Output           | Phys/Buto5h_5pi_exclLine/Particles                                                                                                                                                                                                                                 |
