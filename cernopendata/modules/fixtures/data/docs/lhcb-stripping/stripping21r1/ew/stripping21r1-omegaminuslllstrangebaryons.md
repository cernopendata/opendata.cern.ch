[[stripping21r1 lines]](./stripping21r1-index)

# StrippingOmegaminusLLLStrangeBaryons

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/OmegaminusLLLStrangeBaryons/Particles                                                                                                                                                                                         |
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

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) /Particles')\>0 |

**FilterDesktop/PionsForLambdaStrangeBaryons**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 20.0)              |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/PionsForLambdaStrangeBaryons/Particles                         |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseProtons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseProtons](./stripping21r1-stdalllooseprotons) /Particles')\>0 |

**FilterDesktop/ProtonsForLambdaLooseStrangeBaryons**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 9.0)                   |
| Inputs          | [ 'Phys/ [StdAllLooseProtons](./stripping21r1-stdalllooseprotons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/ProtonsForLambdaLooseStrangeBaryons/Particles                      |

**CombineParticles/Lambda2pPiLOmegaStrangeBaryons**

|                  |                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForLambdaStrangeBaryons' , 'Phys/ProtonsForLambdaLooseStrangeBaryons' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p\~-' : 'ALL' }                        |
| CombinationCut   | (ADAMASS('Lambda0') \< 30.0\*MeV)                                                                     |
| MotherCut        | (BPVIPCHI2() \> 9.0) & (VFASPF(VCHI2) \< 15.0) &(BPVVDCHI2 \> 70.0) & (ADMASS('Lambda0') \< 6.0\*MeV) |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                              |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                      |
| Output           | Phys/Lambda2pPiLOmegaStrangeBaryons/Particles                                                         |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) /Particles')\>0 |

**FilterDesktop/KaonsForOmegaStrangeBaryons**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (ISLONG) & (TRCHI2DOF \< 4.0 ) & (BPVIPCHI2() \> 3.0)               |
| Inputs          | [ 'Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/KaonsForOmegaStrangeBaryons/Particles                          |

**CombineParticles/OmegaminusLLLStrangeBaryons**

|                  |                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForOmegaStrangeBaryons' , 'Phys/Lambda2pPiLOmegaStrangeBaryons' ]                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' }                                                                                                |
| CombinationCut   | (ADAMASS('Omega-') \< 50.0\*MeV)                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2)\< 9.0) & (BPVVDCHI2 \> 10.0) & ((CHILD(PX,1)\*CHILD(PX,0)+CHILD(PY,1)\*CHILD(PY,0)+CHILD(PZ,1)\*CHILD(PZ,0))/(CHILD(P,1)\*CHILD(P,0)) \> 0.9996) & (BPVIPCHI2()\<1000) |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                                                                                           |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                                                                                                   |
| Output           | Phys/OmegaminusLLLStrangeBaryons/Particles                                                                                                                                            |
