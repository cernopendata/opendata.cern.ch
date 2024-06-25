[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLb2dp_Line

## Properties:

|                |                           |
|----------------|---------------------------|
| OutputLocation | Phys/Lb2dp_Line/Particles |
| Postscale      | 1.0000000                 |
| HLT1           | None                      |
| HLT2           | None                      |
| Prescale       | 1.0000000                 |
| L0DU           | None                      |
| ODIN           | None                      |

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

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)/Particles',True)\>0 |

FilterDesktop/KaonForLb2dp

|                 |                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Code            | ((TRCHI2DOF\< 3.0) & (TRGHOSTPROB\< 0.5) & (MIPCHI2DV(PRIMARY)\> 16.0) & (P\> 25000 \*MeV)) & (PT\> 1000 \*MeV) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p1-commonparticles-stdallnopidskaons)' ]                           |
| DecayDescriptor | None                                                                                                            |
| Output          | Phys/KaonForLb2dp/Particles                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r0p1-commonparticles-stdallnopidsprotons)/Particles',True)\>0 |

FilterDesktop/ProtonForLb2dp

|                 |                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((TRCHI2DOF\< 3.0) & (TRGHOSTPROB\< 0.5) & (MIPCHI2DV(PRIMARY)\> 16.0) & ((PIDp-PIDpi)\> 10) & ((PIDp-PIDK)\> 10) & (P\> 15000 \*MeV)) & (PT\> 1000 \*MeV) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r0p1-commonparticles-stdallnopidsprotons)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                                       |
| Output          | Phys/ProtonForLb2dp/Particles                                                                                                                              |

CombineParticles/Lb2dp_Line

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonForLb2dp' , 'Phys/ProtonForLb2dp' ]                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                              |
| CombinationCut   | ((ACHILD(PT,1)+ACHILD(PT,2)) \> 3000 \*MeV)                                                                              |
| MotherCut        | (BPVDIRA \> 0.9999) & (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVVDCHI2\> 150) & (PT\> 1500) & (M_Lb\> 5200.0) & (M_Lb\< 6000.0) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ '[Lambda_b0 -\> K+ p~-]cc' ]                                                                                       |
| Output           | Phys/Lb2dp_Line/Particles                                                                                                |
