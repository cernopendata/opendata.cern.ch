[[stripping21r1 lines]](./stripping21r1-index)

# StrippingJpsiMuMuforD0MuMuLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/JpsiMuMuforD0MuMuLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 0.50000000                           |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

FilterDesktop/JpsiMuMuforD0MuMuLine

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 750.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 5000.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 5000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MINTREE('mu+'==ABSID,MIPCHI2DV(PRIMARY)) \> 3.0 \*MeV) & (MAXTREE('mu+'==ABSID,MIPCHI2DV(PRIMARY)) \> 8.0 \*MeV) & (MAXTREE('mu+'==ABSID,PT)\> 1100.0 \*MeV) & (MM \> 2900) & (MM \< 3280) & (VFASPF(VCHI2PDOF)\< 10.0) & (PT \> 1800.0) & (BPVDIRA\> 0.9997) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)' ]                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/JpsiMuMuforD0MuMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
