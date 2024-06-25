[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingCcbar2LstLambdaLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Ccbar2LstLambdaLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

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

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsProtons

|      |                                    |
|------|------------------------------------|
| Code | 0StdNoPIDsProtons/Particles',True) |

FilterDesktop/DetachedProtonForLstCcbar2LstLambda

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (P\>5000\*MeV) & (PT\> 100.0\*MeV) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.1)           |
| Inputs          | [ 'Phys/[StdNoPIDsProtons](./stripping21r0p2-commonparticles-stdnopidsprotons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/DetachedProtonForLstCcbar2LstLambda/Particles                                  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsKaons/Particles',True) |

FilterDesktop/DetachedKaonForLstCcbar2LstLambda

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (PT\> 100.0\*MeV) & (TRCHI2DOF \< 5.0) & (PROBNNk\> 0.1)                        |
| Inputs          | [ 'Phys/[StdNoPIDsKaons](./stripping21r0p2-commonparticles-stdnopidskaons)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/DetachedKaonForLstCcbar2LstLambda/Particles                                |

CombineParticles/DetachedLstForCcbar2LstLambda

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKaonForLstCcbar2LstLambda' , 'Phys/DetachedProtonForLstCcbar2LstLambda' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                 |
| CombinationCut   | (in_range( 1400 \*MeV, AM, 1600 \*MeV))                                                     |
| MotherCut        | (in_range( 1400 \*MeV, MM, 1600 \*MeV)) & (VFASPF(VCHI2PDOF)\<16.0)                         |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                               |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                       |
| Output           | Phys/DetachedLstForCcbar2LstLambda/Particles                                                |

GaudiSequencer/MERGED:MergedLambdaForJpsiCcbar2LstLambda

GaudiSequencer/MERGEDINPUTS:MergedLambdaForJpsiCcbar2LstLambda

GaudiSequencer/INPUT:LambdaLLForCcbar2LstLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaLL/Particles',True) |

FilterDesktop/LambdaLLForCcbar2LstLambda

|                 |                                                                                                                                                                                                                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 16) & (ADMASS('Lambda0')\<30 \*MeV) & (INTREE( ('pi+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 100.0\*MeV))) & (INTREE( ('p+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.1) & (PT\> 100.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>4) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r0p2-commonparticles-stdlooselambdall)' ]                                                                                                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                     |
| Output          | Phys/LambdaLLForCcbar2LstLambda/Particles                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdaDDForCcbar2LstLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/LambdaDDForCcbar2LstLambda

|                 |                                                                                                                                                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 16) & (ADMASS('Lambda0')\< 30 \*MeV) & (INTREE( ('pi+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 100.0\*MeV))) & (INTREE( ('p+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.1) & (PT\> 100.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>4) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r0p2-commonparticles-stdlooselambdadd)' ]                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                      |
| Output          | Phys/LambdaDDForCcbar2LstLambda/Particles                                                                                                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdaLDForCcbar2LstLambda

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaLD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaLD/Particles',True) |

FilterDesktop/LambdaLDForCcbar2LstLambda

|                 |                                                                                                                                                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 16) & (ADMASS('Lambda0')\< 30 \*MeV) & (INTREE( ('pi+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNpi\> 0.1) & (PT\> 100.0\*MeV))) & (INTREE( ('p+'==ABSID) & (TRCHI2DOF \< 5.0) & (PROBNNp\> 0.1) & (PT\> 100.0\*MeV))) & (ADWM( 'KS0' , WM( 'pi+' , 'pi-') ) \> 20\*MeV ) & (BPVDLS\>4) |
| Inputs          | [ 'Phys/[StdLooseLambdaLD](./stripping21r0p2-commonparticles-stdlooselambdald)' ]                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                      |
| Output          | Phys/LambdaLDForCcbar2LstLambda/Particles                                                                                                                                                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergedLambdaForJpsiCcbar2LstLambda

|                 |                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                             |
| Inputs          | [ 'Phys/LambdaDDForCcbar2LstLambda' , 'Phys/LambdaLDForCcbar2LstLambda' , 'Phys/LambdaLLForCcbar2LstLambda' ] |
| DecayDescriptor | None                                                                                                            |
| Output          | Phys/MergedLambdaForJpsiCcbar2LstLambda/Particles                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Ccbar2LstLambdaLine

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedLstForCcbar2LstLambda' , 'Phys/MergedLambdaForJpsiCcbar2LstLambda' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' } |
| CombinationCut   | (in_range( 2700.0 \*MeV, AM, 15100.0 \*MeV))                                                                 |
| MotherCut        | (in_range( 2750.0 \*MeV, MM, 15000.0 \*MeV)) & (VFASPF(VCHI2PDOF) \< 16 ) & (BPVDLS\>3)                      |
| DecayDescriptor  | [J/psi(1S) -\> Lambda(1520)0 Lambda~0]cc                                                                   |
| DecayDescriptors | [ ' [J/psi(1S) -\> Lambda(1520)0 Lambda~0]cc' ]                                                          |
| Output           | Phys/Ccbar2LstLambdaLine/Particles                                                                           |
