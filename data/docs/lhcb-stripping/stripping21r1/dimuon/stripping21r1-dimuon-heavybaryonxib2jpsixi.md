[[stripping21r1 lines]](./stripping21r1-index)

# StrippingHeavyBaryonXib2JpsiXi

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/HeavyBaryonXib2JpsiXi/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80.0)                                                                   |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon/Particles                                            |

GaudiSequencer/SeqMergedPionsForHeavyBaryon

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)/Particles')\>0 |

FilterDesktop/MergedPionsForHeavyBaryon

|                 |                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                 |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' , 'Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)' ] |
| DecayDescriptor | None                                                                                                                                                                |
| Output          | Phys/MergedPionsForHeavyBaryon/Particles                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/PionsForHeavyBaryon

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (PIDK \< 5.0)    |
| Inputs          | [ 'Phys/MergedPionsForHeavyBaryon' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/PionsForHeavyBaryon/Particles     |

GaudiSequencer/SeqStdLooseLambdaMergedForHeavyBaryon

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/StdLooseLambdaMergedForHeavyBaryon

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' , 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ] |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/StdLooseLambdaMergedForHeavyBaryon/Particles                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LambdaForHeavyBaryon

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MAXTREE('p+'==ABSID, PT) \> 500.\*MeV) & (MAXTREE('pi-'==ABSID, PT) \> 100.\*MeV) & (ADMASS('Lambda0') \< 15.\*MeV) & (VFASPF(VCHI2) \< 20 ) & (BPVDLS\> 5.0 ) |
| Inputs          | [ 'Phys/StdLooseLambdaMergedForHeavyBaryon' ]                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/LambdaForHeavyBaryon/Particles                                                                                                                             |

CombineParticles/Ximinus2LambdaPiHeavyBaryon

|                  |                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LambdaForHeavyBaryon' , 'Phys/PionsForHeavyBaryon' ]                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : '(PT\>0.1\*GeV) & (BPVIPCHI2()\>9)' , 'pi-' : '(PT\>0.1\*GeV) & (BPVIPCHI2()\>9)' } |
| CombinationCut   | (ADAMASS('Xi-') \< 30.0\*MeV)                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) &(BPVDLS \> 5.0)                                                                                                           |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                                           |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                                                   |
| Output           | Phys/Ximinus2LambdaPiHeavyBaryon/Particles                                                                                                          |

CombineParticles/HeavyBaryonXib2JpsiXi

|                  |                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon' , 'Phys/Ximinus2LambdaPiHeavyBaryon' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Xi-' : 'ALL' , 'Xi~+' : 'ALL' }                           |
| CombinationCut   | (ADAMASS('Xi_b-') \<600\*MeV )                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (ADMASS('Xi_b-') \< 300.0 \*MeV)                                     |
| DecayDescriptor  | [Xi_b- -\> Xi- J/psi(1S)]cc                                                                   |
| DecayDescriptors | [ '[Xi_b- -\> Xi- J/psi(1S)]cc' ]                                                           |
| Output           | Phys/HeavyBaryonXib2JpsiXi/Particles                                                            |
