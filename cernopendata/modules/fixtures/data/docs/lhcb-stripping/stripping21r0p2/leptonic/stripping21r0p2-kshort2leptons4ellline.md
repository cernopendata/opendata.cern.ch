[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons4eLLLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Kshort2Leptons4eLLLine/Particles |
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
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r0p2-stddielectronfromtracks) ' ]                                                                       |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/Kshort2LeptonsDiElectronsV/Particles                                                                                                                 |

**CombineParticles/Kshort2Leptons4eLLLine**

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsDiElectronsV' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' }                                                                                   |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 2.0 \*mm)                                                                       |
| MotherCut        | (M \< 800.0 \*MeV) &(MIPDV(PRIMARY) \< 2 \*mm) & ((BPVVDSIGN\*M/P) \> 0.8953\*2.9979e-01) & (VFASPF(VCHI2/VDOF) \< 50) |
| DecayDescriptor  | KS0 -\> J/psi(1S) J/psi(1S)                                                                                            |
| DecayDescriptors | [ 'KS0 -\> J/psi(1S) J/psi(1S)' ]                                                                                    |
| Output           | Phys/Kshort2Leptons4eLLLine/Particles                                                                                  |
