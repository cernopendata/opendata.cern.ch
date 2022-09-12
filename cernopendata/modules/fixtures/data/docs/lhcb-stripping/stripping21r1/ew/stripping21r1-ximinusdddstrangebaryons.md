[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXiminusDDDStrangeBaryons

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/XiminusDDDStrangeBaryons/Particles                                                                                                                                                                                            |
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

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownPions](./stripping21r1-stdnopidsdownpions) /Particles')\>0 |

**FilterDesktop/PionsForLambdaDStrangeBaryons**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 4.0)                              |
| Inputs          | [ 'Phys/ [StdNoPIDsDownPions](./stripping21r1-stdnopidsdownpions) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/PionsForLambdaDStrangeBaryons/Particles                            |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownProtons_Particles**

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownProtons](./stripping21r1-stdnopidsdownprotons) /Particles')\>0 |

**FilterDesktop/ProtonsForLambdaDStrangeBaryons**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | HASRICH & ((PIDp-PIDpi) \> -5.0) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 4.0) |
| Inputs          | [ 'Phys/ [StdNoPIDsDownProtons](./stripping21r1-stdnopidsdownprotons) ' ]   |
| DecayDescriptor | None                                                                          |
| Output          | Phys/ProtonsForLambdaDStrangeBaryons/Particles                                |

**CombineParticles/Lambda2pPiDStrangeBaryons**

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForLambdaDStrangeBaryons' , 'Phys/ProtonsForLambdaDStrangeBaryons' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p\~-' : 'ALL' }                         |
| CombinationCut   | (ADAMASS('Lambda0') \< 30.0\*MeV)                                                                      |
| MotherCut        | (BPVIPCHI2() \> 2.0) & (VFASPF(VCHI2) \< 15.0) &(BPVVDCHI2 \> 100.0) & (ADMASS('Lambda0') \< 6.0\*MeV) |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                               |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                       |
| Output           | Phys/Lambda2pPiDStrangeBaryons/Particles                                                               |

**FilterDesktop/PionsForXiDDStrangeBaryons**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 4.0)                              |
| Inputs          | [ 'Phys/ [StdNoPIDsDownPions](./stripping21r1-stdnopidsdownpions) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/PionsForXiDDStrangeBaryons/Particles                               |

**CombineParticles/XiminusDDDStrangeBaryons**

|                  |                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda2pPiDStrangeBaryons' , 'Phys/PionsForXiDDStrangeBaryons' ]                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                              |
| CombinationCut   | (ADAMASS('Xi-') \< 50.0\*MeV)                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2)\< 25.0) & (BPVVDCHI2 \> 5.0) & ((CHILD(PX,1)\*CHILD(PX,0)+CHILD(PY,1)\*CHILD(PY,0)+CHILD(PZ,1)\*CHILD(PZ,0))/(CHILD(P,1)\*CHILD(P,0)) \> 0.9996) & (BPVIPCHI2()\<1000) |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                                                                             |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                                                                                     |
| Output           | Phys/XiminusDDDStrangeBaryons/Particles                                                                                                                                               |
