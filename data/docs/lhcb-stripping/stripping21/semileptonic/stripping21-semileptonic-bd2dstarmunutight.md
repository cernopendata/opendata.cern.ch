[[stripping21 lines]](./stripping21-index)

# StrippingBd2DstarMuNuTight

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Bd2DstarMuNuTight/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/SelMuForBd2DstarMuNuTight

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | (PT \> 800 \*MeV) & (P \> 2.0\*GeV) & (ISMUON) & (HASMUON) & (TRGHOSTPROB \< 0.5) & (PIDmu \> -5) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                         |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/SelMuForBd2DstarMuNuTight/Particles                                                          |

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/SelDstarsForBd2DstarMuNuTight

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF) \< 20 ) & (PT\>1250 \*MeV) & (ADMASS('D\*(2010)+')\< 70\*MeV)& CHILDCUT(CHILDCUT( (PT \> 350\*MeV) & (P \> 2.0\*GeV) & (MIPDV(PRIMARY) \> 0.04\*mm) & (TRGHOSTPROB \< 0.5) & (PIDK \> -5 ),1),2) & CHILDCUT(CHILDCUT( (PT\> 350\*MeV) & (P \> 2.0\*GeV) & (TRGHOSTPROB \< 0.5) & (MIPDV(PRIMARY) \> 0.04\*mm) ,2),2) & CHILDCUT( (PT\>1600\*MeV) & (ADMASS('D0') \< 60 \*MeV ) & (BPVVDCHI2 \> 50) & (VFASPF(VCHI2/VDOF)\<10),2) & CHILDCUT( (PT\>110\*MeV) & (MIPDV(PRIMARY) \> 0.04\*mm),1) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output          | Phys/SelDstarsForBd2DstarMuNuTight/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

CombineParticles/Bd2DstarMuNuTight

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarsForBd2DstarMuNuTight' , 'Phys/SelMuForBd2DstarMuNuTight' ]                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                          |
| CombinationCut   | ((AM \> 3000.\*MeV) )                                                                                                                                                 |
| MotherCut        | (BPVDIRA\> 0.999 ) & in_range(3000.\*MeV,M,5280.\*MeV) & (MINTREE(ABSID=='D0', VFASPF(VZ))-VFASPF(VZ) \> -2.5\*mm) & (BPVVDZ \> 0.5\*mm) & (VFASPF(VCHI2/VDOF)\< 25 ) |
| DecayDescriptor  | None                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> D\*(2010)- mu+]cc' , '[B0 -\> D\*(2010)+ mu+]cc' ]                                                                                                   |
| Output           | Phys/Bd2DstarMuNuTight/Particles                                                                                                                                      |
