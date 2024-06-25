[[stripping21 lines]](./stripping21-index)

# StrippingFullDSTDiMuonDiMuonHighMassSameSignLine

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonDiMuonHighMassSameSignLine/Particles |
| Postscale      | 1.0000000                                              |
| HLT            | None                                                   |
| Prescale       | 0.20000000                                             |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuonSameSign_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuonSameSign](./stripping21-commonparticles-stdloosedimuonsamesign)/Particles')\>0 |

FilterDesktop/FullDSTDiMuonDiMuonHighMassSameSignLine

|                 |                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 1000.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MM \> 8500.0) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0 \*MeV) |
| Inputs          | [ 'Phys/[StdLooseDiMuonSameSign](./stripping21-commonparticles-stdloosedimuonsamesign)' ]                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                    |
| Output          | Phys/FullDSTDiMuonDiMuonHighMassSameSignLine/Particles                                                                                                                                                  |
