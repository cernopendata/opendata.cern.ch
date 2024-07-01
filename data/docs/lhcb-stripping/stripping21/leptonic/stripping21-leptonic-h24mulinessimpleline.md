[[stripping21 lines]](./stripping21-index)

# StrippingH24MuLinesSimpleLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/H24MuLinesSimpleLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/SelA1H24MuLinesSimple

|                  |                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.4 ) & (PIDmu \> -3 ) & (PPINFO(LHCb.ProtoParticle.MuonNShared,99999)\<= 3 ) ' , 'mu-' : '(TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.4 ) & (PIDmu \> -3 ) & (PPINFO(LHCb.ProtoParticle.MuonNShared,99999)\<= 3 ) ' } |
| CombinationCut   | (AM \< 2000 \* MeV ) & (AMAXDOCA('')\<0.1 \* mm)                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2)\< 1 ) & (MM \< 2000 \* MeV)                                                                                                                                                                                                                                     |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                                                                                                                        |
| Output           | Phys/SelA1H24MuLinesSimple/Particles                                                                                                                                                                                                                                           |

CombineParticles/H24MuLinesSimpleLine

|                  |                                     |
|------------------|-------------------------------------|
| Inputs           | [ 'Phys/SelA1H24MuLinesSimple' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }      |
| CombinationCut   | (AMAXDOCA('')\< 0.25 \* mm )        |
| MotherCut        | (VFASPF(VCHI2)\< 2 )                |
| DecayDescriptor  | H_10 -\> KS0 KS0                    |
| DecayDescriptors | [ 'H_10 -\> KS0 KS0' ]            |
| Output           | Phys/H24MuLinesSimpleLine/Particles |

AddExtraInfo/ExtraInfo_StrippingH24MuLinesSimpleLine

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelA1H24MuLinesSimple' ]                                                                    |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/ExtraInfo_StrippingH24MuLinesSimpleLine/Particles                                                |
| Tools           | [ 'ConeVariables/Tool1' , 'ConeVariables/Tool2' , 'ConeVariables/Tool3' , 'VertexIsolation/Tool4' ] |
