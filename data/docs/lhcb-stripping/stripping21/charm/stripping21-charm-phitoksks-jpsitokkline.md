[[stripping21 lines]](./stripping21-index)

# StrippingPhiToKSKS_JPsiToKKLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/PhiToKSKS_JPsiToKKLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 0.010000000                           |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingPhiToKSKS_JPsiToKKLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForPhiToKSKS

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV) & (PIDK \> 7) & (MIPCHI2DV(PRIMARY) \< 9) & (TRGHOSTPROB \< 0.35) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' ]    |
| DecayDescriptor | None                                                                               |
| Output          | Phys/KaonsForPhiToKSKS/Particles                                                   |

CombineParticles/Sel_PhiToKSKS_JPsiToKK

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForPhiToKSKS' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 120 +30\*MeV) & (APT \> 500\*MeV)& (ACUTDOCACHI2(20,''))           |
| MotherCut        | (DMASS('J/psi(1S)') \< 120 +20\*MeV)& (VFASPF(VCHI2/VDOF) \< 6) & (MIPCHI2DV(PRIMARY) \< 9) |
| DecayDescriptor  | J/psi(1S) -\> K+ K-                                                                         |
| DecayDescriptors | [ 'J/psi(1S) -\> K+ K-' ]                                                                 |
| Output           | Phys/Sel_PhiToKSKS_JPsiToKK/Particles                                                       |

FitDecayTrees/FITTER_SEL_PhiToKSKS_JPsiToKK

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | DECTREE('J/psi(1S) -\> K+ K-')               |
| Inputs          | [ 'Phys/Sel_PhiToKSKS_JPsiToKK' ]          |
| DecayDescriptor | None                                         |
| Output          | Phys/FITTER_SEL_PhiToKSKS_JPsiToKK/Particles |

FilterDesktop/PhiToKSKS_JPsiToKKLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | (DMASS('J/psi(1S)') \< 120 \*MeV)          |
| Inputs          | [ 'Phys/FITTER_SEL_PhiToKSKS_JPsiToKK' ] |
| DecayDescriptor | None                                       |
| Output          | Phys/PhiToKSKS_JPsiToKKLine/Particles      |
