[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingKs2PiPiForRnSLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Ks2PiPiForRnSLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 0.0010000000                     |
| L0DU           | None                             |
| ODIN           | None                             |

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

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForRnS

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 100)                                                   |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/PionsForRnS/Particles                                                    |

CombineParticles/Ks2PiPiForRnSLine

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForRnS' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\> 100.)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\> 100.)' }      |
| CombinationCut   | (ADAMASS('KS0')\<100\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                 |
| MotherCut        | ((M\>400) & (M\<600)& (BPVDIRA\>0) & ((BPVVDSIGN\*M/P) \> 1.610411922) & (MIPDV(PRIMARY)\<0.4\*mm)) |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                     |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                             |
| Output           | Phys/Ks2PiPiForRnSLine/Particles                                                                    |
