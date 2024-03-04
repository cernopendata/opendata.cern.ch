[[stripping21 lines]](./stripping21-index)

# StrippingB2KstTauTau_TauTau_Line

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2KstTauTau_TauTau_Line/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21-commonparticles-stdtightdetachedtau3pi)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/KstarB2KstTauTau

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' , 'Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'K-' : '( (TRCHI2DOF \< 4) & (PROBNNk\>0.2))' , 'pi+' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' , 'pi-' : '( (TRCHI2DOF \< 4) & (PROBNNpi\>0.5))' } |
| CombinationCut   | (AM \> 700\*MeV) & (AM \< 1100\*MeV)                                                                                                                                                                               |
| MotherCut        | (PT \> 1000\*MeV) & (VFASPF(VCHI2) \< 15)                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                 |
| Output           | Phys/KstarB2KstTauTau/Particles                                                                                                                                                                                    |

CombineParticles/B2KstTauTau_TauTau_Line

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstarB2KstTauTau' , 'Phys/[StdTightDetachedTau3pi](./stripping21-commonparticles-stdtightdetachedtau3pi)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                         |
| CombinationCut   | (AM \> 2000\*MeV) & (AM \< 10000\*MeV)                                                                                |
| MotherCut        | (VFASPF(VCHI2) \< 100) &(BPVVDCHI2 \> 80)                                                                             |
| DecayDescriptor  | None                                                                                                                  |
| DecayDescriptors | [ 'B0 -\> K\*(892)0 tau+ tau-' ]                                                                                    |
| Output           | Phys/B2KstTauTau_TauTau_Line/Particles                                                                                |
