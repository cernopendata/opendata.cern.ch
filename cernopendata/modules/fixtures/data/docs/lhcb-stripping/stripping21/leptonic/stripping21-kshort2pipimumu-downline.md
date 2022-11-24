[[stripping21 lines]](./stripping21-index)

# StrippingKshort2PiPiMuMu_DownLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Kshort2PiPiMuMu_DownLine/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDownMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDownMuons](./stripping21-stdloosedownmuons) /Particles')\>0 |

**FilterDesktop/DownMuonsForKshort2PiPiMuMu**

|                 |                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 3000.0 \*MeV) & (PT \> 300\* MeV) & (PIDmu-PIDpi \> -1) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| Inputs          | [ 'Phys/ [StdLooseDownMuons](./stripping21-stdloosedownmuons) ' ]                                            |
| DecayDescriptor | None                                                                                                           |
| Output          | Phys/DownMuonsForKshort2PiPiMuMu/Particles                                                                     |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownPions](./stripping21-stdnopidsdownpions) /Particles')\>0 |

**FilterDesktop/DownPionsForKshort2PiPiMuMu**

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300\* MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| Inputs          | [ 'Phys/ [StdNoPIDsDownPions](./stripping21-stdnopidsdownpions) ' ]                    |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/DownPionsForKshort2PiPiMuMu/Particles                                               |

**CombineParticles/Kshort2PiPiMuMu_DownLine**

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DownMuonsForKshort2PiPiMuMu' , 'Phys/DownPionsForKshort2PiPiMuMu' ]                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                  |
| CombinationCut   | (AM \< 550.0 \*MeV) & (AMAXDOCA('')\<0.2) & (AM34 \< 260.0 \*MeV) &(AHASCHILD( (MIPCHI2DV(PRIMARY)\>15) ) )                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8) & (PT \> 2500.0 \*MeV) &(M \< 540.0 \*MeV) &(BPVVDCHI2\>9) & (BPVIPCHI2()\< 20) & (BPVDIRA \> 0.9999) |
| DecayDescriptor  | KS0 -\> pi+ pi- mu+ mu-                                                                                                         |
| DecayDescriptors | [ 'KS0 -\> pi+ pi- mu+ mu-' ]                                                                                                 |
| Output           | Phys/Kshort2PiPiMuMu_DownLine/Particles                                                                                         |
