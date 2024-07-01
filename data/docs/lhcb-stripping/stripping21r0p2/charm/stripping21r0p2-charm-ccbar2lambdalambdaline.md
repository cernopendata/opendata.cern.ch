[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingCcbar2LambdaLambdaLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Ccbar2LambdaLambdaLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:MergedLambdaForJpsiCcbar2LambdaLambda

GaudiSequencer/MERGEDINPUTS:MergedLambdaForJpsiCcbar2LambdaLambda

GaudiSequencer/INPUT:LambdaLLForCcbar2LambdaLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaLL/Particles',True) |

FilterDesktop/LambdaLLForCcbar2LambdaLambda

|                 |                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 9) & (ADMASS('Lambda0')\<30 \*MeV) & (INTREE( ('pi+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 250.0\*MeV))) & (INTREE( ('p+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.3) & (PT\> 250.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>5) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r0p2-commonparticles-stdlooselambdall)' ]                                                                                                                                                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/LambdaLLForCcbar2LambdaLambda/Particles                                                                                                                                                                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdaDDForCcbar2LambdaLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/LambdaDDForCcbar2LambdaLambda

|                 |                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 9) & (ADMASS('Lambda0')\< 30 \*MeV) & (INTREE( ('pi+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 250.0\*MeV))) & (INTREE( ('p+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.3) & (PT\> 250.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>5) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r0p2-commonparticles-stdlooselambdadd)' ]                                                                                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                 |
| Output          | Phys/LambdaDDForCcbar2LambdaLambda/Particles                                                                                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdaLDForCcbar2LambdaLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaLD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaLD/Particles',True) |

FilterDesktop/LambdaLDForCcbar2LambdaLambda

|                 |                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 9) & (ADMASS('Lambda0')\< 30 \*MeV) & (INTREE( ('pi+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 250.0\*MeV))) & (INTREE( ('p+'==ABSID) & (MIPCHI2DV(PRIMARY) \> 4.0) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.3) & (PT\> 250.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>5) |
| Inputs          | [ 'Phys/[StdLooseLambdaLD](./stripping21r0p2-commonparticles-stdlooselambdald)' ]                                                                                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                 |
| Output          | Phys/LambdaLDForCcbar2LambdaLambda/Particles                                                                                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergedLambdaForJpsiCcbar2LambdaLambda

|                 |                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                      |
| Inputs          | [ 'Phys/LambdaDDForCcbar2LambdaLambda' , 'Phys/LambdaLDForCcbar2LambdaLambda' , 'Phys/LambdaLLForCcbar2LambdaLambda' ] |
| DecayDescriptor | None                                                                                                                     |
| Output          | Phys/MergedLambdaForJpsiCcbar2LambdaLambda/Particles                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Ccbar2LambdaLambdaLine

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergedLambdaForJpsiCcbar2LambdaLambda' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                  |
| CombinationCut   | (in_range( 2700.0 \*MeV, AM, 15100.0 \*MeV))                             |
| MotherCut        | (in_range( 2750.0 \*MeV, MM, 15000.0 \*MeV)) & (VFASPF(VCHI2PDOF) \< 9 ) |
| DecayDescriptor  | J/psi(1S) -\> Lambda0 Lambda~0                                           |
| DecayDescriptors | [ 'J/psi(1S) -\> Lambda0 Lambda~0' ]                                   |
| Output           | Phys/Ccbar2LambdaLambdaLine/Particles                                    |
