[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLFVTau2MuEtaP2pipipiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/LFVTau2MuEtaP2pipipiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

GaudiSequencer/SeqPi0ForselEtap_pi0

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0ForselEtap_pi0

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                        |
| Output          | Phys/Pi0ForselEtap_pi0/Particles                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/selEtap_pi0

|                  |                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ForselEtap_pi0' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' , 'pi-' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' , 'pi0' : '(PT \> 250\*MeV)' } |
| CombinationCut   | (ADAMASS('eta') \< 80\*MeV) \| (ADAMASS('eta_prime') \< 80\*MeV)                                                                                                                                                                                                                                |
| MotherCut        | (PT \> 500\*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0)                                                                                                                                                                                                                                                  |
| DecayDescriptor  | eta_prime -\> pi+ pi- pi0                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- pi0' ]                                                                                                                                                                                                                                                               |
| Output           | Phys/selEtap_pi0/Particles                                                                                                                                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

CombineParticles/LFVTau2MuEtaP2pipipiLine

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r0p1-commonparticles-stdloosemuons)' , 'Phys/selEtap_pi0' ]                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'eta_prime' : 'ALL' , 'mu+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' , 'mu-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' } |
| CombinationCut   | (ADAMASS('tau+')\<150\*MeV)                                                                                                                                                                                                                                          |
| MotherCut        | (BPVIPCHI2()\< 100) & (VFASPF(VCHI2/VDOF)\<6.) & (BPVLTIME()\*c_light \> 50.\*micrometer) & (BPVLTIME()\*c_light \< 400.\*micrometer) & (PT\>500\*MeV) & (D2DVVD(2) \< 80\*micrometer)                                                                               |
| DecayDescriptor  | [tau+ -\> mu+ eta_prime]cc                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[tau+ -\> mu+ eta_prime]cc ' ]                                                                                                                                                                                                                                |
| Output           | Phys/LFVTau2MuEtaP2pipipiLine/Particles                                                                                                                                                                                                                              |

AddRelatedInfo/RelatedInfo1_LFVTau2MuEtaP2pipipiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipipiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_LFVTau2MuEtaP2pipipiLine/Particles |

AddRelatedInfo/RelatedInfo2_LFVTau2MuEtaP2pipipiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipipiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_LFVTau2MuEtaP2pipipiLine/Particles |
