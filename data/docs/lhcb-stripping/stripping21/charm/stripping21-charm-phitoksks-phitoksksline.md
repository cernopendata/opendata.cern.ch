[[stripping21 lines]](./stripping21-index)

# StrippingPhiToKSKS_PhiToKsKsLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/PhiToKSKS_PhiToKsKsLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingPhiToKSKS_PhiToKsKsLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqKsForPhiToKSKS

GaudiSequencer/SEQ:KsLLForPhiToKSKS

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KsLLForPhiToKSKS

|                 |                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV) & (ADMASS('KS0') \< 50 \*MeV) & (BPVVD \> 10.0 \*mm) & (BPVVDCHI2 \> 100) & CHILDCUT((TRGHOSTPROB \< 0.35),1) & CHILDCUT((TRGHOSTPROB \< 0.35),2) & (VFASPF(VCHI2PDOF) \< 4) & (BPVDIRA \> 0.9999) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                |
| Output          | Phys/KsLLForPhiToKSKS/Particles                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KsDDForPhiToKSKS

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KsDDForPhiToKSKS

|                 |                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\> 200 \*MeV) & (ADMASS('KS0') \< 50 \*MeV) & (BPVVD \> 10.0 \*mm) & (BPVVDCHI2 \> 100) & (VFASPF(VCHI2PDOF) \< 4) & (BPVDIRA \> 0.999) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                                    |
| DecayDescriptor | None                                                                                                                                       |
| Output          | Phys/KsDDForPhiToKSKS/Particles                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/KsForPhiToKSKS

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Code            | ALL                                                     |
| Inputs          | [ 'Phys/KsDDForPhiToKSKS' , 'Phys/KsLLForPhiToKSKS' ] |
| DecayDescriptor | None                                                    |
| Output          | Phys/KsForPhiToKSKS/Particles                           |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Sel_PhiToKSKS_PhiToKsKs

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsForPhiToKSKS' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                   |
| CombinationCut   | ( (ACHILDCUT(CHILDCUT(ISLONG,1),1)) \| (ACHILDCUT(CHILDCUT(ISLONG,1),2)) ) & (APT \> 400 \*MeV) & (AM \< 1100 + 30\*MeV) & (ACUTDOCACHI2(20,'')) |
| MotherCut        | (M \< 1100 +20\*MeV) & (VFASPF(VCHI2/VDOF) \< 6) & (MIPCHI2DV(PRIMARY) \< 9)                                                                     |
| DecayDescriptor  | phi(1020) -\> KS0 KS0                                                                                                                            |
| DecayDescriptors | [ 'phi(1020) -\> KS0 KS0' ]                                                                                                                    |
| Output           | Phys/Sel_PhiToKSKS_PhiToKsKs/Particles                                                                                                           |

FitDecayTrees/FITTER_SEL_PhiToKSKS_PhiToKsKs

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('phi(1020) -\> KS0 KS0')              |
| Inputs          | [ 'Phys/Sel_PhiToKSKS_PhiToKsKs' ]          |
| DecayDescriptor | None                                          |
| Output          | Phys/FITTER_SEL_PhiToKSKS_PhiToKsKs/Particles |

FilterDesktop/PhiToKSKS_PhiToKsKsLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | (M \< 1100 \*MeV)                           |
| Inputs          | [ 'Phys/FITTER_SEL_PhiToKSKS_PhiToKsKs' ] |
| DecayDescriptor | None                                        |
| Output          | Phys/PhiToKSKS_PhiToKsKsLine/Particles      |
