[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons2pi2eLULine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2pi2eLULine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**FilterDesktop/Kshort2LeptonsPionsL**

|                 |                                                                              |
|-----------------|------------------------------------------------------------------------------|
| Code            | (PT \> 100.0) &(MIPCHI2DV(PRIMARY) \> 16) &(TRGHOSTPROB \< 0.5) &(PIDK \< 5) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r0p2-stdallnopidspions) ' ]      |
| DecayDescriptor | None                                                                         |
| Output          | Phys/Kshort2LeptonsPionsL/Particles                                          |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsElectrons**

|      |                                           |
|------|-------------------------------------------|
| Code | 0 StdAllNoPIDsElectrons /Particles',True) |

**FilterDesktop/Kshort2LeptonsElectronsL**

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 50 ) &( PT \> 100.0 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -1 ) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsElectrons](./stripping21r0p2-stdallnopidselectrons) ' ]         |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Kshort2LeptonsElectronsL/Particles                                                 |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsUpElectrons**

|      |                                          |
|------|------------------------------------------|
| Code | 0 StdNoPIDsUpElectrons /Particles',True) |

**FilterDesktop/Kshort2LeptonsElectronsU**

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 10 ) &( PT \> 50 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -3.5 ) |
| Inputs          | [ 'Phys/ [StdNoPIDsUpElectrons](./stripping21r0p2-stdnopidsupelectrons) ' ]          |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/Kshort2LeptonsElectronsU/Particles                                                |

**CombineParticles/Kshort2Leptons2pi2eLULine**

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsElectronsL' , 'Phys/Kshort2LeptonsElectronsU' , 'Phys/Kshort2LeptonsPionsL' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                       |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'pi+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'e+' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 800.0 \*MeV) &( MIPDV(PRIMARY) \< 5 \*mm) & ( BPVVDCHI2 \> 2500) & ( VFASPF(VCHI2/VDOF) \< 25)                                                                                                                              |
| DecayDescriptor  | KS0 -\> pi+ pi- e+ e-                                                                                                                                                                                                              |
| DecayDescriptors | [ 'KS0 -\> pi+ pi- e+ e-' ]                                                                                                                                                                                                      |
| Output           | Phys/Kshort2Leptons2pi2eLULine/Particles                                                                                                                                                                                           |
