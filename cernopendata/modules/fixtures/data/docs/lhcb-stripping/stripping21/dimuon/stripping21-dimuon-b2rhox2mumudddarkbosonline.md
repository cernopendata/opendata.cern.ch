[[stripping21 lines]](./stripping21-index)

# StrippingB2RhoX2MuMuDDDarkBosonLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/B2RhoX2MuMuDDDarkBosonLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingB2RhoX2MuMuDDDarkBosonLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiBDarkBosonFilter

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                           |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                           |

CombineParticles/Rho2PiPiDarkBosonSel

|                  |                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiBDarkBosonFilter' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                        |
| CombinationCut   | (AM \> 550\*MeV) & (AM \< 1050\*MeV) & ADOCACHI2CUT(25,'')                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MIPCHI2DV(PRIMARY)\> 16) & HASVERTEX & (M \> 600\*MeV) & (M \< 1000\*MeV) |
| DecayDescriptor  | None                                                                                                  |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                         |
| Output           | Phys/Rho2PiPiDarkBosonSel/Particles                                                                   |

LoKi::VoidFilter/SelFilterPhys_StdLooseDownMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDownMuons](./stripping21-commonparticles-stdloosedownmuons)/Particles')\>0 |

FilterDesktop/MuDXDarkBosonFilter

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (TRGHP\<0.3) & (PIDmu\>-5) & (TRCHI2DOF\<3) & (P\>0\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>100\*MeV) |
| Inputs          | [ 'Phys/[StdLooseDownMuons](./stripping21-commonparticles-stdloosedownmuons)' ]                    |
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

CombineParticles/B2RhoX2MuMuDDDarkBosonLine

|                  |                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Rho2PiPiDarkBosonSel' , 'Phys/X2MuMuDDDarkBosonSel' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'rho(770)0' : 'ALL' }                                                                                                                                                        |
| CombinationCut   | (AM\<5800\*MeV) & (AM\>4800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                              |
| MotherCut        | (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (PT\>1000\*MeV) & (VFASPF(VCHI2/VDOF)\<25) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<50) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                        |
| DecayDescriptors | [ 'B0 -\> rho(770)0 KS0' ]                                                                                                                                                                                |
| Output           | Phys/B2RhoX2MuMuDDDarkBosonLine/Particles                                                                                                                                                                   |
