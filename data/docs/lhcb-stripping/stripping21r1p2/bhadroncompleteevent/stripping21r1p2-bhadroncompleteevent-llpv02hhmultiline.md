[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLLPV02HHMultiLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/LLPV02HHMultiLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

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

GaudiSequencer/MERGED:LLPV02HHMultiLine

GaudiSequencer/MERGEDINPUTS:LLPV02HHMultiLine

GaudiSequencer/INPUT:HHMultiSelection

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

LoKi::VoidFilter/HHMultiSelection

|      |                                                        |
|------|--------------------------------------------------------|
| Code | ( ((ndimu \>= 100) & (ndih \>= 100)) \| (ndih \>= 6) ) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LLPV02HHMultiLine

|                 |                                  |
|-----------------|----------------------------------|
| Code            | ALL                              |
| Inputs          | [ 'Phys/V02HHLLPV0' ]          |
| DecayDescriptor | None                             |
| Output          | Phys/LLPV02HHMultiLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
