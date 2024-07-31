[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLLPV02mumuSingleLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/LLPV02mumuSingleLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:LLPV02mumuSingleLine

GaudiSequencer/MERGEDINPUTS:LLPV02mumuSingleLine

GaudiSequencer/INPUT:MuMuSingleSelection

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/V02HHLLPV0

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)' , 'pi-' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)' } |
| CombinationCut   | ( ADOCACHI2CUT(25.0, '') )                                                                                                       |
| MotherCut        | ( CHI2VX \< 16.0 ) & ( MIPCHI2DV(PRIMARY) \< 10.0 )                                                                              |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                          |
| Output           | Phys/V02HHLLPV0/Particles                                                                                                        |

LoKi::VoidFilter/MuMuSingleSelection

|      |                                                      |
|------|------------------------------------------------------|
| Code | ( ((ndimu \>= 1) & (ndih \>= 0)) \| (ndih \>= 100) ) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LLPV02mumuSingleLine

|                 |                                     |
|-----------------|-------------------------------------|
| Code            | ALL                                 |
| Inputs          | [ 'Phys/V02HHLLPV0' ]             |
| DecayDescriptor | None                                |
| Output          | Phys/LLPV02mumuSingleLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
