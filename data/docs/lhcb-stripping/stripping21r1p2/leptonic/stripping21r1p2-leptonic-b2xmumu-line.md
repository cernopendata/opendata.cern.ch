[[stripping21r1p2 lines]](./stripping21r1p2-index)

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseMuons/Particles',True) |

CombineParticles/Sel_B2XMuMu_DiMuon

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1p2-commonparticles-stdallloosemuons)' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (PIDmu\> -3.0)' , 'mu-' : '(TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (PIDmu\> -3.0)' } |
| CombinationCut   | (AM \< 7100.0 \*MeV)                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (BPVVDCHI2 \> 9.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 )                                                |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ 'J/psi(1S) -\> mu- mu+' , 'J/psi(1S) -\> mu+ mu+' , ' J/psi(1S) -\> mu- mu-' ]                                                                                 |
| Output           | Phys/Sel_B2XMuMu_DiMuon/Particles                                                                                                                                  |

GaudiSequencer/MERGED:Selection_B2XMuMu_daughters

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_daughters

GaudiSequencer/INPUT:B2XMuMu_PhiFilter

GaudiSequencer/MERGED:B2XMuMu_PhiMerge

GaudiSequencer/MERGEDINPUTS:B2XMuMu_PhiMerge

GaudiSequencer/INPUT:B2XMuMu_PhiSubMMZ_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_PhiSubMMZ_Sel

|                 |                                      |
|-----------------|--------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi-')     |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]   |
| DecayDescriptor | None                                 |
| Output          | Phys/B2XMuMu_PhiSubMMZ_Sel/Particles |
| MaxMM           | 6050.0000                            |
| MinMM           | 0.0000000                            |
| PIDs            | [ [ 'K+' , 'K-' ] ]              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_PhiSubMMP_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_PhiSubMMP_Sel

|                 |                                      |
|-----------------|--------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi+')     |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]   |
| DecayDescriptor | None                                 |
| Output          | Phys/B2XMuMu_PhiSubMMP_Sel/Particles |
| MaxMM           | 6050.0000                            |
| MinMM           | 0.0000000                            |
| PIDs            | [ [ 'K+' , 'K+' ] ]              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_PhiSubMMM_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_PhiSubMMM_Sel

|                 |                                      |
|-----------------|--------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi- pi-')     |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]   |
| DecayDescriptor | None                                 |
| Output          | Phys/B2XMuMu_PhiSubMMM_Sel/Particles |
| MaxMM           | 6050.0000                            |
| MinMM           | 0.0000000                            |
| PIDs            | [ [ 'K-' , 'K-' ] ]              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/B2XMuMu_PhiMerge

|                 |                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                              |
| Inputs          | [ 'Phys/B2XMuMu_PhiSubMMM_Sel' , 'Phys/B2XMuMu_PhiSubMMP_Sel' , 'Phys/B2XMuMu_PhiSubMMZ_Sel' ] |
| DecayDescriptor | None                                                                                             |
| Output          | Phys/B2XMuMu_PhiMerge/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

SubstitutePID/B2XMuMu_PhiSub_Sel

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                 |
| Inputs          | [ 'Phys/B2XMuMu_PhiMerge' ]                                                                                       |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/B2XMuMu_PhiSub_Sel/Particles                                                                                   |
| Substitutions   | { 'rho(770)0 -\> K+ K+' : 'phi(1020)' , 'rho(770)0 -\> K+ K-' : 'phi(1020)' , 'rho(770)0 -\> K- K-' : 'phi(1020)' } |

FilterDesktop/B2XMuMu_PhiFilter

|                 |                                  |
|-----------------|----------------------------------|
| Code            | (ABSID=='phi(1020)')             |
| Inputs          | [ 'Phys/B2XMuMu_PhiSub_Sel' ]  |
| DecayDescriptor | None                             |
| Output          | Phys/B2XMuMu_PhiFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_KstarFilter

GaudiSequencer/MERGED:B2XMuMu_KstarMerge

GaudiSequencer/MERGEDINPUTS:B2XMuMu_KstarMerge

GaudiSequencer/INPUT:B2XMuMu_KstarSubMMZ_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

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

GaudiSequencer/INPUT:B2XMuMu_KstarSubMMP_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

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

GaudiSequencer/INPUT:B2XMuMu_KstarSubMMM_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

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

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
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

GaudiSequencer/INPUT:Selection_B2XMuMu_Rho

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_rho2pipizero

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
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

GaudiSequencer/INPUT:B2XMuMu_F2Filter

GaudiSequencer/MERGED:B2XMuMu_F2Merge

GaudiSequencer/MERGEDINPUTS:B2XMuMu_F2Merge

GaudiSequencer/INPUT:B2XMuMu_F2SubMMZ_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_F2SubMMZ_Sel

