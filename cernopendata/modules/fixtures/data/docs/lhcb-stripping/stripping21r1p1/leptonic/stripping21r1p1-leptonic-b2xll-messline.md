[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2XLL_meSSLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/B2XLL_meSSLine/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XLL_meSSLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseElectrons](./stripping21r1p1-commonparticles-stdlooseelectrons)/Particles',True)\>0 |

CombineParticles/MuESSForB2XLL

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseElectrons](./stripping21r1p1-commonparticles-stdlooseelectrons)' , 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNpi\<0.95) & (PROBNNe\>0.05)' , 'e-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNpi\<0.95) & (PROBNNe\>0.05)' , 'mu+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNpi\<0.95) & (HASMUON) & (ISMUON) & (PROBNNmu\>0.05)' , 'mu-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNpi\<0.95) & (HASMUON) & (ISMUON) & (PROBNNmu\>0.05)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | [J/psi(1S) -\> mu+ e+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ e+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/MuESSForB2XLL/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

FilterDesktop/SelMuESSForB2XLL

|                 |                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT)\>300 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY))\>9) & (VFASPF(VCHI2/VDOF)\<9) & (BPVVDCHI2\> 16) & (MIPCHI2DV(PRIMARY) \> 0 ) |
| Inputs          | [ 'Phys/MuESSForB2XLL' ]                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                 |
| Output          | Phys/SelMuESSForB2XLL/Particles                                                                                                                                                                                      |

GaudiSequencer/SeqMergeB2XLL_meSS

GaudiSequencer/SEQ:KaonsForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNk \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/KaonsForB2XLL/Particles                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PionsForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KstarsForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKstar2Kpi](./stripping21r1p1-commonparticles-stdloosekstar2kpi)/Particles',True)\>0 |

FilterDesktop/KstarsForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21r1p1-commonparticles-stdloosekstar2kpi)' ]                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KstarsForB2XLL/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:RhosForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseRho0_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseRho0](./stripping21r1p1-commonparticles-stdlooserho0)/Particles',True)\>0 |

FilterDesktop/RhosForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLooseRho0](./stripping21r1p1-commonparticles-stdlooserho0)' ]                                                                    |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/RhosForB2XLL/Particles                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PhisForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21r1p1-commonparticles-stdloosephi2kk)/Particles',True)\>0 |

FilterDesktop/PhisForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1p1-commonparticles-stdloosephi2kk)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForB2XLL/Particles                                                                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:JPsisForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseJpsi2MuMu_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseJpsi2MuMu](./stripping21r1p1-commonparticles-stdloosejpsi2mumu)/Particles',True)\>0 |

FilterDesktop/JPsisForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 3200\*MeV) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r1p1-commonparticles-stdloosejpsi2mumu)' ]                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/JPsisForB2XLL/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:ProtonsForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/ProtonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNp \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/ProtonsForB2XLL/Particles                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DZerosForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21r1p1-commonparticles-stdloosed02kpi)/Particles',True)\>0 |

FilterDesktop/DZerosForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21r1p1-commonparticles-stdloosed02kpi)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/DZerosForB2XLL/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DPlusForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2hhh_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2hhh](./stripping21r1p1-commonparticles-stdloosedplus2hhh)/Particles',True)\>0 |

FilterDesktop/DPlusForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLooseDplus2hhh](./stripping21r1p1-commonparticles-stdloosedplus2hhh)' ]                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/DPlusForB2XLL/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DStarsForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21r1p1-commonparticles-stdloosedstarwithd02kpi)/Particles',True)\>0 |

FilterDesktop/DStarsForB2XLL

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1p1-commonparticles-stdloosedstarwithd02kpi)' ]                                              |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/DStarsForB2XLL/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_OmegasForB2XLL_omega2pipipizero

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

GaudiSequencer/SeqSelection_PiZeros_pi0

