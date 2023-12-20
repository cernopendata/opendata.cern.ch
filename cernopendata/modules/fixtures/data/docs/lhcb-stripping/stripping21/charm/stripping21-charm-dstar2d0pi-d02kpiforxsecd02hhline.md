[[stripping21 lines]](./stripping21-index)

# StrippingDstar2D0Pi_D02KPiForXSecD02HHLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/Dstar2D0Pi_D02KPiForXSecD02HHLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | HLT_PASS_RE('Hlt1MB.\*')                         |
| Prescale       | 0.10000000                                       |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/Dstar2D0Pi_D02KPiForXSecD02HHLine

|                  |                                                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 10.0)& (BPVIPCHI2() \> 6.0)&(PIDK - PIDpi \> 0.0)' , 'K-' : '(TRCHI2DOF \< 10.0)& (BPVIPCHI2() \> 6.0)&(PIDK - PIDpi \> 0.0)' , 'pi+' : '(TRCHI2DOF \< 10.0)& (BPVIPCHI2() \> 6.0)&(PIDK - PIDpi \< 0.0)' , 'pi-' : '(TRCHI2DOF \< 10.0)& (BPVIPCHI2() \> 6.0)&(PIDK - PIDpi \< 0.0)' } |
| CombinationCut   | (ADAMASS('D0') \< 80.0)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (ADMASS('D0') \< 75.0)& (VFASPF(VCHI2/VDOF) \< 25.0)& (BPVLTIME() \> 0.0002)& (BPVLTFITCHI2() \< 100.0)                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' , 'D0 -\> K- pi+' , 'D0 -\> K+ pi-' , 'D0 -\> K+ K-' ]                                                                                                                                                                                                                                                  |
| Output           | Phys/Dstar2D0Pi_D02KPiForXSecD02HHLine/Particles                                                                                                                                                                                                                                                                             |
