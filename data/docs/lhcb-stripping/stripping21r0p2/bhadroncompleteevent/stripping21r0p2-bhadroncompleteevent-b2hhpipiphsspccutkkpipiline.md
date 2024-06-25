[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2hhpipiPhsSpcCutKKpipiLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2hhpipiPhsSpcCutKKpipiLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/B2hhpipiPhsSpcCutSelBachelorKaon

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 200\*MeV) & (PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\> 2) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF\<3) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]                  |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/B2hhpipiPhsSpcCutSelBachelorKaon/Particles                                                        |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/B2hhpipiPhsSpcCutSelBachelor2Pion

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 200\*MeV) & (PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\> 2) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF\<3) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                   |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/B2hhpipiPhsSpcCutSelBachelor2Pion/Particles                                                        |

CombineParticles/B2hhpipiPhsSpcCutSelB2KKpipiPhsSpcCut

|                  |                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2hhpipiPhsSpcCutSelBachelor2Pion' , 'Phys/B2hhpipiPhsSpcCutSelBachelorKaon' ]                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                     |
| CombinationCut   | ((ADAMASS('B0') \< 300 \*MeV) \| (ADAMASS('B_s0') \< 300 \*MeV)) & (AMAXDOCA('') \< 0.2 \*mm) & (((AMASS(1,2) \< 1864.83 \*MeV) & (AMASS(3,4) \< 1864.83 \*MeV)) \| ((AMASS(1,4) \< 1864.83 \*MeV) & (AMASS(2,3) \< 1864.83 \*MeV)) \| (AMASS(1,2,3) \< 1869.65 \*MeV) \| (AMASS(1,2,4) \< 1869.65 \*MeV) \| (AMASS(1,3,4) \< 1869.65 \*MeV) \| (AMASS(2,3,4) \< 1869.65 \*MeV)) |
| MotherCut        | (VFASPF(VCHI2) \< 30.) & (BPVDIRA\> 0.999) & (BPVVDCHI2 \> 10.) & (BPVIPCHI2()\<30) & (PT \> 2.\*GeV )                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [B0 -\> K+ K- pi+ pi-]cc                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B0 -\> K+ K- pi+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/B2hhpipiPhsSpcCutSelB2KKpipiPhsSpcCut/Particles                                                                                                                                                                                                                                                                                                                             |

FilterDesktop/B2hhpipiPhsSpcCutKKpipiLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2hhpipiPhsSpcCutMvaB2KKpipi')\>.05 |
| Inputs          | [ 'Phys/B2hhpipiPhsSpcCutSelB2KKpipiPhsSpcCut' ]                 |
| DecayDescriptor | None                                                               |
| Output          | Phys/B2hhpipiPhsSpcCutKKpipiLine/Particles                         |
