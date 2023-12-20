[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLb2pMuNuVubFakemuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Lb2pMuNuVubFakemuLine/Particles    |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS_RE('Hlt2Topo2Body.\*Decision') |
| Prescale       | 0.050000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingLb2pMuNuVubFakemuLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)/Particles')\>0 |

FilterDesktop/fakeMu_forLb2pMuNuVub

|                 |                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (~ISMUON) & (INMUON)& (MIPCHI2DV(PRIMARY)\> 16.0 ) |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)' ]                                                       |
| DecayDescriptor | None                                                                                                                                      |
| Output          | Phys/fakeMu_forLb2pMuNuVub/Particles                                                                                                      |

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

CombineParticles/pMu_fakemu_Lb_forLb2pMuNuVub

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/fakeMu_forLb2pMuNuVub' , 'Phys/p_forLb2pMuNuVub' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }          |
| CombinationCut   | (AM\>1000.0\*MeV)                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (Lb_PT \> 1500.0)& (BPVVDCHI2 \>150.0) |
| DecayDescriptor  | None                                                                                   |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ mu-]cc' ]                                                     |
| Output           | Phys/pMu_fakemu_Lb_forLb2pMuNuVub/Particles                                            |

TisTosParticleTagger/Lb2pMuNuVubFakemuLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/pMu_fakemu_Lb_forLb2pMuNuVub' ] |
| DecayDescriptor | None                                      |
| Output          | Phys/Lb2pMuNuVubFakemuLine/Particles      |
| TisTosSpecs     | { 'Hlt2.\*Topo2Body.\*Decision%TOS' : 0 } |
