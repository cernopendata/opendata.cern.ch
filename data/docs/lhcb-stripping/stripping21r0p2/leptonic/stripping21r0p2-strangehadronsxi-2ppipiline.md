[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingStrangeHadronsXi-2ppipiLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/StrangeHadronsXi-2ppipiLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

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

**CombineParticles/StrangeHadronsXi-2ppipiLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p2-stdallloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' , 'p\~-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' } |
| CombinationCut   | (ADAMASS('Xi-') \< 300.0\*MeV) & (AMAXDOCA('')\< 1 \*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (ADMASS('Xi-') \< 300.0\*MeV) & (VFASPF(VCHI2/VDOF)\<25.0) & (BPVLTIME()\> 6.0 \* ps) & (PT\>500.0) & (BPVVDCHI2 \> 30)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | [Xi- -\> p\~- pi+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Xi- -\> p\~- pi+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output           | Phys/StrangeHadronsXi-2ppipiLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
