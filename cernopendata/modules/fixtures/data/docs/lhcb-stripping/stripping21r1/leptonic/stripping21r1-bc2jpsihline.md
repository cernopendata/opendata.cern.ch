[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBc2JpsiHLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/Bc2JpsiHLine/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiMuon](./stripping21r1-stdloosedimuon) /Particles')\>0 |

**FilterDesktop/Jpsi2MuMuForBc2JpsiH_SelP2MuMu**

|                 |                                                                                                                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT) \> 1200.0 \*MeV) & (MINTREE('mu+'==ABSID,P) \> -5.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 5.0) & (ADMASS('J/psi(1S)') \< 80.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 9.0) & (PT \> 2000.0 \*MeV) |
| Inputs          | [ 'Phys/ [StdLooseDiMuon](./stripping21r1-stdloosedimuon) ' ]                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                     |
| Output          | Phys/Jpsi2MuMuForBc2JpsiH_SelP2MuMu/Particles                                                                                                                                                                            |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/SelPion_Sel_Bc2JpsiH**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT \> 2000.0 \*MeV) & (P \> -5.0 \*MeV) & (TRCHI2DOF \< 5.0)         |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/SelPion_Sel_Bc2JpsiH/Particles                                   |

**CombineParticles/Bc2JpsiHLine**

|                  |                                                                           |
|------------------|---------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Jpsi2MuMuForBc2JpsiH_SelP2MuMu' , 'Phys/SelPion_Sel_Bc2JpsiH' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }      |
| CombinationCut   | (ADAMASS('B_c+') \< 400.0 \*MeV)                                          |
| MotherCut        | (VFASPF(VCHI2PDOF)\< 9.0 ) & (PT \> 6000.0 \*MeV)                         |
| DecayDescriptor  | [ B_c+ -\> J/psi(1S) pi+ ]cc                                            |
| DecayDescriptors | [ '[ B_c+ -\> J/psi(1S) pi+ ]cc' ]                                    |
| Output           | Phys/Bc2JpsiHLine/Particles                                               |
