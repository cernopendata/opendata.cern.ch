[[stripping21r1 lines]](./stripping21r1-index)

# StrippingChiAndWForCharmAssociative

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/ChiAndWForCharmAssociative/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

**FilterDesktop/SelWForCharmAssociative**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ( 'mu+'== ABSID ) & ( PT \> 15 \* GeV )                             |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/SelWForCharmAssociative/Particles                              |

**LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) /Particles')\>0 |

**CombineParticles/SelPreChiAndWForCharmAssociative**

|                  |                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonForCharmAssociative' , 'Phys/SelWForCharmAssociative' , 'Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) ' ]                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : ' ( M \< 3.21 \* GeV ) \| in_range ( 8.5 \* GeV , M , 12.0 \* GeV ) ' , 'gamma' : ' ( PT \> 400 \* MeV ) & ( CL \> 0.05 ) ' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | ( AM12 - AM1 \< 1.05 \* GeV ) \| ( AM12 - AM1 \< 1.05 \* GeV )                                                                                                                             |
| MotherCut        | ALL                                                                                                                                                                                        |
| DecayDescriptor  | [chi_b2(2P) -\> J/psi(1S) gamma mu+]cc                                                                                                                                                   |
| DecayDescriptors | [ '[chi_b2(2P) -\> J/psi(1S) gamma mu+]cc' ]                                                                                                                                           |
| Output           | Phys/SelPreChiAndWForCharmAssociative/Particles                                                                                                                                            |

**Pi0Veto::Tagger/ChiAndWForCharmAssociative**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | "gamma" == ID                                 |
| Inputs          | [ 'Phys/SelPreChiAndWForCharmAssociative' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/ChiAndWForCharmAssociative/Particles     |
