[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2JKDarkBosonLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/B2JKDarkBosonLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

**LoKi::VoidFilter/StrippingB2JKDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/MuJDarkBosonFilter**

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (PIDmu\>-4) & (TRCHI2DOF\<4) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>125\*MeV) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                   |
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

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) ' ]                                      |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                           |

**CombineParticles/B2JKDarkBosonLine**

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/J2MuMuDarkBosonSel' , 'Phys/KBDarkBosonFilter' ]                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                           |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                               |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                                                                                                                            |
| Output           | Phys/B2JKDarkBosonLine/Particles                                                                                                                                                                             |
