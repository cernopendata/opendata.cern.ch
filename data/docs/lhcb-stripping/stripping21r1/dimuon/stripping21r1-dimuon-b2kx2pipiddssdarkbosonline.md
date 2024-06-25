[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2KX2PiPiDDSSDarkBosonLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/B2KX2PiPiDDSSDarkBosonLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingB2KX2PiPiDDSSDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)/Particles')\>0 |

FilterDesktop/PiDXDarkBosonFilter

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (TRCHI2DOF\<4) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>25) & (PT\>125\*MeV) & (PROBNNpi\>0.1) |
| Inputs          | [ 'Phys/[StdNoPIDsDownPions](./stripping21r1-commonparticles-stdnopidsdownpions)' ]                     |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/PiDXDarkBosonFilter/Particles                                                                        |

CombineParticles/X2PiPiSSDDDarkBosonSel

|                  |                                                             |
|------------------|-------------------------------------------------------------|
| Inputs           | [ 'Phys/PiDXDarkBosonFilter' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }              |
| CombinationCut   | (AM \< 5000\*MeV) & (APT \> 0\*MeV)& (ADOCACHI2CUT(25,''))  |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<25) |
| DecayDescriptor  | None                                                        |
| DecayDescriptors | [ '[KS0 -\> pi+ pi+]cc' ]                               |
| Output           | Phys/X2PiPiSSDDDarkBosonSel/Particles                       |

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

CombineParticles/B2KX2PiPiDDSSDarkBosonLine

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/X2PiPiSSDDDarkBosonSel' ]                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                 |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                               |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 25),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B+ -\> K+ KS0]cc' ]                                                                                                                                                                                  |
| Output           | Phys/B2KX2PiPiDDSSDarkBosonLine/Particles                                                                                                                                                                    |
