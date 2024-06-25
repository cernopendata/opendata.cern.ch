[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingStrangeSLKs2PiMuNuLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/StrangeSLKs2PiMuNuLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLoosePions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/StrangeSLKs2PiMuNuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' , 'Phys/ [StdAllLoosePions](./stripping21r1p2-stdallloosepions) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)& (TRGHOSTPROB\<0.1)' , 'mu-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)& (TRGHOSTPROB\<0.1)' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) & (TRGHOSTPROB\<0.1)' } |
| CombinationCut   | (AM\< 600.0) & (AMAXDOCA('')\<0.2\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (M\< 600.0) & (M\> 200.0) & (P\> 3000) & (VFASPF(VCHI2/VDOF)\< 6.0) & (VFASPF(sqrt(VX\*VX+VY\*VY)) \> 4) & ( VFASPF(VZ)\<650) & (BPVVDCHI2 \> 100.0) & (BPVLTIME()\> 6.0 \* ps) & ((MIPDV(PRIMARY)/BPVVDZ)\< 0.02) & (MIPDV(PRIMARY)\>0.2\*mm) & (MIPCHI2DV(PRIMARY)\>4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | [KS0 -\> pi+ mu-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[KS0 -\> pi+ mu-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/StrangeSLKs2PiMuNuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
