[[stripping21 lines]](./stripping21-index)

# Strippingtau2LambdaMuLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/tau2LambdaMuLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21-stdloosepions) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles')\>0 |

**CombineParticles/tau2LambdaMuSelLambda**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLoosePions](./stripping21-stdloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : ' ( PT \> 250 \* MeV ) & ( TRCHI2DOF \< 4 ) & ( BPVIPCHI2 () \> 5 ) & (PIDp\>3) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(ISLONG) & (TRCHI2DOF \< 4 ) & (TRGHOSTPROB\<0.5) & ( BPVIPCHI2 () \> 5 ) & (PT\>250\*MeV) & (PIDpi - PIDK \> -5)' , 'pi-' : '(ISLONG) & (TRCHI2DOF \< 4 ) & (TRGHOSTPROB\<0.5) & ( BPVIPCHI2 () \> 5 ) & (PT\>250\*MeV) & (PIDpi - PIDK \> -5)' , 'p\~-' : ' ( PT \> 250 \* MeV ) & ( TRCHI2DOF \< 4 ) & ( BPVIPCHI2 () \> 5 ) & (PIDp\>3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (ADAMASS('Lambda0')\<100\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MotherCut        | ( VFASPF(VCHI2) \< 10 ) & (MIPCHI2DV(PRIMARY)\> 16.) & (ADMASS('Lambda0')\<90\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/tau2LambdaMuSelLambda/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**CombineParticles/tau2LambdaMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' , 'Phys/tau2LambdaMuSelLambda' ]                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3. ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.3 )' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3. ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.3 )' } |
| CombinationCut   | ( (ADAMASS('tau+')\<150\*MeV) )                                                                                                                                                                                                                                                                                                                                    |
| MotherCut        | ( VFASPF(VCHI2) \< 16 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 250 )                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ ' [ tau+ -\> Lambda0 mu+ ]cc' ]                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/tau2LambdaMuLine/Particles                                                                                                                                                                                                                                                                                                                                    |
