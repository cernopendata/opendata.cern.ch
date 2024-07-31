[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBd2eeKstarBDTLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Bd2eeKstarBDTLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedDiElectron_Particles

|      |                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedDiElectron](./stripping21r1-commonparticles-stdloosedetacheddielectron)/Particles')\>0 |

FilterDesktop/eeForBd2eeKstarBDT

|                 |                                                                                                                                                                                                                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (((MM\<1.5\*GeV)) \| ((MM\>2.2\*GeV) & (MM\<4.2\*GeV))) & (INTREE( (ID=='e+') & (PT\> 200.0 \*MeV) & (TRCHI2DOF \< 5.0) & (BPVIPCHI2() \> 1.0) & (PIDe\>-2.0) & (TRGHOSTPROB\<0.5 ) )) & (INTREE( (ID=='e-') & (PT\> 200.0 \*MeV) & (TRCHI2DOF \< 5.0) & (BPVIPCHI2() \> 1.0) & (PIDe\>-2.0) & (TRGHOSTPROB\<0.5 ) )) |
| Inputs          | [ 'Phys/[StdLooseDetachedDiElectron](./stripping21r1-commonparticles-stdloosedetacheddielectron)' ]                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                      |
| Output          | Phys/eeForBd2eeKstarBDT/Particles                                                                                                                                                                                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdVeryLooseDetachedKst2Kpi_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r1-commonparticles-stdveryloosedetachedkst2kpi)/Particles')\>0 |

FilterDesktop/KstarForBd2eeKstarBDT

|                 |                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\< 16.0) & (ADMASS('K\*(892)0')\< 150.0 \*MeV) & (INTREE( (ABSID=='K+') & (PT\> 400.0 \*MeV) & (P\>3000.0 \*MeV) & (TRCHI2DOF \< 5.0) & (BPVIPCHI2()\> 4.0 ) & (PIDK\>-5.0) & (TRGHOSTPROB\<0.35 ) )) & (INTREE( (ABSID=='pi+') & (PT\> 250.0 \*MeV) & (P\>2000.0 \*MeV) & (TRCHI2DOF \< 5.0) & (BPVIPCHI2()\> 4.0 ) & (PIDK\<10.0) & (TRGHOSTPROB\<0.35) )) |
| Inputs          | [ 'Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r1-commonparticles-stdveryloosedetachedkst2kpi)' ]                                                                                                                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                            |
| Output          | Phys/KstarForBd2eeKstarBDT/Particles                                                                                                                                                                                                                                                                                                                                            |

CombineParticles/Sel_Bd2eeKstarBDT

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstarForBd2eeKstarBDT' , 'Phys/eeForBd2eeKstarBDT' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0')\< 1200.0 \*MeV)                                                    |
| MotherCut        | (ADMASS('B0')\< 1000.0 \*MeV) & (VFASPF(VCHI2/VDOF)\< 16.0) & (BPVDIRA\> 0.999 )  |
| DecayDescriptor  | [ B0 -\> J/psi(1S) K\*(892)0 ]cc                                                |
| DecayDescriptors | [ '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' ]                                        |
| Output           | Phys/Sel_Bd2eeKstarBDT/Particles                                                  |

FilterDesktop/Bd2eeKstarBDTLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Code            | FILTER('Bd2eeKstarBDTSelection/Bd2eeKstarBDT') |
| Inputs          | [ 'Phys/Sel_Bd2eeKstarBDT' ]                 |
| DecayDescriptor | None                                           |
| Output          | Phys/Bd2eeKstarBDTLine/Particles               |

AddRelatedInfo/RelatedInfo1_Bd2eeKstarBDTLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bd2eeKstarBDTLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_Bd2eeKstarBDTLine/Particles |
