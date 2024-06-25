[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingStrangeSLKs2PiPiMuNuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/StrangeSLKs2PiPiMuNuLine/Particles |
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

**LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLoosePions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/StrangeSLKs2PiPiMuNuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' , 'Phys/ [StdAllLoosePions](./stripping21r1p2-stdallloosepions) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'mu-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)& (PROBNNmu\> 0.3) & (MIPCHI2DV(PRIMARY)\>60.0) & (MIPDV(PRIMARY) \> 1) & (ISMUON) & (PROBNNpi\<0.7) & (PROBNNk\<0.7)' , 'pi+' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' , 'pi-' : ' (TRCHI2DOF\< 3) & (TRGHOSTPROB\<0.2)&(PROBNNpi\> 0.4) & (MIPCHI2DV(PRIMARY)\>60.0) & (\~ISMUON) & (PROBNNmu\<0.7) & (PROBNNk\<0.7) ' } |
| CombinationCut   | (AM\< 600.0) & (AMAXDOCA('')\<3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MotherCut        | (M\< 600.0) & ((BPVVDSIGN\*M/P) \> 1.610411922) & (VFASPF(VCHI2/VDOF)\< 25.0) & (BPVVDCHI2 \> 100.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [K+ -\> pi+ pi- mu+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[K+ -\> pi+ pi- mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/StrangeSLKs2PiPiMuNuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
