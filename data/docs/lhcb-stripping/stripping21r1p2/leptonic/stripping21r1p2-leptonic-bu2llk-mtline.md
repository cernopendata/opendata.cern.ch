[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBu2LLK_mtLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2LLK_mtLine/Particles |
| Postscale      | 1.0000000                    |
| HLT1           | None                         |
| HLT2           | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_mtLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdTightDetachedTau3pi

|      |                                          |
|------|------------------------------------------|
| Code | 0StdTightDetachedTau3pi/Particles',True) |

CombineParticles/MuTauForBu2LLK

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' , 'Phys/[StdTightDetachedTau3pi](./stripping21r1p2-commonparticles-stdtightdetachedtau3pi)' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'mu-' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'tau+' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(PT \> 0)' , 'tau-' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(PT \> 0)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                                                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 150)                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [J/psi(1S) -\> mu+ tau-]cc                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ tau-]cc' ]                                                                                                                                                                                                                                                       |
| Output           | Phys/MuTauForBu2LLK/Particles                                                                                                                                                                                                                                                              |

FilterDesktop/SelMuTauForBu2LLK

|                 |                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 350 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 150) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) |
| Inputs          | [ 'Phys/MuTauForBu2LLK' ]                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                         |
| Output          | Phys/SelMuTauForBu2LLK/Particles                                                                                                                                                                                             |

GaudiSequencer/MERGED:MergeBu2LLK_mt

GaudiSequencer/MERGEDINPUTS:MergeBu2LLK_mt

GaudiSequencer/INPUT:pKsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdAllLooseProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdAllLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseKaons/Particles',True) |

CombineParticles/pKsForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r1p2-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseProtons](./stripping21r1p2-commonparticles-stdalllooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/pKsForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:pKsSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

CombineParticles/pKsSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/pKsSSForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_mt

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | ALL                                               |
| Inputs          | [ 'Phys/pKsForBu2LLK' , 'Phys/pKsSSForBu2LLK' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/MergeBu2LLK_mt/Particles                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_mtLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_mt' , 'Phys/SelMuTauForBu2LLK' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K\*\_0(1430)0' : 'ALL' , 'K\*\_0(1430)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'K_2(1770)+' : 'ALL' , 'K_2(1770)-' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'N(1440)0' : 'ALL' , 'N(1440)~0' : 'ALL' , "f'\_2(1525)" : 'ALL' , 'f_2(1950)' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'rho(770)0' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 5000 \*MeV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) pi+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , '[ B+ -\> J/psi(1S) K_2(1770)+ ]cc' , ' B0 -\> J/psi(1S) KS0 ' , ' B0 -\> J/psi(1S) rho(770)0 ' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B0 -\> J/psi(1S) K\*\_0(1430)0 ]cc' , ' B_s0 -\> J/psi(1S) phi(1020) ' , " B_s0 -\> J/psi(1S) f'\_2(1525) " , ' B_s0 -\> J/psi(1S) f_2(1950) ' , '[ Lambda_b0 -\> J/psi(1S) Lambda0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) N(1440)0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda(1520)0 ]cc' ] |
| Output           | Phys/Bu2LLK_mtLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

AddRelatedInfo/RelatedInfo1_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo4_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo5_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo6_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo7_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo7_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo8_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo8_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo9_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo9_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo10_Bu2LLK_mtLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                 |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo10_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo11_Bu2LLK_mtLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                 |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo11_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo12_Bu2LLK_mtLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                 |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo12_Bu2LLK_mtLine/Particles |
