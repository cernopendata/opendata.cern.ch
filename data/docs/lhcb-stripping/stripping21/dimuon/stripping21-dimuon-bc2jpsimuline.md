[[stripping21 lines]](./stripping21-index)

# StrippingBc2JpsiMuLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bc2JpsiMuLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)/Particles')\>0 |

FilterDesktop/Jpsi2MuMuForBc2JpsiMu_SelP2MuMu

|                 |                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT((TRCHI2DOF \< 5.0),1)) & (CHILDCUT((TRCHI2DOF \< 5.0),2)) & (CHILDCUT((PT \> 1400.0 \*MeV),1)) & (CHILDCUT((PT \> 1400.0 \*MeV),2)) & (ADMASS('J/psi(1S)') \< 150.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 9.0) & (PT \> -10.0 \*MeV) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21-commonparticles-stdloosedimuon)' ]                                                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                                                                   |
| Output          | Phys/Jpsi2MuMuForBc2JpsiMu_SelP2MuMu/Particles                                                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21-commonparticles-stdallnopidsmuons)/Particles')\>0 |

FilterDesktop/SelMuonBc_Sel_Bc2JpsiMu

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | (PT \> 2500.0 \*MeV) & (P \> -5.0 \*MeV) & (TRCHI2DOF \< 5.0) & (TRGHOSTPROB\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21-commonparticles-stdallnopidsmuons)' ]  |
| DecayDescriptor | None                                                                               |
| Output          | Phys/SelMuonBc_Sel_Bc2JpsiMu/Particles                                             |

CombineParticles/Bc2JpsiMuLine

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Jpsi2MuMuForBc2JpsiMu_SelP2MuMu' , 'Phys/SelMuonBc_Sel_Bc2JpsiMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }          |
| CombinationCut   | (in_range( 3200.0 \*MeV, AM, 6400.0 \*MeV))                                   |
| MotherCut        | (VFASPF(VCHI2PDOF)\< 9.0 ) & (PT \> 6000.0 \*MeV)                             |
| DecayDescriptor  | [ B_c+ -\> J/psi(1S) mu+ ]cc                                                |
| DecayDescriptors | [ '[ B_c+ -\> J/psi(1S) mu+ ]cc' ]                                        |
| Output           | Phys/Bc2JpsiMuLine/Particles                                                  |
