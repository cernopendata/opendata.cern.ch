[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLb2pMuNuVubSSLine

## Properties:

|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| OutputLocation | Phys/Lb2pMuNuVubSSLine/Particles                                                        |
| Postscale      | 1.0000000                                                                               |
| HLT            | HLT_PASS_RE('Hlt2.\*SingleMuon.\*Decision')\| HLT_PASS_RE('Hlt2TopoMu2Body.\*Decision') |
| Prescale       | 1.0000000                                                                               |
| L0DU           | L0_CHANNEL_RE('Muon')                                                                   |
| ODIN           | None                                                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingLb2pMuNuVubSSLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/Mu_forLb2pMuNuVub

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 16.0 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                         |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/Mu_forLb2pMuNuVub/Particles                                                                                    |

TisTosParticleTagger/Mu_forLb2pMuNuVubTOS

|                 |                                     |
|-----------------|-------------------------------------|
| Inputs          | [ 'Phys/Mu_forLb2pMuNuVub' ]      |
| DecayDescriptor | None                                |
| Output          | Phys/Mu_forLb2pMuNuVubTOS/Particles |
| TisTosSpecs     | { 'L0.\*Muon.\*Decision%TOS' : 0 }  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/p_forLb2pMuNuVub

|                 |                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 6.0 )& (P\> 15000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (PIDp-PIDpi\> 10.0 )& (PIDp-PIDK\> 10.0 ) & (MIPCHI2DV(PRIMARY)\> 16.0 )& (switch(ISMUON,1,0) \< 1) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                       |
| Output          | Phys/p_forLb2pMuNuVub/Particles                                                                                                                                                            |

CombineParticles/pMuSS_Lb_forLb2pMuNuVub

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Mu_forLb2pMuNuVubTOS' , 'Phys/p_forLb2pMuNuVub' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }          |
| CombinationCut   | (AM\>1000.0\*MeV)                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (Lb_PT \> 1500.0)& (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                   |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ mu+]cc' ]                                                     |
| Output           | Phys/pMuSS_Lb_forLb2pMuNuVub/Particles                                                 |

TisTosParticleTagger/Lb2pMuNuVubSSLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/pMuSS_Lb_forLb2pMuNuVub' ]                                                 |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/Lb2pMuNuVubSSLine/Particles                                                     |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
