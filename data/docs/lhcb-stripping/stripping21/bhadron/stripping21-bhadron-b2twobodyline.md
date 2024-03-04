[[stripping21 lines]](./stripping21-index)

# StrippingB2twobodyLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/B2twobodyLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB2twobodyLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 70 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqInputForB2twobody

GaudiSequencer/SEQ:PiForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PiForB2twobody

|                 |                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0\*MeV)& (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF\<4.0)& (PIDpi-PIDK \> 2.0)& (PIDpi-PIDp \> 2.0)& (TRGHP \< 0.3) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                     |
| DecayDescriptor | None                                                                                                                          |
| Output          | Phys/PiForB2twobody/Particles                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KForB2twobody

|                 |                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0\*MeV)& (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF\<4.0)& (PIDK-PIDpi \> 2.0)& (PIDK-PIDp \> 2.0)& (TRGHP \< 0.3) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]                                                    |
| DecayDescriptor | None                                                                                                                         |
| Output          | Phys/KForB2twobody/Particles                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:pForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/pForB2twobody

|                 |                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0\*MeV)& (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF\<4.0)& (PIDp-PIDpi \> 2.0)& (PIDp-PIDK \> 2.0)& (TRGHP \< 0.3) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                                |
| DecayDescriptor | None                                                                                                                         |
| Output          | Phys/pForB2twobody/Particles                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KsForB2twobody

GaudiSequencer/SeqMergedKsForKsForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/MergedKsForKsForB2twobody

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/MergedKsForKsForB2twobody/Particles                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KsForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 40.0\*MeV)& (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>400.0)& (MIPCHI2DV(PRIMARY)\>0.0)& CHILDCUT ( PT \> 200.0 , 1 )& CHILDCUT ( PT \> 200.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 16.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 16.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 ) |
| Inputs          | [ 'Phys/MergedKsForKsForB2twobody' ]                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                         |
| Output          | Phys/KsForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LmForB2twobody

GaudiSequencer/SeqMergedLmForLmForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/MergedLmForLmForB2twobody

|                 |                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' , 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ] |
| DecayDescriptor | None                                                                                                                                                        |
| Output          | Phys/MergedLmForLmForB2twobody/Particles                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LmForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 15.0\*MeV)& (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>400.0)& (MIPCHI2DV(PRIMARY)\>0.0)& CHILDCUT ( PT \> 500.0 , 1 )& CHILDCUT ( PT \> 100.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 4.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 16.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 ) |
| Inputs          | [ 'Phys/MergedLmForLmForB2twobody' ]                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                            |
| Output          | Phys/LmForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DzForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/DzForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>225.0)& (MIPCHI2DV(PRIMARY)\>0.0)& CHILDCUT ( PT \> 250.0 , 1 )& CHILDCUT ( PT \> 250.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 )& (ADMASS('D0') \< 40.0\*MeV)& CHILDCUT ( PIDK-PIDpi \> -5.0 , 1 )& CHILDCUT ( PIDpi-PIDK \> -5.0 , 2 ) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)' ]                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/DzForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DpForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

FilterDesktop/DpForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>225.0)& (MIPCHI2DV(PRIMARY)\>9.0)& CHILDCUT ( PT \> 250.0 , 1 )& CHILDCUT ( PT \> 250.0 , 2 )& CHILDCUT ( PT \> 250.0 , 3 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 3 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 3 )& (ADMASS('D+') \< 40.0\*MeV)& CHILDCUT ( PIDK-PIDpi \> -5.0 , 1 )& CHILDCUT ( PIDpi-PIDK \> -5.0 , 2 )& CHILDCUT ( PIDpi-PIDK \> -5.0 , 3 ) |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output          | Phys/DpForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DsForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseDsplus2KKPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)/Particles')\>0 |

FilterDesktop/DsForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>225.0)& (MIPCHI2DV(PRIMARY)\>9.0)& CHILDCUT ( PT \> 250.0 , 1 )& CHILDCUT ( PT \> 250.0 , 2 )& CHILDCUT ( PT \> 250.0 , 3 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 3 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 3 )& (ADMASS('D_s+') \< 40.0\*MeV)& CHILDCUT ( PIDK-PIDpi \> -5.0 , 1 )& CHILDCUT ( PIDK-PIDpi \> 0.0 , 2 )& CHILDCUT ( PIDpi-PIDK \> -5.0 , 3 ) |
| Inputs          | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output          | Phys/DsForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LcForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdac2PKPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)/Particles')\>0 |

