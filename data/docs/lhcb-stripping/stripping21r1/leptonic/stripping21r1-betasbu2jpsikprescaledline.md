[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBu2JpsiKPrescaledLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/BetaSBu2JpsiKPrescaledLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | HLT_PASS_RE('Hlt2DiMuonJPsiDecision')     |
| Prescale       | 0.50000000                                |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) /Particles')\>0 |

**FilterDesktop/NoIPKaonsForBetaSBetaS**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5 ) & (PIDK \> 0)                                     |
| Inputs          | [ 'Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/NoIPKaonsForBetaSBetaS/Particles                               |

**CombineParticles/BetaSBu2JpsiKPrescaledLine**

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/NoIPKaonsForBetaSBetaS' , 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(PT \> 500.\*MeV)' , 'K-' : '(PT \> 500.\*MeV)' }                            |
| CombinationCut   | in_range(5050,AM,5550)                                                                                                    |
| MotherCut        | in_range(5150,M,5450) & (VFASPF(VCHI2PDOF) \< 10)                                                                         |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                                 |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                                         |
| Output           | Phys/BetaSBu2JpsiKPrescaledLine/Particles                                                                                 |
