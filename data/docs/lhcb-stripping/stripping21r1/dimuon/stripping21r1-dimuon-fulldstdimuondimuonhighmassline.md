[[stripping21r1 lines]](./stripping21r1-index)

# StrippingFullDSTDiMuonDiMuonHighMassLine

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonDiMuonHighMassLine/Particles |
| Postscale      | 1.0000000                                      |
| HLT            | None                                           |
| Prescale       | 1.0000000                                      |
| L0DU           | None                                           |
| ODIN           | None                                           |

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

FilterDesktop/FullDSTDiMuonDiMuonHighMassLine

|                 |                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 1000.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MM \> 8500.0) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0) & (MINTREE('mu+'==ABSID,PIDmu)\>0) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)' ]                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                 |
| Output          | Phys/FullDSTDiMuonDiMuonHighMassLine/Particles                                                                                                                                                                                       |
