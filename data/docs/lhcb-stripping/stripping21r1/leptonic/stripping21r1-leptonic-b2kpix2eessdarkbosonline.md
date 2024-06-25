[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2KpiX2EESSDarkBosonLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2KpiX2EESSDarkBosonLine/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 0.10000000                              |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingB2KpiX2EESSDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

DiElectronMaker/EESSDarkBosonSel

|                 |                                 |
|-----------------|---------------------------------|
| Inputs          | [ 'Rec/ProtoP/Charged' ]      |
| DecayDescriptor | J/psi(1S)                       |
| Output          | Phys/EESSDarkBosonSel/Particles |

FilterDesktop/SSFilterEEDarkBosonFilter

|                 |                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 250\*MeV) & (MINTREE('e+'==ABSID,PIDe) \> 0) & (MINTREE('e+'==ABSID,MIPCHI2DV(PRIMARY)) \> 9) & (MINTREE('e+'==ABSID,PT) \> 100\*MeV) & (MAXTREE('e+'==ABSID,TRGHP) \< 0.4) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10) |
| Inputs          | [ 'Phys/EESSDarkBosonSel' ]                                                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                            |
| Output          | Phys/SSFilterEEDarkBosonFilter/Particles                                                                                                                                                                                        |

SubstitutePID/SSEESubPIDDarkBosonSel

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | DECTREE('J/psi(1S) -\> e+ e-')         |
| Inputs          | [ 'Phys/SSFilterEEDarkBosonFilter' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/SSEESubPIDDarkBosonSel/Particles  |
| Substitutions   | { 'J/psi(1S) -\> e+ e-' : 'KS0' }      |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KBDarkBosonFilter

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]                        |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiBDarkBosonFilter

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                         |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                           |

CombineParticles/B2KpiX2EESSDarkBosonLine

|                  |                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' , 'Phys/SSEESubPIDDarkBosonSel' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                              |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                        |
| DecayDescriptors | [ '[B0 -\> K+ pi- KS0]cc' ]                                                                                                                                                                             |
| Output           | Phys/B2KpiX2EESSDarkBosonLine/Particles                                                                                                                                                                     |
