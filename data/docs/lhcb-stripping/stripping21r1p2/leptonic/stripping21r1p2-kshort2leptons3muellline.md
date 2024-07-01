[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingKshort2Leptons3mueLLLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Kshort2Leptons3mueLLLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**FilterDesktop/Kshort2LeptonsMuonsL**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 50.0) &(MIPCHI2DV(PRIMARY) \> 20) &(TRGHOSTPROB \< 0.5) &(PIDmu \> -5) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]         |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsMuonsL/Particles                                           |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsElectrons**

|      |                                           |
|------|-------------------------------------------|
| Code | 0 StdAllNoPIDsElectrons /Particles',True) |

**FilterDesktop/Kshort2LeptonsElectronsL**

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 50 ) &( PT \> 100.0 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -1 ) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsElectrons](./stripping21r1p2-stdallnopidselectrons) ' ]         |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Kshort2LeptonsElectronsL/Particles                                                 |

**CombineParticles/Kshort2Leptons3mueLLLine**

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsElectronsL' , 'Phys/Kshort2LeptonsMuonsL' ]                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                           |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) &( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu-' ) ) == 3 ) ) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 800.0 \*MeV) &( MIPDV(PRIMARY) \< 1 \*mm) & ( BPVVDCHI2 \> 50) & ( VFASPF(VCHI2/VDOF) \< 50)                                                                    |
| DecayDescriptor  | [KS0 -\> mu+ mu- mu+ e-]cc                                                                                                                                           |
| DecayDescriptors | [ '[KS0 -\> mu+ mu- mu+ e-]cc' ]                                                                                                                                   |
| Output           | Phys/Kshort2Leptons3mueLLLine/Particles                                                                                                                                |
