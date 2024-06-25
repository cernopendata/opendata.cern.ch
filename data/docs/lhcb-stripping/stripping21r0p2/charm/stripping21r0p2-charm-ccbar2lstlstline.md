[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingCcbar2LstLstLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Ccbar2LstLstLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsProtons

|      |                                    |
|------|------------------------------------|
| Code | 0StdNoPIDsProtons/Particles',True) |

FilterDesktop/DetachedProtonForLstCcbar2LstLst

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P\>5000\*MeV) & (PT\> 100.0\*MeV) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.1)           |
| Inputs          | [ 'Phys/[StdNoPIDsProtons](./stripping21r0p2-commonparticles-stdnopidsprotons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/DetachedProtonForLstCcbar2LstLst/Particles                                     |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsKaons/Particles',True) |

FilterDesktop/DetachedKaonForLstCcbar2LstLst

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (PT\> 100.0\*MeV) & (TRCHI2DOF \< 5.0) & (PROBNNk\> 0.1)                        |
| Inputs          | [ 'Phys/[StdNoPIDsKaons](./stripping21r0p2-commonparticles-stdnopidskaons)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/DetachedKaonForLstCcbar2LstLst/Particles                                   |

CombineParticles/DetachedLstForCcbar2LstLst

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKaonForLstCcbar2LstLst' , 'Phys/DetachedProtonForLstCcbar2LstLst' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }           |
| CombinationCut   | (in_range( 1400 \*MeV, AM, 1600 \*MeV))                                               |
| MotherCut        | (in_range( 1400 \*MeV, MM, 1600 \*MeV)) & (VFASPF(VCHI2PDOF)\<16.0)                   |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                         |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                 |
| Output           | Phys/DetachedLstForCcbar2LstLst/Particles                                             |

CombineParticles/Ccbar2LstLstLine

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedLstForCcbar2LstLst' ]                                                |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' }                    |
| CombinationCut   | (in_range( 2800.0 \*MeV, AM, 6100.0 \*MeV))                                            |
| MotherCut        | (in_range( 2850.0 \*MeV, MM, 6000.0 \*MeV)) & (VFASPF(VCHI2PDOF) \< 16 ) & (BPVDLS\>3) |
| DecayDescriptor  | J/psi(1S) -\> Lambda(1520)0 Lambda(1520)~0                                             |
| DecayDescriptors | [ ' J/psi(1S) -\> Lambda(1520)0 Lambda(1520)~0' ]                                    |
| Output           | Phys/Ccbar2LstLstLine/Particles                                                        |
