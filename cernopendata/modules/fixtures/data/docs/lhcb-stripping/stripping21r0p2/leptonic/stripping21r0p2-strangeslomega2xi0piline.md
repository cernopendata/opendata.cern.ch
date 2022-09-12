[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingStrangeSLOmega2Xi0PiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/StrangeSLOmega2Xi0PiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0**

|      |                                         |
|------|-----------------------------------------|
| Code | 0 StdLooseResolvedPi0 /Particles',True) |

**CombineParticles/Xi02Lambdapi0_sel**

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/L02PPi_sel_SL' , 'Phys/ [StdLooseResolvedPi0](./stripping21r0p2-stdlooseresolvedpi0) ' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'pi0' : '(PT \> 500.0)' }                                          |
| CombinationCut   | (ADAMASS('Xi0') \< 300.0\*MeV) & (AMAXDOCA('')\< 1 \*mm)                                                                    |
| MotherCut        | (ADMASS('Xi0') \< 300.0\*MeV) & (BPVLTIME()\> 6.0 \* ps) & (VFASPF(VCHI2/VDOF)\< 25.0) & (PT\>500.0) & (BPVIPCHI2()\< 36.0) |
| DecayDescriptor  | [Xi0 -\> Lambda0 pi0]cc                                                                                                   |
| DecayDescriptors | [ '[Xi0 -\> Lambda0 pi0]cc' ]                                                                                           |
| Output           | Phys/Xi02Lambdapi0_sel/Particles                                                                                            |

**CombineParticles/StrangeSLOmega2Xi0PiLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p2-stdallloosepions) ' , 'Phys/Xi02Lambdapi0_sel' ]                                                                                                                                                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'Xi0' : "(ADMASS('Xi0') \< 50.0\*MeV)" , 'Xi\~0' : "(ADMASS('Xi0') \< 50.0\*MeV)" , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (PROBNNmu\<0.7) & (PROBNNp\<0.7) & (PROBNNk\<0.7)' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (PROBNNmu\<0.7) & (PROBNNp\<0.7) & (PROBNNk\<0.7)' } |
| CombinationCut   | (ADAMASS('Omega-') \< 300.0\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (ADMASS('Omega-') \< 300.0\*MeV) & (BPVLTIME()\> 4.0 \* ps) & (VFASPF(VCHI2/VDOF)\< 25.0) & (PT\>500.0)                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [Omega- -\> Xi0 pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Omega- -\> Xi0 pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/StrangeSLOmega2Xi0PiLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