|                 |                                     |
|-----------------|-------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi-')    |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]  |
| DecayDescriptor | None                                |
| Output          | Phys/B2XMuMu_F2SubMMZ_Sel/Particles |
| MaxMM           | 6050.0000                           |
| MinMM           | 0.0000000                           |
| PIDs            | [ [ 'p+' , 'p~-' ] ]            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_F2SubMMP_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_F2SubMMP_Sel

|                 |                                     |
|-----------------|-------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi+')    |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]  |
| DecayDescriptor | None                                |
| Output          | Phys/B2XMuMu_F2SubMMP_Sel/Particles |
| MaxMM           | 6050.0000                           |
| MinMM           | 0.0000000                           |
| PIDs            | [ [ 'p+' , 'p+' ] ]             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_F2SubMMM_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_F2SubMMM_Sel

|                 |                                     |
|-----------------|-------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi- pi-')    |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]  |
| DecayDescriptor | None                                |
| Output          | Phys/B2XMuMu_F2SubMMM_Sel/Particles |
| MaxMM           | 6050.0000                           |
| MinMM           | 0.0000000                           |
| PIDs            | [ [ 'p~-' , 'p~-' ] ]           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/B2XMuMu_F2Merge

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                           |
| Inputs          | [ 'Phys/B2XMuMu_F2SubMMM_Sel' , 'Phys/B2XMuMu_F2SubMMP_Sel' , 'Phys/B2XMuMu_F2SubMMZ_Sel' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/B2XMuMu_F2Merge/Particles                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

SubstitutePID/B2XMuMu_F2Sub_Sel

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                    |
| Inputs          | [ 'Phys/B2XMuMu_F2Merge' ]                                                                                           |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/B2XMuMu_F2Sub_Sel/Particles                                                                                       |
| Substitutions   | { 'rho(770)0 -\> p+ p+' : 'f_2(1950)' , 'rho(770)0 -\> p+ p~-' : 'f_2(1950)' , 'rho(770)0 -\> p~- p~-' : 'f_2(1950)' } |

FilterDesktop/B2XMuMu_F2Filter

|                 |                                 |
|-----------------|---------------------------------|
| Code            | (ABSID=='f_2(1950)')            |
| Inputs          | [ 'Phys/B2XMuMu_F2Sub_Sel' ]  |
| DecayDescriptor | None                            |
| Output          | Phys/B2XMuMu_F2Filter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Kshort

GaudiSequencer/MERGED:Selection_B2XMuMu_Kshort

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Kshort

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksdd

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksll

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksll

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)          |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Ksll/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_dzero

LoKi::VoidFilter/SELECT:Phys/StdLooseD02KPi

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseD02KPi/Particles',True) |

FilterDesktop/Selection_B2XMuMu_dzero

|                 |                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21r1p2-commonparticles-stdloosed02kpi)' ]                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                          |
| Output          | Phys/Selection_B2XMuMu_dzero/Particles                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_StdAllNoPIDsKaons

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsKaons/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_StdAllNoPIDsPions

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Kstar2kspi

GaudiSequencer/MERGED:Selection_B2XMuMu_Kshort

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Kshort

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksdd

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksll

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksll

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)          |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Ksll/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Kstar2kspi

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Kshort' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                   |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                           |
| Output           | Phys/Selection_B2XMuMu_Kstar2kspi/Particles                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Kstar2kpizero

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsKaons/Particles                                    |

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
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

GaudiSequencer/INPUT:Phys/StdLooseDplus2hhh

LoKi::VoidFilter/SELECT:Phys/StdLooseDplus2hhh

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseDplus2hhh/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdLooseDstarWithD02KPi

LoKi::VoidFilter/SELECT:Phys/StdLooseDstarWithD02KPi

|      |                                           |
|------|-------------------------------------------|
| Code | 0StdLooseDstarWithD02KPi/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Lambda

GaudiSequencer/MERGED:Selection_B2XMuMu_Lambda

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Lambda

GaudiSequencer/INPUT:Selection_B2XMuMu_Lambdall

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseLambdaLL

|      |                                        |
|------|----------------------------------------|
| Code | 0StdVeryLooseLambdaLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdall

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)              |
| Inputs          | [ 'Phys/[StdVeryLooseLambdaLL](./stripping21r1p2-commonparticles-stdverylooselambdall)' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Selection_B2XMuMu_Lambdall/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Lambdadd

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdadd

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)      |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Lambdadd/Particles                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_Lambda

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ALL                                                                         |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Lambdadd' , 'Phys/Selection_B2XMuMu_Lambdall' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Lambda/Particles                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_LambdastarFilter

GaudiSequencer/MERGED:B2XMuMu_LambdastarMerge

GaudiSequencer/MERGEDINPUTS:B2XMuMu_LambdastarMerge

