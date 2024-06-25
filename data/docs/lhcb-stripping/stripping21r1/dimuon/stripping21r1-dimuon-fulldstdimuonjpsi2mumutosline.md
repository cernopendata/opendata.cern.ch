[[stripping21r1 lines]](./stripping21r1-index)

# StrippingFullDSTDiMuonJpsi2MuMuTOSLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonJpsi2MuMuTOSLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT            | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseJpsi2MuMu_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)/Particles')\>0 |

FilterDesktop/FullDSTDiMuonJpsi2MuMu_SelJpsi2MuMu

|                 |                                                                                                                                                                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 650.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 10000.0 \*MeV) & (MINTREE('mu+'==ABSID,PIDmu) \> 0.0) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (MM \> 3010.0) & (MM \< 3170.0) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> 3000.0) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r1-commonparticles-stdloosejpsi2mumu)' ]                                                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                                                                     |
| Output          | Phys/FullDSTDiMuonJpsi2MuMu_SelJpsi2MuMu/Particles                                                                                                                                                                                                       |

TisTosParticleTagger/FullDSTDiMuonJpsi2MuMuTOSLine

|                 |                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/FullDSTDiMuonJpsi2MuMu_SelJpsi2MuMu' ]                                                                 |
| DecayDescriptor | None                                                                                                             |
| Output          | Phys/FullDSTDiMuonJpsi2MuMuTOSLine/Particles                                                                     |
| TisTosSpecs     | { 'Hlt1DiMuonHighMassDecision%TOS' : 0 , 'Hlt2DiMuonJPsiHighPTDecision%TOS' : 0 , 'L0.\*Mu.\*Decision%TOS' : 0 } |
