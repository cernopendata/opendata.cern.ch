[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons4eUVLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Kshort2Leptons4eUVLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdDiElectronFromTracks

|      |                                           |
|------|-------------------------------------------|
| Code | 0StdDiElectronFromTracks/Particles',True) |

FilterDesktop/Kshort2LeptonsDiElectronsV

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE(ABSID\<14,PT) \> 100.0) &(MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 16) &(MAXTREE(ABSID\<14,TRGHOSTPROB) \< 0.5) &(MINTREE(ABSID\<14,PIDe) \> -4) |
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r0p2-commonparticles-stddielectronfromtracks)' ]                                                         |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/Kshort2LeptonsDiElectronsV/Particles                                                                                                                 |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsUpElectrons

|      |                                        |
|------|----------------------------------------|
| Code | 0StdNoPIDsUpElectrons/Particles',True) |

FilterDesktop/Kshort2LeptonsElectronsU

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 10 ) &( PT \> 50 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -3.5 )      |
| Inputs          | [ 'Phys/[StdNoPIDsUpElectrons](./stripping21r0p2-commonparticles-stdnopidsupelectrons)' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Kshort2LeptonsElectronsU/Particles                                                     |

ChargedProtoParticleMaker/MyProtoParticlesVeloKshort2Leptons

|        |                                       |
|--------|---------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                |
| Output | Rec/ProtoP/MyProtosVeloKshort2Leptons |

NoPIDsParticleMaker/StdNoPIDsVeloElectronsKshort2Leptons

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/MyProtosVeloKshort2Leptons' ]       |
| DecayDescriptor | Electron                                            |
| Output          | Phys/StdNoPIDsVeloElectronsKshort2Leptons/Particles |

FilterDesktop/Kshort2LeptonsElectronsV

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 40 ) &( PT \> 0 ) &( TRGHOSTPROB \< 0.5 ) & ( PIDe \> -1000 ) |
| Inputs          | [ 'Phys/StdNoPIDsVeloElectronsKshort2Leptons' ]                                     |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Kshort2LeptonsElectronsV/Particles                                               |

CombineParticles/Kshort2Leptons4eUVLine

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsDiElectronsV' , 'Phys/Kshort2LeptonsElectronsU' , 'Phys/Kshort2LeptonsElectronsV' ]                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                     |
| CombinationCut   | (AM \< 880.0 \*MeV) & (AMAXDOCA('') \< 0.8 \*mm) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'e-' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 880.0 \*MeV) &( MIPDV(PRIMARY) \< 15 \*mm) & ( BPVVDCHI2 \> 2000) & ( VFASPF(VCHI2/VDOF) \< 20)                                                                 |
| DecayDescriptor  | None                                                                                                                                                                   |
| DecayDescriptors | [ 'KS0 -\> J/psi(1S) e+ e+' , 'KS0 -\> J/psi(1S) e+ e-' , 'KS0 -\> J/psi(1S) e- e+' , 'KS0 -\> J/psi(1S) e- e-' ]                                                    |
| Output           | Phys/Kshort2Leptons4eUVLine/Particles                                                                                                                                  |
