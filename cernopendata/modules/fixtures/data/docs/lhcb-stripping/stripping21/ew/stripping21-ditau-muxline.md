[[stripping21 lines]](./stripping21-index)

# StrippingDitau_MuXLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Ditau_MuXLine/Particles             |
| Postscale      | 1.0000000                                |
| HLT            | HLT_PASS('Hlt2SingleMuonHighPTDecision') |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) /Particles')\>0 |

**CombineParticles/Ditau_MuXLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' , 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(0.01 \< TRPCHI2) & (1.0 \> BPVIP()) & (2 \>= SUMCONE( 0.1, ONE, "Phys/StdAllNoPIDsPions")) & (10000.0 \< PT) & (0.7 \< E / ( E + SUMCONE( 0.5, E, "Phys/StdAllNoPIDsPions" ) ) )' , 'mu-' : '(0.01 \< TRPCHI2) & (1.0 \> BPVIP()) & (2 \>= SUMCONE( 0.1, ONE, "Phys/StdAllNoPIDsPions")) & (10000.0 \< PT) & (0.7 \< E / ( E + SUMCONE( 0.5, E, "Phys/StdAllNoPIDsPions" ) ) )' , 'pi+' : '(0.01 \< TRPCHI2) & (1.0 \> BPVIP()) & (2 \>= SUMCONE( 0.1, ONE, "Phys/StdAllNoPIDsPions")) & (3000.0 \< PT) & (0.1 \< E / ( E + SUMCONE( 0.5, E, "Phys/StdAllNoPIDsPions" ) ) )' , 'pi-' : '(0.01 \< TRPCHI2) & (1.0 \> BPVIP()) & (2 \>= SUMCONE( 0.1, ONE, "Phys/StdAllNoPIDsPions")) & (3000.0 \< PT) & (0.1 \< E / ( E + SUMCONE( 0.5, E, "Phys/StdAllNoPIDsPions" ) ) )' } |
| CombinationCut   | (AALLSAMEBPV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (11000.0 \< MM)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [Z0 -\> mu+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Z0 -\> mu+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/Ditau_MuXLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
