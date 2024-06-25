[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBc2JpsiHBDTLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/Bc2JpsiHBDTLine/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/Jpsi2MuMuForBc2JpsiHBDT_SelP2MuMu

|                 |                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('mu+'==ABSID,PT)\>500\*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF)\<3) & (MINTREE('mu+'==ABSID,PIDmu)\>0.) & ((MM\>3.0\*GeV) & (MM\<3.2\*GeV) & (VFASPF(VCHI2PDOF)\<16)) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1-commonparticles-stdloosedimuon)' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                          |
| Output          | Phys/Jpsi2MuMuForBc2JpsiHBDT_SelP2MuMu/Particles                                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/SelPion_Sel_Bc2JpsiHBDT

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | ((TRCHI2DOF\<3) & (TRGHOSTPROB\<0.6) & (PT\>1.0\*GeV))                              |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/SelPion_Sel_Bc2JpsiHBDT/Particles                                              |

CombineParticles/Sel_Bc2JpsiHBDT

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Jpsi2MuMuForBc2JpsiHBDT_SelP2MuMu' , 'Phys/SelPion_Sel_Bc2JpsiHBDT' ]                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                      |
| CombinationCut   | (in_range(5.8\*GeV, AM, 7.0\*GeV))                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16) & (in_range(6.0\*GeV, DTF_FUN(M,True,strings( ['J/psi(1S)'])), 6.75\*GeV)) & (BPVIPCHI2()\<25) |
| DecayDescriptor  | [ B_c+ -\> J/psi(1S) pi+ ]cc                                                                                            |
| DecayDescriptors | [ '[ B_c+ -\> J/psi(1S) pi+ ]cc' ]                                                                                    |
| Output           | Phys/Sel_Bc2JpsiHBDT/Particles                                                                                            |

FilterDesktop/Bc2JpsiHBDTLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | FILTER('Bc2JpsiHBDTSelection/Bc2JpsiHBDT') |
| Inputs          | [ 'Phys/Sel_Bc2JpsiHBDT' ]               |
| DecayDescriptor | None                                       |
| Output          | Phys/Bc2JpsiHBDTLine/Particles             |
