[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBs2JpsieePhiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/BetaSBs2JpsieePhiLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 0.10000000                           |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiElectron_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiElectron](./stripping21-stdloosedielectron) /Particles')\>0 |

**FilterDesktop/SelJpsi2eeForBetaSBs2JpsieePhi**

|                 |                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2500.0 \*MeV) & (MM \< 3300.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdLooseDiElectron](./stripping21-stdloosedielectron) ' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                        |
| Output          | Phys/SelJpsi2eeForBetaSBs2JpsieePhi/Particles                                                                                                                                                               |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) /Particles')\>0 |

**FilterDesktop/SelPhi2KKForBetaSBs2JpsieePhi**

|                 |                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.0 \*MeV) & (MINTREE('K+'==ABSID,PIDK-PIDpi) \> -2.0 ) & (MAXTREE('K+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) & (MM \> 990.0 \*MeV) & (MM \< 1050.0 \*MeV) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) ' ]                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                    |
| Output          | Phys/SelPhi2KKForBetaSBs2JpsieePhi/Particles                                                                                                                                            |

**CombineParticles/BetaSBs2JpsieePhiLine**

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelJpsi2eeForBetaSBs2JpsieePhi' , 'Phys/SelPhi2KKForBetaSBs2JpsieePhi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                         |
| CombinationCut   | (AM \> 4600.0 \*MeV) & (AM \< 6000.0 \*MeV)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.99)                                   |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                                       |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                               |
| Output           | Phys/BetaSBs2JpsieePhiLine/Particles                                               |
