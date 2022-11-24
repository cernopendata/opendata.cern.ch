[[stripping21r1 lines]](./stripping21r1-index)

# StrippingWmuAKTJetsLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/WmuAKTJetsLine/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/selWmuAKTJetsWmu**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT\>10.0\*GeV) & (PT\<200000.0\*GeV)                               |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/selWmuAKTJetsWmu/Particles                                     |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1-stdjets) /Particles')\>0 |

**CombineParticles/WmuAKTJetsLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdJets](./stripping21r1-stdjets) ' , 'Phys/selWmuAKTJetsWmu' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 15.0 \* GeV ) ' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | AALLSAMEBPV & ( dr_13 \> 0.5 )& ( dr_23 \> 0.5 )                                      |
| MotherCut        | ALL                                                                                   |
| DecayDescriptor  | [H+ -\> CELLjet CELLjet mu+]cc                                                      |
| DecayDescriptors | [ '[H+ -\> CELLjet CELLjet mu+]cc' ]                                              |
| Output           | Phys/WmuAKTJetsLine/Particles                                                         |
