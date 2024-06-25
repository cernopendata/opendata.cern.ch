[[stripping21 lines]](./stripping21-index)

# StrippingB2XuMuNuB2PiLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/B2XuMuNuB2PiLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 0.10000000                      |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XuMuNuB2PiLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuL0TOS_forB2XuMuNu

|                 |                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.5)& (PIDmu-PIDpi\> 3.0 )& (PIDmu-PIDp\> 0.0 )& (PIDmu-PIDK\> 0.0 )& (MIPCHI2DV(PRIMARY)\> 12 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                             |
| Output          | Phys/MuL0TOS_forB2XuMuNu/Particles                                                                                                                                               |

TisTosParticleTagger/MuL0TOS_forB2XuMuNuTOS

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/MuL0TOS_forB2XuMuNu' ]      |
| DecayDescriptor | None                                  |
| Output          | Phys/MuL0TOS_forB2XuMuNuTOS/Particles |
| TisTosSpecs     | { 'L0.\*Muon.\*Decision%TOS' : 0 }    |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/Pi_forB2XuMuNu

|                 |                                                                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 3000.0 \*MeV) & (PT\> 800.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK-PIDpi\< -5.0 )& (PIDp \< -0.0 )& (PIDmu \< -0.0 ) & (MIPCHI2DV(PRIMARY)\> 16 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                                |
| DecayDescriptor | None                                                                                                                                                                     |
| Output          | Phys/Pi_forB2XuMuNu/Particles                                                                                                                                            |

CombineParticles/PiMu_forB2XuMuNu

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuL0TOS_forB2XuMuNuTOS' , 'Phys/Pi_forB2XuMuNu' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }       |
| CombinationCut   | (AM\>1500.0\*MeV) & (AM\<5500.0\*MeV)                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (ratio \> 0.4) |
| DecayDescriptor  | None                                                                                 |
| DecayDescriptors | [ '[B0 -\> pi+ mu-]cc' ]                                                         |
| Output           | Phys/PiMu_forB2XuMuNu/Particles                                                      |

TisTosParticleTagger/B2XuMuNuB2PiLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PiMu_forB2XuMuNu' ]                                                        |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/B2XuMuNuB2PiLine/Particles                                                      |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
