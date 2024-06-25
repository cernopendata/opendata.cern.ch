[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB0d2DstarTauNuWSForB2XTauNuAllLines

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/B0d2DstarTauNuWSForB2XTauNuAllLines/Particles |
| Postscale      | 1.0000000                                          |
| HLT1           | None                                               |
| HLT2           | None                                               |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseDstarWithD02KPi

|      |                                           |
|------|-------------------------------------------|
| Code | 0StdLooseDstarWithD02KPi/Particles',True) |

FilterDesktop/SelDstarsForB2XTauNuAllLines

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF) \< 25.0 ) & (M-MAXTREE('D0'==ABSID,M)\>135.0\*MeV) & (M-MAXTREE('D0'==ABSID,M)\<160.0\*MeV) & (PT\>1250.0 \*MeV) & ((ADMASS('D\*(2010)+')\< 50.0\*MeV))& CHILDCUT(CHILDCUT( (PT \> 150.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> -3),1),2) & CHILDCUT(CHILDCUT( (PT\> 150.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDK \< 50.0),2),2)& CHILDCUT( (PT\>1200.0\*MeV) & (ADMASS('D0') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0),2) & CHILDCUT( (PT\>50.0\*MeV) & (TRCHI2DOF \< 30.0) & (TRGHP \< 0.6),1) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r0p2-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output          | Phys/SelDstarsForB2XTauNuAllLines/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3pi

|      |                                          |
|------|------------------------------------------|
| Code | 0StdLooseDetachedTau3pi/Particles',True) |

CombineParticles/SelB0d2DstarTauNuWS

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarsForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r0p2-commonparticles-stdloosedetachedtau3pi)' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                     |
| CombinationCut   | (((DAMASS('B0') \> -2579.0\*MeV) & (DAMASS('B0') \< 300.0\*MeV)) or ((DAMASS('B0') \> 720.0\*MeV) & (DAMASS('B0') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B0 -\> D\*(2010)- tau-]cc' ]                                                                                                                               |
| Output           | Phys/SelB0d2DstarTauNuWS/Particles                                                                                                                                 |

TisTosParticleTagger/B0d2DstarTauNuWSForB2XTauNuAllLines

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/SelB0d2DstarTauNuWS' ]                   |
| DecayDescriptor | None                                               |
| Output          | Phys/B0d2DstarTauNuWSForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                      |
