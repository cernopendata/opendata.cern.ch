[[stripping21 lines]](./stripping21-index)

# StrippingB23MuNu_TriMuLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/B23MuNu_TriMuLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

LoKi::VoidFilter/StrippingB23MuNu_TriMuLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

FilterDesktop/Selection_B23MuNu_Muons

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (TRGHP \< 0.35) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDmu\> 0.0) & (PIDmu-PIDK\> 0.0) & (PT \> 0) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                     |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/Selection_B23MuNu_Muons/Particles                                                                              |

CombineParticles/B23MuNu_TriMuLine

|                  |                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B23MuNu_Muons' ]                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                                                                                                                                                                                   |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 10000.0 \*MeV) & (BPVDIRA \> 0.999) & (PT \> 2000.0) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF) \< 4.0) & (M \> 0.0) & (M \< 7500.0) &(BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 10000.0 \*MeV) & (BPVDIRA \> 0.999) & (PT \> 2000.0) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF) \< 4.0) & (M \> 0.0) & (M \< 7500.0) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> mu+ mu+ mu-]cc' , '[B+ -\> mu+ mu+ mu+]cc' ]                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/B23MuNu_TriMuLine/Particles                                                                                                                                                                                                                                                                                                                                 |
