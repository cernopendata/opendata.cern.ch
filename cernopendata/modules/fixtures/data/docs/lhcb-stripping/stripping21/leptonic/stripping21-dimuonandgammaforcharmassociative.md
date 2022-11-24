[[stripping21 lines]](./stripping21-index)

# StrippingDiMuonAndGammaForCharmAssociative

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/DiMuonAndGammaForCharmAssociative/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | None                                             |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**CombineParticles/SelDiMuonForCharmAssociative**

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ISMUON & ( PT \> 650 \* MeV ) & ( TRCHI2DOF \< 5 ) ' , 'mu-' : ' ISMUON & ( PT \> 650 \* MeV ) & ( TRCHI2DOF \< 5 ) ' } |
| CombinationCut   | psi \| psi_prime \| ( 8 \* GeV \< AM )                                                                                                           |
| MotherCut        | chi2vx \< 20                                                                                                                                     |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                            |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                    |
| Output           | Phys/SelDiMuonForCharmAssociative/Particles                                                                                                      |

**LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) /Particles')\>0 |

**CombineParticles/DiMuonAndGammaForCharmAssociative**

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonForCharmAssociative' , 'Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : ' dimuon_tight ' , 'gamma' : ' PT \> 3.0 \* GeV ' }                            |
| CombinationCut   | AALL                                                                                                        |
| MotherCut        | ALL                                                                                                         |
| DecayDescriptor  | chi_b2(1P) -\> J/psi(1S) gamma                                                                              |
| DecayDescriptors | [ ' chi_b2(1P) -\> J/psi(1S) gamma' ]                                                                     |
| Output           | Phys/DiMuonAndGammaForCharmAssociative/Particles                                                            |
