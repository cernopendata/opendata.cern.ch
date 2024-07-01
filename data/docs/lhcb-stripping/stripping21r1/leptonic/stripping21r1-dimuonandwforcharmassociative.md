[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDiMuonAndWForCharmAssociative

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/DiMuonAndWForCharmAssociative/Particles |
| Postscale      | 1.0000000                                    |
| HLT            | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/SelWForCharmAssociative**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ( 'mu+'== ABSID ) & ( PT \> 15 \* GeV )                             |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/SelWForCharmAssociative/Particles                              |

**CombineParticles/SelDiMuonForCharmAssociative**

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ISMUON & ( PT \> 650 \* MeV ) & ( TRCHI2DOF \< 5 ) ' , 'mu-' : ' ISMUON & ( PT \> 650 \* MeV ) & ( TRCHI2DOF \< 5 ) ' } |
| CombinationCut   | psi \| psi_prime \| ( 8 \* GeV \< AM )                                                                                                           |
| MotherCut        | chi2vx \< 20                                                                                                                                     |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                            |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                    |
| Output           | Phys/SelDiMuonForCharmAssociative/Particles                                                                                                      |

**CombineParticles/DiMuonAndWForCharmAssociative**

|                  |                                                                            |
|------------------|----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonForCharmAssociative' , 'Phys/SelWForCharmAssociative' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }       |
| CombinationCut   | AALL                                                                       |
| MotherCut        | ALL                                                                        |
| DecayDescriptor  | [chi_b2(2P) -\> J/psi(1S) mu+]cc                                         |
| DecayDescriptors | [ '[chi_b2(2P) -\> J/psi(1S) mu+]cc' ]                                 |
| Output           | Phys/DiMuonAndWForCharmAssociative/Particles                               |
