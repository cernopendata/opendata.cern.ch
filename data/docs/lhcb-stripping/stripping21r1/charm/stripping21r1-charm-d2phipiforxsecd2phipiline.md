[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2PhiPiForXSecD2PhiPiLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/D2PhiPiForXSecD2PhiPiLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | HLT_PASS_RE('Hlt1MB.\*')                 |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D2PhiPiForXSecPhi2KK

|                  |                                                                                                                                                                                                                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& ((PIDK-PIDpi) \> 0.0)& (BPVIPCHI2() \> 1.0)' , 'K-' : '(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& ((PIDK-PIDpi) \> 0.0)& (BPVIPCHI2() \> 1.0)' } |
| CombinationCut   | (AALL)                                                                                                                                                                                                                                                                                                     |
| MotherCut        | (in_range(1000.0, M, 1040.0))                                                                                                                                                                                                                                                                              |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                                                                                                                                                                |
| Output           | Phys/D2PhiPiForXSecPhi2KK/Particles                                                                                                                                                                                                                                                                        |

CombineParticles/D2PhiPiForXSecD2PhiPiLine

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2PhiPiForXSecPhi2KK' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]      |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : '(ALL)' , 'pi+' : '(BPVIPCHI2() \> 1.0)' , 'pi-' : '(BPVIPCHI2() \> 1.0)' }               |
| CombinationCut   | (in_range(1770.0, AM, 2070.0))                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.0)& (((BPVVDCHI2 \> 16.0)\|(BPVLTIME() \> 0.150 \* picosecond)))& (BPVDIRA \> bpvdirathresh) |
| DecayDescriptor  | None                                                                                                                   |
| DecayDescriptors | [ '[D_s+ -\> pi+ phi(1020)]cc' ]                                                                                   |
| Output           | Phys/D2PhiPiForXSecD2PhiPiLine/Particles                                                                               |
