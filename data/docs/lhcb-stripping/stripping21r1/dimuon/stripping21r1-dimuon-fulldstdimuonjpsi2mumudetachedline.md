[[stripping21r1 lines]](./stripping21r1-index)

# StrippingFullDSTDiMuonJpsi2MuMuDetachedLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseJpsi2MuMu_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)/Particles')\>0 |

FilterDesktop/FullDSTDiMuonJpsi2MuMuDetachedLine

|                 |                                                                                                                                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 500.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -8000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MINTREE('mu+'==ABSID,PIDmu) \> 0.0) & (MM \> 2996.916) & (MM \< 3196.916) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> -1000.0) & ((BPVDLS\>3)\|(BPVDLS\<-3)) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)' ]                                                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                        |
| Output          | Phys/FullDSTDiMuonJpsi2MuMuDetachedLine/Particles                                                                                                                                                                                                                                           |
