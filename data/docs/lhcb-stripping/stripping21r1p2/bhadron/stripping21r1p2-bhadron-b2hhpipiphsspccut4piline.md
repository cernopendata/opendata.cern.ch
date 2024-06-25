[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2hhpipiPhsSpcCut4piLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2hhpipiPhsSpcCut4piLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/B2hhpipiPhsSpcCutSelBachelorPion

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 200\*MeV) & (PROBNNpi \> 0.03) & (MIPCHI2DV(PRIMARY)\> 1.5) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF\<3) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                      |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/B2hhpipiPhsSpcCutSelBachelorPion/Particles                                                            |

CombineParticles/B2hhpipiPhsSpcCutSelB24piPhsSpcCut

|                  |                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2hhpipiPhsSpcCutSelBachelorPion' ]                                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                               |
| CombinationCut   | (ADAMASS('B0') \< 300 \*MeV) & (AMAXDOCA('') \< 0.2 \*mm) & (((AMASS(1,2) \< 1864.83 \*MeV) & (AMASS(3,4) \< 1864.83 \*MeV)) \| ((AMASS(1,4) \< 1864.83 \*MeV) & (AMASS(2,3) \< 1864.83 \*MeV)) \| (AMASS(1,2,3) \< 1869.65 \*MeV) \| (AMASS(1,2,4) \< 1869.65 \*MeV) \| (AMASS(1,3,4) \< 1869.65 \*MeV) \| (AMASS(2,3,4) \< 1869.65 \*MeV)) |
| MotherCut        | (VFASPF(VCHI2) \< 30.) & (BPVDIRA\> 0.999) & (BPVVDCHI2 \> 10.) & (BPVIPCHI2()\<30) & (PT \> 2.\*GeV )                                                                                                                                                                                                                                       |
| DecayDescriptor  | [B0 -\> pi+ pi- pi+ pi-]cc                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B0 -\> pi+ pi- pi+ pi-]cc' ]                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/B2hhpipiPhsSpcCutSelB24piPhsSpcCut/Particles                                                                                                                                                                                                                                                                                            |

FilterDesktop/B2hhpipiPhsSpcCut4piLine

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2hhpipiPhsSpcCutMvaB24pi')\>-.03 |
| Inputs          | [ 'Phys/B2hhpipiPhsSpcCutSelB24piPhsSpcCut' ]                  |
| DecayDescriptor | None                                                             |
| Output          | Phys/B2hhpipiPhsSpcCut4piLine/Particles                          |
