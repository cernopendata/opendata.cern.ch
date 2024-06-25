[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBs2JpsiKstarWideLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/BetaSBs2JpsiKstarWideLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**FilterDesktop/NarrowJpsiForBetaSBetaS**

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV)                                                |
| Inputs          | [ 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) ' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/NarrowJpsiForBetaSBetaS/Particles                                                    |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKaons](./stripping21r1-stdloosekaons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21r1-stdloosepions) /Particles')\>0 |

**CombineParticles/DetachedKstarWideListForBetaSBetaS**

|                  |                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21r1-stdloosekaons) ' , 'Phys/ [StdLoosePions](./stripping21r1-stdloosepions) ' ]                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : ' (PT \> 500 \*MeV) & (PIDK \> 0) & (TRGHOSTPROB \< 0.8)' , 'K-' : ' (PT \> 500 \*MeV) & (PIDK \> 0) & (TRGHOSTPROB \< 0.8)' , 'pi+' : ' (PT \> 500 \*MeV) & (PIDK \< 0) & (TRGHOSTPROB \< 0.8)' , 'pi-' : ' (PT \> 500 \*MeV) & (PIDK \< 0) & (TRGHOSTPROB \< 0.8)' } |
| CombinationCut   | (in_range(750,AM,1900)) & (ADOCACHI2CUT(30, ''))                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' , '[K\*\_0(1430)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                        |
| Output           | Phys/DetachedKstarWideListForBetaSBetaS/Particles                                                                                                                                                                                                                                            |

**CombineParticles/BetaSBs2JpsiKstarWideLine**

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKstarWideListForBetaSBetaS' , 'Phys/NarrowJpsiForBetaSBetaS' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' } |
| CombinationCut   | in_range(5100,AM,5700)                                                             |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10) & (BPVDIRA \>0.999) & (BPVVD \> 1.5 \*mm)                |
| DecayDescriptor  | [B_s\~0 -\> J/psi(1S) K\*(892)0]cc                                               |
| DecayDescriptors | [ '[B_s\~0 -\> J/psi(1S) K\*(892)0]cc' ]                                       |
| Output           | Phys/BetaSBs2JpsiKstarWideLine/Particles                                           |
