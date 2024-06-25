[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDiMuonAndWForPromptCharm

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/DiMuonAndWForPromptCharm/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**FilterDesktop/SelWForPromptCharm**

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ( 'mu+'== ABSID ) & ( PT \> 15 \* GeV ) & ( -100 \* GeV \< ptCone ) & ( -100 \* GeV \< etCone ) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                             |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/SelWForPromptCharm/Particles                                                               |

**FilterDesktop/SelMuonForPromptCharm**

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | ISMUON & in_range ( 2 , ETA , 4.9 ) & ( PT \> 550 \* MeV ) & ( PIDmu - PIDpi \> 0 ) & ( CLONEDIST \> 5000 ) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                         |
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

**CombineParticles/DiMuonAndWForPromptCharm**

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDiMuonForPromptCharm' , 'Phys/SelWForPromptCharm' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | AALL                                                                 |
| MotherCut        | ALL                                                                  |
| DecayDescriptor  | None                                                                 |
| DecayDescriptors | [ ' [ chi_b0(2P) -\> J/psi(1S) mu+ ]cc ' ]                       |
| Output           | Phys/DiMuonAndWForPromptCharm/Particles                              |
