[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2KKX2MuMuDDDarkBosonLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/B2KKX2MuMuDDDarkBosonLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingB2KKX2MuMuDDDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDownMuons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDownMuons](./stripping21r1-commonparticles-stdloosedownmuons)/Particles')\>0 |

FilterDesktop/MuDXDarkBosonFilter

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (PIDmu\>-5) & (TRCHI2DOF\<3) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>100\*MeV) |
| Inputs          | [ 'Phys/[StdLooseDownMuons](./stripping21r1-commonparticles-stdloosedownmuons)' ]                  |
| DecayDescriptor | None                                                                                                 |
| Output          | Phys/MuDXDarkBosonFilter/Particles                                                                   |

CombineParticles/X2MuMuDDDarkBosonSel

|                  |                                                             |
|------------------|-------------------------------------------------------------|
| Inputs           | [ 'Phys/MuDXDarkBosonFilter' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }              |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 0\*MeV)& (ADOCACHI2CUT(25,''))  |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<25) |
| DecayDescriptor  | None                                                        |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                     |
| Output           | Phys/X2MuMuDDDarkBosonSel/Particles                         |

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

CombineParticles/B2KKX2MuMuDDDarkBosonLine

|                  |                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/X2MuMuDDDarkBosonSel' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                              |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                        |
| DecayDescriptors | [ 'B0 -\> K+ K- KS0' ]                                                                                                                                                                                    |
| Output           | Phys/B2KKX2MuMuDDDarkBosonLine/Particles                                                                                                                                                                    |
