[[stripping21r1 lines]](./stripping21r1-index)

# StrippingMicroDSTDiMuonDiMuonIncLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/MicroDSTDiMuonDiMuonIncLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiMuon](./stripping21r1-stdloosedimuon) /Particles')\>0 |

**FilterDesktop/MicroDSTDiMuonDiMuonIncLine**

|                 |                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 650.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (in_range( 3000.0 \*MeV, MM, 100000000.0 \*MeV)) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0) |
| Inputs          | [ 'Phys/ [StdLooseDiMuon](./stripping21r1-stdloosedimuon) ' ]                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                |
| Output          | Phys/MicroDSTDiMuonDiMuonIncLine/Particles                                                                                                                                                                                          |
