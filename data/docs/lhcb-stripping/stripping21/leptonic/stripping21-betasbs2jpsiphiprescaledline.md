[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBs2JpsiPhiPrescaledLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/BetaSBs2JpsiPhiPrescaledLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | HLT_PASS_RE('Hlt2DiMuonJPsiDecision')       |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) /Particles')\>0 |

**FilterDesktop/Phi2KKForBetaSBetaS**

|                 |                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (in_range(980,M,1050))& (PT \> 500.\*MeV) & (VFASPF(VCHI2) \< 25)& (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 5 )& (MINTREE('K+'==ABSID, PIDK) \> 0) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) ' ]                                                                                 |
| DecayDescriptor | None                                                                                                                                          |
| Output          | Phys/Phi2KKForBetaSBetaS/Particles                                                                                                            |

**CombineParticles/BetaSBs2JpsiPhiPrescaledLine**

|                  |                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Phi2KKForBetaSBetaS' , 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21-stdmassconstrainedjpsi2mumu) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                                                           |
| CombinationCut   | in_range(5050,AM,5650)                                                                                               |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF) \< 20)                                                                    |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                                                                         |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                                                                 |
| Output           | Phys/BetaSBs2JpsiPhiPrescaledLine/Particles                                                                          |
