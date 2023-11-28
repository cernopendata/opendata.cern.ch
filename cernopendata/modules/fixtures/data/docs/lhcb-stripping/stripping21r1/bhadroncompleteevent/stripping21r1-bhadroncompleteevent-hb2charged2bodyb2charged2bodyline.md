[[stripping21r1 lines]](./stripping21r1-index)

# StrippingHb2Charged2BodyB2Charged2BodyLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/Hb2Charged2BodyB2Charged2BodyLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | None                                             |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/Hb2Charged2BodyB2Charged2BodyLine

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ]                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPCHI2DV(PRIMARY) \> 12 )' , 'pi-' : '(TRGHOSTPROB \< 0.5) & (TRCHI2DOF \< 3) & (PT \> 1000 \* MeV) & ( MIPCHI2DV(PRIMARY) \> 12 )' } |
| CombinationCut   | (AMAXCHILD(MAXTREE('pi+'==ABSID,PT)) \> 1400 ) & ( AMAXCHILD(MAXTREE('pi+'==ABSID,MIPCHI2DV(PRIMARY))) \> 40 ) & (AMAXDOCA('') \< 0.08 ) & (AM \> 4600 \* MeV) & (AM \< 6000 \* MeV)                                             |
| MotherCut        | (PT \> 1200 \* MeV) & (M \> 4800 \* MeV) & (M \< 5800 \* MeV) & ( BPVIPCHI2() \< 12 ) & (BPVLTIME() \> 0.0006 )                                                                                                                  |
| DecayDescriptor  | B0 -\> pi+ pi-                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'B0 -\> pi+ pi-' ]                                                                                                                                                                                                           |
| Output           | Phys/Hb2Charged2BodyB2Charged2BodyLine/Particles                                                                                                                                                                                 |
