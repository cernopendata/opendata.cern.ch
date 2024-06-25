[[stripping21 lines]](./stripping21-index)

# StrippingHeavyBaryonOmegab2JpsiOmega

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/HeavyBaryonOmegab2JpsiOmega/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80.0)                                                                 |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon/Particles                                          |

GaudiSequencer/SeqMergedKaonsForHeavyBaryon

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseDownKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDownKaons](./stripping21-commonparticles-stdloosedownkaons)/Particles')\>0 |

FilterDesktop/MergedKaonsForHeavyBaryon

|                 |                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                           |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdLooseDownKaons](./stripping21-commonparticles-stdloosedownkaons)' ] |
| DecayDescriptor | None                                                                                                                                                          |
| Output          | Phys/MergedKaonsForHeavyBaryon/Particles                                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KaonsForHeavyBaryon

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (PIDK \> -5.0)   |
| Inputs          | [ 'Phys/MergedKaonsForHeavyBaryon' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/KaonsForHeavyBaryon/Particles     |

GaudiSequencer/SeqStdLooseLambdaMergedForHeavyBaryon

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/StdLooseLambdaMergedForHeavyBaryon

|                 |                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' , 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ] |
| DecayDescriptor | None                                                                                                                                                        |
| Output          | Phys/StdLooseLambdaMergedForHeavyBaryon/Particles                                                                                                           |

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

CombineParticles/Omegaminus2LambdaKHeavyBaryon

|                  |                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForHeavyBaryon' , 'Phys/LambdaForHeavyBaryon' ]                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>0.1\*GeV) & (BPVIPCHI2()\>9)' , 'K-' : '(PT\>0.1\*GeV) & (BPVIPCHI2()\>9)' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' } |
| CombinationCut   | (ADAMASS('Omega-') \< 30.0\*MeV)                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (BPVDLS\> 5.0)                                                                                                         |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                                                       |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                                                               |
| Output           | Phys/Omegaminus2LambdaKHeavyBaryon/Particles                                                                                                      |

CombineParticles/HeavyBaryonOmegab2JpsiOmega

|                  |                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MassConstrainedJpsiForHeavyBaryonsHeavyBaryon' , 'Phys/Omegaminus2LambdaKHeavyBaryon' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Omega-' : 'ALL' , 'Omega~+' : 'ALL' }                       |
| CombinationCut   | (ADAMASS('Omega_b-') \<600\*MeV )                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<25) & (ADMASS('Omega_b-') \<500.0 \*MeV)                                     |
| DecayDescriptor  | [Omega_b- -\> Omega- J/psi(1S)]cc                                                               |
| DecayDescriptors | [ '[Omega_b- -\> Omega- J/psi(1S)]cc' ]                                                       |
| Output           | Phys/HeavyBaryonOmegab2JpsiOmega/Particles                                                        |
