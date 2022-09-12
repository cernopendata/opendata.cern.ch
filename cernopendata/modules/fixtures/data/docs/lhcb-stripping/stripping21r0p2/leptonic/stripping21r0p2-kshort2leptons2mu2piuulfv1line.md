[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons2mu2piUULFV1Line

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2mu2piUULFV1Line/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

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
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ]         |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsMuonsL/Particles                                           |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsUpPions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdNoPIDsUpPions /Particles',True) |

**FilterDesktop/Kshort2LeptonsPionsU**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 50) &(MIPCHI2DV(PRIMARY) \> 10) &(TRGHOSTPROB \< 0.35) &(PIDK \< -3.5) |
| Inputs          | [ 'Phys/ [StdNoPIDsUpPions](./stripping21r0p2-stdnopidsuppions) ' ]         |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsPionsU/Particles                                           |

**CombineParticles/Kshort2Leptons2mu2piUULFV1Line**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsMuonsL' , 'Phys/Kshort2LeptonsPionsU' ]                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                           |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'pi-' ) ) == 2 ) ) |
| MotherCut        | ( M \< 800.0 \*MeV) &( MIPDV(PRIMARY) \< 1 \*mm) & ( BPVVDCHI2 \> 2500) & ( VFASPF(VCHI2/VDOF) \< 35)                                                                    |
| DecayDescriptor  | [KS0 -\> mu+ mu+ pi- pi-]cc                                                                                                                                            |
| DecayDescriptors | [ '[KS0 -\> mu+ mu+ pi- pi-]cc' ]                                                                                                                                    |
| Output           | Phys/Kshort2Leptons2mu2piUULFV1Line/Particles                                                                                                                            |
