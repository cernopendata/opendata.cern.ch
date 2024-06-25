[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2XMuMu_Line

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/B2XMuMu_Line/Particles |
| Postscale      | 1.0000000                   |
| HLT1           | None                        |
| HLT2           | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XMuMu_LineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

CombineParticles/Sel_B2XMuMu_DiMuon

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r0p1-commonparticles-stdallloosemuons)' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDmu\> -3.0)' , 'mu-' : '(TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDmu\> -3.0)' } |
| CombinationCut   | (AM \< 7100.0 \*MeV)                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (BPVVDCHI2 \> 9.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 )                                                |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ 'J/psi(1S) -\> mu- mu+' , 'J/psi(1S) -\> mu+ mu+' , ' J/psi(1S) -\> mu- mu-' ]                                                                                 |
| Output           | Phys/Sel_B2XMuMu_DiMuon/Particles                                                                                                                                  |

GaudiSequencer/SeqSelection_B2XMuMu_daughters

GaudiSequencer/SEQ:B2XMuMu_KstarFilter

GaudiSequencer/SeqB2XMuMu_KstarMerge

GaudiSequencer/SEQ:B2XMuMu_KstarSubMMZ_Sel

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                               |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 9.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                         |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' , 'rho(770)0 -\> pi+ pi+' , 'rho(770)0 -\> pi- pi-' ]                                                                                                            |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                         |

