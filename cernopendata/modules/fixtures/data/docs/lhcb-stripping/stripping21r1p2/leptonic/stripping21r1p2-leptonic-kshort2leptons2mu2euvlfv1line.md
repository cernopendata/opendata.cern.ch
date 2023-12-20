[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingKshort2Leptons2mu2eUVLFV1Line

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2mu2eUVLFV1Line/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

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
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1p2-commonparticles-stdallloosemuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Kshort2LeptonsMuonsL/Particles                                                 |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsUpElectrons

|      |                                        |
|------|----------------------------------------|
| Code | 0StdNoPIDsUpElectrons/Particles',True) |

FilterDesktop/Kshort2LeptonsElectronsU

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | ( MIPCHI2DV(PRIMARY) \> 10 ) &( PT \> 50 ) &( TRGHOSTPROB \< 0.35 ) & ( PIDe \> -3.5 )      |
| Inputs          | [ 'Phys/[StdNoPIDsUpElectrons](./stripping21r1p2-commonparticles-stdnopidsupelectrons)' ] |
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

CombineParticles/Kshort2Leptons2mu2eUVLFV1Line

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsElectronsU' , 'Phys/Kshort2LeptonsElectronsV' , 'Phys/Kshort2LeptonsMuonsL' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                       |
| CombinationCut   | (AM \< 878.0 \*MeV) & (AMAXDOCA('') \< 0.8 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'e-' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'e-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 878.0 \*MeV) &( MIPDV(PRIMARY) \< 15 \*mm) & ( BPVVDCHI2 \> 1000) & ( VFASPF(VCHI2/VDOF) \< 25)                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[KS0 -\> mu+ mu+ e+ e+]cc' , '[KS0 -\> mu+ mu+ e+ e-]cc' , '[KS0 -\> mu+ mu+ e- e+]cc' , '[KS0 -\> mu+ mu+ e- e-]cc' ]                                                                                                |
| Output           | Phys/Kshort2Leptons2mu2eUVLFV1Line/Particles                                                                                                                                                                                       |
