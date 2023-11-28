[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLLPV02HHSingleLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/LLPV02HHSingleLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 0.0015000000                      |
| L0DU           | None                              |
| ODIN           | None                              |

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

GaudiSequencer/MERGED:LLPV02HHSingleLine

GaudiSequencer/MERGEDINPUTS:LLPV02HHSingleLine

GaudiSequencer/INPUT:HHSingleSelection

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/V02HHLLPV0

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)' , 'pi-' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 25.0)' } |
| CombinationCut   | ( ADOCACHI2CUT(25.0, '') )                                                                                                       |
| MotherCut        | ( CHI2VX \< 16.0 ) & ( MIPCHI2DV(PRIMARY) \< 10.0 )                                                                              |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                          |
| Output           | Phys/V02HHLLPV0/Particles                                                                                                        |

LoKi::VoidFilter/HHSingleSelection

|      |                                                        |
|------|--------------------------------------------------------|
| Code | ( ((ndimu \>= 100) & (ndih \>= 100)) \| (ndih \>= 1) ) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LLPV02HHSingleLine

|                 |                                   |
|-----------------|-----------------------------------|
| Code            | ALL                               |
| Inputs          | [ 'Phys/V02HHLLPV0' ]           |
| DecayDescriptor | None                              |
| Output          | Phys/LLPV02HHSingleLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
