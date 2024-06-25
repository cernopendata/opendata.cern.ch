[[stripping21r1 lines]](./stripping21r1-index)

# StrippingFullDSTDiMuonPsi2MuMuTOSLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/FullDSTDiMuonPsi2MuMuTOSLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

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

FilterDesktop/FullDSTDiMuonPsi2MuMu_SelP2MuMu

|                 |                                                                                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 1000.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> 10000.0 \*MeV) & (MINTREE('mu+'==ABSID,PIDmu) \> 0.0) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (ADMASS('psi(2S)') \< 100.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 20.0) & (PT \> 3000.0 \*MeV) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)' ]                                                                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                                                                               |
| Output          | Phys/FullDSTDiMuonPsi2MuMu_SelP2MuMu/Particles                                                                                                                                                                                                                     |

TisTosParticleTagger/FullDSTDiMuonPsi2MuMuTOSLine

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/FullDSTDiMuonPsi2MuMu_SelP2MuMu' ]                                                                      |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/FullDSTDiMuonPsi2MuMuTOSLine/Particles                                                                       |
| TisTosSpecs     | { 'Hlt1DiMuonHighMassDecision%TOS' : 0 , 'Hlt2DiMuonPsi2SHighPTDecision%TOS' : 0 , 'L0.\*Mu.\*Decision%TOS' : 0 } |
