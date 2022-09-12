[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLLP2MuXHighPTHighIPMuonLine

## Properties:

|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| OutputLocation | Phys/LLP2MuXHighPTHighIPMuonLine/Particles                                          |
| Postscale      | 1.0000000                                                                           |
| HLT            | HLT_PASS('Hlt1SingleMuonHighPTDecision') & HLT_PASS('Hlt2SingleMuonHighPTDecision') |
| Prescale       | 1.0000000                                                                           |
| L0DU           | L0_CHANNEL('Muon')                                                                  |
| ODIN           | None                                                                                |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/LLP2MuXHighPTHighIPMuonLine**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ( PT \> 12000.000000 ) & ( MIPDV('') \> 0.250000 )                  |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/LLP2MuXHighPTHighIPMuonLine/Particles                          |
