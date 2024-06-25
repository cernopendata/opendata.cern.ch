[[stripping21r1 lines]](./stripping21r1-index)

# StrippingPhiToKSKS_PhiToKKLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/PhiToKSKS_PhiToKKLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 0.0010000000                         |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingPhiToKSKS_PhiToKKLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForPhiToKSKS

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV) & (PIDK \> 7) & (MIPCHI2DV(PRIMARY) \< 9) & (TRGHOSTPROB \< 0.35) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)' ]  |
| DecayDescriptor | None                                                                               |
| Output          | Phys/KaonsForPhiToKSKS/Particles                                                   |

CombineParticles/Sel_PhiToKSKS_PhiToKK

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForPhiToKSKS' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                 |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 1100 + 30\*MeV) & (ACUTDOCACHI2(20,''))          |
| MotherCut        | (M \< 1100 +20\*MeV) & (VFASPF(VCHI2/VDOF) \< 6) & (MIPCHI2DV(PRIMARY) \< 9) |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                          |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                  |
| Output           | Phys/Sel_PhiToKSKS_PhiToKK/Particles                                         |

FitDecayTrees/FITTER_SEL_PhiToKSKS_PhiToKK

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | DECTREE('phi(1020) -\> K+ K-')              |
| Inputs          | [ 'Phys/Sel_PhiToKSKS_PhiToKK' ]          |
| DecayDescriptor | None                                        |
| Output          | Phys/FITTER_SEL_PhiToKSKS_PhiToKK/Particles |

FilterDesktop/PhiToKSKS_PhiToKKLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | (M \< 1100 \*MeV)                         |
| Inputs          | [ 'Phys/FITTER_SEL_PhiToKSKS_PhiToKK' ] |
| DecayDescriptor | None                                      |
| Output          | Phys/PhiToKSKS_PhiToKKLine/Particles      |
