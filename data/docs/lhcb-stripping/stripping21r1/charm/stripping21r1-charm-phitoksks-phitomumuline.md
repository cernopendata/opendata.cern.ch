[[stripping21r1 lines]](./stripping21r1-index)

# StrippingPhiToKSKS_PhiToMuMuLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/PhiToKSKS_PhiToMuMuLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 0.010000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingPhiToKSKS_PhiToMuMuLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)/Particles')\>0 |

FilterDesktop/MuonsForPhiToKSKS

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV) & (PIDmu \> 0) & (MIPCHI2DV(PRIMARY) \< 9) & (TRGHOSTPROB \< 0.35) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)' ]   |
| DecayDescriptor | None                                                                                |
| Output          | Phys/MuonsForPhiToKSKS/Particles                                                    |

CombineParticles/Sel_PhiToKSKS_PhiToMuMu

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForPhiToKSKS' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                               |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 1100 + 30\*MeV) & (ACUTDOCACHI2(20,''))          |
| MotherCut        | (M \< 1100 +20\*MeV) & (VFASPF(VCHI2/VDOF) \< 6) & (MIPCHI2DV(PRIMARY) \< 9) |
| DecayDescriptor  | phi(1020) -\> mu+ mu-                                                        |
| DecayDescriptors | [ 'phi(1020) -\> mu+ mu-' ]                                                |
| Output           | Phys/Sel_PhiToKSKS_PhiToMuMu/Particles                                       |

FitDecayTrees/FITTER_SEL_PhiToKSKS_PhiToMuMu

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('phi(1020) -\> mu+ mu-')              |
| Inputs          | [ 'Phys/Sel_PhiToKSKS_PhiToMuMu' ]          |
| DecayDescriptor | None                                          |
| Output          | Phys/FITTER_SEL_PhiToKSKS_PhiToMuMu/Particles |

FilterDesktop/PhiToKSKS_PhiToMuMuLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | (M \< 1100 \*MeV)                           |
| Inputs          | [ 'Phys/FITTER_SEL_PhiToKSKS_PhiToMuMu' ] |
| DecayDescriptor | None                                        |
| Output          | Phys/PhiToKSKS_PhiToMuMuLine/Particles      |
