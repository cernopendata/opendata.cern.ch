[[stripping21r1 lines]](./stripping21r1-index)

# StrippingMicroDSTDiMuonDiMuonSameSignLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/MicroDSTDiMuonDiMuonSameSignLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | None                                            |
| Prescale       | 0.050000000                                     |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuonSameSign_Particles**

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiMuonSameSign](./stripping21r1-stdloosedimuonsamesign) /Particles')\>0 |

**FilterDesktop/MicroDSTDiMuonDiMuonSameSignLine**

|                 |                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 650.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MM \> 3000.0) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0 \*MeV) |
| Inputs          | [ 'Phys/ [StdLooseDiMuonSameSign](./stripping21r1-stdloosedimuonsamesign) ' ]                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                    |
| Output          | Phys/MicroDSTDiMuonDiMuonSameSignLine/Particles                                                                                                                                                         |
