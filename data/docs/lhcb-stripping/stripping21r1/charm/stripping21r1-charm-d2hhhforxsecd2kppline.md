[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2HHHForXSecD2KPPLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/D2HHHForXSecD2KPPLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | HLT_PASS_RE('Hlt1MB.\*')             |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

CombineParticles/D2HHHForXSecD2KPPLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 200.0)& (BPVIPCHI2() \> 1.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \> 0.0)' , 'K-' : '(PT \> 200.0)& (BPVIPCHI2() \> 1.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \> 0.0)' , 'pi+' : '(PT \> 200.0)& (BPVIPCHI2() \> 1.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 3.0)' , 'pi-' : '(PT \> 200.0)& (BPVIPCHI2() \> 1.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 3.0)' } |
| CombinationCut   | (in_range(1580.0, AM, 2260.0))& (AMAXCHILD(PT) \> 400.0)& (AMAXCHILD(BPVIPCHI2()) \> 4.0)& (ANUM(PT \> 400.0) \>= 2)& (ANUM(BPVIPCHI2() \> 4.0) \>= 2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.0)& (((BPVVDCHI2 \> 16.0)\|(BPVLTIME() \> 0.150 \* picosecond)))& (BPVDIRA \> bpvdirathresh)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D2HHHForXSecD2KPPLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