FilterDesktop/LcForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)& (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2\>225.0)& (MIPCHI2DV(PRIMARY)\>9.0)& CHILDCUT ( PT \> 250.0 , 1 )& CHILDCUT ( PT \> 250.0 , 2 )& CHILDCUT ( PT \> 250.0 , 3 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 2 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 3 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 3 )& (ADMASS('Lambda_c+') \< 40.0\*MeV)& CHILDCUT ( PIDK-PIDpi \> -5.0 , 1 )& CHILDCUT ( PIDp-PIDpi \> 0.0 , 2 )& CHILDCUT ( PIDp-PIDK \> 0.0 , 2 )& CHILDCUT ( PIDpi-PIDK \> -5.0 , 3 ) |
| Inputs          | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21-commonparticles-stdlooselambdac2pkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output          | Phys/LcForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PhForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedPhi2KK_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedPhi2KK](./stripping21-commonparticles-stdloosedetachedphi2kk)/Particles')\>0 |

FilterDesktop/PhForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ADMASS('phi(1020)') \< 30.0\*MeV)& ( PT \> 1000.0 )& ( VFASPF(VCHI2/VDOF) \< 10.0 )& ( BPVVDCHI2 \> 100.0 )& ( MIPCHI2DV(PRIMARY) \> 16.0 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 9.0 , 2 )& CHILDCUT ( PT \> 300.0 , 1 )& CHILDCUT ( PT \> 300.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 ) |
| Inputs          | [ 'Phys/[StdLooseDetachedPhi2KK](./stripping21-commonparticles-stdloosedetachedphi2kk)' ]                                                                                                                                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                          |
| Output          | Phys/PhForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:JpForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/JpForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ADMASS('J/psi(1S)') \< 3000.0\*MeV)& ( PT \> 1000.0 )& ( VFASPF(VCHI2/VDOF) \< 10.0 )& ( BPVVDCHI2 \> 16.0 )& ( MIPCHI2DV(PRIMARY) \> 0.0 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 0.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 0.0 , 2 )& CHILDCUT ( PT \> 500.0 , 1 )& CHILDCUT ( PT \> 500.0 , 2 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 2 ) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)' ]                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                          |
| Output          | Phys/JpForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DSForB2twobody

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/DSForB2twobody

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (M-MAXTREE('D0'==ABSID,M)\<153.0)& ( PT \> 1000.0 )& ( VFASPF(VCHI2/VDOF) \< 10.0 )& ( BPVVDCHI2 \> 0.0 )& ( MIPCHI2DV(PRIMARY) \> 0.0 )& CHILDCUT ( PT \> 100.0 , 1 )& CHILDCUT ( MIPCHI2DV ( PRIMARY ) \> 0.0 , 1 )& CHILDCUT ( TRCHI2DOF \< 5.0 , 1 )& CHILDCUT ( PT \> 500.0 , 2 )& CHILDCUT ( VFASPF(VCHI2/VDOF) \< 10.0 , 2 )& CHILDCUT ( BPVVDCHI2 \> 225.0 , 2 )& CHILDCUT ( MIPCHI2DV(PRIMARY) \> 0.0 , 2 )& CHILDCUT ( ADMASS('D0') \< 40.0\*MeV , 2 )& ( NINGENERATION ( ( PT \> 250.0 ) , 2 ) == 2 )& ( NINGENERATION ( ( MIPCHI2DV ( PRIMARY ) \> 9.0 ) , 2 ) == 2 )& ( NINGENERATION ( ( TRCHI2DOF \< 5.0 ) , 2 ) == 2 ) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output          | Phys/DSForB2twobody/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/InputForB2twobody

