[[stripping21 lines]](./stripping21-index)

# StrippingLFVTau2eMuMuLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/LFVTau2eMuMuLine/Particles |
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

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) /Particles')\>0 |

**CombineParticles/LFVTau2eMuMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' ]                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDe \> 2) ' , 'e-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDe \> 2) ' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (TRGHOSTPROB\<0.3) ' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (TRGHOSTPROB\<0.3) ' } |
| CombinationCut   | (ADAMASS('tau+')\<200\*MeV)                                                                                                                                                                                                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ ' [ tau+ -\> e+ mu+ mu- ]cc' , ' [ tau+ -\> mu+ mu+ e- ]cc' ]                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/LFVTau2eMuMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                    |
