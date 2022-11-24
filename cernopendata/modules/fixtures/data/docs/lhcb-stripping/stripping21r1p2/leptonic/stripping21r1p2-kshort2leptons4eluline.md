[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingKshort2Leptons4eLULine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Kshort2Leptons4eLULine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

**LoKi::VoidFilter/SELECT:Phys/StdDiElectronFromTracks**

|      |                                             |
|------|---------------------------------------------|
| Code | 0 StdDiElectronFromTracks /Particles',True) |

**FilterDesktop/Kshort2LeptonsDiElectronsV**

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE(ABSID\<14,PT) \> 100.0) &(MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 16) &(MAXTREE(ABSID\<14,TRGHOSTPROB) \< 0.5) &(MINTREE(ABSID\<14,PIDe) \> -4) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r1p2-stddielectronfromtracks) ' ]                                                                       |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/Kshort2LeptonsDiElectronsV/Particles                                                                                                                 |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsUpElectrons**

|      |                                          |
|------|------------------------------------------|
| Code | 0 StdNoPIDsUpElectrons /Particles',True) |

**FilterDesktop/Kshort2LeptonsElectronsU**

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 10 ) &( PT \> 50 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -3.5 ) |
| Inputs          | [ 'Phys/ [StdNoPIDsUpElectrons](./stripping21r1p2-stdnopidsupelectrons) ' ]          |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/Kshort2LeptonsElectronsU/Particles                                                |

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

**CombineParticles/Kshort2Leptons4eLULine**

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsDiElectronsV' , 'Phys/Kshort2LeptonsElectronsL' , 'Phys/Kshort2LeptonsElectronsU' ]                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                    |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) &( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'e-' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 800.0 \*MeV) &( MIPDV(PRIMARY) \< 5 \*mm) & ( BPVVDCHI2 \> 2500) & ( VFASPF(VCHI2/VDOF) \< 25)                                                                 |
| DecayDescriptor  | KS0 -\> J/psi(1S) e+ e-                                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> J/psi(1S) e+ e-' ]                                                                                                                                       |
| Output           | Phys/Kshort2Leptons4eLULine/Particles                                                                                                                                 |
