[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingStrangeSLL02PMuNuLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/StrangeSLL02PMuNuLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/StrangeSLL02PMuNuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'mu-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'p+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'p\~-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNp\> 0.3) & (MIPCHI2DV(PRIMARY)\>16.0) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (AM\< 1141.0) & (AMAXDOCA('')\< 0.3 \*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (M\< 1141.0 ) & (BPVLTIME()\> 9.0 \* ps) & (VFASPF(VCHI2/VDOF)\< 9.0) & (BPVVDCHI2 \> 50) & (MIPDV(PRIMARY)\>0.2\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [Lambda0 -\> p+ mu-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Lambda0 -\> p+ mu-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/StrangeSLL02PMuNuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
