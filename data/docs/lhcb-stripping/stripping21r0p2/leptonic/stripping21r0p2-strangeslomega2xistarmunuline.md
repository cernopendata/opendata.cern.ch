[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingStrangeSLOmega2XiStarmunuLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/StrangeSLOmega2XiStarmunuLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

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

**CombineParticles/L02PPi_sel_SL**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p2-stdallloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'p\~-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (ADAMASS('Lambda0')\<30.0 \*MeV) & (AMAXDOCA('')\< 1.0 \*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9.0) & (PT\> 0.0 \*MeV) & (ADMASS('Lambda0') \< 30.0 \*MeV ) & (BPVIPCHI2()\> 16.0) & (BPVLTIME()\> 9.0 \* ps) &(BPVVDCHI2 \> 100) & (MIPDV(PRIMARY)\>0.2\*mm)                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/L02PPi_sel_SL/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**CombineParticles/Xi2LambdaPi_sel**

|                  |                                                                                                                                                                                                                                                                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/L02PPi_sel_SL' , 'Phys/ [StdAllLoosePions](./stripping21r0p2-stdallloosepions) ' ]                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (ADAMASS('Xi-') \< 300.0\*MeV) & (AMAXDOCA('')\< 1 \*mm)                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (ADMASS('Xi-') \< 300.0\*MeV) & (VFASPF(VCHI2/VDOF)\<25.0) & (BPVLTIME()\> 6.0 \* ps) & (PT\>500.0) & (BPVVDCHI2 \> 30)                                                                                                                                                                                                                                    |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/Xi2LambdaPi_sel/Particles                                                                                                                                                                                                                                                                                                                             |

**CombineParticles/XiStar2XiPi_sel**

|                  |                                                                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p2-stdallloosepions) ' , 'Phys/Xi2LambdaPi_sel' ]                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'Xi-' : 'ALL' , 'Xi\~+' : 'ALL' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (AM\> 1480.0) & (AM\< 1580.0)                                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (M\> 1480.0) & (M\< 1580.0) & (VFASPF(VCHI2/VDOF)\< 1480.0)                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | [Xi\*0 -\> Xi- pi+]cc                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[Xi\*0 -\> Xi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/XiStar2XiPi_sel/Particles                                                                                                                                                                                                                                                                                                                     |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/StrangeSLOmega2XiStarmunuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' , 'Phys/XiStar2XiPi_sel' ]                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'Xi\*0' : 'ALL' , 'Xi\*\~0' : 'ALL' , 'mu+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'mu-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' } |
| CombinationCut   | (AM\< 1972.0)                                                                                                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (M\< 1972.0) & (BPVLTIME()\> 4.0 \* ps) & (VFASPF(VCHI2/VDOF)\< 25.0)                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor  | [Omega- -\> Xi\*0 mu-]cc                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[Omega- -\> Xi\*0 mu-]cc' ]                                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/StrangeSLOmega2XiStarmunuLine/Particles                                                                                                                                                                                                                                                                                                                                                       |