GaudiSequencer/SEQ:Selection_PiZeros_pi0resolved

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_PiZeros_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | PT\>800\*MeV                                                                              |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_PiZeros_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_PiZeros_pi0merged

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_PiZeros_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | PT\>800\*MeV                                                                          |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_PiZeros_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_PiZeros_pi0

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Selection_PiZeros_pi0merged' , 'Phys/Selection_PiZeros_pi0resolved' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Selection_PiZeros_pi0/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Selection_OmegasForB2XLL_omega2pipipizero

|                  |                                                                  |
|------------------|------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForB2XLL' , 'Phys/Selection_PiZeros_pi0' ]        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }   |
| CombinationCut   | (ADAMASS('omega(782)') \< 200 \*MeV)                             |
| MotherCut        | (ADMASS('omega(782)') \< 200 \*MeV) & (VFASPF(VPCHI2)\> 0.00001) |
| DecayDescriptor  | omega(782) -\> pi+ pi- pi0                                       |
| DecayDescriptors | [ 'omega(782) -\> pi+ pi- pi0' ]                               |
| Output           | Phys/Selection_OmegasForB2XLL_omega2pipipizero/Particles         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelectionOff0Forf0(980)sForB2XLL

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

CombineParticles/SelectionOff0Forf0(980)sForB2XLL

|                  |                                                 |
|------------------|-------------------------------------------------|
| Inputs           | [ 'Phys/PionsForB2XLL' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }  |
| CombinationCut   | (AM\<2700.0\*MeV)                               |
| MotherCut        | (M\<2700.0\*MeV)                                |
| DecayDescriptor  | f_0(980) -\> pi+ pi-                            |
| DecayDescriptors | [ 'f_0(980) -\> pi+ pi-' ]                    |
| Output           | Phys/SelectionOff0Forf0(980)sForB2XLL/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SeqKStarPlusForB2XLL

GaudiSequencer/SEQ:Selection_KStarPlus1ForB2XLL_Kstar2kaonpion

GaudiSequencer/SeqSelection_KShorts_Kshort

GaudiSequencer/SEQ:Selection_KShorts_Ksdd

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/Selection_KShorts_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50\*MeV) & (BPVLTIME() \> 0.5\*ps)                        |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_KShorts_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_KShorts_Ksll

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/Selection_KShorts_Ksll

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50\*MeV) & (BPVLTIME() \> 0.5\*ps)                        |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_KShorts_Ksll/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_KShorts_Kshort

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ALL                                                                 |
| Inputs          | [ 'Phys/Selection_KShorts_Ksdd' , 'Phys/Selection_KShorts_Ksll' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/Selection_KShorts_Kshort/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

CombineParticles/Selection_KStarPlus1ForB2XLL_Kstar2kaonpion

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForB2XLL' , 'Phys/Selection_KShorts_Kshort' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                                        |
| MotherCut        | (ADMASS('K\*(892)+') \< 300 \*MeV)                                                                           |
| DecayDescriptor  | None                                                                                                         |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' , '[K\*(892)+ -\> KS0 pi+]cc' ]                                           |
| Output           | Phys/Selection_KStarPlus1ForB2XLL_Kstar2kaonpion/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_KStarPlus2ForB2XLL_Kstar2kaonpion

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNk \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/KaonsForB2XLL/Particles                                                                                                                                                                                                  |

GaudiSequencer/SeqSelection_PiZeros_pi0

GaudiSequencer/SEQ:Selection_PiZeros_pi0resolved

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_PiZeros_pi0resolved

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | PT\>800\*MeV                                                                              |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Selection_PiZeros_pi0resolved/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_PiZeros_pi0merged

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

FilterDesktop/Selection_PiZeros_pi0merged

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | PT\>800\*MeV                                                                          |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Selection_PiZeros_pi0merged/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_PiZeros_pi0

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Selection_PiZeros_pi0merged' , 'Phys/Selection_PiZeros_pi0resolved' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Selection_PiZeros_pi0/Particles                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Selection_KStarPlus2ForB2XLL_Kstar2kaonpion

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2XLL' , 'Phys/Selection_PiZeros_pi0' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' } |
| CombinationCut   | ATRUE                                                                                                        |
| MotherCut        | (ADMASS('K\*(892)+') \< 300 \*MeV)                                                                           |
| DecayDescriptor  | None                                                                                                         |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' , '[K\*(892)+ -\> KS0 pi+]cc' ]                                           |
| Output           | Phys/Selection_KStarPlus2ForB2XLL_Kstar2kaonpion/Particles                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/KStarPlusForB2XLL

