[[stripping21 lines]](./stripping21-index)

# StrippingB2KX2PiPiDarkBosonLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2KX2PiPiDarkBosonLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**LoKi::VoidFilter/StrippingB2KX2PiPiDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PiXDarkBosonFilter**

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>3000\*MeV) & (MIPCHI2DV(PRIMARY)\>36) & (PT\>250\*MeV) & (PROBNNpi\>0.6) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ]                                          |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/PiXDarkBosonFilter/Particles                                                                            |

**CombineParticles/X2PiPiDarkBosonSel**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiXDarkBosonFilter' ]                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                        |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 250\*MeV) & (ACUTDOCA(0.2\*mm,''))& (ADOCACHI2CUT(25,'')) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<5)                            |
| DecayDescriptor  | None                                                                                  |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                               |
| Output           | Phys/X2PiPiDarkBosonSel/Particles                                                     |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KBhardDarkBosonFilter**

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNK\>0.2) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>3000\*MeV) & (MIPCHI2DV(PRIMARY)\>36) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) ' ]                                         |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/KBhardDarkBosonFilter/Particles                                                                        |

**CombineParticles/B2KX2PiPiDarkBosonLine**

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBhardDarkBosonFilter' , 'Phys/X2PiPiDarkBosonSel' ]                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                 |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                               |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B+ -\> K+ KS0]cc' ]                                                                                                                                                                                  |
| Output           | Phys/B2KX2PiPiDarkBosonLine/Particles                                                                                                                                                                        |
