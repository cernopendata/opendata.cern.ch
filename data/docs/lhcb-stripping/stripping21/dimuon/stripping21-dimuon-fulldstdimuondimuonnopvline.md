[[stripping21 lines]](./stripping21-index)

# StrippingFullDSTDiMuonDiMuonNoPVLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonDiMuonNoPVLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingFullDSTDiMuonDiMuonNoPVLineVOIDFilter

|      |                                                             |
|------|-------------------------------------------------------------|
| Code | recSummary(LHCb.RecSummary.nPVs, 'Rec/Vertex/Primary')\<0.5 |

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/FullDSTDiMuonDiMuonNoPVLine

|                 |                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 650.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MM \> 2900.0) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)' ]                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                              |
| Output          | Phys/FullDSTDiMuonDiMuonNoPVLine/Particles                                                                                                                                                        |
