[[stripping21 lines]](./stripping21-index)

# StrippingFullDSTDiMuonPsi2MuMuDetachedLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonPsi2MuMuDetachedLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | None                                             |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/FullDSTDiMuonPsi2MuMuDetachedLine

|                 |                                                                                                                                                                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 500.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -8000.0 \*MeV) & (MINTREE('mu+'==ABSID,PIDmu) \> 0.0) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (ADMASS('psi(2S)') \< 100.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0 \*MeV) & ((BPVDLS\>3)\|(BPVDLS\<-3)) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)' ]                                                                                                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                             |
| Output          | Phys/FullDSTDiMuonPsi2MuMuDetachedLine/Particles                                                                                                                                                                                                                                                 |
