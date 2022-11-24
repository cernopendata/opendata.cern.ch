[[stripping21 lines]](./stripping21-index)

# StrippingB2JKstDarkBosonLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2JKstDarkBosonLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingB2JKstDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/MuJDarkBosonFilter**

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (PIDmu\>-4) & (TRCHI2DOF\<4) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>125\*MeV) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ]                                     |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/MuJDarkBosonFilter/Particles                                                                     |

**CombineParticles/J2MuMuDarkBosonSel**

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuJDarkBosonFilter' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                     |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 100\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,'')) |
| MotherCut        | (BPVDIRA \> 0) & (VFASPF(VCHI2/VDOF)\<12)                                          |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                      |
| Output           | Phys/J2MuMuDarkBosonSel/Particles                                                  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedKst2Kpi_Particles**

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDetachedKst2Kpi](./stripping21-stdloosedetachedkst2kpi) /Particles')\>0 |

**FilterDesktop/KstDarkBosonFilter**

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 25)                                                      |
| Inputs          | [ 'Phys/ [StdLooseDetachedKst2Kpi](./stripping21-stdloosedetachedkst2kpi) ' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/KstDarkBosonFilter/Particles                                               |

**CombineParticles/B2JKstDarkBosonLine**

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/J2MuMuDarkBosonSel' , 'Phys/KstDarkBosonFilter' ]                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }                                                                                                                           |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                               |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                                                                                                                                                     |
| Output           | Phys/B2JKstDarkBosonLine/Particles                                                                                                                                                                           |
