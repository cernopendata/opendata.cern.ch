[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingTriggerTestLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/TriggerTestLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/MuonsForRnS

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 36)                                                    |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MuonsForRnS/Particles                                                    |

CombineParticles/TriggerTestLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForRnS' ]                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                       |
| CombinationCut   | (AMAXDOCA('')\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (MINTREE('mu-' == ABSID, MIPDV(PRIMARY)) \> 0.5) & (CHILDCUT((TRGHOSTPROB \< 0.3),1)) & (CHILDCUT((TRGHOSTPROB \< 0.3),2)) & (MINTREE('mu-' == ABSID, MIPCHI2DV(PRIMARY)) \> 1.5) & (MAXTREE('mu-' == ABSID, MIPCHI2DV(PRIMARY)) \< 1500) & ( VFASPF (sqrt(VX\*VX+VY\*VY)) \> 4) & ( VFASPF ( VZ ) \< 650) & ((MIPDV(PRIMARY)/BPVVDZ)\< 0.0166666666667) & (MM \< 450) & (VFASPF(VCHI2PDOF)\<9 ) & (DOCAMAX \< 0.3) & (BPVVDZ \> 0) & (BPVDIRA \> 0) |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Output           | Phys/TriggerTestLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                       |