|                 |                                                                                                                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                               |
| Inputs          | [ 'Phys/DSForB2twobody' , 'Phys/DpForB2twobody' , 'Phys/DsForB2twobody' , 'Phys/DzForB2twobody' , 'Phys/JpForB2twobody' , 'Phys/KForB2twobody' , 'Phys/KsForB2twobody' , 'Phys/LcForB2twobody' , 'Phys/LmForB2twobody' , 'Phys/PhForB2twobody' , 'Phys/PiForB2twobody' , 'Phys/pForB2twobody' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                              |
| Output          | Phys/InputForB2twobody/Particles                                                                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/preselForB2twobody

|      |                                                      |
|------|------------------------------------------------------|
| Code | (CONTAINS('Phys/InputForB2twobody/Particles')\> 1.5) |

CombineParticles/B2twobodyLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InputForB2twobody' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'Lambda~0' : 'ALL' , 'p+' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| CombinationCut   | (in_range(4700.0\*MeV, AM, 8000.0\*MeV))& (APT\>5000.0\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10.0)& (BPVVDCHI2 \> 225.0)& (BPVIPCHI2() \< 15.0)& (BPVDIRA \> 0.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'B0 -\> pi+ pi-' , '[B0 -\> K- pi+]cc' , '[B+ -\> D0 pi+]cc' , '[B+ -\> D~0 pi+]cc' , '[B0 -\> D- pi+]cc' , '[B0 -\> D_s- pi+]cc' , '[B+ -\> phi(1020) pi+]cc' , '[B+ -\> J/psi(1S) pi+]cc' , '[B0 -\> D\*(2010)- pi+]cc' , '[Lambda_b0 -\> p+ pi-]cc' , '[Lambda_b0 -\> Lambda_c+ pi-]cc' , 'B0 -\> K+ K-' , '[B+ -\> D0 K+]cc' , '[B+ -\> D~0 K+]cc' , '[B0 -\> D- K+]cc' , '[B0 -\> D_s- K+]cc' , '[B+ -\> K+ phi(1020)]cc' , '[B+ -\> J/psi(1S) K+]cc' , '[B0 -\> D\*(2010)- K+]cc' , '[Lambda_b0 -\> K- p+]cc' , '[Lambda_b0 -\> K- Lambda_c+]cc' , 'B0 -\> p+ p~-' , '[Xi_bc+ -\> D0 p+]cc' , '[Xi_bc+ -\> D~0 p+]cc' , '[Lambda_b0 -\> D- p+]cc' , '[Lambda_b0 -\> D_s- p+]cc' , '[B0 -\> Lambda_c~- p+]cc' , '[Xi_bc+ -\> p+ phi(1020)]cc' , '[Xi_bc+ -\> J/psi(1S) p+]cc' , '[Lambda_b0 -\> D\*(2010)- p+]cc' , 'B0 -\> KS0 phi(1020)' , 'B0 -\> J/psi(1S) KS0' , '[B+ -\> D\*(2010)+ KS0]cc' , '[Lambda_b0 -\> Lambda0 phi(1020)]cc' , '[Lambda_b0 -\> J/psi(1S) Lambda0]cc' , '[Xi_bc+ -\> D\*(2010)+ Lambda0]cc' , '[Xi_b- -\> D\*(2010)- Lambda0]cc' , 'B0 -\> D0 D~0' , '[B+ -\> D+ D0]cc' , '[B+ -\> D0 D_s+]cc' , '[Xi_bc+ -\> D0 Lambda_c+]cc' , '[B+ -\> D\*(2010)+ D0]cc' , '[B0 -\> D~0 D~0]cc' , '[B+ -\> D+ D~0]cc' , '[B+ -\> D_s+ D~0]cc' , '[Xi_bc+ -\> D~0 Lambda_c+]cc' , '[B0 -\> D~0 phi(1020)]cc' , '[B0 -\> D~0 J/psi(1S)]cc' , '[B+ -\> D\*(2010)+ D~0]cc' , 'B0 -\> D+ D-' , '[B+ -\> D+ phi(1020)]cc' , '[B+ -\> D+ J/psi(1S)]cc' , '[B0 -\> D\*(2010)- D+]cc' , '[B0 -\> D- D_s+]cc' , '[Lambda_b0 -\> D- Lambda_c+]cc' , 'B0 -\> D_s+ D_s-' , '[B+ -\> D_s+ phi(1020)]cc' , '[B+ -\> D_s+ J/psi(1S)]cc' , '[B0 -\> D\*(2010)- D_s+]cc' , '[Lambda_b0 -\> D_s- Lambda_c+]cc' , 'B0 -\> Lambda_c+ Lambda_c~-' , '[Xi_bc+ -\> Lambda_c+ phi(1020)]cc' , '[Xi_bc+ -\> J/psi(1S) Lambda_c+]cc' , '[Lambda_b0 -\> D\*(2010)- Lambda_c+]cc' , 'B0 -\> phi(1020) phi(1020)' , 'B0 -\> J/psi(1S) phi(1020)' , '[B+ -\> D\*(2010)+ phi(1020)]cc' , '[B+ -\> D\*(2010)+ J/psi(1S)]cc' , 'B0 -\> D\*(2010)+ D\*(2010)-' ] |
| Output           | Phys/B2twobodyLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
