[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingKshort2Leptons2mu2piVVLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2mu2piVVLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

ChargedProtoParticleMaker/MyProtoParticlesVeloKshort2Leptons

|        |                                       |
|--------|---------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                |
| Output | Rec/ProtoP/MyProtosVeloKshort2Leptons |

NoPIDsParticleMaker/StdNoPIDsVeloPionsKshort2Leptons

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/MyProtosVeloKshort2Leptons' ]   |
| DecayDescriptor | Pion                                            |
| Output          | Phys/StdNoPIDsVeloPionsKshort2Leptons/Particles |

FilterDesktop/Kshort2LeptonsPionsV

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 50) &(MIPCHI2DV(PRIMARY) \> 10) &(TRGHOSTPROB \< 0.35) &(PIDK \< -3.5) |
| Inputs          | [ 'Phys/StdNoPIDsVeloPionsKshort2Leptons' ]                                 |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsPionsV/Particles                                           |

CombineParticles/Kshort2Leptons2mu2piVVLine

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsMuonsL' , 'Phys/Kshort2LeptonsPionsV' ]                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                           |
| CombinationCut   | (AM \< 900.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'pi+' ) ) == 2 ) ) |
| MotherCut        | ( M \< 900.0 \*MeV) &( MIPDV(PRIMARY) \< 8 \*mm) & ( BPVVDCHI2 \> 2500) & ( VFASPF(VCHI2/VDOF) \< 40)                                                                    |
| DecayDescriptor  | None                                                                                                                                                                     |
| DecayDescriptors | [ 'KS0 -\> mu+ mu- pi+ pi+' , 'KS0 -\> mu+ mu- pi+ pi-' , 'KS0 -\> mu+ mu- pi- pi+' , 'KS0 -\> mu+ mu- pi- pi-' ]                                                      |
| Output           | Phys/Kshort2Leptons2mu2piVVLine/Particles                                                                                                                                |
