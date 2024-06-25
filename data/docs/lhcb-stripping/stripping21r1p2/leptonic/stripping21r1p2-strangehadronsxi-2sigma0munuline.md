[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingStrangeHadronsXi-2Sigma0munuLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/StrangeHadronsXi-2Sigma0munuLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdLooseProtons**

|      |                                     |
|------|-------------------------------------|
| Code | 0 StdLooseProtons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLoosePions /Particles',True) |

**CombineParticles/L02PPi_sel**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r1p2-stdallloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r1p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'p\~-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (ADAMASS('Lambda0')\<30.0 \*MeV) & (AMAXDOCA('')\< 1.0 \*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9.0) & (PT\> 500 \*MeV) & (ADMASS('Lambda0') \< 30.0 \*MeV ) & (BPVIPCHI2()\> 16.0) & (BPVLTIME()\> 9.0 \* ps) &(BPVVDCHI2 \> 100) & (MIPDV(PRIMARY)\>0.2\*mm)                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/L02PPi_sel/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**CombineParticles/Sigma2LambdaGamma_sel**

|                  |                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/L02PPi_sel' , 'Phys/ [StdLooseAllPhotons](./stripping21r1p2-stdlooseallphotons) ' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'gamma' : 'ALL' }                                                                    |
| CombinationCut   | (ADAMASS('Sigma0')\<150.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV) & (ADMASS('Sigma+') \< 150.0 \*MeV ) & (MIPDV(PRIMARY)\>0.05\*mm) & (BPVLTIME()\> 6.0 \* ps) |
| DecayDescriptor  | [Sigma0 -\> Lambda0 gamma]cc                                                                                                                |
| DecayDescriptors | [ '[Sigma0 -\> Lambda0 gamma]cc' ]                                                                                                        |
| Output           | Phys/Sigma2LambdaGamma_sel/Particles                                                                                                          |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/StrangeHadronsXi-2Sigma0munuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Sigma2LambdaGamma_sel' , 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]                                                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'Sigma0' : 'ALL' , 'Sigma\~0' : 'ALL' , 'mu+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\> 60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'mu-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\> 60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' } |
| CombinationCut   | (AM\< 1620.0) & (AMAXDOCA('')\< 1 \*mm)                                                                                                                                                                                                                                                                                                                                                                |
| MotherCut        | (M\< 1620.0) & (BPVLTIME()\> 6.0 \* ps) & (VFASPF(VCHI2/VDOF)\< 25.0) & (BPVVDCHI2 \> 30) & (MIPDV(PRIMARY)\>0.05\*mm)                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | [Xi- -\> Sigma0 mu- ]cc                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[Xi- -\> Sigma0 mu- ]cc' ]                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/StrangeHadronsXi-2Sigma0munuLine/Particles                                                                                                                                                                                                                                                                                                                                                        |
