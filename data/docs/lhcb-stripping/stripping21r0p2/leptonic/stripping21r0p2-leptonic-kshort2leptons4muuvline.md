[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingKshort2Leptons4muUVLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Kshort2Leptons4muUVLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

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

ChargedProtoParticleMaker/MyProtoParticlesUpKshort2Leptons

|        |                                     |
|--------|-------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]              |
| Output | Rec/ProtoP/MyProtosUpKshort2Leptons |

NoPIDsParticleMaker/StdNoPIDsUpMuonsKshort2Leptons

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/MyProtosUpKshort2Leptons' ]   |
| DecayDescriptor | Muon                                          |
| Output          | Phys/StdNoPIDsUpMuonsKshort2Leptons/Particles |

FilterDesktop/Kshort2LeptonsMuonsU

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | (PT \> 50) &(MIPCHI2DV(PRIMARY) \> 10) &(TRGHOSTPROB \< 0.35) &(PIDmu \> -3.5) |
| Inputs          | [ 'Phys/StdNoPIDsUpMuonsKshort2Leptons' ]                                    |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Kshort2LeptonsMuonsU/Particles                                            |

ChargedProtoParticleMaker/MyProtoParticlesVeloKshort2Leptons

|        |                                       |
|--------|---------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                |
| Output | Rec/ProtoP/MyProtosVeloKshort2Leptons |

NoPIDsParticleMaker/StdNoPIDsVeloMuonsKshort2Leptons

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/MyProtosVeloKshort2Leptons' ]   |
| DecayDescriptor | Muon                                            |
| Output          | Phys/StdNoPIDsVeloMuonsKshort2Leptons/Particles |

FilterDesktop/Kshort2LeptonsMuonsV

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | (PT \> 50) &(MIPCHI2DV(PRIMARY) \> 10) &(TRGHOSTPROB \< 0.35) &(PIDmu \> -3.5) |
| Inputs          | [ 'Phys/StdNoPIDsVeloMuonsKshort2Leptons' ]                                  |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Kshort2LeptonsMuonsV/Particles                                            |

CombineParticles/Kshort2Leptons4muUVLine

|                  |                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsMuonsL' , 'Phys/Kshort2LeptonsMuonsU' , 'Phys/Kshort2LeptonsMuonsV' ]                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                                                       |
| CombinationCut   | (AM \< 800.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 4 ) & ( ABSID == 'mu+' ) ) == 1 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'mu-' ) ) == 1 ) ) |
| MotherCut        | ( M \< 800.0 \*MeV) &( MIPDV(PRIMARY) \< 1 \*mm) & ( BPVVDCHI2 \> 1500) & ( VFASPF(VCHI2/VDOF) \< 19)                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'KS0 -\> mu+ mu- mu+ mu+' , 'KS0 -\> mu+ mu- mu+ mu-' , 'KS0 -\> mu+ mu- mu- mu+' , 'KS0 -\> mu+ mu- mu- mu-' ]                                                                                                                  |
| Output           | Phys/Kshort2Leptons4muUVLine/Particles                                                                                                                                                                                               |
