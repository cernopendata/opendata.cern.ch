[[stripping21 lines]](./stripping21-index)

# StrippingXiminusLLLStrangeBaryons

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/XiminusLLLStrangeBaryons/Particles                                                                                                                                                                                            |
| Postscale      | 1.0000000                                                                                                                                                                                                                          |
| HLT            | HLT_PASS('Hlt1MBNoBiasDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationRateLimitedDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloRateLimitedDecision') |
| Prescale       | 1.0000000                                                                                                                                                                                                                          |
| L0DU           | None                                                                                                                                                                                                                               |
| ODIN           | None                                                                                                                                                                                                                               |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) /Particles')\>0 |

**FilterDesktop/PionsForLambdaStrangeBaryons**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 20.0)            |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/PionsForLambdaStrangeBaryons/Particles                       |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseProtons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseProtons](./stripping21-stdalllooseprotons) /Particles')\>0 |

**FilterDesktop/ProtonsForLambdaLooseStrangeBaryons**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 9.0)                 |
| Inputs          | [ 'Phys/ [StdAllLooseProtons](./stripping21-stdalllooseprotons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/ProtonsForLambdaLooseStrangeBaryons/Particles                    |

**CombineParticles/Lambda2pPiLStrangeBaryons**

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForLambdaStrangeBaryons' , 'Phys/ProtonsForLambdaLooseStrangeBaryons' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p\~-' : 'ALL' }                         |
| CombinationCut   | (ADAMASS('Lambda0') \< 30.0\*MeV)                                                                      |
| MotherCut        | (BPVIPCHI2() \> 9.0) & (VFASPF(VCHI2) \< 15.0) &(BPVVDCHI2 \> 150.0) & (ADMASS('Lambda0') \< 6.0\*MeV) |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                               |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                       |
| Output           | Phys/Lambda2pPiLStrangeBaryons/Particles                                                               |

**FilterDesktop/PionsForXiStrangeBaryons**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 10.0)            |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/PionsForXiStrangeBaryons/Particles                           |

**CombineParticles/XiminusLLLStrangeBaryons**

|                  |                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda2pPiLStrangeBaryons' , 'Phys/PionsForXiStrangeBaryons' ]                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                               |
| CombinationCut   | (ADAMASS('Xi-') \< 50.0\*MeV)                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2)\< 25.0) & (BPVVDCHI2 \> 30.0) & ((CHILD(PX,1)\*CHILD(PX,0)+CHILD(PY,1)\*CHILD(PY,0)+CHILD(PZ,1)\*CHILD(PZ,0))/(CHILD(P,1)\*CHILD(P,0)) \> 0.9996) & (BPVIPCHI2()\<1000) |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                                                                              |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                                                                                      |
| Output           | Phys/XiminusLLLStrangeBaryons/Particles                                                                                                                                                |