SubPIDMMFilter/B2XMuMu_KstarSubMMZ_Sel

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi-')              |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]            |
| DecayDescriptor | None                                          |
| Output          | Phys/B2XMuMu_KstarSubMMZ_Sel/Particles        |
| MaxMM           | 6050.0000                                     |
| MinMM           | 0.0000000                                     |
| PIDs            | [ [ 'K+' , 'pi-' ] , [ 'pi+' , 'K-' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2XMuMu_KstarSubMMP_Sel

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                               |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 9.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                         |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' , 'rho(770)0 -\> pi+ pi+' , 'rho(770)0 -\> pi- pi-' ]                                                                                                            |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                         |

SubPIDMMFilter/B2XMuMu_KstarSubMMP_Sel

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi+')              |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]            |
| DecayDescriptor | None                                          |
| Output          | Phys/B2XMuMu_KstarSubMMP_Sel/Particles        |
| MaxMM           | 6050.0000                                     |
| MinMM           | 0.0000000                                     |
| PIDs            | [ [ 'K+' , 'pi+' ] , [ 'pi+' , 'K+' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2XMuMu_KstarSubMMM_Sel

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                               |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 9.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                         |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' , 'rho(770)0 -\> pi+ pi+' , 'rho(770)0 -\> pi- pi-' ]                                                                                                            |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                         |

SubPIDMMFilter/B2XMuMu_KstarSubMMM_Sel

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi- pi-')              |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]            |
| DecayDescriptor | None                                          |
| Output          | Phys/B2XMuMu_KstarSubMMM_Sel/Particles        |
| MaxMM           | 6050.0000                                     |
| MinMM           | 0.0000000                                     |
| PIDs            | [ [ 'K-' , 'pi-' ] , [ 'pi-' , 'K-' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2XMuMu_KstarMerge

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                    |
| Inputs          | [ 'Phys/B2XMuMu_KstarSubMMM_Sel' , 'Phys/B2XMuMu_KstarSubMMP_Sel' , 'Phys/B2XMuMu_KstarSubMMZ_Sel' ] |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/B2XMuMu_KstarMerge/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

SubstitutePID/B2XMuMu_KstarSub_Sel

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/B2XMuMu_KstarMerge' ]                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/B2XMuMu_KstarSub_Sel/Particles                                                                                                                             |
| Substitutions   | { 'rho(770)0 -\> K+ pi+' : 'K\*(892)0' , 'rho(770)0 -\> K+ pi-' : 'K\*(892)0' , 'rho(770)0 -\> K- pi-' : 'K\*(892)~0' , 'rho(770)0 -\> pi+ K-' : 'K\*(892)~0' } |

FilterDesktop/B2XMuMu_KstarFilter

|                 |                                    |
|-----------------|------------------------------------|
| Code            | (ABSID=='K\*(892)0')               |
| Inputs          | [ 'Phys/B2XMuMu_KstarSub_Sel' ]  |
| DecayDescriptor | None                               |
| Output          | Phys/B2XMuMu_KstarFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_rho2pipizero

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

GaudiSequencer/SeqSelection_B2XMuMu_pi0

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0merged' , 'Phys/Selection_B2XMuMu_pi0resolved' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Selection_B2XMuMu_rho2pipizero

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' , 'Phys/Selection_B2XMuMu_pi0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                  |
| CombinationCut   | ATRUE                                                                           |
| MotherCut        | (ADMASS('rho(770)+') \< 300.0 \*MeV)                                            |
| DecayDescriptor  | [rho(770)+ -\> pi+ pi0]cc                                                     |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ pi0]cc' ]                                             |
| Output           | Phys/Selection_B2XMuMu_rho2pipizero/Particles                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_StdAllNoPIDsKaons

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsKaons/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_Kstar2kspi

GaudiSequencer/SeqSelection_B2XMuMu_Kshort

GaudiSequencer/SEQ:Selection_B2XMuMu_Ksdd

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_Ksll

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_Ksll

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksll/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_Kshort

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ALL                                                                 |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Ksdd' , 'Phys/Selection_B2XMuMu_Ksll' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/Selection_B2XMuMu_Kshort/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Kstar2kspi

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Kshort' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                               |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 9.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 ) |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                  |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                          |
| Output           | Phys/Selection_B2XMuMu_Kstar2kspi/Particles                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_Kstar2kpizero

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsKaons/Particles                                    |

GaudiSequencer/SeqSelection_B2XMuMu_pi0

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0merged' , 'Phys/Selection_B2XMuMu_pi0resolved' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Selection_B2XMuMu_Kstar2kpizero

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsKaons' , 'Phys/Selection_B2XMuMu_pi0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi0' : 'ALL' }                    |
| CombinationCut   | ATRUE                                                                           |
| MotherCut        | (ADMASS('K\*(892)+') \< 300.0 \*MeV)                                            |
| DecayDescriptor  | [K\*(892)+ -\> K+ pi0]cc                                                      |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' ]                                              |
| Output           | Phys/Selection_B2XMuMu_Kstar2kpizero/Particles                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SeqSelection_B2XMuMu_pi0

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 700.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0merged' , 'Phys/Selection_B2XMuMu_pi0resolved' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_daughters

|                 |                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                 |
| Inputs          | [ 'Phys/B2XMuMu_KstarFilter' , 'Phys/Selection_B2XMuMu_Kstar2kpizero' , 'Phys/Selection_B2XMuMu_Kstar2kspi' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsKaons' , 'Phys/Selection_B2XMuMu_pi0' , 'Phys/Selection_B2XMuMu_rho2pipizero' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                |
| Output          | Phys/Selection_B2XMuMu_daughters/Particles                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XMuMu_Line

|                  |                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Sel_B2XMuMu_DiMuon' , 'Phys/Selection_B2XMuMu_daughters' ]                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi0' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' } |
| CombinationCut   | (AM \> 4600.0 \* MeV) & (AM \< 7100.0 \* MeV)                                                                                                                                                                           |
| MotherCut        | (abs(SUMQ) \< 3) & (M \> 4700.0 \* MeV) & (M \< 7000.0 \* MeV) & (VFASPF(VCHI2/VDOF) \< 8.0) & (BPVIPCHI2() \< 16.0) & (BPVDIRA\> 0.9999) & (BPVVDCHI2 \> 121.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 )         |
| DecayDescriptor  | None                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' , '[B+ -\> J/psi(1S) rho(770)+]cc' , '[B+ -\> J/psi(1S) K+]cc' , '[B+ -\> J/psi(1S) K\*(892)+]cc' , 'B0 -\> J/psi(1S) pi0' ]                                               |
| Output           | Phys/B2XMuMu_Line/Particles                                                                                                                                                                                             |

AddRelatedInfo/RelatedInfo1_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_B2XMuMu_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo2_B2XMuMu_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo3_B2XMuMu_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo4_B2XMuMu_Line/Particles |
