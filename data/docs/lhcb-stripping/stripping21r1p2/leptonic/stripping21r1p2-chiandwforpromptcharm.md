[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingChiAndWForPromptCharm

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/ChiAndWForPromptCharm/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**FilterDesktop/SelWForPromptCharm**

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ( 'mu+'== ABSID ) & ( PT \> 15 \* GeV ) & ( -100 \* GeV \< ptCone ) & ( -100 \* GeV \< etCone ) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]                           |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/SelWForPromptCharm/Particles                                                               |

**FilterDesktop/SelMuonForPromptCharm**

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | ISMUON & in_range ( 2 , ETA , 4.9 ) & ( PT \> 550 \* MeV ) & ( PIDmu - PIDpi \> 0 ) & ( CLONEDIST \> 5000 ) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]                                       |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/SelMuonForPromptCharm/Particles                                                                        |

**CombineParticles/SelDiMuonForPromptCharm**

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/SelMuonForPromptCharm' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | psi \| psi_prime \| ( AM \> 8 \* GeV )         |
| MotherCut        | chi2vx \< 20                                   |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                          |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                  |
| Output           | Phys/SelDiMuonForPromptCharm/Particles         |

**CombineParticles/SelDiMuonAndWForPromptCharm**

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonForPromptCharm' , 'Phys/SelWForPromptCharm' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | AALL                                                                 |
| MotherCut        | ALL                                                                  |
| DecayDescriptor  | None                                                                 |
| DecayDescriptors | [ ' [ chi_b0(2P) -\> J/psi(1S) mu+ ]cc ' ]                       |
| Output           | Phys/SelDiMuonAndWForPromptCharm/Particles                           |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**DaVinci::N3BodyDecays/SelPreChiAndWForPromptCharm**

|                  |                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonAndWForPromptCharm' , 'Phys/SelDiMuonForPromptCharm' , 'Phys/SelWForPromptCharm' , 'Phys/ [StdLooseAllPhotons](./stripping21r1p2-stdlooseallphotons) ' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : ' ( M \< 3.21 \* GeV ) \| in_range ( 8.5 \* GeV , M , 12.0 \* GeV ) ' , 'gamma' : ' ( PT \> 400 \* MeV ) & ( CL \> 0.05 ) ' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | AM13 - AM1 \< 1.01 \* GeV                                                                                                                                                                  |
| MotherCut        | ALL                                                                                                                                                                                        |
| DecayDescriptor  | [ chi_b1(2P) -\> J/psi(1S) mu+ gamma ]cc                                                                                                                                                 |
| DecayDescriptors | [ '[ chi_b1(2P) -\> J/psi(1S) mu+ gamma ]cc' ]                                                                                                                                         |
| Output           | Phys/SelPreChiAndWForPromptCharm/Particles                                                                                                                                                 |

**Pi0Veto::Tagger/ChiAndWForPromptCharm**

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | "gamma" == ID                            |
| Inputs          | [ 'Phys/SelPreChiAndWForPromptCharm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/ChiAndWForPromptCharm/Particles     |
