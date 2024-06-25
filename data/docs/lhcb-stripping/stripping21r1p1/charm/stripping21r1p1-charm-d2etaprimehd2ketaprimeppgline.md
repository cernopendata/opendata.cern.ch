[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingD2EtaPrimeHD2KEtaPrimePPGLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/D2EtaPrimeHD2KEtaPrimePPGLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | HLT_PASS_RE('Hlt2CharmHadD2.\*Decision')     |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r1p1-commonparticles-stdlooseallphotons)/Particles',True)\>0 |

DaVinci::N3BodyDecays/D2EtaPrimeHEtaPrimePPG

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p1-commonparticles-stdallnopidspions)' , 'Phys/[StdLooseAllPhotons](./stripping21r1p1-commonparticles-stdlooseallphotons)' ]                                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'eta' : "(PT \> 1000.0)& (ADMASS('eta') \< 60.0)" , 'gamma' : '(PT \> 1000.0)' , 'pi+' : '(PT \> 500.0)& (P \> 1000.0) & (MIPCHI2DV(PRIMARY) \> 16.0)& (TRCHI2DOF \< 5) & (TRGHOSTPROB \< 0.5) & (in_range(1000.0, P, 100000.0))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 0)' , 'pi-' : '(PT \> 500.0)& (P \> 1000.0) & (MIPCHI2DV(PRIMARY) \> 16.0)& (TRCHI2DOF \< 5) & (TRGHOSTPROB \< 0.5) & (in_range(1000.0, P, 100000.0))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 0)' , 'pi0' : "(PT \> 1000.0)& (ADMASS('pi0') \< 60.0)" } |
| CombinationCut   | in_range( 650.0,AM,1200.0 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MotherCut        | ALL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- gamma' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/D2EtaPrimeHEtaPrimePPG/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

CombineParticles/D2EtaPrimeHD2KEtaPrimePPGLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2EtaPrimeHEtaPrimePPG' , 'Phys/[StdAllNoPIDsKaons](./stripping21r1p1-commonparticles-stdallnopidskaons)' ]                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 600.0)& (P \> 1000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF \< 5) & (TRGHOSTPROB \< 0.5) ' , 'K-' : '(PT \> 600.0)& (P \> 1000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF \< 5) & (TRGHOSTPROB \< 0.5) ' , 'eta_prime' : 'ALL' , 'pi+' : '(PT \> 600.0)& (P \> 1000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)& (TRCHI2DOF \< 5) & (TRGHOSTPROB \< 0.5) ' } |
| CombinationCut   | (APT \> 2000.0)& ( in_range( 1600.0,AM,2200.0) )                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 4)& (BPVLTIME() \> 0.00025)                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[D+ -\> eta_prime K+]cc' ]                                                                                                                                                                                                                                                                                                                                                        |
| Output           | Phys/D2EtaPrimeHD2KEtaPrimePPGLine/Particles                                                                                                                                                                                                                                                                                                                                             |
