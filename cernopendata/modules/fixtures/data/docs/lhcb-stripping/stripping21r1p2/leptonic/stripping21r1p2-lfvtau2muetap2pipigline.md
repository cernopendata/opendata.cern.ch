[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLFVTau2MuEtaP2pipigLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/LFVTau2MuEtaP2pipigLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

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

**LoKi::VoidFilter/SELECT:Phys/StdLoosePions**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLoosePions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**CombineParticles/selEtap_gamma**

|                  |                                                                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseAllPhotons](./stripping21r1p2-stdlooseallphotons) ' , 'Phys/ [StdLoosePions](./stripping21r1p2-stdloosepions) ' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(PT \> 300\*MeV) & (CL \> 0.1)' , 'pi+' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' , 'pi-' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' } |
| CombinationCut   | (ADAMASS('eta') \< 80\*MeV) \| (ADAMASS('eta_prime') \< 80\*MeV)                                                                                                                                                                                                                                                |
| MotherCut        | (PT \> 500\*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0)                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | eta_prime -\> pi+ pi- gamma                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- gamma' ]                                                                                                                                                                                                                                                                             |
| Output           | Phys/selEtap_gamma/Particles                                                                                                                                                                                                                                                                                    |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**CombineParticles/LFVTau2MuEtaP2pipigLine**

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' , 'Phys/selEtap_gamma' ]                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'eta_prime' : 'ALL' , 'mu+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' , 'mu-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' } |
| CombinationCut   | (ADAMASS('tau+')\<150\*MeV)                                                                                                                                                                                                                                          |
| MotherCut        | (BPVIPCHI2()\< 100) & (VFASPF(VCHI2/VDOF)\<6.) & (BPVLTIME()\*c_light \> 50.\*micrometer) & (BPVLTIME()\*c_light \< 400.\*micrometer) & (PT\>500\*MeV) & (D2DVVD(2) \< 80\*micrometer)                                                                               |
| DecayDescriptor  | [tau+ -\> mu+ eta_prime]cc                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[tau+ -\> mu+ eta_prime]cc ' ]                                                                                                                                                                                                                                |
| Output           | Phys/LFVTau2MuEtaP2pipigLine/Particles                                                                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_LFVTau2MuEtaP2pipigLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipigLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_LFVTau2MuEtaP2pipigLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVTau2MuEtaP2pipigLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipigLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_LFVTau2MuEtaP2pipigLine/Particles |
