[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBd2DstarMuNuLoose

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Bd2DstarMuNuLoose/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 0.30000000                       |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/SelMuForBd2DstarMuNuLoose

|                 |                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------|
| Code            | (PT \> 700 \*MeV) & (P \> 2.0\*GeV) & (ISMUON) & (HASMUON) & (TRGHOSTPROB \< 1) & (PIDmu \> -20) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                      |
| DecayDescriptor | None                                                                                             |
| Output          | Phys/SelMuForBd2DstarMuNuLoose/Particles                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/SelDstarsForBd2DstarMuNuLoose

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF) \< 25 ) & (PT\>1250 \*MeV) & (ADMASS('D\*(2010)+')\< 80\*MeV)& CHILDCUT(CHILDCUT( (PT \> 350\*MeV) & (P \> 2.0\*GeV) & (MIPDV(PRIMARY) \> 0.04\*mm) & (TRGHOSTPROB \< 1) & (PIDK \> -5 ),1),2) & CHILDCUT(CHILDCUT( (PT\> 350\*MeV) & (P \> 2.0\*GeV) & (TRGHOSTPROB \< 1) & (MIPDV(PRIMARY) \> 0.04\*mm) ,2),2) & CHILDCUT( (PT\>1600\*MeV) & (ADMASS('D0') \< 60 \*MeV ) & (BPVVDCHI2 \> 50) & (VFASPF(VCHI2/VDOF)\<10),2) & CHILDCUT( (PT\>110\*MeV) & (MIPDV(PRIMARY) \> 0.04\*mm),1) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output          | Phys/SelDstarsForBd2DstarMuNuLoose/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

CombineParticles/Bd2DstarMuNuLoose

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarsForBd2DstarMuNuLoose' , 'Phys/SelMuForBd2DstarMuNuLoose' ]                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                          |
| CombinationCut   | ((AM \> 3000.\*MeV) )                                                                                                                                                 |
| MotherCut        | (BPVDIRA\> 0.999 ) & in_range(3000.\*MeV,M,5280.\*MeV) & (MINTREE(ABSID=='D0', VFASPF(VZ))-VFASPF(VZ) \> -10\*mm) & (BPVVDZ \> -100\*mm) & (VFASPF(VCHI2/VDOF)\< 25 ) |
| DecayDescriptor  | None                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> D\*(2010)- mu+]cc' , '[B0 -\> D\*(2010)+ mu+]cc' ]                                                                                                   |
| Output           | Phys/Bd2DstarMuNuLoose/Particles                                                                                                                                      |
