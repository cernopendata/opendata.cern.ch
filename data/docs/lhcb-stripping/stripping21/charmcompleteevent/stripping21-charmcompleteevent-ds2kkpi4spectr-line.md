[[stripping21 lines]](./stripping21-index)

# StrippingDs2KKpi4Spectr_Line

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Ds2KKpi4Spectr_Line/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingDs2KKpi4Spectr_LineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdVeryTightDsplus2KKPi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryTightDsplus2KKPi](./stripping21-commonparticles-stdverytightdsplus2kkpi)/Particles')\>0 |

FilterDesktop/Ds2KKpi4Spectr_Line

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((MAXTREE('pi+'==ABSID, PIDK-PIDpi) \< 3.0) & (MINTREE('K-'==ABSID, PIDK-PIDpi) \> 7.0 ) &((in_range ( 1010.0\* MeV , M12 , 1030.0\* MeV ))\|(in_range ( 0.0\* MeV , M13 , 0.0\* MeV ) & (abs(COSPOL('[D_s+ -\> ^K- K+ pi+]CC', '[D_s+ -\> K- K+ ^pi+]CC', False)) \> 2.0)))& (SUMTREE( ISBASIC , PT ) \> 2800.0\*MeV) & (2 \<= NINGENERATION((MIPCHI2DV(PRIMARY) \> 10.0 ) , 1)) & (PT \> 1000.0) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.0) & (BPVIPCHI2() \< 9.0) ) |
| Inputs          | [ 'Phys/[StdVeryTightDsplus2KKPi](./stripping21-commonparticles-stdverytightdsplus2kkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output          | Phys/Ds2KKpi4Spectr_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                |