|                 |                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                           |
| Inputs          | [ 'Phys/Selection_KStarPlus1ForB2XLL_Kstar2kaonpion' , 'Phys/Selection_KStarPlus2ForB2XLL_Kstar2kaonpion' ] |
| DecayDescriptor | None                                                                                                          |
| Output          | Phys/KStarPlusForB2XLL/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_DsPlusForB2XLL_DsPlus

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNk \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/KaonsForB2XLL/Particles                                                                                                                                                                                                  |

CombineParticles/Selection_DsPlusForB2XLL_DsPlus

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2XLL' , 'Phys/PionsForB2XLL' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                        |
| MotherCut        | (ADMASS('D_s+') \< 300 \*MeV)                                                |
| DecayDescriptor  | [D_s+ -\> K+ K- pi+]cc                                                     |
| DecayDescriptors | [ '[D_s+ -\> K+ K- pi+]cc' ]                                             |
| Output           | Phys/Selection_DsPlusForB2XLL_DsPlus/Particles                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_DsStarForB2XLL_DsStar

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNk \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/KaonsForB2XLL/Particles                                                                                                                                                                                                  |

CombineParticles/Selection_DsPlusForB2XLL_DsPlus

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2XLL' , 'Phys/PionsForB2XLL' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                        |
| MotherCut        | (ADMASS('D_s+') \< 300 \*MeV)                                                |
| DecayDescriptor  | [D_s+ -\> K+ K- pi+]cc                                                     |
| DecayDescriptors | [ '[D_s+ -\> K+ K- pi+]cc' ]                                             |
| Output           | Phys/Selection_DsPlusForB2XLL_DsPlus/Particles                               |

LoKi::VoidFilter/SelFilterPhys_StdLoosePhotons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhotons](./stripping21r1p1-commonparticles-stdloosephotons)/Particles',True)\>0 |

CombineParticles/Selection_DsStarForB2XLL_DsStar

|                  |                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Selection_DsPlusForB2XLL_DsPlus' , 'Phys/[StdLoosePhotons](./stripping21r1p1-commonparticles-stdloosephotons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'gamma' : '(CL \> 0.25)' }                                                |
| CombinationCut   | ATRUE                                                                                                                      |
| MotherCut        | (ADMASS('D\*\_s+') \< 300 \*MeV)                                                                                           |
| DecayDescriptor  | [D\*\_s+ -\> D_s+ gamma]cc                                                                                               |
| DecayDescriptors | [ '[D\*\_s+ -\> D_s+ gamma]cc' ]                                                                                       |
| Output           | Phys/Selection_DsStarForB2XLL_DsStar/Particles                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_KpipiForB2XLL_kpipi

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForB2XLL

|                 |                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) & (PROBNNk \> 0.05) & (PROBNNpi \< 0.95) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                          |
| Output          | Phys/KaonsForB2XLL/Particles                                                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

CombineParticles/Selection_KpipiForB2XLL_kpipi

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2XLL' , 'Phys/PionsForB2XLL' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                                        |
| MotherCut        | in_range(500\*MeV, M, 3000\*MeV) & ( VFASPF(VCHI2PDOF) \< 36 )               |
| DecayDescriptor  | None                                                                         |
| DecayDescriptors | [ '[K_1(1270)+ -\> K+ pi- pi+]cc' ]                                      |
| Output           | Phys/Selection_KpipiForB2XLL_kpipi/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_KSpipiForB2XLL_kspipi

GaudiSequencer/SeqSelection_KShorts_Kshort

