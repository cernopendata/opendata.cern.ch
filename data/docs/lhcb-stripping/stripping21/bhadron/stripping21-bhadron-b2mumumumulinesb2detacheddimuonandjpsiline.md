[[stripping21 lines]](./stripping21-index)

# StrippingB2MuMuMuMuLinesB2DetachedDimuonAndJpsiLine

## Properties:

|                |                                                           |
|----------------|-----------------------------------------------------------|
| OutputLocation | Phys/B2MuMuMuMuLinesB2DetachedDimuonAndJpsiLine/Particles |
| Postscale      | 1.0000000                                                 |
| HLT            | None                                                      |
| Prescale       | 1.0000000                                                 |
| L0DU           | None                                                      |
| ODIN           | None                                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/B2MuMuMuMuLinesJpsiWide

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 2.5 ) & (MIPCHI2DV(PRIMARY)\> 9.)' , 'mu-' : '(TRCHI2DOF \< 2.5 ) & (MIPCHI2DV(PRIMARY)\> 9.)' } |
| CombinationCut   | (AMAXDOCA('')\<0.3\*mm)                                                                                                                |
| MotherCut        | (ADMASS('J/psi(1S)') \> 200\*MeV) & (BPVDIRA \> 0)                                                                                     |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                  |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                          |
| Output           | Phys/B2MuMuMuMuLinesJpsiWide/Particles                                                                                                 |

CombineParticles/B2MuMuMuMuLinesDetachedDimuons

|                  |                                                                           |
|------------------|---------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                            |
| CombinationCut   | (ASUM(PT)\>1000\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator'))    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16) & (BPVVDCHI2\>16)                                |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                           |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                   |
| Output           | Phys/B2MuMuMuMuLinesDetachedDimuons/Particles                             |

CombineParticles/B2MuMuMuMuLinesB2DetachedDimuonAndJpsiLine

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2MuMuMuMuLinesDetachedDimuons' , 'Phys/B2MuMuMuMuLinesJpsiWide' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                                               |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>2000\*MeV) & (in_range(4600\*MeV,AM,7000\*MeV)) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<6) & (BPVVDCHI2\>50) & (BPVIPCHI2()\<16) & (BPVDIRA\>0.0)                     |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                                               |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                                       |
| Output           | Phys/B2MuMuMuMuLinesB2DetachedDimuonAndJpsiLine/Particles                                          |
