[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2KX2KKDarkBosonLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2KX2KKDarkBosonLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

**LoKi::VoidFilter/StrippingB2KX2KKDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KXDarkBosonFilter**

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>3000\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) ' ]                                       |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/KXDarkBosonFilter/Particles                                                                            |

**CombineParticles/X2KKDarkBosonSel**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KXDarkBosonFilter' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                          |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 250\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,'')) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10)                           |
| DecayDescriptor  | None                                                                                  |
| DecayDescriptors | [ 'KS0 -\> K+ K-' ]                                                                 |
| Output           | Phys/X2KKDarkBosonSel/Particles                                                       |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) ' ]                                      |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                           |

**CombineParticles/B2KX2KKDarkBosonLine**

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/X2KKDarkBosonSel' ]                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                 |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                               |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B+ -\> K+ KS0]cc' ]                                                                                                                                                                                  |
| Output           | Phys/B2KX2KKDarkBosonLine/Particles                                                                                                                                                                          |