GaudiSequencer/SEQ:Selection_KShorts_Ksdd

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/Selection_KShorts_Ksdd

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50\*MeV) & (BPVLTIME() \> 0.5\*ps)                        |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_KShorts_Ksdd/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:Selection_KShorts_Ksll

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/Selection_KShorts_Ksll

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50\*MeV) & (BPVLTIME() \> 0.5\*ps)                        |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/Selection_KShorts_Ksll/Particles                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Selection_KShorts_Kshort

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ALL                                                                 |
| Inputs          | [ 'Phys/Selection_KShorts_Ksdd' , 'Phys/Selection_KShorts_Ksll' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/Selection_KShorts_Kshort/Particles                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForB2XLL

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))))& (M \< 2600\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF\<4) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/PionsForB2XLL/Particles                                                                                                                                                         |

CombineParticles/Selection_KSpipiForB2XLL_kspipi

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForB2XLL' , 'Phys/Selection_KShorts_Kshort' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                                          |
| MotherCut        | in_range(500\*MeV, M, 3000\*MeV) & ( VFASPF(VCHI2PDOF) \< 36 ) |
| DecayDescriptor  | None                                                           |
| DecayDescriptors | [ 'K_1(1270)0 -\> KS0 pi- pi+' ]                             |
| Output           | Phys/Selection_KSpipiForB2XLL_kspipi/Particles                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergeB2XLL_meSS

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Inputs          | [ 'Phys/DPlusForB2XLL' , 'Phys/DStarsForB2XLL' , 'Phys/DZerosForB2XLL' , 'Phys/JPsisForB2XLL' , 'Phys/KStarPlusForB2XLL' , 'Phys/KaonsForB2XLL' , 'Phys/KstarsForB2XLL' , 'Phys/PhisForB2XLL' , 'Phys/PionsForB2XLL' , 'Phys/ProtonsForB2XLL' , 'Phys/RhosForB2XLL' , 'Phys/SelectionOff0Forf0(980)sForB2XLL' , 'Phys/Selection_DsPlusForB2XLL_DsPlus' , 'Phys/Selection_DsStarForB2XLL_DsStar' , 'Phys/Selection_KSpipiForB2XLL_kspipi' , 'Phys/Selection_KpipiForB2XLL_kpipi' , 'Phys/Selection_OmegasForB2XLL_omega2pipipizero' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output          | Phys/MergeB2XLL_meSS/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2XLL_meSSLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeB2XLL_meSS' , 'Phys/SelMuESSForB2XLL' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D\*\_s+' : 'ALL' , 'D\*\_s-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'K_1(1270)0' : 'ALL' , 'K_1(1270)~0' : 'ALL' , 'f_0(980)' : 'ALL' , 'omega(782)' : 'ALL' , 'p+' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'psi(2S)' : 'ALL' , 'p~-' : 'ALL' , 'rho(770)0' : 'ALL' }          |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MotherCut        | ((VFASPF(VCHI2/VDOF)\< 9 ) & (BPVIPCHI2()\< 25 ) & (BPVDIRA\> 0.9995 ) & (BPVVDCHI2\> 100 ))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) pi+ ]cc' , '[ B+ -\> J/psi(1S) p+ ]cc' , '[ B+ -\> J/psi(1S) D+ ]cc' , '[ B+ -\> J/psi(1S) D\*(2010)+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , '[ B+ -\> J/psi(1S) D_s+ ]cc' , '[ B+ -\> J/psi(1S) D\*\_s+ ]cc' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B0 -\> J/psi(1S) D0 ]cc' , '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , 'B0 -\> J/psi(1S) phi(1020)' , 'B0 -\> J/psi(1S) rho(770)0' , 'B0 -\> J/psi(1S) J/psi(1S)' , 'B0 -\> J/psi(1S) psi(2S)' , 'B0 -\> J/psi(1S) omega(782)' , 'B0 -\> J/psi(1S) f_0(980)' , 'B0 -\> J/psi(1S) K_1(1270)0' ] |
| Output           | Phys/B2XLL_meSSLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

AddRelatedInfo/RelatedInfo1_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_B2XLL_meSSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_B2XLL_meSSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_B2XLL_meSSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_B2XLL_meSSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_B2XLL_meSSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XLL_meSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/B2XLL_meSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_B2XLL_meSSLine/Particles |
