[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB23MuNu_TriFakeMuLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B23MuNu_TriFakeMuLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 0.010000000                          |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB23MuNu_TriFakeMuLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)/Particles',True)\>0 |

FilterDesktop/Selection_B23MuNu_FakeMuons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (TRGHP \< 0.35) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PT \> 0)        |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1p1-commonparticles-stdallnopidsmuons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B23MuNu_FakeMuons/Particles                                            |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

FilterDesktop/Selection_B23MuNu_Muons

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (TRGHP \< 0.35) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PT \> 0)& (PIDmu\> 0.0) & (PIDmu-PIDK\> 0.0) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                                |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/Selection_B23MuNu_Muons/Particles                                                                             |

CombineParticles/Sel_B23MuNu_Jpsi

|                  |                                                               |
|------------------|---------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B23MuNu_Muons' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                |
| CombinationCut   | ATRUE                                                         |
| MotherCut        | ALL                                                           |
| DecayDescriptor  | None                                                          |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' , '[J/psi(1S) -\> mu+ mu+]cc' ] |
| Output           | Phys/Sel_B23MuNu_Jpsi/Particles                               |

CombineParticles/B23MuNu_TriFakeMuLine

|                  |                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Sel_B23MuNu_Jpsi' , 'Phys/Selection_B23MuNu_FakeMuons' ]                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                            |
| CombinationCut   | ATRUE                                                                                                                                                                           |
| MotherCut        | (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 10000.0 \*MeV) & (BPVDIRA \> 0.999) & (PT \> 2000.0) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF) \< 4.0) & (M \> 0.0) & (M \< 7500.0) |
| DecayDescriptor  | [B+ -\> J/psi(1S) mu+]cc                                                                                                                                                      |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) mu+]cc' ]                                                                                                                                              |
| Output           | Phys/B23MuNu_TriFakeMuLine/Particles                                                                                                                                            |
