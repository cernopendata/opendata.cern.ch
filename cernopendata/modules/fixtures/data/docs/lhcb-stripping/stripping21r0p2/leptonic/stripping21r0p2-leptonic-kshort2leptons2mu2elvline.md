[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons2mu2eLVLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2mu2eLVLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseMuons/Particles',True) |

FilterDesktop/Kshort2LeptonsMuonsL

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT \> 50.0) &(MIPCHI2DV(PRIMARY) \> 20) &(TRGHOSTPROB \< 0.5) &(PIDmu \> -5)       |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p2-commonparticles-stdallloosemuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Kshort2LeptonsMuonsL/Particles                                                 |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsElectrons

|      |                                         |
|------|-----------------------------------------|
| Code | 0StdAllNoPIDsElectrons/Particles',True) |

FilterDesktop/Kshort2LeptonsElectronsL

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 50 ) &( PT \> 100.0 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -1 )       |
| Inputs          | [ 'Phys/[StdAllNoPIDsElectrons](./stripping21r0p2-commonparticles-stdallnopidselectrons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/Kshort2LeptonsElectronsL/Particles                                                       |

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

CombineParticles/Kshort2Leptons2mu2eLVLine

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsElectronsL' , 'Phys/Kshort2LeptonsElectronsV' , 'Phys/Kshort2LeptonsMuonsL' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                       |
| CombinationCut   | (AM \< 900.0 \*MeV) & (AMAXDOCA('') \< 0.5 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'e+' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 900.0 \*MeV) &( MIPDV(PRIMARY) \< 10 \*mm) & ( BPVVDCHI2 \> 1500) & ( VFASPF(VCHI2/VDOF) \< 40)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                               |
| DecayDescriptors | [ 'KS0 -\> mu+ mu- e+ e+' , 'KS0 -\> mu+ mu- e+ e-' , 'KS0 -\> mu+ mu- e- e+' , 'KS0 -\> mu+ mu- e- e-' ]                                                                                                                        |
| Output           | Phys/Kshort2Leptons2mu2eLVLine/Particles                                                                                                                                                                                           |
