[[stripping21r1 lines]](./stripping21r1-index)

# StrippingA1MuMuLine

## Properties:

|                |                           |
|----------------|---------------------------|
| OutputLocation | Phys/A1MuMuLine/Particles |
| Postscale      | 1.0000000                 |
| HLT            | None                      |
| Prescale       | 1.0000000                 |
| L0DU           | None                      |
| ODIN           | None                      |

## Filter sequence:

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/A1MuMuLine

|                 |                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 2500.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 2500.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 10) & (MM \> 5000.0) & (VFASPF(VCHI2PDOF)\< 12) & (PT \> 7500.0) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)' ]                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                          |
| Output          | Phys/A1MuMuLine/Particles                                                                                                                                                                     |
