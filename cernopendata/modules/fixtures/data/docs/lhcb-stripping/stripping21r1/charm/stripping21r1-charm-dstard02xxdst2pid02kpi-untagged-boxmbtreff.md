[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

## Properties:

|                |                                                           |
|----------------|-----------------------------------------------------------|
| OutputLocation | Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles |
| Postscale      | 1.0000000                                                 |
| HLT            | HLT_PASS_RE('Hlt2CharmHadMinBiasD02KPiDecision')          |
| Prescale       | 1.0000000                                                 |
| L0DU           | None                                                      |
| ODIN           | None                                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'K-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'pi+' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' , 'pi-' : '(PT\> 750.0 \*MeV) & (P\>4000.0 \*MeV) & (TRCHI2DOF\<5.0) & (MIPCHI2DV(PRIMARY)\> 3) & ( TRGHOSTPROB \< 0.5 )' } |
| CombinationCut   | (AMAXDOCA('')\< 0.1 \*mm) & (ADAMASS('D0')\< 70.0 \*MeV) & (AMAXCHILD(PT)\>1100.0 \*MeV) & (APT\> 1800.0)                                                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (BPVDIRA\> 0.9997) & (INGENERATION( (MIPCHI2DV(PRIMARY)\>8),1 ) ) & (BPVVDCHI2\> 20.0) & (MIPCHI2DV(PRIMARY)\< 15.0) & (VFASPF(VCHI2/VDOF)\< 10.0)                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'D0 -\> K+ pi- ' , 'D0 -\> K- pi+ ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

AddRelatedInfo/RelatedInfo1_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff' ]                |
| DecayDescriptor | None                                                                   |
| Output          | Phys/RelatedInfo1_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles |

AddRelatedInfo/RelatedInfo2_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff' ]                |
| DecayDescriptor | None                                                                   |
| Output          | Phys/RelatedInfo2_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles |

AddRelatedInfo/RelatedInfo3_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff' ]                |
| DecayDescriptor | None                                                                   |
| Output          | Phys/RelatedInfo3_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles |

AddRelatedInfo/RelatedInfo4_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff' ]                |
| DecayDescriptor | None                                                                   |
| Output          | Phys/RelatedInfo4_DstarD02xxDst2PiD02Kpi_untagged_BoxMBTrEff/Particles |
