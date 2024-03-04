[[stripping21r1 lines]](./stripping21r1-index)

# StrippingChiCJPsiGammaConvChibLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/ChiCJPsiGammaConvChibLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/ChiCJPsiGammaConvUpsilon_SelMuMu

|                 |                                                                                                                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 400 ) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 3.0) & (MINTREE('mu+'==ABSID,PIDmu)\> 0.0)& (MINTREE('mu+'==ABSID,P) \> 8000 ) & (MM \> 9.0 \*GeV) & (MM \< 12.9 \*GeV) & (VFASPF(VCHI2PDOF)\< 25.0) & (PT \> 0.9 \*GeV) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)' ]                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                              |
| Output          | Phys/ChiCJPsiGammaConvUpsilon_SelMuMu/Particles                                                                                                                                                                                                   |

LoKi::VoidFilter/SelFilterPhys_StdAllTightGammaDD_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllTightGammaDD](./stripping21r1-commonparticles-stdalltightgammadd)/Particles')\>0 |

FilterDesktop/ChiCJPsiGammaConvGammaEE_SelGamma

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (MINTREE('e+'==ABSID,PIDe)\> 0.0) & (MM \< 100.0 \*MeV) & ( PT \> 580.0 \*MeV)        |
| Inputs          | [ 'Phys/[StdAllTightGammaDD](./stripping21r1-commonparticles-stdalltightgammadd)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/ChiCJPsiGammaConvGammaEE_SelGamma/Particles                                      |

CombineParticles/ChiCJPsiGammaConvChibLine

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ChiCJPsiGammaConvGammaEE_SelGamma' , 'Phys/ChiCJPsiGammaConvUpsilon_SelMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'gamma' : 'ALL' }                                   |
| CombinationCut   | (AM \> 9.4 \*GeV) & (AM \< 13.2\*GeV)                                                    |
| MotherCut        | (MM \> 9.5 \*GeV) & (MM \< 13.0\*GeV)                                                    |
| DecayDescriptor  | chi_c1(1P) -\> J/psi(1S) gamma                                                           |
| DecayDescriptors | [ 'chi_c1(1P) -\> J/psi(1S) gamma' ]                                                   |
| Output           | Phys/ChiCJPsiGammaConvChibLine/Particles                                                 |