GaudiSequencer/INPUT:B2XMuMu_LambdastarSubMMZ_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_LambdastarSubMMZ_Sel

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi-')             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]           |
| DecayDescriptor | None                                         |
| Output          | Phys/B2XMuMu_LambdastarSubMMZ_Sel/Particles  |
| MaxMM           | 6050.0000                                    |
| MinMM           | 0.0000000                                    |
| PIDs            | [ [ 'p+' , 'K-' ] , [ 'K+' , 'p~-' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_LambdastarSubMMP_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_LambdastarSubMMP_Sel

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi+ pi+')            |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]          |
| DecayDescriptor | None                                        |
| Output          | Phys/B2XMuMu_LambdastarSubMMP_Sel/Particles |
| MaxMM           | 6050.0000                                   |
| MinMM           | 0.0000000                                   |
| PIDs            | [ [ 'p+' , 'K+' ] , [ 'K+' , 'p+' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_LambdastarSubMMM_Sel

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

CombineParticles/Selection_B2XMuMu_Rho

|                  |                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM \> 0.0 \* MeV) & (AM \< 6200.0 \* MeV) & (ADOCACHI2CUT(20.,''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 12.0) & (BPVDIRA\> -0.9) & (M \> 0.0 \* MeV) & (M \< 6200.0 \* MeV) & (BPVVDCHI2 \> 16.0) & (MIPCHI2DV(PRIMARY) \> 0.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 6.0 ) |
| DecayDescriptor  | None                                                                                                                                                                                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                 |
| Output           | Phys/Selection_B2XMuMu_Rho/Particles                                                                                                                                                          |

SubPIDMMFilter/B2XMuMu_LambdastarSubMMM_Sel

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | DECTREE('rho(770)0 -\> pi- pi-')              |
| Inputs          | [ 'Phys/Selection_B2XMuMu_Rho' ]            |
| DecayDescriptor | None                                          |
| Output          | Phys/B2XMuMu_LambdastarSubMMM_Sel/Particles   |
| MaxMM           | 6050.0000                                     |
| MinMM           | 0.0000000                                     |
| PIDs            | [ [ 'p~-' , 'K-' ] , [ 'K-' , 'p~-' ] ] |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/B2XMuMu_LambdastarMerge

|                 |                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                   |
| Inputs          | [ 'Phys/B2XMuMu_LambdastarSubMMM_Sel' , 'Phys/B2XMuMu_LambdastarSubMMP_Sel' , 'Phys/B2XMuMu_LambdastarSubMMZ_Sel' ] |
| DecayDescriptor | None                                                                                                                  |
| Output          | Phys/B2XMuMu_LambdastarMerge/Particles                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

SubstitutePID/B2XMuMu_LambdastarSub_Sel

|                 |                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                           |
| Inputs          | [ 'Phys/B2XMuMu_LambdastarMerge' ]                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                          |
| Output          | Phys/B2XMuMu_LambdastarSub_Sel/Particles                                                                                                                                      |
| Substitutions   | { 'rho(770)0 -\> K+ p~-' : 'Lambda(1520)~0' , 'rho(770)0 -\> p+ K+' : 'Lambda(1520)0' , 'rho(770)0 -\> p+ K-' : 'Lambda(1520)0' , 'rho(770)0 -\> p~- K-' : 'Lambda(1520)~0' } |

FilterDesktop/B2XMuMu_LambdastarFilter

|                 |                                         |
|-----------------|-----------------------------------------|
| Code            | (ABSID=='Lambda(1520)0')                |
| Inputs          | [ 'Phys/B2XMuMu_LambdastarSub_Sel' ]  |
| DecayDescriptor | None                                    |
| Output          | Phys/B2XMuMu_LambdastarFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0resolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0merged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_a1

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

DaVinci::N3BodyDecays/Selection_B2XMuMu_a1

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                           |
| CombinationCut   | (AM \> 0.0 \* MeV) &(AM \< 4200.0 \* MeV) & (ADOCACHI2CUT(20.,'')) &(AHASCHILD(MIPCHI2DV(PRIMARY) \> 16.0 ))             |
| MotherCut        | (M \> 0.0 \* MeV) &(M \< 4000.0 \* MeV) & (VFASPF(VCHI2PDOF) \< 8.0) & (BPVVDCHI2 \> 36.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ '[a_1(1260)+ -\> pi+ pi+ pi-]cc' ]                                                                                 |
| Output           | Phys/Selection_B2XMuMu_a1/Particles                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_K1_PickDecay

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

DaVinci::N3BodyDecays/Selection_B2XMuMu_a1

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                           |
| CombinationCut   | (AM \> 0.0 \* MeV) &(AM \< 4200.0 \* MeV) & (ADOCACHI2CUT(20.,'')) &(AHASCHILD(MIPCHI2DV(PRIMARY) \> 16.0 ))             |
| MotherCut        | (M \> 0.0 \* MeV) &(M \< 4000.0 \* MeV) & (VFASPF(VCHI2PDOF) \< 8.0) & (BPVVDCHI2 \> 36.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ '[a_1(1260)+ -\> pi+ pi+ pi-]cc' ]                                                                                 |
| Output           | Phys/Selection_B2XMuMu_a1/Particles                                                                                      |

SubstitutePID/B2XMuMu_a1k1_SubPIDAlg

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (DECTREE('a_1(1260)+ -\> pi+ pi+ pi-')) \| (DECTREE('a_1(1260)- -\> pi- pi- pi+'))            |
| Inputs          | [ 'Phys/Selection_B2XMuMu_a1' ]                                                             |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/B2XMuMu_a1k1_SubPIDAlg/Particles                                                         |
| Substitutions   | { 'a_1(1260)+ -\> pi+ pi+ pi-' : 'K_1(1270)+' , 'a_1(1260)- -\> pi- pi- pi+' : 'K_1(1270)-' } |

SubPIDMMFilter/B2XMuMu_a1k1_SubPIDAlgp

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | DECTREE('K_1(1270)+ -\> pi+ pi+ pi-')                         |
| Inputs          | [ 'Phys/B2XMuMu_a1k1_SubPIDAlg' ]                           |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2XMuMu_a1k1_SubPIDAlgp/Particles                        |
| MaxMM           | 4200.0000                                                     |
| MinMM           | 0.0000000                                                     |
| PIDs            | [ [ 'K+' , 'pi+' , 'pi-' ] , [ 'pi+' , 'K+' , 'pi-' ] ] |

SubPIDMMFilter/B2XMuMu_a1k1_SubPIDAlgm

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | DECTREE('K_1(1270)- -\> pi- pi- pi+')                         |
| Inputs          | [ 'Phys/B2XMuMu_a1k1_SubPIDAlg' ]                           |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2XMuMu_a1k1_SubPIDAlgm/Particles                        |
| MaxMM           | 4200.0000                                                     |
| MinMM           | 0.0000000                                                     |
| PIDs            | [ [ 'K-' , 'pi-' , 'pi+' ] , [ 'pi-' , 'K-' , 'pi+' ] ] |

FilterDesktop/B2XMuMu_K1_PickDecay

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | (DECTREE('K_1(1270)+ -\> K+ pi+ pi-')) \| (DECTREE('K_1(1270)- -\> pi+ K- pi-')) |
| Inputs          | [ 'Phys/B2XMuMu_a1k1_SubPIDAlgm' , 'Phys/B2XMuMu_a1k1_SubPIDAlgp' ]            |
| DecayDescriptor | None                                                                             |
| Output          | Phys/B2XMuMu_K1_PickDecay/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_K2_PickDecay

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

DaVinci::N3BodyDecays/Selection_B2XMuMu_a1

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                           |
| CombinationCut   | (AM \> 0.0 \* MeV) &(AM \< 4200.0 \* MeV) & (ADOCACHI2CUT(20.,'')) &(AHASCHILD(MIPCHI2DV(PRIMARY) \> 16.0 ))             |
| MotherCut        | (M \> 0.0 \* MeV) &(M \< 4000.0 \* MeV) & (VFASPF(VCHI2PDOF) \< 8.0) & (BPVVDCHI2 \> 36.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ '[a_1(1260)+ -\> pi+ pi+ pi-]cc' ]                                                                                 |
| Output           | Phys/Selection_B2XMuMu_a1/Particles                                                                                      |

SubstitutePID/B2XMuMu_a1k2_SubPIDAlg

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (DECTREE('a_1(1260)+ -\> pi+ pi+ pi-')) \| (DECTREE('a_1(1260)- -\> pi- pi- pi+'))            |
| Inputs          | [ 'Phys/Selection_B2XMuMu_a1' ]                                                             |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/B2XMuMu_a1k2_SubPIDAlg/Particles                                                         |
| Substitutions   | { 'a_1(1260)+ -\> pi+ pi+ pi-' : 'K_2(1770)+' , 'a_1(1260)- -\> pi- pi- pi+' : 'K_2(1770)-' } |

SubPIDMMFilter/B2XMuMu_a1k2_SubPIDAlgp

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | DECTREE('K_2(1770)+ -\> pi+ pi+ pi-')  |
| Inputs          | [ 'Phys/B2XMuMu_a1k2_SubPIDAlg' ]    |
| DecayDescriptor | None                                   |
| Output          | Phys/B2XMuMu_a1k2_SubPIDAlgp/Particles |
| MaxMM           | 4200.0000                              |
| MinMM           | 0.0000000                              |
| PIDs            | [ [ 'K+' , 'K+' , 'K-' ] ]         |

SubPIDMMFilter/B2XMuMu_a1k2_SubPIDAlgm

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | DECTREE('K_2(1770)- -\> pi- pi- pi+')  |
| Inputs          | [ 'Phys/B2XMuMu_a1k2_SubPIDAlg' ]    |
| DecayDescriptor | None                                   |
| Output          | Phys/B2XMuMu_a1k2_SubPIDAlgm/Particles |
| MaxMM           | 4200.0000                              |
| MinMM           | 0.0000000                              |
| PIDs            | [ [ 'K-' , 'K-' , 'K+' ] ]         |

FilterDesktop/B2XMuMu_K2_PickDecay

|                 |                                                                              |
|-----------------|------------------------------------------------------------------------------|
| Code            | (DECTREE('K_2(1770)+ -\> K- K+ K+')) \| (DECTREE('K_2(1770)- -\> K+ K- K-')) |
| Inputs          | [ 'Phys/B2XMuMu_a1k2_SubPIDAlgm' , 'Phys/B2XMuMu_a1k2_SubPIDAlgp' ]        |
| DecayDescriptor | None                                                                         |
| Output          | Phys/B2XMuMu_K2_PickDecay/Particles                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:B2XMuMu_K10_PickDecay

GaudiSequencer/MERGED:Selection_B2XMuMu_Kshort

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Kshort

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksdd

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksll

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksll

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)          |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Ksll/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

DaVinci::N3BodyDecays/Selection_B2XMuMu_k10

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Kshort' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                           |
| CombinationCut   | (AM \> 0.0 \* MeV) &(AM \< 4200.0 \* MeV) & (ADOCACHI2CUT(20.,'')) &(AHASCHILD(MIPCHI2DV(PRIMARY) \> 16.0 ))             |
| MotherCut        | (M \> 0.0 \* MeV) &(M \< 4000.0 \* MeV) & (VFASPF(VCHI2PDOF) \< 8.0) & (BPVVDCHI2 \> 36.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ 'K_1(1270)0 -\> pi+ pi- KS0' ]                                                                                       |
| Output           | Phys/Selection_B2XMuMu_k10/Particles                                                                                     |

FilterDesktop/B2XMuMu_K10_PickDecay

|                 |                                         |
|-----------------|-----------------------------------------|
| Code            | (DECTREE('K_1(1270)0 -\> KS0 pi+ pi-')) |
| Inputs          | [ 'Phys/Selection_B2XMuMu_k10' ]      |
| DecayDescriptor | None                                    |
| Output          | Phys/B2XMuMu_K10_PickDecay/Particles    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_k12omegak

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsKaons/Particles                                    |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0foromega

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0foromega

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegaresolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegaresolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0foromegaresolved/Particles                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegamerged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegamerged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0foromegamerged/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0foromega

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0foromegamerged' , 'Phys/Selection_B2XMuMu_pi0foromegaresolved' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0foromega/Particles                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/Selection_B2XMuMu_omega2pipipizero

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' , 'Phys/Selection_B2XMuMu_pi0foromega' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                          |
| CombinationCut   | (ADAMASS('omega(782)') \< 400 \* MeV)                                                   |
| MotherCut        | (ADMASS('omega(782)') \< 400 \*MeV) & (VFASPF(VPCHI2)\> 1e-05 )                         |
| DecayDescriptor  | omega(782) -\> pi+ pi- pi0                                                              |
| DecayDescriptors | [ 'omega(782) -\> pi+ pi- pi0' ]                                                      |
| Output           | Phys/Selection_B2XMuMu_omega2pipipizero/Particles                                       |

CombineParticles/Selection_B2XMuMu_k12omegak

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsKaons' , 'Phys/Selection_B2XMuMu_omega2pipipizero' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'omega(782)' : 'ALL' }                          |
| CombinationCut   | (AM \> 300 \* MeV) & (AM \< 2100 \* MeV)                                                     |
| MotherCut        | (M \> 400 \* MeV) & (M \< 2000 \* MeV) & (VFASPF(VCHI2PDOF) \< 8)                            |
| DecayDescriptor  | [K_1(1400)+ -\> K+ omega(782)]cc                                                           |
| DecayDescriptors | [ '[K_1(1400)+ -\> K+ omega(782)]cc' ]                                                   |
| Output           | Phys/Selection_B2XMuMu_k12omegak/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_k12omegaks

GaudiSequencer/MERGED:Selection_B2XMuMu_Kshort

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Kshort

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksdd

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)  |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_B2XMuMu_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Ksll

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Ksll

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.0\* MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)          |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Ksll/Particles                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0foromega

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0foromega

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegaresolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegaresolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0foromegaresolved/Particles                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegamerged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegamerged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0foromegamerged/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0foromega

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0foromegamerged' , 'Phys/Selection_B2XMuMu_pi0foromegaresolved' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0foromega/Particles                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/Selection_B2XMuMu_omega2pipipizero

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' , 'Phys/Selection_B2XMuMu_pi0foromega' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                          |
| CombinationCut   | (ADAMASS('omega(782)') \< 400 \* MeV)                                                   |
| MotherCut        | (ADMASS('omega(782)') \< 400 \*MeV) & (VFASPF(VPCHI2)\> 1e-05 )                         |
| DecayDescriptor  | omega(782) -\> pi+ pi- pi0                                                              |
| DecayDescriptors | [ 'omega(782) -\> pi+ pi- pi0' ]                                                      |
| Output           | Phys/Selection_B2XMuMu_omega2pipipizero/Particles                                       |

CombineParticles/Selection_B2XMuMu_k12omegaks

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Kshort' , 'Phys/Selection_B2XMuMu_omega2pipipizero' ] |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'omega(782)' : 'ALL' }                             |
| CombinationCut   | (AM \> 300 \* MeV) & (AM \< 2100 \* MeV)                                          |
| MotherCut        | (M \> 400 \* MeV) & (M \< 2000 \* MeV) & (VFASPF(VCHI2PDOF) \< 8)                 |
| DecayDescriptor  | K_1(1400)0 -\> KS0 omega(782)                                                     |
| DecayDescriptors | [ 'K_1(1400)0 -\> KS0 omega(782)' ]                                             |
| Output           | Phys/Selection_B2XMuMu_k12omegaks/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Xi

GaudiSequencer/MERGED:Selection_B2XMuMu_Xi

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Xi

GaudiSequencer/INPUT:Selection_B2XMuMu_XiLLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseLambdaLL

|      |                                        |
|------|----------------------------------------|
| Code | 0StdVeryLooseLambdaLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdall

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)              |
| Inputs          | [ 'Phys/[StdVeryLooseLambdaLL](./stripping21r1p2-commonparticles-stdverylooselambdall)' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Selection_B2XMuMu_Lambdall/Particles                                                   |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_LongXiPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_LongXiPions/Particles                                          |

CombineParticles/Selection_B2XMuMu_XiLLL

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Lambdall' , 'Phys/Selection_B2XMuMu_LongXiPions' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                 |
| CombinationCut   | (ADAMASS('Xi-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Xi-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                               |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                       |
| Output           | Phys/Selection_B2XMuMu_XiLLL/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_XiDDL

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdadd

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)      |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Lambdadd/Particles                                           |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_LongXiPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_LongXiPions/Particles                                          |

CombineParticles/Selection_B2XMuMu_XiDDL

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Lambdadd' , 'Phys/Selection_B2XMuMu_LongXiPions' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                 |
| CombinationCut   | (ADAMASS('Xi-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Xi-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                               |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                       |
| Output           | Phys/Selection_B2XMuMu_XiDDL/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_XiDDD

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdadd

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)      |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Lambdadd/Particles                                           |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsDownPions

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsDownPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_DownXiPions

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                              |
| Inputs          | [ 'Phys/[StdNoPIDsDownPions](./stripping21r1p2-commonparticles-stdnopidsdownpions)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Selection_B2XMuMu_DownXiPions/Particles                                            |

CombineParticles/Selection_B2XMuMu_XiDDD

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_DownXiPions' , 'Phys/Selection_B2XMuMu_Lambdadd' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                 |
| CombinationCut   | (ADAMASS('Xi-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Xi-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Xi- -\> Lambda0 pi-]cc                                                                               |
| DecayDescriptors | [ '[Xi- -\> Lambda0 pi-]cc' ]                                                                       |
| Output           | Phys/Selection_B2XMuMu_XiDDD/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_Xi

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                    |
| Inputs          | [ 'Phys/Selection_B2XMuMu_XiDDD' , 'Phys/Selection_B2XMuMu_XiDDL' , 'Phys/Selection_B2XMuMu_XiLLL' ] |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/Selection_B2XMuMu_Xi/Particles                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_Omega

GaudiSequencer/MERGED:Selection_B2XMuMu_Omega

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_Omega

GaudiSequencer/INPUT:Selection_B2XMuMu_OmegaLLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseLambdaLL

|      |                                        |
|------|----------------------------------------|
| Code | 0StdVeryLooseLambdaLL/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdall

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)              |
| Inputs          | [ 'Phys/[StdVeryLooseLambdaLL](./stripping21r1p2-commonparticles-stdverylooselambdall)' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/Selection_B2XMuMu_Lambdall/Particles                                                   |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_LongOmegaKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_LongOmegaKaons/Particles                                       |

CombineParticles/Selection_B2XMuMu_OmegaLLL

|                  |                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Lambdall' , 'Phys/Selection_B2XMuMu_LongOmegaKaons' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('Omega-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Omega-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                        |
| Output           | Phys/Selection_B2XMuMu_OmegaLLL/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_OmegaDDL

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdadd

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)      |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Lambdadd/Particles                                           |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_LongOmegaKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_LongOmegaKaons/Particles                                       |

CombineParticles/Selection_B2XMuMu_OmegaDDL

|                  |                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_Lambdadd' , 'Phys/Selection_B2XMuMu_LongOmegaKaons' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('Omega-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Omega-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                        |
| Output           | Phys/Selection_B2XMuMu_OmegaDDL/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_OmegaDDD

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

FilterDesktop/Selection_B2XMuMu_Lambdadd

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0') \< 30.0 \*MeV) & (PT \> 0.0 \*MeV) & (BPVLTIME() \> 2 \*ps)      |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Selection_B2XMuMu_Lambdadd/Particles                                           |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsDownKaons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsDownKaons/Particles',True) |

FilterDesktop/Selection_B2XMuMu_DownOmegaKaons

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5)&(MIPCHI2DV(PRIMARY) \> 6.0)                                              |
| Inputs          | [ 'Phys/[StdNoPIDsDownKaons](./stripping21r1p2-commonparticles-stdnopidsdownkaons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Selection_B2XMuMu_DownOmegaKaons/Particles                                         |

CombineParticles/Selection_B2XMuMu_OmegaDDD

|                  |                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_DownOmegaKaons' , 'Phys/Selection_B2XMuMu_Lambdadd' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('Omega-') \< 65.0 \* MeV) & (ADOCACHI2CUT(20.0, ''))                                              |
| MotherCut        | (PT \> 0.0 \* MeV) & (ADMASS('Omega-') \< 50.0 \* MeV) & (VFASPF(VCHI2) \< 20.0) & (BPVLTIME() \> 2 \* ps) |
| DecayDescriptor  | [Omega- -\> Lambda0 K-]cc                                                                                |
| DecayDescriptors | [ '[Omega- -\> Lambda0 K-]cc' ]                                                                        |
| Output           | Phys/Selection_B2XMuMu_OmegaDDD/Particles                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_Omega

|                 |                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_OmegaDDD' , 'Phys/Selection_B2XMuMu_OmegaDDL' , 'Phys/Selection_B2XMuMu_OmegaLLL' ] |
| DecayDescriptor | None                                                                                                            |
| Output          | Phys/Selection_B2XMuMu_Omega/Particles                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_f1

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

DaVinci::N4BodyDecays/Selection_B2XMuMu_f1

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' ]                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                           |
| CombinationCut   | (AM \> 0.0 \* MeV) &(AM \< 4200.0 \* MeV) & (ADOCACHI2CUT(20.,'')) &(AHASCHILD(MIPCHI2DV(PRIMARY) \> 16.0 ))             |
| MotherCut        | (M \> 0.0 \* MeV) &(M \< 4000.0 \* MeV) & (VFASPF(VCHI2PDOF) \< 8.0) & (BPVVDCHI2 \> 36.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ 'f_1(1285) -\> pi+ pi- pi+ pi-' ]                                                                                    |
| Output           | Phys/Selection_B2XMuMu_f1/Particles                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_omega2pipipizero

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Selection_B2XMuMu_StdAllNoPIDsPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (TRGHP \< 0.5) & (MIPCHI2DV(PRIMARY) \> 6.0) & (HASRICH)                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_StdAllNoPIDsPions/Particles                                    |

GaudiSequencer/MERGED:Selection_B2XMuMu_pi0foromega

GaudiSequencer/MERGEDINPUTS:Selection_B2XMuMu_pi0foromega

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegaresolved

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegaresolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                            |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_B2XMuMu_pi0foromegaresolved/Particles                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Selection_B2XMuMu_pi0foromegamerged

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

FilterDesktop/Selection_B2XMuMu_pi0foromegamerged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT \> 800.0 )                                                                        |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_B2XMuMu_pi0foromegamerged/Particles                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_pi0foromega

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                             |
| Inputs          | [ 'Phys/Selection_B2XMuMu_pi0foromegamerged' , 'Phys/Selection_B2XMuMu_pi0foromegaresolved' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/Selection_B2XMuMu_pi0foromega/Particles                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/Selection_B2XMuMu_omega2pipipizero

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' , 'Phys/Selection_B2XMuMu_pi0foromega' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                          |
| CombinationCut   | (ADAMASS('omega(782)') \< 400 \* MeV)                                                   |
| MotherCut        | (ADMASS('omega(782)') \< 400 \*MeV) & (VFASPF(VPCHI2)\> 1e-05 )                         |
| DecayDescriptor  | omega(782) -\> pi+ pi- pi0                                                              |
| DecayDescriptors | [ 'omega(782) -\> pi+ pi- pi0' ]                                                      |
| Output           | Phys/Selection_B2XMuMu_omega2pipipizero/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_B2XMuMu_daughters

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Inputs          | [ 'Phys/B2XMuMu_F2Filter' , 'Phys/B2XMuMu_K10_PickDecay' , 'Phys/B2XMuMu_K1_PickDecay' , 'Phys/B2XMuMu_K2_PickDecay' , 'Phys/B2XMuMu_KstarFilter' , 'Phys/B2XMuMu_LambdastarFilter' , 'Phys/B2XMuMu_PhiFilter' , 'Phys/Selection_B2XMuMu_Kshort' , 'Phys/Selection_B2XMuMu_Kstar2kpizero' , 'Phys/Selection_B2XMuMu_Kstar2kspi' , 'Phys/Selection_B2XMuMu_Lambda' , 'Phys/Selection_B2XMuMu_Omega' , 'Phys/Selection_B2XMuMu_Rho' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsKaons' , 'Phys/Selection_B2XMuMu_StdAllNoPIDsPions' , 'Phys/Selection_B2XMuMu_Xi' , 'Phys/Selection_B2XMuMu_a1' , 'Phys/Selection_B2XMuMu_dzero' , 'Phys/Selection_B2XMuMu_f1' , 'Phys/Selection_B2XMuMu_k12omegak' , 'Phys/Selection_B2XMuMu_k12omegaks' , 'Phys/Selection_B2XMuMu_omega2pipipizero' , 'Phys/Selection_B2XMuMu_pi0' , 'Phys/Selection_B2XMuMu_rho2pipizero' , 'Phys/[StdLooseDplus2hhh](./stripping21r1p2-commonparticles-stdloosedplus2hhh)' , 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1p2-commonparticles-stdloosedstarwithd02kpi)' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output          | Phys/Selection_B2XMuMu_daughters/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/B2XMuMu_Line

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Sel_B2XMuMu_DiMuon' , 'Phys/Selection_B2XMuMu_daughters' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'K_1(1270)0' : 'ALL' , 'K_1(1270)~0' : 'ALL' , 'K_1(1400)+' : 'ALL' , 'K_1(1400)-' : 'ALL' , 'K_1(1400)0' : 'ALL' , 'K_1(1400)~0' : 'ALL' , 'K_2(1770)+' : 'ALL' , 'K_2(1770)-' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'Omega-' : 'ALL' , 'Omega~+' : 'ALL' , 'Xi-' : 'ALL' , 'Xi~+' : 'ALL' , 'a_1(1260)+' : 'ALL' , 'a_1(1260)-' : 'ALL' , 'f_1(1285)' : 'ALL' , 'f_2(1950)' : 'ALL' , 'omega(782)' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' , 'rho(770)0' : 'ALL' } |
| CombinationCut   | (AM \> 4600.0 \* MeV) & (AM \< 7100.0 \* MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (abs(SUMQ) \< 3) & (M \> 4700.0 \* MeV) & (M \< 7000.0 \* MeV) & (VFASPF(VCHI2/VDOF) \< 8.0) & (BPVIPCHI2() \< 16.0) & (BPVDIRA\> 0.9999) & (BPVVDCHI2 \> 64.0) & (MAXTREE(ISBASIC,MIPCHI2DV(PRIMARY))\> 9.0 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) phi(1020)' , '[B0 -\> J/psi(1S) K\*(892)0]cc' , 'B0 -\> J/psi(1S) rho(770)0' , '[B+ -\> J/psi(1S) rho(770)+]cc' , 'B0 -\> J/psi(1S) f_2(1950)' , 'B0 -\> J/psi(1S) KS0' , '[B0 -\> J/psi(1S) D~0]cc' , '[B+ -\> J/psi(1S) K+]cc' , '[B+ -\> J/psi(1S) pi+]cc' , '[B+ -\> J/psi(1S) K\*(892)+]cc' , '[B+ -\> J/psi(1S) D+]cc' , '[B+ -\> J/psi(1S) D\*(2010)+]cc' , '[Lambda_b0 -\> J/psi(1S) Lambda0]cc' , '[Lambda_b0 -\> J/psi(1S) Lambda(1520)0]cc' , 'B0 -\> J/psi(1S) pi0' , '[B+ -\> J/psi(1S) a_1(1260)+]cc' , '[B+ -\> J/psi(1S) K_1(1270)+]cc' , '[B+ -\> J/psi(1S) K_2(1770)+]cc' , 'B0 -\> J/psi(1S) K_1(1270)0' , '[B+ -\> J/psi(1S) K_1(1400)+]cc' , 'B0 -\> J/psi(1S) K_1(1400)0' , '[Xi_b- -\> J/psi(1S) Xi-]cc' , '[Omega_b- -\> J/psi(1S) Omega-]cc' , 'B0 -\> J/psi(1S) f_1(1285)' , 'B0 -\> J/psi(1S) omega(782)' ]                                                                  |
| Output           | Phys/B2XMuMu_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

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

AddRelatedInfo/RelatedInfo5_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo5_B2XMuMu_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XMuMu_Line

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B2XMuMu_Line' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo6_B2XMuMu_Line/Particles |
