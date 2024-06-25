[[stripping21 lines]](./stripping21-index)

# StrippingB2KpiX2EEDarkBosonLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2KpiX2EEDarkBosonLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**LoKi::VoidFilter/StrippingB2KpiX2EEDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21-stddielectronfromtracks) /Particles')\>0 |

**FilterDesktop/OSFilterEEDarkBosonFilter**

|                 |                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 250\*MeV) & (MINTREE('e+'==ABSID,PIDe) \> 0) & (MINTREE('e+'==ABSID,MIPCHI2DV(PRIMARY)) \> 9) & (MINTREE('e+'==ABSID,PT) \> 100\*MeV) & (MAXTREE('e+'==ABSID,TRGHP) \< 0.4) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21-stddielectronfromtracks) ' ]                                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                                            |
| Output          | Phys/OSFilterEEDarkBosonFilter/Particles                                                                                                                                                                                        |

**SubstitutePID/OSEESubPIDDarkBosonSel**

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | DECTREE('J/psi(1S) -\> e+ e-')         |
| Inputs          | [ 'Phys/OSFilterEEDarkBosonFilter' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/OSEESubPIDDarkBosonSel/Particles  |
| Substitutions   | { 'J/psi(1S) -\> e+ e-' : 'KS0' }      |

****Tools:****

**SubstitutePIDTool**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Substitutions :          | { 'J/psi(1S) -\> e+ e-' : 'KS0' }                                                                         |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) ' ]                                        |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                           |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PiBDarkBosonFilter**

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ]                                         |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                           |

**CombineParticles/B2KpiX2EEDarkBosonLine**

|                  |                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/OSEESubPIDDarkBosonSel' , 'Phys/PiBDarkBosonFilter' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                              |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                        |
| DecayDescriptors | [ '[B0 -\> K+ pi- KS0]cc' ]                                                                                                                                                                             |
| Output           | Phys/B2KpiX2EEDarkBosonLine/Particles                                                                                                                                                                       |
