[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2SMuMu_InclPsi2SToMuMuLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 0.10000000                                        |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }                    |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))                       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                                               |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                                               |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                                       |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                                         |

FilterDesktop/BetaSPsi2SMuMu_InclPsi2SToMuMu

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ALL                                           |
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ]       |
| DecayDescriptor | None                                          |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMu/Particles |

TisTosParticleTagger/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_InclPsi2SToMuMu' ]                    |
| DecayDescriptor | None                                                           |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos/Particles |
| TisTosSpecs     | { 'Hlt1DiMuonHighMassDecision%TOS' : 0 }                       |

TisTosParticleTagger/BetaSPsi2SMuMu_InclPsi2SToMuMuLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos' ] |
| DecayDescriptor | None                                                         |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuLine/Particles            |
| TisTosSpecs     | { 'Hlt2DiMuonPsi2SDecision%TOS' : 0 }                        |
